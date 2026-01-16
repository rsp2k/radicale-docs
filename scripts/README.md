# Documentation Migration & Validation Scripts

This directory contains Python scripts for migrating content from `ADVANCED-FEATURES.md` to the Starlight documentation site and validating Diataxis compliance.

## Scripts

### `migrate-docs.py` - Content Migration Tool

Extracts sections from the source `ADVANCED-FEATURES.md` and converts them to Starlight-compatible `.mdx` files with proper Diataxis classification.

**Features:**
- Extracts content by line ranges
- Applies Diataxis language patterns
- Generates appropriate frontmatter
- Creates target directories automatically
- Supports dry-run mode for testing

**Usage:**

```bash
# Show what would be migrated (dry run)
./scripts/migrate-docs.py --dry-run

# Migrate all sections
./scripts/migrate-docs.py

# Migrate only metrics-related sections
./scripts/migrate-docs.py --section metrics

# Migrate a specific section
./scripts/migrate-docs.py --section "Version Labels"

# Use custom source/destination paths
./scripts/migrate-docs.py --source /path/to/ADVANCED-FEATURES.md --base /path/to/radicale-docs
```

**Section Mappings:**

The script knows how to extract and categorize these sections:

| Source Section | Diataxis Type | Target Path |
|---------------|---------------|-------------|
| Prometheus Metrics | reference | `src/content/docs/reference/metrics.mdx` |
| Metrics Quick Start | tutorial | `src/content/docs/tutorials/metrics.mdx` |
| Prometheus Integration | how-to | `src/content/docs/how-to/monitoring/prometheus.mdx` |
| Enhanced VTODO Support | reference | `src/content/docs/reference/vtodo-rfc9253.mdx` |
| CardDAV Directory Gateway | reference | `src/content/docs/reference/directory-gateway.mdx` |
| LDAP Configuration | how-to | `src/content/docs/how-to/directory/ldap.mdx` |
| Active Directory Integration | how-to | `src/content/docs/how-to/directory/active-directory.mdx` |
| WebSocket Real-time Sync | reference | `src/content/docs/reference/websocket-protocol.mdx` |
| WebSocket Client Integration | tutorial | `src/content/docs/tutorials/websocket.mdx` |
| RFC 3253 Versioning | reference | `src/content/docs/reference/versioning-deltav.mdx` |
| Versioning Configuration | how-to | `src/content/docs/how-to/versioning/enable.mdx` |
| Version Labels | how-to | `src/content/docs/how-to/versioning/labels.mdx` |
| Activities (Change Sets) | how-to | `src/content/docs/how-to/versioning/activities.mdx` |
| Versioning Concepts | explanation | `src/content/docs/explanations/versioning.mdx` |

### `check-diataxis.py` - Diataxis Compliance Checker

Scans `.mdx` files to validate that content follows Diataxis principles and detects anti-patterns.

**Features:**
- Validates frontmatter completeness
- Detects Diataxis anti-patterns in content
- Infers content type from actual content
- Reports type mismatches
- Provides actionable suggestions
- Supports severity filtering

**Usage:**

```bash
# Check all documentation
./scripts/check-diataxis.py

# Check with verbose suggestions
./scripts/check-diataxis.py --verbose

# Check specific directory
./scripts/check-diataxis.py src/content/docs/tutorials/

# Check single file
./scripts/check-diataxis.py src/content/docs/reference/metrics.mdx

# Show only errors
./scripts/check-diataxis.py --severity error

# Show only warnings and errors
./scripts/check-diataxis.py --severity warning
```

**What It Checks:**

1. **Frontmatter Validation:**
   - Required fields: `title`, `description`
   - Recommended field: `diataxis_type`
   - Valid values: `tutorial`, `how-to`, `reference`, `explanation`

