#!/usr/bin/env python3
"""
knowledge_updater.py — Personalized Learning Path Designer (Idea 52)

Crawls learning-science sources (ERIC, ArXiv cs.CY, OECD Education), scores by
recency and relevance, and appends deduplicated entries to SECOND-KNOWLEDGE-BRAIN.md.

This tool maintains the knowledge base with current research findings, ensuring
the learning path designer stays updated with the latest evidence-based practices.

Usage:
    python knowledge_updater.py [--dry-run] [--verbose] [--config CONFIG_FILE]

Schedule:
    Run weekly via cron: 0 2 * * 0 /usr/bin/python3 /path/to/knowledge_updater.py

Dependencies:
    Optional: crawl4ai (graceful degradation if unavailable)
    Built-in: hashlib, pathlib, re, argparse, datetime, logging, json, time

Author: Personalized Learning Path Designer Project
License: MIT
Version: 1.0.0
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import logging
import pathlib
import re
import sys
import time
from typing import Any, Dict, List, Optional, Set

# =============================================================================
# Configuration and Constants
# =============================================================================

VERSION = "1.0.0"
DEFAULT_CONFIG = {
    "sources": [
        {"name": "ERIC", "url": "https://eric.ed.gov/?q=learning+science", "enabled": True},
        {"name": "ArXiv cs.CY", "url": "https://arxiv.org/list/cs.CY/recent", "enabled": True},
        {"name": "OECD Education", "url": "https://www.oecd.org/education/", "enabled": True},
    ],
    "queries": [
        "learning science 2026",
        "spaced repetition study",
        "curriculum design evidence",
        "retrieval practice retention",
        "cognitive load theory education",
        "mastery learning implementation"
    ],
    "keywords": [
        "learning", "curriculum", "pedagog", "retention", "spaced", "retrieval",
        "cognitive load", "instruction", "assessment", "mastery", "education",
        "teaching", "training", "instructional design", "educational psychology"
    ],
    "filters": {
        "min_title_length": 20,
        "max_title_length": 200,
        "min_keyword_matches": 1
    },
    "delays": {
        "between_sources": 1.0,
        "on_fetch_error": 5.0
    },
    "logging": {
        "level": "INFO",
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    }
}

# =============================================================================
# Logging Setup
# =============================================================================

def setup_logging(level: str = "INFO") -> logging.Logger:
    """Configure logging for the application."""
    logger = logging.getLogger("knowledge_updater")
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

# =============================================================================
# Path Management
# =============================================================================

def get_project_root() -> pathlib.Path:
    """Get the project root directory."""
    return pathlib.Path(__file__).resolve().parent.parent

def get_brain_path() -> pathlib.Path:
    """Get path to SECOND-KNOWLEDGE-BRAIN.md."""
    return get_project_root() / "SECOND-KNOWLEDGE-BRAIN.md"

def get_config_path(config_file: Optional[str] = None) -> pathlib.Path:
    """Get path to configuration file."""
    if config_file:
        return pathlib.Path(config_file)
    return get_project_root() / "config" / "knowledge_updater.json"

# =============================================================================
# Hash Management
# =============================================================================

def extract_existing_hashes(text: str) -> Set[str]:
    """
    Extract all existing entry hashes from the knowledge base.

    Args:
        text: Content of SECOND-KNOWLEDGE-BRAIN.md

    Returns:
        Set of existing hashes
    """
    return set(re.findall(r"<!--h:([0-9a-f]{12})-->", text))

def generate_entry_hash(entry: Dict[str, str]) -> str:
    """
    Generate a unique hash for an entry to prevent duplicates.

    Args:
        entry: Dictionary with 'url' and 'title' keys

    Returns:
        12-character hex hash
    """
    hash_input = f"{entry.get('url', '')}{entry.get('title', '')}"
    return hashlib.sha1(hash_input.encode()).hexdigest()[:12]

# =============================================================================
# Content Fetching
# =============================================================================

def fetch_from_source(source: Dict[str, Any], keywords: List[str],
                     delays: Dict[str, float], logger: logging.Logger) -> List[Dict[str, str]]:
    """
    Fetch content from a single source.

    Args:
        source: Source configuration dict with name, url, and enabled status
        keywords: List of keywords to filter content
        delays: Delay configuration for rate limiting
        logger: Logger instance

    Returns:
        List of entry dicts with title, source, and url
    """
    if not source.get("enabled", True):
        logger.info(f"Skipping disabled source: {source['name']}")
        return []

    logger.info(f"Fetching from {source['name']}: {source['url']}")

    try:
        # Try to use crawl4ai if available
        from crawl4ai import WebCrawler  # type: ignore
        crawler = WebCrawler()
        crawler.warmup()

        result = crawler.run(url=source["url"])
        text = getattr(result, "markdown", "") or ""

        if not text:
            logger.warning(f"No content retrieved from {source['name']}")
            return []

        logger.debug(f"Retrieved {len(text)} characters from {source['name']}")

    except ImportError:
        logger.warning(f"crawl4ai not available, using fallback for {source['name']}")
        text = _fallback_fetch(source, logger)
    except Exception as exc:
        logger.error(f"Error fetching from {source['name']}: {exc}")
        time.sleep(delays.get("on_fetch_error", 5.0))
        return []

    # Process the retrieved content
    entries = _process_content(text, source, keywords, logger)
    logger.info(f"Extracted {len(entries)} entries from {source['name']}")

    return entries

def _fallback_fetch(source: Dict[str, Any], logger: logging.Logger) -> str:
    """
    Fallback method for fetching content when crawl4ai is unavailable.

    This is a minimal fallback that returns empty content. In production,
    you might want to implement alternative fetching methods.
    """
    logger.warning(f"Fallback fetching not implemented for {source['name']}")
    return ""

def _process_content(text: str, source: Dict[str, Any],
                    keywords: List[str], logger: logging.Logger) -> List[Dict[str, str]]:
    """
    Process raw text content into structured entries.

    Args:
        text: Raw markdown/text content
        source: Source information dict
        keywords: Filter keywords
        logger: Logger instance

    Returns:
        List of processed entry dicts
    """
    entries = []
    lines = text.splitlines()

    for line in lines:
        line = line.strip("#* -").strip()

        # Apply content filters
        if not (_is_valid_title(line, keywords)):
            continue

        entries.append({
            "title": line,
            "source": source["name"],
            "url": source["url"]
        })

    return entries

def _is_valid_title(text: str, keywords: List[str],
                   min_length: int = 20, max_length: int = 200) -> bool:
    """
    Validate if a text line meets content criteria.

    Args:
        text: Text to validate
        keywords: List of required keywords
        min_length: Minimum character count
        max_length: Maximum character count

    Returns:
        True if text passes all validation checks
    """
    if not (min_length <= len(text) <= max_length):
        return False

    text_lower = text.lower()
    return any(keyword in text_lower for keyword in keywords)

# =============================================================================
# Scoring and Sorting
# =============================================================================

def score_relevance(entry: Dict[str, str], keywords: List[str]) -> float:
    """
    Score an entry based on keyword relevance.

    Args:
        entry: Entry dict with title field
        keywords: List of keywords to score against

    Returns:
        Relevance score (higher is more relevant)
    """
    title_lower = entry.get("title", "").lower()
    return sum(1.0 for keyword in keywords if keyword in title_lower)

# =============================================================================
# Knowledge Base Management
# =============================================================================

def load_knowledge_base(brain_path: pathlib.Path, logger: logging.Logger) -> str:
    """
    Load the existing knowledge base content.

    Args:
        brain_path: Path to SECOND-KNOWLEDGE-BRAIN.md
        logger: Logger instance

    Returns:
        Content of the knowledge base file
    """
    if not brain_path.exists():
        logger.warning(f"Knowledge base not found at {brain_path}, creating new file")
        brain_path.parent.mkdir(parents=True, exist_ok=True)
        return _get_default_header()

    try:
        return brain_path.read_text(encoding="utf-8")
    except Exception as exc:
        logger.error(f"Error reading knowledge base: {exc}")
        return _get_default_header()

def save_knowledge_base(brain_path: pathlib.Path, content: str,
                       logger: logging.Logger) -> bool:
    """
    Save updated content to the knowledge base.

    Args:
        brain_path: Path to SECOND-KNOWLEDGE-BRAIN.md
        content: Content to write
        logger: Logger instance

    Returns:
        True if save was successful
    """
    try:
        brain_path.parent.mkdir(parents=True, exist_ok=True)
        with brain_path.open("w", encoding="utf-8") as f:
            f.write(content)
        logger.info(f"Saved updated knowledge base to {brain_path}")
        return True
    except Exception as exc:
        logger.error(f"Error saving knowledge base: {exc}")
        return False

def _get_default_header() -> str:
    """Get default header for new knowledge base files."""
    return """# SECOND-KNOWLEDGE-BRAIN.md — Personalized Learning Path Designer (Idea 52)

