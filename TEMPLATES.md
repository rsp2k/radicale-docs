# Diátaxis Templates for Radicale Documentation

This document provides templates for each Diátaxis documentation type, showcasing Starlight components while maintaining strict boundaries.

## Template Structure

Each template demonstrates:
- Appropriate frontmatter metadata
- Starlight components suitable for the type
- Language patterns specific to the mental state
- Common boundary violations to avoid

## Key Starlight Components by Type

### Tutorials (Learning-Oriented)
- **Steps**: Sequential learning progression
- **Code**: Complete, working examples
- **Aside (note)**: Brief contextual notes
- **Avoid**: Tabs (creates choice paralysis), Aside (caution/danger)

### How-To Guides (Problem-Oriented)
- **Tabs**: Multiple solution paths
- **Aside (tip/caution)**: Real-world warnings
- **Code**: Practical snippets
- **Avoid**: Steps (implies single path), lengthy explanations

### Reference (Information-Oriented)
- **Code**: Syntax examples
- **Tables**: Parameter listings
- **LinkCard**: Related references
- **Avoid**: Aside (too opinionated), Steps (implies instruction)

### Explanations (Understanding-Oriented)
- **Card/CardGrid**: Conceptual organization
- **Aside (note/tip)**: Informed opinions
- **Diagrams**: Mental models
- **Avoid**: Steps, specific instructions, code snippets

---

## Tutorial Template

```mdx
---
title: Tutorial Title (Action-Oriented, e.g., "Build Your First Calendar Server")
description: One-line outcome statement
diataxis_type: tutorial
---

import { Steps, Aside, Code } from '@astrojs/starlight/components';

## What You'll Build

[Single paragraph describing the tangible outcome. Use "you'll" language to set expectations.]

By the end of this tutorial, you'll have a working calendar server that:
- Does specific thing A
- Does specific thing B
- Does specific thing C

<Aside type="note">
This tutorial takes approximately [X] minutes and assumes [prerequisites].
</Aside>

## Prerequisites

- Prerequisite A (with version)
- Prerequisite B
- Basic familiarity with [concept]

## Steps

<Steps>

1. **First Action with Visible Result**

   [Brief explanation of what this step accomplishes, not why.]

   ```bash
   # Complete, working command
   command --flag value
   ```

   **You should see:**
   ```
   Expected output
   ```

   <Aside type="note">
   If you see [X], this is normal. Brief contextual note only.
   </Aside>

2. **Second Action with Visible Result**

   [Continue pattern: do this, see that.]

   ```python
   # Complete, working code
   code_example()
   ```

3. **Final Action with Complete Working System**

   [Culminating step that ties everything together.]

   ```bash
   final_command
   ```

</Steps>

## Try It Out

[Verification step with visible feedback.]

```bash
curl http://localhost:5232/
```

You should see the Radicale web interface.

## What You've Learned

[Reflection on what was built, building confidence. Avoid "congratulations" - let achievement speak.]

You now have [specific system] that can [capabilities]. This foundation allows [next possibilities].

## Next Steps

- [Link to related tutorial building on this]
- [Link to how-to for customization]
- [Link to explanation of concepts]
```

---

## How-To Guide Template

```mdx
---
title: Task Title (Verb Phrase, e.g., "Configure htpasswd Authentication")
description: One-line problem statement
diataxis_type: how-to
---

import { Tabs, TabItem, Aside } from '@astrojs/starlight/components';

## Problem

[One paragraph describing the specific problem this solves. Use "you want to" or "you need to" language.]

## Prerequisites

- Already have [existing state]
- Access to [required resource]

## Solution

[Present the most common/recommended approach first, then alternatives.]

### Basic Configuration

[Instructions from user perspective, not machinery perspective.]

1. Open your configuration file:

   ```bash
   nano /etc/radicale/config
   ```

2. Add the authentication section:

   ```ini
   [auth]
   type = htpasswd
   htpasswd_filename = /path/to/users
   htpasswd_encryption = bcrypt
   ```

<Aside type="tip">
Use bcrypt for production. Plain passwords are only suitable for testing.
</Aside>

### Creating the Password File

<Tabs>
  <TabItem label="htpasswd (recommended)">
    ```bash
    htpasswd -c -B /path/to/users username
    ```
  </TabItem>
  <TabItem label="Python (if htpasswd unavailable)">
    ```python
    import bcrypt
    password = b"secretpassword"
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    with open('/path/to/users', 'w') as f:
        f.write(f'username:{hashed.decode()}\n')
    ```
  </TabItem>
</Tabs>

### Handling Edge Cases

<Aside type="caution">
If you're using SELinux, you must set the correct context on the password file.
</Aside>

[Address real-world complications. Branch into solutions.]

**If your password file is on a network mount:**
- Solution approach A
- Solution approach B

### Verification

[Test that the solution worked.]

```bash
curl -u username:password http://localhost:5232/
```

## Variations

[Alternative approaches for different contexts.]

### Using SHA-512 Instead

[When and why you'd choose this.]

```ini
htpasswd_encryption = sha512
```

## Related Tasks

- [Link to related how-to]
- [Link to troubleshooting guide]
```

