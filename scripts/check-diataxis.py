#!/usr/bin/env python3
"""
Diataxis Compliance Checker

This script scans .mdx files in the Starlight docs to validate that content
follows Diataxis principles and patterns.

Usage:
    ./scripts/check-diataxis.py [--fix] [--verbose] [path/to/docs/]

Examples:
    # Check all docs
    ./scripts/check-diataxis.py

    # Check specific directory
    ./scripts/check-diataxis.py src/content/docs/tutorials/

    # Verbose output with suggestions
    ./scripts/check-diataxis.py --verbose

    # Auto-fix frontmatter issues (experimental)
    ./scripts/check-diataxis.py --fix
"""

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple


@dataclass
class Violation:
    """Represents a Diataxis compliance violation."""
    file_path: Path
    line_number: int
    severity: str  # error, warning, info
    category: str  # frontmatter, language, structure
    message: str
    suggestion: Optional[str] = None


@dataclass
class FileAnalysis:
    """Analysis results for a single file."""
    file_path: Path
    declared_type: Optional[str] = None
    inferred_type: Optional[str] = None
    violations: List[Violation] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    @property
    def has_errors(self) -> bool:
        return any(v.severity == 'error' for v in self.violations)

    @property
    def type_mismatch(self) -> bool:
        return (
            self.declared_type and self.inferred_type
            and self.declared_type != self.inferred_type
        )


# Diataxis anti-patterns: phrases that violate the content type principles
ANTI_PATTERNS = {
    'tutorial': {
        'forbidden_phrases': [
            (r'\b(?:you can|you may|optionally|alternatively)\b', 'Tutorials should be prescriptive, not suggestive'),
            (r'\b(?:if you want to|you might)\b', 'Tutorials guide, not offer choices'),
            (r'\bconsider\b', 'Tutorials direct, not suggest options'),
            (r'\bvarious ways\b', 'Tutorials show one clear path'),
        ],
        'required_elements': [
            (r'(?:you will|we will|let\'s)', 'Tutorials need learning objectives'),
        ],
        'structure': [
            'Should have clear steps',
            'Should build toward a working result',
            'Should be complete and tested',
        ],
    },
    'how-to': {
        'forbidden_phrases': [
            (r'\b(?:let\'s|we will learn|you will learn)\b', 'How-tos are task-focused, not learning-focused'),
            (r'\b(?:understand|learn about|concept)\b', 'How-tos solve problems, not explain concepts'),
            (r'\bwhy\b(?! not)', 'How-tos focus on how, not why'),
            (r'\b(?:first|then|next|finally)\b.*\b(?:first|then|next|finally)\b', 'Too tutorial-like with sequential steps'),
        ],
        'required_elements': [
            (r'(?:configure|set up|enable|create|add|remove)', 'How-tos need action verbs'),
        ],
        'structure': [
            'Should solve a specific problem',
            'Should be flexible in approach',
            'Should assume some knowledge',
        ],
    },
    'reference': {
        'forbidden_phrases': [
            (r'\b(?:you should|we recommend|best practice)\b', 'Reference docs are neutral, not prescriptive'),
            (r'\b(?:step 1|step 2|first|then|next)\b', 'Reference docs don\'t have steps'),
            (r'\b(?:tutorial|learn|how to)\b', 'Reference docs are lookup, not instructional'),
        ],
        'required_elements': [
            (r'(?:specifies|defines|contains|includes|lists)', 'Reference docs need factual language'),
        ],
        'structure': [
            'Should be comprehensive',
            'Should be structured for lookup',
            'Should be precise and accurate',
        ],
    },
    'explanation': {
        'forbidden_phrases': [
            (r'\b(?:step 1|step 2|configure|enable|create)\b', 'Explanations discuss concepts, not procedures'),
            (r'\b(?:you should|you must|required)\b', 'Explanations inform, not instruct'),
            (r'\bcurl -X\b', 'Explanations explain, don\'t show commands'),
        ],
        'required_elements': [
            (r'(?:because|why|reason|how .* works)', 'Explanations need conceptual framing'),
        ],
        'structure': [
            'Should provide understanding',
            'Should discuss alternatives',
            'Should connect concepts',
        ],
    },
}