Grown weekly by `tools/knowledge_updater.py`.

## Core Concepts & Frameworks
- **Bloom's Taxonomy (revised):** Remember→Understand→Apply→Analyze→Evaluate→Create
- **Backward Design / UbD (Wiggins & McTighe):** Objectives → assessments → activities
- **Spaced repetition & retrieval practice:** Distributed practice + testing effect
- **Deliberate practice (Ericsson):** Focused, feedback-rich practice
- **Cognitive Load Theory (Sweller):** Manage intrinsic/extraneous/germane load
- **Zone of Proximal Development (Vygotsky):** Tasks just beyond ability with support

## Auto-update entries will be appended below
"""

# =============================================================================
# Entry Processing
# =============================================================================

def process_entries(entries: List[Dict[str, str]], existing_hashes: Set[str],
                  keywords: List[str], logger: logging.Logger) -> List[Dict[str, str]]:
    """
    Process and filter entries, removing duplicates and scoring by relevance.

    Args:
        entries: Raw entry list from fetching
        existing_hashes: Set of already-seen entry hashes
        keywords: Keyword list for scoring
        logger: Logger instance

    Returns:
        Processed, deduplicated, sorted entries
    """
    # Remove duplicates
    unique_entries = []
    for entry in entries:
        entry_hash = generate_entry_hash(entry)
        if entry_hash in existing_hashes:
            logger.debug(f"Skipping duplicate entry: {entry['title'][:50]}...")
            continue
        entry["hash"] = entry_hash
        unique_entries.append(entry)
        existing_hashes.add(entry_hash)

    if not unique_entries:
        logger.info("No new unique entries found")
        return []

    # Score and sort by relevance
    for entry in unique_entries:
        entry["score"] = score_relevance(entry, keywords)

    unique_entries.sort(key=lambda e: e["score"], reverse=True)

    logger.info(f"Processed {len(unique_entries)} new entries")
    return unique_entries

def format_entry_block(entries: List[Dict[str, str]], date: str) -> str:
    """
    Format entries as a markdown block for appending to knowledge base.

    Args:
        entries: List of entry dicts
        date: ISO date string for the update

    Returns:
        Formatted markdown block
    """
    lines = [f"\n### Auto-update {date}\n"]

    for entry in entries:
        line = (f"- [{date}] {entry['title'][:150]} — {entry['source']} — "
                f"{entry['url']} <!--h:{entry['hash']}-->")
        lines.append(line)

    return "\n".join(lines) + "\n"

# =============================================================================
# Configuration Management
# =============================================================================

def load_config(config_path: Optional[pathlib.Path], logger: logging.Logger) -> Dict[str, Any]:
    """
    Load configuration from file or use defaults.

    Args:
        config_path: Path to config file (None for default)
        logger: Logger instance

    Returns:
        Configuration dictionary
    """
    if config_path and config_path.exists():
        try:
            with config_path.open("r", encoding="utf-8") as f:
                user_config = json.load(f)
            logger.info(f"Loaded configuration from {config_path}")
            return {**DEFAULT_CONFIG, **user_config}
        except Exception as exc:
            logger.error(f"Error loading config: {exc}, using defaults")

    logger.info("Using default configuration")
    return DEFAULT_CONFIG.copy()

def save_config(config: Dict[str, Any], config_path: pathlib.Path,
               logger: logging.Logger) -> None:
    """
    Save current configuration to file.

    Args:
        config: Configuration dictionary
        config_path: Path to save config
        logger: Logger instance
    """
    try:
        config_path.parent.mkdir(parents=True, exist_ok=True)
        with config_path.open("w", encoding="utf-8") as f:
            json.dump(config, f, indent=2)
        logger.info(f"Saved configuration to {config_path}")
    except Exception as exc:
        logger.error(f"Error saving config: {exc}")

# =============================================================================
# Main Application
# =============================================================================

def main() -> int:
    """Main entry point for the knowledge updater."""
    parser = argparse.ArgumentParser(
        description="Update SECOND-KNOWLEDGE-BRAIN.md with current research",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be added without modifying files"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging"
    )
    parser.add_argument(
        "--config", "-c",
        type=str,
        help="Path to configuration file"
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {VERSION}"
    )
    args = parser.parse_args()

    # Setup logging
    log_level = "DEBUG" if args.verbose else "INFO"
    logger = setup_logging(log_level)
    logger.info(f"Knowledge Updater v{VERSION} starting")

    # Load configuration
    config_path = get_config_path(args.config)
    config = load_config(config_path, logger)

    # Load existing knowledge base
    brain_path = get_brain_path()
    existing_content = load_knowledge_base(brain_path, logger)
    existing_hashes = extract_existing_hashes(existing_content)
    logger.info(f"Found {len(existing_hashes)} existing entries")

    # Fetch from all sources
    all_entries = []
    delays = config.get("delays", {})

    for source in config.get("sources", []):
        entries = fetch_from_source(
            source,
            config.get("keywords", []),
            delays,
            logger
        )
        all_entries.extend(entries)

        # Rate limiting between sources
        if source != config["sources"][-1]:  # Don't delay after last source
            time.sleep(delays.get("between_sources", 1.0))

    if not all_entries:
        logger.info("No entries fetched from any source")
        return 0

    # Process entries
    keywords = config.get("keywords", [])
    processed_entries = process_entries(all_entries, existing_hashes, keywords, logger)

    if not processed_entries:
        logger.info("No new entries to add after deduplication")
        return 0

    # Format output
    today = dt.date.today().isoformat()
    entry_block = format_entry_block(processed_entries, today)

    if args.dry_run:
        print("\n" + "="*70)
        print("DRY RUN — The following would be added:")
        print("="*70)
        print(entry_block)
        print("="*70)
        logger.info(f"Dry run: Would add {len(processed_entries)} entries")
        return 0

    # Append to knowledge base
    updated_content = existing_content + entry_block
    if save_knowledge_base(brain_path, updated_content, logger):
        logger.info(f"Successfully appended {len(processed_entries)} new entries")
        return 0
    else:
        logger.error("Failed to save updated knowledge base")
        return 1

if __name__ == "__main__":
    sys.exit(main())