2. **Anti-Pattern Detection:**
   - **Tutorials** shouldn't say "you can" or "optionally" (should be prescriptive)
   - **How-tos** shouldn't say "let's learn" or explain why (should be task-focused)
   - **Reference** docs shouldn't have steps or recommendations (should be neutral)
   - **Explanations** shouldn't have commands or procedures (should be conceptual)

3. **Type Inference:**
   - Compares declared type with content analysis
   - Reports mismatches for review

4. **Structure Checks:**
   - Explanations with too many code blocks
   - Reference docs with sequential steps
   - How-tos missing prerequisites

**Example Output:**

```
src/content/docs/tutorials/first-server.mdx
  Declared type: tutorial
  2 violation(s):
    [WARNING] Line 45: Anti-pattern detected in tutorial: Tutorials should be prescriptive, not suggestive
      → Found: you can
    [INFO] Line 1: Missing typical tutorial language patterns
      → Tutorials need learning objectives

============================================================
SUMMARY
============================================================
Total files analyzed: 1
Files with violations: 1
Files with errors: 0
Total violations: 2
Type mismatches: 0

By severity:
  Errors: 0
  Warnings: 1
  Info: 1
```

## Diataxis Overview

The documentation follows the [Diataxis framework](https://diataxis.fr/), which organizes content into four types:

### Tutorial (Learning-Oriented)
- **Purpose:** Help beginners learn by doing
- **Voice:** Second person ("you will")
- **Content:** Step-by-step, complete, tested
- **Example:** "Your First Calendar Server"

### How-To Guide (Task-Oriented)
- **Purpose:** Solve specific problems
- **Voice:** Imperative ("configure", "enable")
- **Content:** Flexible, assumes knowledge
- **Example:** "Setting Up LDAP Authentication"

### Reference (Information-Oriented)
- **Purpose:** Provide technical details
- **Voice:** Third person, neutral
- **Content:** Comprehensive, structured for lookup
- **Example:** "Configuration Options"

### Explanation (Understanding-Oriented)
- **Purpose:** Explain concepts and decisions
- **Voice:** Third person, conceptual
- **Content:** Why things work, alternatives
- **Example:** "How CalDAV Scheduling Works"

## Development Workflow

### 1. Migrate Content

```bash
# Test migration with dry run
./scripts/migrate-docs.py --dry-run

# Migrate specific sections
./scripts/migrate-docs.py --section "Prometheus"
```

### 2. Review Generated Files

Check the generated `.mdx` files for:
- Correct frontmatter
- Appropriate Diataxis classification
- Clean formatting
- Working links

### 3. Validate Compliance

```bash
# Check for violations
./scripts/check-diataxis.py --verbose

# Fix violations based on suggestions
```

### 4. Manual Refinement

The scripts provide a good starting point, but manual review is essential for:
- Improving language patterns
- Restructuring content for the target type
- Adding missing elements (prerequisites, learning objectives, etc.)
- Ensuring technical accuracy

## Requirements

- Python 3.9+
- No external dependencies (uses standard library only)

## Contributing

When adding new sections to migrate:

1. Add a `Section` definition in `migrate-docs.py` with:
   - Title, line range, Diataxis type
   - Target path following Starlight conventions
   - Clear description

2. Test with `--dry-run` first

3. Update this README with the new section mapping

## Troubleshooting

### Migration Issues

**Problem:** "Invalid line range for section"
- **Solution:** Check that line numbers in `SECTIONS` list match current `ADVANCED-FEATURES.md`

**Problem:** Frontmatter not generated correctly
- **Solution:** Review `generate_frontmatter()` function for the section's Diataxis type

### Validation Issues

**Problem:** Too many false positives
- **Solution:** Adjust patterns in `ANTI_PATTERNS` dictionary or use `--severity` filter

**Problem:** Type inference incorrect
- **Solution:** Update heuristics in `CONTENT_HEURISTICS` dictionary

## License

These scripts are part of the Radicale project and follow the same GPLv3 license.
