# Script Usage Examples

This document provides practical examples of using the migration and validation scripts.

## Quick Start

```bash
# Test everything works
./scripts/test-scripts.sh

# See what would be migrated
./scripts/migrate-docs.py --dry-run

# Check current documentation quality
./scripts/check-diataxis.py --verbose
```

## Migration Examples

### Example 1: Migrate All Sections

```bash
# First, do a dry run to see what will happen
./scripts/migrate-docs.py --dry-run

# Review the output, then migrate for real
./scripts/migrate-docs.py
```

**Output:**
```
Reading source: /home/rpm/claude/radicale/Radicale/ADVANCED-FEATURES.md
Loaded 2001 lines

Migrating 14 section(s)...

Processing: Prometheus Metrics (reference)
  Lines: 38-230
  Target: src/content/docs/reference/metrics.mdx
✓ Created: /home/rpm/claude/radicale/radicale-docs/src/content/docs/reference/metrics.mdx

Processing: Metrics Quick Start (tutorial)
  Lines: 42-56
  Target: src/content/docs/tutorials/metrics.mdx
✓ Created: /home/rpm/claude/radicale/radicale-docs/src/content/docs/tutorials/metrics.mdx

...

Migration complete!
Processed 14 section(s)
```

### Example 2: Migrate Specific Feature

Let's say you want to migrate just the WebSocket documentation:

```bash
# See what WebSocket sections exist
./scripts/migrate-docs.py --dry-run | grep -i websocket

# Migrate all WebSocket-related sections
./scripts/migrate-docs.py --section websocket
```

**Output:**
```
Migrating 2 section(s)...

Processing: WebSocket Real-time Sync (reference)
  Lines: 610-962
  Target: src/content/docs/reference/websocket-protocol.mdx
✓ Created: /home/rpm/claude/radicale/radicale-docs/src/content/docs/reference/websocket-protocol.mdx

Processing: WebSocket Client Integration (tutorial)
  Lines: 785-944
  Target: src/content/docs/tutorials/websocket.mdx
✓ Created: /home/rpm/claude/radicale/radicale-docs/src/content/docs/tutorials/websocket.mdx

Migration complete!
Processed 2 section(s)
```

### Example 3: Migrate One Specific Section

```bash
# Migrate only the "Version Labels" how-to guide
./scripts/migrate-docs.py --section "Version Labels"
```

**Output:**
```
Migrating 1 section(s)...

Processing: Version Labels (how-to)
  Lines: 1356-1528
  Target: src/content/docs/how-to/versioning/labels.mdx
✓ Created: /home/rpm/claude/radicale/radicale-docs/src/content/docs/how-to/versioning/labels.mdx

Migration complete!
Processed 1 section(s)
```

### Example 4: Custom Source Path

If you're working with a different branch or fork:

```bash
./scripts/migrate-docs.py \
  --source /path/to/different/ADVANCED-FEATURES.md \
  --base /path/to/different/radicale-docs \
  --section "Prometheus"
```

## Validation Examples

### Example 1: Check All Documentation

```bash
# Basic check (shows violations only)
./scripts/check-diataxis.py

# Verbose (shows inferred types and suggestions)
./scripts/check-diataxis.py --verbose
```

**Output:**
```
Found 7 .mdx file(s) to analyze...

/home/rpm/claude/radicale/radicale-docs/src/content/docs/index.mdx
  1 violation(s):
    [WARNING] Line 1: Missing diataxis_type field
      → Add 'diataxis_type: tutorial|how-to|reference|explanation'

/home/rpm/claude/radicale/radicale-docs/src/content/docs/tutorials/first-server.mdx
  Declared type: tutorial
  Inferred type: tutorial
  3 violation(s):
    [WARNING] Line 13: Anti-pattern detected in tutorial: Tutorials should be prescriptive, not suggestive
      → Found: you can
    [WARNING] Line 134: Anti-pattern detected in tutorial: Tutorials should be prescriptive, not suggestive
      → Found: you can
    [INFO] Line 1: Missing typical tutorial language patterns
      → Tutorials need learning objectives

============================================================
SUMMARY
============================================================
Total files analyzed: 7
Files with violations: 2
Files with errors: 0
Total violations: 4
Type mismatches: 0

By severity:
  Errors: 0
  Warnings: 3
  Info: 1

Diataxis type distribution:
  tutorial: 3
```

### Example 2: Check Specific Directory

```bash
# Check only tutorials
./scripts/check-diataxis.py src/content/docs/tutorials/ --verbose

# Check only reference docs
./scripts/check-diataxis.py src/content/docs/reference/

# Check only how-to guides
./scripts/check-diataxis.py src/content/docs/how-to/
```

### Example 3: Check Single File

```bash
# Check a specific file after editing
./scripts/check-diataxis.py src/content/docs/tutorials/metrics.mdx --verbose
```

**Output:**
```
src/content/docs/tutorials/metrics.mdx
  Declared type: tutorial
  Inferred type: tutorial

============================================================
SUMMARY
============================================================
Total files analyzed: 1
Files with violations: 0
Files with errors: 0
Total violations: 0
Type mismatches: 0
```