---

## Reference Template

```mdx
---
title: Component Name (Noun, e.g., "Configuration Options")
description: Neutral description of what this documents
diataxis_type: reference
---

import { LinkCard } from '@astrojs/starlight/components';

## Overview

[One paragraph neutral description. Avoid "you" language. Mirror the product structure.]

Radicale configuration uses INI format with sections for each subsystem. Options are specified as `key = value` pairs.

## Syntax

[Describe the format neutrally.]

```ini
[section]
option = value
```

## Sections

[Organize by product structure, not by user task.]

### `[server]`

Controls HTTP server behavior.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `hosts` | string | `127.0.0.1:5232` | Addresses to bind |
| `max_connections` | integer | `20` | Maximum concurrent connections |
| `max_content_length` | integer | `100000000` | Maximum request body size in bytes |
| `timeout` | integer | `30` | Socket timeout in seconds |

**Example:**

```ini
[server]
hosts = 0.0.0.0:5232, [::]:5232
max_connections = 50
```

### `[auth]`

Controls authentication mechanism.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `type` | string | `denyall` | Authentication backend |
| `delay` | integer | `1` | Delay after failed login (seconds) |

[Continue systematic description.]

## Types

[Define data types used in tables above.]

- **string**: Text value, no quotes needed
- **integer**: Whole number
- **boolean**: `True` or `False` (case-insensitive)

## Environment Variables

[List environment variable equivalents.]

| Variable | Equivalent Option | Example |
|----------|------------------|---------|
| `RADICALE_CONFIG` | N/A | `/etc/radicale/config` |

## Related Documentation

<LinkCard
  title="CLI Commands"
  description="Command-line options reference"
  href="/reference/cli/"
/>

<LinkCard
  title="Configuration Guide"
  description="How to configure authentication"
  href="/how-to/auth/htpasswd/"
/>
```

---

## Explanation Template

```mdx
---
title: Concept Title (Noun Phrase, e.g., "Radicale Architecture")
description: Understanding-oriented description
diataxis_type: explanation
---

import { Card, CardGrid, Aside } from '@astrojs/starlight/components';

## Understanding [Concept]

[Opening paragraphs provide higher perspective. No instructions. Readable "in the bath."]

Radicale's architecture reflects a fundamental tension in CalDAV server design: simplicity versus features. Understanding this tension explains many design decisions.

## Core Concepts

<CardGrid>
  <Card title="Pluggable Architecture" icon="puzzle">
    Each subsystem (auth, storage, rights) uses a plugin pattern. This allows customization without forking.
  </Card>
  <Card title="File-Based Storage" icon="document">
    Collections are folders, items are files. This design prioritizes transparency and tool compatibility over raw performance.
  </Card>
  <Card title="Stateless Handlers" icon="random">
    Each request is independent. No session state reduces complexity but requires careful synchronization.
  </Card>
</CardGrid>

## Why This Design?

[Make connections. Offer informed opinions. Answer "can you tell me about..." questions.]

Most CalDAV servers assume database backends and complex caching layers. Radicale inverts this assumption. The file-based storage makes several things obvious:

- **Backups**: Copy files, use rsync, leverage standard tools
- **Debugging**: Look at the files directly, use grep
- **Version control**: Git integration becomes natural

This comes with tradeoffs. File-based storage is slower for large collections. The `.Radicale.lock` mechanism prevents concurrent writes but creates a bottleneck under heavy load.

<Aside type="note">
The locking mechanism reflects a philosophical choice: prefer correctness and simplicity over theoretical maximum throughput.
</Aside>

## Historical Context

[Provide background that enriches understanding.]

Early CalDAV servers (Chandler, Darwin Calendar Server) focused on enterprise features. Radicale emerged in 2008 targeting personal/small team use. This context explains why features like multi-tenancy came later.

## The Plugin System

[Explain how parts relate to each other.]

The plugin architecture separates concerns:

```
Request → Auth Plugin → Rights Plugin → Storage Plugin → Response
```

Each plugin sees a consistent interface. This means:

1. Authentication backends don't know about storage format
2. Storage backends don't handle authorization
3. Rights backends don't parse calendar data

This separation makes testing simpler but creates integration challenges when plugins need to share state.

## Design Tensions

[Discuss tradeoffs and decisions.]

### Simplicity vs Features

Every feature addition requires evaluating cost to simplicity:

- **Git versioning**: Adds complexity but provides obvious value
- **WebSocket sync**: Higher complexity, benefits mostly power users
- **Multi-tenancy**: Moderate complexity, serves specific deployment models

### Performance vs Transparency

File-based storage prioritizes transparency. Each item is a readable file. This makes debugging trivial but requires careful optimization:

- Cache files in `.Radicale.cache/` directories
- Sync tokens avoid full collection scans
- Lock files prevent corruption

## When This Matters

[Connect to practical decisions users face.]

Understanding the architecture helps when:

- **Choosing deployment models**: WSGI vs standalone reflects stateless design
- **Debugging issues**: File structure makes problems visible
- **Evaluating features**: Some requests conflict with core design

<Aside type="tip">
If you need database-level performance for thousands of users, Radicale's file-based design may not fit. Consider DAViCal or Baikal. If you value simplicity and transparency, this architecture serves you well.
</Aside>

## Related Concepts

- [Link to explanation of CalDAV protocol]
- [Link to explanation of storage design]
- [Link to explanation of when to use versioning]
```