# Heuristics for inferring content type from actual content
CONTENT_HEURISTICS = {
    'tutorial': {
        'indicators': [
            r'in this tutorial',
            r'you will (?:learn|build|create)',
            r'by the end of this',
            r'step \d+',
            r'let\'s (?:start|begin|create)',
        ],
        'weight': 1.0,
    },
    'how-to': {
        'indicators': [
            r'this guide shows',
            r'to (?:configure|enable|set up)',
            r'prerequisites?:',
            r'(?:^|\n)## Prerequisites',
            r'follow these steps',
        ],
        'weight': 1.0,
    },
    'reference': {
        'indicators': [
            r'(?:^|\n)## (?:Options|Parameters|Properties|Methods)',
            r'\| .+ \| .+ \|',  # Tables
            r'returns?:',
            r'parameters?:',
            r'this (?:page|section) describes',
        ],
        'weight': 1.0,
    },
    'explanation': {
        'indicators': [
            r'why (?:does|is|should)',
            r'because',
            r'the reason',
            r'how .* works?',
            r'understanding',
        ],
        'weight': 1.0,
    },
}


def extract_frontmatter(content: str) -> Tuple[Optional[Dict[str, str]], int]:
    """Extract YAML frontmatter from content. Returns (frontmatter_dict, end_line)."""
    if not content.startswith('---\n'):
        return None, 0

    # Find end of frontmatter
    end_match = re.search(r'\n---\n', content[4:])
    if not end_match:
        return None, 0

    end_pos = end_match.start() + 4
    frontmatter_text = content[4:end_pos]
    end_line = content[:end_pos + 4].count('\n')

    # Parse frontmatter (simplified - doesn't handle complex YAML)
    frontmatter = {}
    for line in frontmatter_text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            frontmatter[key.strip()] = value.strip()

    return frontmatter, end_line


def infer_content_type(content: str) -> Optional[str]:
    """Infer the Diataxis type from content using heuristics."""
    scores: Dict[str, float] = {
        'tutorial': 0,
        'how-to': 0,
        'reference': 0,
        'explanation': 0,
    }

    content_lower = content.lower()

    for content_type, config in CONTENT_HEURISTICS.items():
        for pattern in config['indicators']:
            matches = len(re.findall(pattern, content_lower, re.IGNORECASE))
            scores[content_type] += matches * config['weight']

    if max(scores.values()) > 0:
        return max(scores, key=scores.get)

    return None


def check_frontmatter(file_path: Path, content: str) -> List[Violation]:
    """Check frontmatter for required Diataxis fields."""
    violations = []

    frontmatter, _ = extract_frontmatter(content)

    if not frontmatter:
        violations.append(Violation(
            file_path=file_path,
            line_number=1,
            severity='error',
            category='frontmatter',
            message='Missing YAML frontmatter',
            suggestion='Add frontmatter with at least: title, description, diataxis_type'
        ))
        return violations

    # Check for required fields
    required_fields = ['title', 'description']
    for field in required_fields:
        if field not in frontmatter:
            violations.append(Violation(
                file_path=file_path,
                line_number=1,
                severity='error',
                category='frontmatter',
                message=f"Missing required field: {field}",
                suggestion=f"Add '{field}: <value>' to frontmatter"
            ))

    # Check for diataxis_type
    if 'diataxis_type' not in frontmatter:
        violations.append(Violation(
            file_path=file_path,
            line_number=1,
            severity='warning',
            category='frontmatter',
            message='Missing diataxis_type field',
            suggestion="Add 'diataxis_type: tutorial|how-to|reference|explanation'"
        ))
    else:
        diataxis_type = frontmatter['diataxis_type']
        if diataxis_type not in ['tutorial', 'how-to', 'reference', 'explanation']:
            violations.append(Violation(
                file_path=file_path,
                line_number=1,
                severity='error',
                category='frontmatter',
                message=f"Invalid diataxis_type: {diataxis_type}",
                suggestion="Use one of: tutorial, how-to, reference, explanation"
            ))

    return violations


