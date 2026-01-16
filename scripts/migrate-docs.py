#!/usr/bin/env python3
"""
Radicale Documentation Migration Tool

This script extracts sections from ADVANCED-FEATURES.md and converts them
to Starlight-compatible .mdx files with proper Diataxis classification.

Usage:
    ./scripts/migrate-docs.py [--dry-run] [--section SECTION_NAME]

Examples:
    # Migrate all sections
    ./scripts/migrate-docs.py

    # Dry run to see what would be created
    ./scripts/migrate-docs.py --dry-run

    # Migrate only metrics section
    ./scripts/migrate-docs.py --section metrics
"""

import argparse
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple


@dataclass
class Section:
    """Represents a documentation section to be migrated."""
    title: str
    start_line: int
    end_line: int
    diataxis_type: str  # tutorial, how-to, reference, explanation
    target_path: str
    description: str


# Diataxis language patterns for content transformation
DIATAXIS_PATTERNS = {
    'tutorial': {
        'voice': 'second person',
        'intro_pattern': 'In this tutorial, you will',
        'avoid_words': ['you can', 'you may', 'optionally', 'alternatively'],
        'prefer_words': ['you will', 'next', 'now', 'first', 'then'],
    },
    'how-to': {
        'voice': 'imperative',
        'intro_pattern': 'This guide shows how to',
        'avoid_words': ['let\'s', 'we will', 'you will learn'],
        'prefer_words': ['configure', 'set up', 'enable', 'create'],
    },
    'reference': {
        'voice': 'third person',
        'intro_pattern': 'This page describes',
        'avoid_words': ['you should', 'we recommend', 'best practice'],
        'prefer_words': ['specifies', 'defines', 'lists', 'contains'],
    },
    'explanation': {
        'voice': 'third person',
        'intro_pattern': 'This explains',
        'avoid_words': ['step 1', 'first', 'next', 'then', 'configure'],
        'prefer_words': ['because', 'why', 'how it works', 'the reason'],
    },
}


# Section definitions mapping line ranges to target files
SECTIONS = [
    Section(
        title="Prometheus Metrics",
        start_line=38,
        end_line=230,
        diataxis_type="reference",
        target_path="src/content/docs/reference/metrics.mdx",
        description="Complete reference for Prometheus metrics exposed by Radicale"
    ),
    Section(
        title="Metrics Quick Start",
        start_line=42,
        end_line=56,
        diataxis_type="tutorial",
        target_path="src/content/docs/tutorials/metrics.mdx",
        description="Learn to set up Prometheus metrics monitoring in 5 minutes"
    ),
    Section(
        title="Prometheus Integration",
        start_line=147,
        end_line=230,
        diataxis_type="how-to",
        target_path="src/content/docs/how-to/monitoring/prometheus.mdx",
        description="Configure Prometheus to scrape Radicale metrics"
    ),
    Section(
        title="Enhanced VTODO Support",
        start_line=234,
        end_line=417,
        diataxis_type="reference",
        target_path="src/content/docs/reference/vtodo-rfc9253.mdx",
        description="RFC 9253 Task Extensions API reference"
    ),
    Section(
        title="CardDAV Directory Gateway",
        start_line=421,
        end_line=606,
        diataxis_type="reference",
        target_path="src/content/docs/reference/directory-gateway.mdx",
        description="LDAP/Active Directory integration reference"
    ),
    Section(
        title="LDAP Configuration",
        start_line=436,
        end_line=468,
        diataxis_type="how-to",
        target_path="src/content/docs/how-to/directory/ldap.mdx",
        description="Configure LDAP directory gateway for contact lookup"
    ),
    Section(
        title="Active Directory Integration",
        start_line=517,
        end_line=551,
        diataxis_type="how-to",
        target_path="src/content/docs/how-to/directory/active-directory.mdx",
        description="Integrate Radicale with Microsoft Active Directory"
    ),
    Section(
        title="WebSocket Real-time Sync",
        start_line=610,
        end_line=962,
        diataxis_type="reference",
        target_path="src/content/docs/reference/websocket-protocol.mdx",
        description="WebSocket real-time sync protocol specification"
    ),
    Section(
        title="WebSocket Client Integration",
        start_line=785,
        end_line=944,
        diataxis_type="tutorial",
        target_path="src/content/docs/tutorials/websocket.mdx",
        description="Build a WebSocket sync client for real-time updates"
    ),
    Section(
        title="RFC 3253 Versioning",
        start_line=965,
        end_line=1788,
        diataxis_type="reference",
        target_path="src/content/docs/reference/versioning-deltav.mdx",
        description="RFC 3253 DeltaV versioning protocol reference"
    ),
    Section(
        title="Versioning Configuration",
        start_line=979,
        end_line=1023,
        diataxis_type="how-to",
        target_path="src/content/docs/how-to/versioning/enable.mdx",
        description="Enable and configure git-backed versioning"
    ),
    Section(
        title="Version Labels",
        start_line=1356,
        end_line=1528,
        diataxis_type="how-to",
        target_path="src/content/docs/how-to/versioning/labels.mdx",
        description="Use version labels for release management"
    ),
    Section(
        title="Activities (Change Sets)",
        start_line=1530,
        end_line=1788,
        diataxis_type="how-to",
        target_path="src/content/docs/how-to/versioning/activities.mdx",
        description="Group related changes into activities"
    ),
    Section(
        title="Versioning Concepts",
        start_line=969,
        end_line=977,
        diataxis_type="explanation",
        target_path="src/content/docs/explanations/versioning.mdx",
        description="Understanding DeltaV versioning and when to use it"
    ),
]