---

## Common Boundary Violations to Avoid

### Tutorial Mistakes
- **Including explanation**: "The reason this works is..." → NO. Focus on doing and seeing results.
- **Offering choices**: "You can use X or Y" → NO. One path, reliable results.
- **Skipping visible feedback**: Every step should produce observable output.

### How-To Mistakes
- **Writing from machinery perspective**: "The server processes..." → NO. "You configure..."
- **Avoiding complexity**: Real-world problems have edge cases. Address them.
- **Making it tutorial-like**: Don't hold hands. Assume competence.

### Reference Mistakes
- **Adding instructions**: "To use this, do..." → NO. Describe what it is.
- **Including opinions**: "The best option is..." → NO. Neutral description.
- **Organizing by task**: Organize by product structure, not user goals.

### Explanation Mistakes
- **Including instructions**: "First, configure..." → NO. Discuss concepts.
- **Focusing on details**: Big picture over implementation specifics.
- **Avoiding opinions**: Explanations benefit from informed perspective.

---

## Frontmatter Guide

### Minimal Frontmatter

```yaml
---
title: Page Title
description: One-line description for SEO/search
diataxis_type: tutorial  # or how-to, reference, explanation
---
```

### Extended Frontmatter

```yaml
---
title: Page Title
description: One-line description
diataxis_type: tutorial

# Control sidebar
sidebar:
  label: Custom Sidebar Label
  order: 2
  badge:
    text: New
    variant: success

# SEO/social
head:
  - tag: meta
    attrs:
      property: og:image
      content: /og-image.png

# Template override (usually not needed)
template: doc

# RFC tracking (for reference docs)
rfc_numbers: [4791, 6352]
compliance_level: 95

# Hero for splash pages
hero:
  tagline: Brief tagline
  image:
    file: ../../assets/image.svg
  actions:
    - text: Action Text
      link: /path/
      icon: right-arrow
      variant: primary
---
```

### Badge Variants

In sidebar configuration:
- `success`: Green (tutorials, achievements)
- `note`: Blue (how-to guides, informational)
- `caution`: Orange (reference, requires attention)
- `tip`: Purple (explanations, conceptual)
- `danger`: Red (deprecated, warnings)

---

## Component Quick Reference

### Layout Components

```mdx
import { Card, CardGrid, LinkCard, Aside, Steps, Tabs, TabItem } from '@astrojs/starlight/components';

<Card title="Title" icon="icon-name">Content</Card>

<CardGrid>
  <Card title="Card 1" icon="star">...</Card>
  <Card title="Card 2" icon="rocket">...</Card>
</CardGrid>

<LinkCard title="Link Title" description="Description" href="/path/" />

<Aside type="note">Note content</Aside>
<Aside type="tip">Tip content</Aside>
<Aside type="caution">Warning content</Aside>
<Aside type="danger">Danger content</Aside>

<Steps>
1. First step
2. Second step
</Steps>

<Tabs>
  <TabItem label="Option 1">Content 1</TabItem>
  <TabItem label="Option 2">Content 2</TabItem>
</Tabs>
```

### Available Icons

Common Starlight icons: `star`, `rocket`, `document`, `open-book`, `puzzle`, `random`, `approve-check`, `right-arrow`, `external`, `information`, `warning`, `error`

See [Starlight Icons](https://starlight.astro.build/reference/icons/) for full list.

---

## Language Patterns by Type

### Tutorial Language
- "You'll build/create/set up..."
- "You should see..."
- "This creates/produces/results in..."
- Avoid: "You could", "Optionally", "The reason is"

### How-To Language
- "To [achieve goal], [do action]"
- "If [condition], then [solution]"
- Avoid: "Learn about", "Understand", "This teaches"

### Reference Language
- "[Component] is/does/provides..."
- "The [parameter] controls/specifies/defines..."
- Avoid: "You should", "We recommend", "To use this"

### Explanation Language
- "This reflects/illustrates/demonstrates..."
- "The relationship between X and Y..."
- "This matters because..."
- Avoid: "Step 1", "To configure", specific instructions
