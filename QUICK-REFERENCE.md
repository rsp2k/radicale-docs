# Diátaxis + Starlight Quick Reference Card

Visual quick reference for creating Radicale documentation. Print or keep open while writing.

---

## The Compass Tool

```
                 ACQUISITION          APPLICATION
               (learning new)      (using existing)

              ┌────────────────┬────────────────┐
              │                │                │
   ACTION     │   TUTORIAL     │    HOW-TO      │
 (practical)  │  "You'll build"│ "You need to"  │
              │                │                │
              ├────────────────┼────────────────┤
              │                │                │
 COGNITION    │  EXPLANATION   │   REFERENCE    │
(theoretical) │ "Understanding"│  "The X is/    │
              │                │   provides"    │
              └────────────────┴────────────────┘
```

**To classify any documentation:**
1. Action or cognition? (Doing vs understanding)
2. Acquisition or application? (Learning vs using existing knowledge)

---

## Type at a Glance

| Aspect | Tutorial | How-To | Reference | Explanation |
|--------|----------|--------|-----------|-------------|
| **Purpose** | Learning | Problem-solving | Information lookup | Understanding |
| **User asks** | "Can you teach me?" | "How do I?" | "What is?" | "Why/When?" |
| **Answers** | Yes, by doing | Here's how | Here's the facts | Here's why |
| **Form** | Lesson | Steps/recipe | Dry description | Discursive |
| **Analogy** | Teaching child to cook | Recipe | Ingredient reference | Food science |

---

## Title Patterns

| Type | Pattern | Examples |
|------|---------|----------|
| **Tutorial** | Action verb + object | "Build Your First Calendar Server"<br>"Set Up Server Metrics"<br>"Enable Calendar Versioning" |
| **How-To** | Task verb + context | "Configure htpasswd Authentication"<br>"Deploy with Caddy"<br>"Troubleshoot Scheduling Problems" |
| **Reference** | Noun phrase | "Configuration Options"<br>"HTTP Methods"<br>"CLI Commands" |
| **Explanation** | Concept noun | "Radicale Architecture"<br>"How CalDAV Works"<br>"Security Model" |

---

## Opening Patterns

### Tutorial
```mdx
## What You'll Build

By the end of this tutorial, you'll have [tangible outcome].

<Aside type="note">
Takes X minutes, assumes [prerequisites]
</Aside>

## Steps

<Steps>
1. **First action with visible result**
```

### How-To
```mdx
## Problem

You need to [specific goal], [context].

## Prerequisites

- Already have [state]
- Access to [resource]

## Solution

[Most common approach first]
```

### Reference
```mdx
## Overview

[Neutral description of what this documents]

## Syntax

[Format description]

[Tables with parameters]
```

### Explanation
```mdx
## Understanding [Concept]

[Higher perspective opening, readable without computer]

## Core Concepts

<CardGrid>
  <Card title="Concept A">Description</Card>
</CardGrid>
```

---

## Component Cheat Sheet

```mdx
import { Steps, Aside, Card, CardGrid, LinkCard, Tabs, TabItem } from '@astrojs/starlight/components';
```

| Component | Tutorial | How-To | Reference | Explanation | Purpose |
|-----------|:--------:|:------:|:---------:|:-----------:|---------|
| **Steps** | ✅ | ❌ | ❌ | ❌ | Sequential learning |
| **Tabs** | ❌ | ✅ | ⚠️ | ❌ | Multiple solutions |
| **Aside (note)** | ✅ | ✅ | ❌ | ✅ | Brief context |
| **Aside (tip/caution/danger)** | ❌ | ✅ | ❌ | ⚠️ | Warnings/tips |
| **CardGrid** | ❌ | ❌ | ❌ | ✅ | Organize concepts |
| **LinkCard** | ✅ | ✅ | ✅ | ✅ | Navigation |
| **Tables** | ❌ | ⚠️ | ✅ | ⚠️ | Structured data |

✅ Primary use | ⚠️ Use sparingly | ❌ Avoid (boundary violation)

---

## Language Quick Test

| Type | Says | Doesn't Say |
|------|------|-------------|
| **Tutorial** | "You'll build"<br>"You should see"<br>"This creates" | "You could"<br>"Optionally"<br>"The reason is" |
| **How-To** | "You need to"<br>"If X, then Y"<br>"To verify" | "Learn about"<br>"Understand"<br>"This teaches" |
| **Reference** | "X is/provides"<br>"Controls"<br>"Specifies" | "You should"<br>"We recommend"<br>"To use this" |
| **Explanation** | "This reflects"<br>"The relationship"<br>"This matters because" | "Step 1"<br>"To configure"<br>"Do this" |