def read_source_file(source_path: Path) -> List[str]:
    """Read the source markdown file and return lines."""
    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Error: Source file not found: {source_path}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading source file: {e}", file=sys.stderr)
        sys.exit(1)


def extract_section(lines: List[str], section: Section) -> str:
    """Extract content for a section based on line numbers."""
    # Line numbers are 1-indexed in the file, 0-indexed in list
    start_idx = section.start_line - 1
    end_idx = section.end_line

    if start_idx < 0 or end_idx > len(lines):
        raise ValueError(f"Invalid line range for section '{section.title}': {section.start_line}-{section.end_line}")

    content_lines = lines[start_idx:end_idx]
    return ''.join(content_lines)


def apply_diataxis_patterns(content: str, diataxis_type: str) -> str:
    """Apply Diataxis language patterns to content."""
    patterns = DIATAXIS_PATTERNS.get(diataxis_type, {})

    # This is a simplified transformation - in practice, more sophisticated
    # NLP or manual review would be needed for complete conversion

    if diataxis_type == 'tutorial':
        # Convert passive instructions to active learning voice
        content = re.sub(r'^(.*?) can be (.+?)$', r'You will \2', content, flags=re.MULTILINE)

    elif diataxis_type == 'how-to':
        # Convert explanatory text to imperative instructions
        content = re.sub(r'^To (.+?), (.+?)$', r'\2 to \1', content, flags=re.MULTILINE)

    elif diataxis_type == 'reference':
        # Ensure technical precision and third-person voice
        content = re.sub(r'\bYou can\b', 'This', content)
        content = re.sub(r'\bYou should\b', 'Use', content)

    elif diataxis_type == 'explanation':
        # Add conceptual framing
        # (Most transformations require semantic understanding)
        pass

    return content


def clean_markdown_for_mdx(content: str) -> str:
    """Clean markdown content for MDX compatibility."""
    # Remove internal anchor links that may not work in Starlight
    content = re.sub(r'\{#[a-z0-9-]+\}', '', content)

    # Ensure code blocks have language specified
    content = re.sub(r'^```\s*$', '```text', content, flags=re.MULTILINE)

    return content