def check_content_patterns(
    file_path: Path,
    content: str,
    declared_type: Optional[str]
) -> List[Violation]:
    """Check content for anti-patterns based on declared type."""
    violations = []

    if not declared_type or declared_type not in ANTI_PATTERNS:
        return violations

    patterns = ANTI_PATTERNS[declared_type]
    lines = content.split('\n')

    # Check forbidden phrases
    for pattern, reason in patterns.get('forbidden_phrases', []):
        for line_num, line in enumerate(lines, 1):
            if re.search(pattern, line, re.IGNORECASE):
                violations.append(Violation(
                    file_path=file_path,
                    line_number=line_num,
                    severity='warning',
                    category='language',
                    message=f"Anti-pattern detected in {declared_type}: {reason}",
                    suggestion=f"Found: {re.search(pattern, line, re.IGNORECASE).group()}"
                ))

    # Check for required elements (at least one should be present)
    required_found = False
    for pattern, reason in patterns.get('required_elements', []):
        if re.search(pattern, content, re.IGNORECASE):
            required_found = True
            break

    if not required_found and patterns.get('required_elements'):
        violations.append(Violation(
            file_path=file_path,
            line_number=1,
            severity='info',
            category='language',
            message=f"Missing typical {declared_type} language patterns",
            suggestion=patterns['required_elements'][0][1]
        ))

    return violations


def check_structure(
    file_path: Path,
    content: str,
    declared_type: Optional[str]
) -> List[Violation]:
    """Check document structure for Diataxis compliance."""
    violations = []

    if not declared_type:
        return violations

    # Check for code blocks in explanations (usually inappropriate)
    if declared_type == 'explanation':
        code_blocks = re.findall(r'```[\s\S]+?```', content)
        if len(code_blocks) > 2:
            violations.append(Violation(
                file_path=file_path,
                line_number=1,
                severity='warning',
                category='structure',
                message='Explanation has many code blocks - consider moving to how-to',
                suggestion='Explanations should focus on concepts, not procedures'
            ))

    # Check for step-by-step in reference docs
    if declared_type == 'reference':
        step_pattern = r'(?:step \d+|first,|then,|finally,)'
        if re.search(step_pattern, content, re.IGNORECASE):
            violations.append(Violation(
                file_path=file_path,
                line_number=1,
                severity='warning',
                category='structure',
                message='Reference doc has step-by-step instructions',
                suggestion='Reference docs should be organized for lookup, not sequential reading'
            ))

    # Check for missing prerequisites in how-to
    if declared_type == 'how-to':
        if not re.search(r'prerequisite|before you begin|you need', content, re.IGNORECASE):
            violations.append(Violation(
                file_path=file_path,
                line_number=1,
                severity='info',
                category='structure',
                message='How-to guide missing prerequisites section',
                suggestion='Add a prerequisites section to set expectations'
            ))

    return violations


def analyze_file(file_path: Path, verbose: bool = False) -> FileAnalysis:
    """Analyze a single MDX file for Diataxis compliance."""
    analysis = FileAnalysis(file_path=file_path)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        analysis.violations.append(Violation(
            file_path=file_path,
            line_number=0,
            severity='error',
            category='file',
            message=f"Error reading file: {e}"
        ))
        return analysis

    # Extract declared type from frontmatter
    frontmatter, _ = extract_frontmatter(content)
    if frontmatter and 'diataxis_type' in frontmatter:
        analysis.declared_type = frontmatter['diataxis_type']

    # Infer type from content
    analysis.inferred_type = infer_content_type(content)

    # Run checks
    analysis.violations.extend(check_frontmatter(file_path, content))
    analysis.violations.extend(check_content_patterns(file_path, content, analysis.declared_type))
    analysis.violations.extend(check_structure(file_path, content, analysis.declared_type))

    # Check for type mismatch
    if analysis.type_mismatch:
        analysis.violations.append(Violation(
            file_path=file_path,
            line_number=1,
            severity='warning',
            category='frontmatter',
            message=f"Type mismatch: declared as '{analysis.declared_type}' but content suggests '{analysis.inferred_type}'",
            suggestion=f"Review content or update diataxis_type to '{analysis.inferred_type}'"
        ))

    if verbose and analysis.inferred_type:
        analysis.warnings.append(f"Inferred type: {analysis.inferred_type}")

    return analysis