---

## Frontmatter Templates

### Tutorial
```yaml
---
title: Build Your First Calendar Server
description: Create working server in 15 minutes
diataxis_type: tutorial
sidebar:
  order: 1
  badge:
    text: 15 min
    variant: success
---
```

### How-To
```yaml
---
title: Configure htpasswd Authentication
description: Secure with file-based passwords
diataxis_type: how-to
sidebar:
  order: 1
  badge:
    text: Task
    variant: note
---
```

### Reference
```yaml
---
title: Configuration Options
description: Complete parameter reference
diataxis_type: reference
sidebar:
  order: 1
  badge:
    text: Lookup
    variant: caution
---
```

### Explanation
```yaml
---
title: Radicale Architecture
description: Understanding design principles
diataxis_type: explanation
sidebar:
  order: 1
  badge:
    text: Concept
    variant: tip
---
```

---

## Steps Component (Tutorials Only)

```mdx
<Steps>

1. **Action with visible result**

   Brief description of what this accomplishes.

   ```bash
   command --flag value
   ```

   **You should see:**
   ```
   Expected output
   ```

   <Aside type="note">
   Brief contextual note only
   </Aside>

2. **Next action**

   Continue pattern...

</Steps>
```

**Key points:**
- Every step has visible feedback
- "You should see:" pattern mandatory
- Bold step titles
- Minimal explanation

---

## Tabs Component (How-To Only)

```mdx
<Tabs>
  <TabItem label="Recommended Method">
    ```bash
    command_a
    ```
  </TabItem>

  <TabItem label="Alternative">
    ```bash
    command_b
    ```
  </TabItem>

  <TabItem label="If X (context)">
    <Aside type="caution">
    Warning about this approach
    </Aside>

    ```bash
    command_c
    ```
  </TabItem>
</Tabs>
```

**Key points:**
- Label recommended option
- Present common case first
- Can nest Aside for warnings
- Use when multiple valid approaches exist

---

## Aside Types

```mdx
<Aside type="note">
Contextual information, clarification
</Aside>

<Aside type="tip">
Helpful suggestion, best practice
</Aside>

<Aside type="caution">
Warning about edge case, gotcha
</Aside>

<Aside type="danger">
Critical security or data loss warning
</Aside>
```

**By type:**
- **Tutorial**: Only `note`, minimal usage
- **How-To**: All types, especially caution/danger for edge cases
- **Reference**: Avoid entirely
- **Explanation**: `note` and `tip` for informed opinions

---

## CardGrid (Explanations Only)

```mdx
<CardGrid>
  <Card title="Concept Name" icon="icon-name">
    What this means and why it matters. Conceptual
    description without specific instructions.
  </Card>

  <Card title="Another Concept" icon="icon-name">
    Description of related concept.
  </Card>
</CardGrid>
```

**Common icons:**
- `star` - highlights, important
- `rocket` - performance, speed
- `document` - files, storage
- `puzzle` - architecture, plugins
- `random` - stateless, distributed
- `open-book` - learning
- `approve-check` - verification

---

## Tables (Reference Primarily)

```mdx
| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `name` | string | `value` | Neutral description of what it controls |
| `count` | integer | `10` | Another neutral description |
```

**Key points:**
- Systematic, complete coverage
- Neutral descriptions (no "you should")
- Include type and default
- Organize by product structure

---

## Common Violations & Fixes

### ❌ Explanation in Tutorial
**Bad**: "The reason this works is because of plugin architecture..."
**Fix**: Brief note + link to `/explanations/architecture/`

### ❌ Instructions in Reference
**Bad**: "To configure auth, first open your config..."
**Fix**: Neutral table of options + link to `/how-to/auth/`

### ❌ Choice in Tutorial
**Bad**: "You can use pip or apt, choose what works for you"
**Fix**: One reliable method + link to `/how-to/installation/` for alternatives

### ❌ Machinery Perspective in How-To
**Bad**: "The server processes the request and iterates through..."
**Fix**: "Configure the server: [command]"

### ❌ Steps in How-To
**Bad**: `<Steps>` for branching solution
**Fix**: Numbered list + `<Tabs>` for alternatives

---

## Verification Patterns

### Tutorial Verification
```mdx
```bash
command
```

**You should see:**
```
expected output
```
```

Every command has expected output.

### How-To Verification
```mdx
### Verification

Test that it works:

```bash
curl -u user:pass http://localhost:5232/
```

You should see successful response with status 200.
```

One verification section at end.

---

## Closing Patterns

### Tutorial Closing
```mdx
## What You've Learned

You now have [system] that can [capabilities].
This foundation allows [next possibilities].

## Next Steps

- [Link to related tutorial building on this]
- [Link to how-to for customization]
- [Link to explanation of concepts]
```