def generate_frontmatter(section: Section) -> str:
    """Generate YAML frontmatter for MDX file."""
    frontmatter = f"""---
title: {section.title}
description: {section.description}
diataxis_type: {section.diataxis_type}
"""

    # Add type-specific frontmatter
    if section.diataxis_type == 'tutorial':
        frontmatter += "difficulty: beginner\n"
        frontmatter += "time: 15 minutes\n"
    elif section.diataxis_type == 'how-to':
        frontmatter += "prerequisites:\n"
        frontmatter += "  - Basic Radicale configuration knowledge\n"
    elif section.diataxis_type == 'reference':
        frontmatter += "sidebar:\n"
        frontmatter += "  order: 10\n"

    frontmatter += "---\n\n"

    return frontmatter


def add_diataxis_intro(section: Section, content: str) -> str:
    """Add Diataxis-appropriate introduction to content."""
    patterns = DIATAXIS_PATTERNS.get(section.diataxis_type, {})
    intro_pattern = patterns.get('intro_pattern', '')

    # Check if content already has an intro paragraph
    lines = content.split('\n')
    if lines and lines[0].startswith('##'):
        # Insert intro before first heading
        intro = f"{intro_pattern} {section.title.lower()}.\n\n"
        return intro + content

    return content


def write_output_file(target_path: Path, content: str, dry_run: bool = False) -> None:
    """Write content to target file, creating directories as needed."""
    if dry_run:
        print(f"[DRY RUN] Would write to: {target_path}")
        print(f"[DRY RUN] Content preview (first 200 chars):\n{content[:200]}...\n")
        return

    try:
        target_path.parent.mkdir(parents=True, exist_ok=True)
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Created: {target_path}")
    except Exception as e:
        print(f"✗ Error writing {target_path}: {e}", file=sys.stderr)


def migrate_section(
    source_lines: List[str],
    section: Section,
    base_path: Path,
    dry_run: bool = False
) -> None:
    """Migrate a single section to its target location."""
    print(f"\nProcessing: {section.title} ({section.diataxis_type})")
    print(f"  Lines: {section.start_line}-{section.end_line}")
    print(f"  Target: {section.target_path}")

    try:
        # Extract content
        content = extract_section(source_lines, section)

        # Apply transformations
        content = apply_diataxis_patterns(content, section.diataxis_type)
        content = clean_markdown_for_mdx(content)
        content = add_diataxis_intro(section, content)

        # Generate frontmatter
        frontmatter = generate_frontmatter(section)

        # Combine frontmatter and content
        full_content = frontmatter + content

        # Write to target
        target_path = base_path / section.target_path
        write_output_file(target_path, full_content, dry_run)

    except Exception as e:
        print(f"✗ Error processing section '{section.title}': {e}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description='Migrate ADVANCED-FEATURES.md content to Starlight docs',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without writing files'
    )
    parser.add_argument(
        '--section',
        type=str,
        help='Migrate only the specified section (by title substring match)'
    )
    parser.add_argument(
        '--source',
        type=Path,
        default=Path('/home/rpm/claude/radicale/Radicale/ADVANCED-FEATURES.md'),
        help='Path to source ADVANCED-FEATURES.md file'
    )
    parser.add_argument(
        '--base',
        type=Path,
        default=Path('/home/rpm/claude/radicale/radicale-docs'),
        help='Base path for radicale-docs project'
    )

    args = parser.parse_args()

    # Read source file
    print(f"Reading source: {args.source}")
    source_lines = read_source_file(args.source)
    print(f"Loaded {len(source_lines)} lines")

    # Filter sections if requested
    sections_to_migrate = SECTIONS
    if args.section:
        sections_to_migrate = [
            s for s in SECTIONS
            if args.section.lower() in s.title.lower()
        ]
        if not sections_to_migrate:
            print(f"No sections found matching: {args.section}", file=sys.stderr)
            sys.exit(1)

    print(f"\nMigrating {len(sections_to_migrate)} section(s)...")

    # Migrate each section
    for section in sections_to_migrate:
        migrate_section(source_lines, section, args.base, args.dry_run)

    print(f"\n{'[DRY RUN] ' if args.dry_run else ''}Migration complete!")
    print(f"Processed {len(sections_to_migrate)} section(s)")

    if args.dry_run:
        print("\nRun without --dry-run to actually create files.")


if __name__ == '__main__':
    main()
