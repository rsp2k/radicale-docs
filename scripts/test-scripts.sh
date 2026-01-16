#!/bin/bash
# Test script demonstrating migrate-docs.py and check-diataxis.py functionality

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.."

echo "==========================================="
echo "Testing Radicale Documentation Scripts"
echo "==========================================="
echo ""

# Test 1: Check help messages
echo "Test 1: Verifying help messages work..."
python3 scripts/migrate-docs.py --help > /dev/null
python3 scripts/check-diataxis.py --help > /dev/null
echo "✓ Both scripts have working help"
echo ""

# Test 2: Dry run migration
echo "Test 2: Testing migration dry run..."
python3 scripts/migrate-docs.py --dry-run --section "Metrics Quick Start" 2>&1 | grep -q "DRY RUN"
echo "✓ Dry run mode works"
echo ""

# Test 3: Check existing docs
echo "Test 3: Checking Diataxis compliance..."
python3 scripts/check-diataxis.py --severity error > /dev/null
echo "✓ No critical errors in documentation"
echo ""

# Test 4: Verbose checking
echo "Test 4: Running verbose compliance check..."
OUTPUT=$(python3 scripts/check-diataxis.py --verbose 2>&1 | tail -20)
echo "$OUTPUT" | grep -q "SUMMARY"
echo "✓ Verbose checking works and produces summary"
echo ""

# Test 5: Section-specific migration
echo "Test 5: Testing section filtering..."
python3 scripts/migrate-docs.py --dry-run --section "metrics" 2>&1 | grep -q "Migrating.*section"
echo "✓ Section filtering works"
echo ""

echo "==========================================="
echo "All tests passed!"
echo "==========================================="
echo ""
echo "Next steps:"
echo "  1. Run: ./scripts/migrate-docs.py --dry-run"
echo "     (Review what would be migrated)"
echo ""
echo "  2. Run: ./scripts/migrate-docs.py --section 'section-name'"
echo "     (Migrate specific sections)"
echo ""
echo "  3. Run: ./scripts/check-diataxis.py --verbose"
echo "     (Check for Diataxis compliance)"
echo ""
echo "  4. Review and manually refine generated content"
echo ""