**Reflects on capabilities gained, no "congratulations"**

### How-To Closing
```mdx
## Related Tasks

- [Link to related how-to]
- [Link to troubleshooting]
- [Link to reference for options]
```

**No reflection, just navigation to related tasks**

### Reference Closing
```mdx
## Related Documentation

<LinkCard
  title="Related Reference"
  href="/reference/other/"
/>
```

**Links to related references only**

### Explanation Closing
```mdx
## Related Concepts

- [Link to related explanation]
- [Link to reference for details]
- [Link to how-to for implementation]
```

**Links to deepen understanding**

---

## Quality Checklist

### Before Publishing, Ask:

**Type Purity:**
- [ ] Does title match type convention?
- [ ] Is opening pattern correct?
- [ ] Are components appropriate for type?
- [ ] Is language consistent with type?

**Boundary Check:**
- [ ] Any explanation in tutorial? → Move to explanation page
- [ ] Any instructions in reference? → Move to how-to
- [ ] Any choices in tutorial? → Pick one, move others to how-to
- [ ] Any step-by-step in explanation? → Move to tutorial/how-to

**Component Check:**
- [ ] Steps only in tutorial?
- [ ] Tabs only in how-to?
- [ ] Aside appropriate for type?
- [ ] CardGrid only for concepts?

**User Serving:**
- [ ] Can user accomplish their goal?
- [ ] Is it easy to find what they need?
- [ ] Does it feel good to use?
- [ ] Does it respect their mental state?

---

## The Two-Question Compass

When uncertain about classification:

### Question 1: Action or Cognition?
- **Action** (practical doing) → Tutorial or How-To
- **Cognition** (theoretical understanding) → Reference or Explanation

### Question 2: Acquisition or Application?
- **Acquisition** (learning new) → Tutorial or Explanation
- **Application** (using existing knowledge) → How-To or Reference

```
    Action + Acquisition = TUTORIAL
    Action + Application = HOW-TO
Cognition + Application = REFERENCE
Cognition + Acquisition = EXPLANATION
```

---

## Decision Trees

### Should I use Steps?

- Is this teaching someone something new? **YES** → Use Steps
- Is this a tutorial? **YES** → Use Steps
- Is this a how-to guide? **NO** → Use numbered list + Tabs
- Is this reference/explanation? **NO** → Don't use Steps

### Should I use Tabs?

- Are there multiple valid approaches? **YES** → Consider Tabs
- Is this a tutorial? **NO** → Pick one method only
- Is this a how-to? **YES** → Use Tabs for alternatives
- Is this reference? **MAYBE** → Only for syntax variants
- Is this explanation? **NO** → Discuss concepts, don't show alternatives

### Should I use CardGrid?

- Am I organizing concepts? **YES** → Use CardGrid
- Is this an explanation? **YES** → Use CardGrid
- Is this a splash page? **YES** → Use CardGrid
- Am I showing tasks? **NO** → Use list instead
- Am I showing data? **NO** → Use table instead

---

## File Paths Reference

All templates and examples in `/home/rpm/claude/radicale/radicale-docs/`:

**Documentation Files:**
- `TEMPLATES.md` - Complete templates
- `DIATAXIS-EXAMPLES.md` - Detailed examples
- `STARLIGHT-COMPONENTS-GUIDE.md` - Component reference
- `SUMMARY.md` - Implementation summary
- `QUICK-REFERENCE.md` - This file

**Example Content:**
- `src/content/docs/tutorials/first-server.mdx` - Tutorial example
- `src/content/docs/tutorials/metrics.mdx` - Tutorial example
- `src/content/docs/tutorials/versioning.mdx` - Tutorial example
- `src/content/docs/how-to/auth/htpasswd.mdx` - How-to example
- `src/content/docs/reference/configuration.mdx` - Reference example
- `src/content/docs/explanations/architecture.mdx` - Explanation example

---

## Remember

**Diátaxis serves users, not documentation authors.**

The framework exists to create documentation that truly helps the person on the other side of the screen. When in doubt, ask:

1. What mental state is my reader in?
2. What are they trying to accomplish?
3. Does my content serve that need?

If content doesn't clearly fit one type, it probably violates boundaries. Split it into multiple pages, each serving one mental state.

---

## Quick Links

- **Diátaxis Framework**: https://diataxis.fr/
- **Starlight Components**: https://starlight.astro.build/components/
- **Starlight Icons**: https://starlight.astro.build/reference/icons/
- **Starlight Frontmatter**: https://starlight.astro.build/reference/frontmatter/

---

**Print this card and keep it visible while writing documentation.**