### Example 4: Filter by Severity

```bash
# Show only errors (critical issues that must be fixed)
./scripts/check-diataxis.py --severity error

# Show warnings and errors (skip info)
./scripts/check-diataxis.py --severity warning

# Show everything including suggestions
./scripts/check-diataxis.py --severity info --verbose
```

**Example Error Output:**
```
src/content/docs/tutorials/broken.mdx
  2 violation(s):
    [ERROR] Line 1: Missing required field: title
      → Add 'title: <value>' to frontmatter
    [ERROR] Line 1: Invalid diataxis_type: guide
      → Use one of: tutorial, how-to, reference, explanation

============================================================
SUMMARY
============================================================
Total files analyzed: 1
Files with violations: 1
Files with errors: 2
Total violations: 2
```

## Complete Workflow Example

Here's a complete workflow for migrating and validating content:

### Step 1: Preview Migration

```bash
# See everything that would be migrated
./scripts/migrate-docs.py --dry-run | less
```

### Step 2: Migrate in Stages

```bash
# Start with reference docs (usually easiest)
./scripts/migrate-docs.py --section "Prometheus Metrics"
./scripts/migrate-docs.py --section "VTODO"
./scripts/migrate-docs.py --section "Directory Gateway"

# Then tutorials
./scripts/migrate-docs.py --section "Quick Start"
./scripts/migrate-docs.py --section "WebSocket Client"

# Then how-to guides
./scripts/migrate-docs.py --section "LDAP Configuration"
./scripts/migrate-docs.py --section "Active Directory"

# Finally explanations
./scripts/migrate-docs.py --section "Versioning Concepts"
```

### Step 3: Check Each Migration

```bash
# Check what you just migrated
./scripts/check-diataxis.py src/content/docs/reference/metrics.mdx --verbose
```

### Step 4: Review and Fix Violations

When the checker reports violations:

```bash
# Example violation: Tutorial uses "you can"
# Line 45: Anti-pattern detected in tutorial: Tutorials should be prescriptive, not suggestive
#   → Found: you can

# Open the file and change:
# ❌ "You can enable metrics by..."
# ✅ "Enable metrics by..."

# Or for tutorial voice:
# ✅ "You will enable metrics by..."
```

### Step 5: Validate Everything

```bash
# Final check of all documentation
./scripts/check-diataxis.py --verbose

# Make sure no errors remain
./scripts/check-diataxis.py --severity error
```

## Common Issues and Solutions

### Issue: Too Many Anti-Pattern Warnings

**Problem:** The checker reports many "you can" violations in tutorials.

**Solution:** Tutorials should be prescriptive. Change:
- "You can configure..." → "Configure..." or "You will configure..."
- "Optionally, you can..." → Remove optional steps or create separate advanced tutorial

### Issue: Type Mismatch Detected

**Problem:** Checker says "declared as 'tutorial' but content suggests 'how-to'"

**Example:**
```
Type mismatch: declared as 'tutorial' but content suggests 'how-to'
  → Review content or update diataxis_type to 'how-to'
```

**Solution:** Review the content:
- If it's step-by-step learning → Keep as tutorial, add learning objectives
- If it's solving a specific problem → Change to how-to guide

### Issue: Missing Prerequisites

**Problem:** How-to guide doesn't list prerequisites.

**Solution:** Add a prerequisites section:
```mdx
---
title: Configure LDAP Authentication
description: Set up LDAP authentication for Radicale
diataxis_type: how-to
---

## Prerequisites

Before you begin, ensure you have:
- Radicale 3.5.0 or later installed
- Access to an LDAP server
- Basic understanding of LDAP concepts

## Configuration
...
```

### Issue: Reference Doc Has Steps

**Problem:** Reference documentation includes procedural steps.

**Solution:** Move procedures to a how-to guide:
- Keep options, parameters, and specifications in reference
- Extract "how to use this" into a separate how-to guide

## Integration with CI/CD

Add these checks to your CI pipeline:

```yaml
# .github/workflows/docs-quality.yml
name: Documentation Quality

on: [pull_request]

jobs:
  check-diataxis:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Check Diataxis Compliance
        run: |
          python3 scripts/check-diataxis.py --severity error
          if [ $? -ne 0 ]; then
            echo "❌ Documentation has Diataxis compliance errors"
            exit 1
          fi
```

## Tips for Manual Refinement

After migration, manually refine content:

### For Tutorials
- Add clear learning objectives at the start
- Ensure every step is tested and works
- Remove optional paths (one clear route only)
- Include expected output for each step

### For How-To Guides
- Focus on solving one specific problem
- Assume reader knowledge (link to prerequisites)
- Allow flexibility (multiple approaches OK)
- Use imperative mood consistently

### For Reference
- Organize for quick lookup (tables, lists)
- Be comprehensive and accurate
- Use neutral, third-person voice
- No opinions or recommendations

### For Explanations
- Focus on "why" not "how"
- Discuss alternatives and trade-offs
- Connect concepts together
- Minimal or no code examples

## Getting Help

- See `README.md` for detailed documentation
- Run `./scripts/test-scripts.sh` to verify setup
- Check script help: `--help` flag on both scripts