def format_violation_report(analysis: FileAnalysis, verbose: bool = False) -> str:
    """Format violation report for display."""
    if not analysis.violations and not verbose:
        return ""

    lines = [f"\n{analysis.file_path}"]

    if analysis.declared_type:
        lines.append(f"  Declared type: {analysis.declared_type}")
    if verbose and analysis.inferred_type:
        lines.append(f"  Inferred type: {analysis.inferred_type}")

    if analysis.violations:
        lines.append(f"  {len(analysis.violations)} violation(s):")

        # Group by severity
        errors = [v for v in analysis.violations if v.severity == 'error']
        warnings = [v for v in analysis.violations if v.severity == 'warning']
        infos = [v for v in analysis.violations if v.severity == 'info']

        for severity, violations in [('ERROR', errors), ('WARNING', warnings), ('INFO', infos)]:
            for v in violations:
                lines.append(f"    [{severity}] Line {v.line_number}: {v.message}")
                if verbose and v.suggestion:
                    lines.append(f"      → {v.suggestion}")

    return '\n'.join(lines)


def scan_directory(base_path: Path, verbose: bool = False) -> List[FileAnalysis]:
    """Scan directory for MDX files and analyze each."""
    results = []

    mdx_files = sorted(base_path.rglob('*.mdx'))
    print(f"Found {len(mdx_files)} .mdx file(s) to analyze...")

    for file_path in mdx_files:
        if verbose:
            print(f"Analyzing: {file_path.relative_to(base_path)}")

        analysis = analyze_file(file_path, verbose)
        results.append(analysis)

    return results


def print_summary(results: List[FileAnalysis]) -> None:
    """Print summary statistics."""
    total_files = len(results)
    files_with_errors = sum(1 for r in results if r.has_errors)
    files_with_violations = sum(1 for r in results if r.violations)
    total_violations = sum(len(r.violations) for r in results)

    type_mismatches = sum(1 for r in results if r.type_mismatch)

    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print(f"Total files analyzed: {total_files}")
    print(f"Files with violations: {files_with_violations}")
    print(f"Files with errors: {files_with_errors}")
    print(f"Total violations: {total_violations}")
    print(f"Type mismatches: {type_mismatches}")

    # Count by severity
    errors = sum(sum(1 for v in r.violations if v.severity == 'error') for r in results)
    warnings = sum(sum(1 for v in r.violations if v.severity == 'warning') for r in results)
    infos = sum(sum(1 for v in r.violations if v.severity == 'info') for r in results)

    print(f"\nBy severity:")
    print(f"  Errors: {errors}")
    print(f"  Warnings: {warnings}")
    print(f"  Info: {infos}")

    # Type distribution
    type_counts: Dict[str, int] = {}
    for r in results:
        if r.declared_type:
            type_counts[r.declared_type] = type_counts.get(r.declared_type, 0) + 1

    if type_counts:
        print(f"\nDiataxis type distribution:")
        for dtype, count in sorted(type_counts.items()):
            print(f"  {dtype}: {count}")


def main():
    parser = argparse.ArgumentParser(
        description='Check Diataxis compliance for Starlight documentation',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        'path',
        nargs='?',
        type=Path,
        default=Path('/home/rpm/claude/radicale/radicale-docs/src/content/docs'),
        help='Path to docs directory or specific file'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show detailed analysis including suggestions'
    )
    parser.add_argument(
        '--fix',
        action='store_true',
        help='Attempt to auto-fix violations (experimental)'
    )
    parser.add_argument(
        '--severity',
        choices=['error', 'warning', 'info', 'all'],
        default='all',
        help='Minimum severity level to report'
    )

    args = parser.parse_args()

    if not args.path.exists():
        print(f"Error: Path does not exist: {args.path}", file=sys.stderr)
        sys.exit(1)

    # Scan files
    if args.path.is_file():
        results = [analyze_file(args.path, args.verbose)]
    else:
        results = scan_directory(args.path, args.verbose)

    # Filter by severity
    severity_levels = {'error': 3, 'warning': 2, 'info': 1}
    min_severity = severity_levels.get(args.severity, 0)

    # Print violations
    has_output = False
    for analysis in results:
        if args.severity != 'all':
            # Filter violations by severity
            analysis.violations = [
                v for v in analysis.violations
                if severity_levels[v.severity] >= min_severity
            ]

        report = format_violation_report(analysis, args.verbose)
        if report:
            print(report)
            has_output = True

    if not has_output:
        print("\n✓ No violations found!")

    # Print summary
    print_summary(results)

    # Exit code based on errors
    has_errors = any(r.has_errors for r in results)
    sys.exit(1 if has_errors else 0)


if __name__ == '__main__':
    main()
