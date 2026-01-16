# Diátaxis Implementation Examples for Radicale Docs

This document provides concrete examples from the implemented .mdx files, highlighting how Starlight components maintain Diátaxis boundaries.

## Table of Contents

1. [Tutorial Examples](#tutorial-examples)
2. [How-To Examples](#how-to-examples)
3. [Reference Examples](#reference-examples)
4. [Explanation Examples](#explanation-examples)
5. [Component Usage Patterns](#component-usage-patterns)
6. [Common Violations and Fixes](#common-violations-and-fixes)

---

## Tutorial Examples

### File: `tutorials/first-server.mdx`

**Classification**: Tutorial (Acquisition + Action)
- Mental state: Learning through doing
- Goal: Build confidence through visible success

#### Opening Pattern

```mdx
## What You'll Build

By the end of this tutorial, you'll have a working calendar server running
on your computer that you can access from any CalDAV client.
```

**Why this works**: Sets clear expectations using "you'll" language. Describes tangible outcome, not abstract concepts.

#### Steps Component Usage

```mdx
<Steps>
1. **Install Radicale**

   Install Radicale using pip:

   ```bash
   pip3 install --user radicale
   ```

   **You should see:**
   ```
   Successfully installed radicale-3.5.10 ...
   ```
</Steps>
```

**Why this works**:
- Sequential numbering provides clear progression
- Each step has action (install) and feedback (you should see)
- "You should see" pattern builds confidence through verification

#### Aside for Minimal Context

```mdx
<Aside type="note">
The `--user` flag installs Radicale in your home directory,
avoiding system-wide changes.
</Aside>
```

**Why this works**: Brief contextual note doesn't derail the learning flow. Answers "why this command?" without becoming an explanation.

**Boundary Maintenance**: Notice what's NOT included:
- No "you could also use X" (creates choice paralysis)
- No deep explanation of pip internals (wrong mental state)
- No troubleshooting (assumes success path)

---

### File: `tutorials/versioning.mdx`

**Classification**: Tutorial (Acquisition + Action)

#### Verification Pattern

```mdx
6. **Verify the auto-commit**

   Check the git log:

   ```bash
   cd ~/.local/share/radicale/collections
   git log --oneline -5
   ```

   **You should see:**
   ```
   abc1235 Changes by anonymous
   abc1234 Initial calendar state
   ```

   The new commit captures your event creation.
```

**Why this works**: Every action produces observable output. The learner sees evidence of success immediately.

#### Closing Reflection

```mdx
## What You've Learned

You now have a Radicale server that treats your calendar data as code,
automatically versioning every change in git. You've seen how to audit
changes, restore deleted data, and use standard git tools to understand
calendar history.
```

**Why this works**:
- Reflects on capabilities gained (not abstract knowledge)
- Builds confidence by stating what the learner can now do
- Avoids "congratulations" - lets achievement speak for itself
- Uses "you've seen" not "you learned about" (action-oriented)

---

## How-To Examples

### File: `how-to/auth/htpasswd.mdx`

**Classification**: How-To (Application + Action)
- Mental state: Problem-solving with specific goal
- Goal: Complete a concrete task

#### Problem Statement

```mdx
## Problem

You need to restrict access to your Radicale server using usernames
and passwords stored in a file, avoiding the complexity of LDAP or
database authentication.
```

**Why this works**:
- Starts with the problem, not the solution
- User-centered language ("you need to")
- Defines scope (file-based, not LDAP)

#### Tabs for Multiple Solutions

```mdx
<Tabs>
  <TabItem label="htpasswd (recommended)">
    Install htpasswd if not available:

    ```bash
    sudo apt install apache2-utils
    ```

    Create the first user:

    ```bash
    htpasswd -c -B /etc/radicale/users alice
    ```
  </TabItem>

  <TabItem label="Python bcrypt">
    Install the bcrypt library:

    ```bash
    pip3 install bcrypt
    ```

    Create a password hash:

    ```python
    import bcrypt
    # ...
    ```
  </TabItem>

  <TabItem label="Plain text (testing only)">
    <Aside type="danger">
    Plain text passwords are insecure. Only use for local testing.
    </Aside>

    Configuration:

    ```ini
    [auth]
    htpasswd_encryption = plain
    ```
  </TabItem>
</Tabs>
```

**Why this works**:
- Acknowledges multiple valid approaches (real-world complexity)
- Presents recommended solution first
- Labels help users choose appropriate path
- Danger aside warns about security implications

**Boundary Maintenance**: This is NOT a tutorial because:
- Doesn't hold hands through each step
- Assumes competence (user can choose appropriate method)
- Addresses edge cases (SELinux, network mounts)
- Written from user perspective, not learning journey

#### Edge Cases Section

```mdx
### Handling Edge Cases

#### SELinux Contexts

If you're using SELinux, set the correct context on the password file:

```bash
semanage fcontext -a -t radicale_var_lib_t "/etc/radicale/users"
restorecon -v /etc/radicale/users
```
```

**Why this works**: How-to guides serve real-world complexity. Edge cases aren't "advanced topics" - they're part of the problem space.

---

## Reference Examples

### File: `reference/configuration.mdx`

**Classification**: Reference (Application + Cognition)
- Mental state: Looking up specific information
- Goal: Find facts quickly without narrative

#### Neutral Description

```mdx
## Overview

Radicale configuration uses INI format with sections for each subsystem.
Options are specified as `key = value` pairs. Configuration files are
loaded from multiple locations in order, with later files overriding
earlier ones.
```

**Why this works**:
- Neutral tone (no "you" language)
- Describes what the system is/does
- No instructions ("to configure, do X")
- Mirrors the product structure

#### Table Format

```mdx
| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `hosts` | string | `127.0.0.1:5232` | Addresses and ports to bind |
| `max_connections` | integer | `20` | Maximum concurrent connections |
| `timeout` | integer | `30` | Socket timeout in seconds |
```

**Why this works**:
- Structured for lookup, not reading
- Systematic coverage of all parameters
- Neutral descriptions without opinion
- Complete information (type, default, description)

#### Example Without Instruction

```ini
[server]
hosts = 0.0.0.0:5232, [::]:5232
max_connections = 50
timeout = 60
```

**Why this works**:
- Shows syntax without instructing
- No "now do this" or "to configure"
- Illustrates format for quick reference

**Boundary Maintenance**: Notice what's NOT included:
- No "you should" recommendations (that's explanation territory)
- No step-by-step instructions (that's how-to territory)
- No context on when to use options (that's explanation)

---

## Explanation Examples

### File: `explanations/architecture.mdx`

**Classification**: Explanation (Acquisition + Cognition)
- Mental state: Understanding concepts and relationships
- Goal: Develop mental models, not perform tasks

#### Opening with Context

```mdx
## Understanding Radicale's Design

Radicale's architecture reflects a fundamental tension in CalDAV
server design: simplicity versus features. Most CalDAV servers
assume enterprise deployment with database backends, complex caching,
and multi-process architectures. Radicale inverts these assumptions,
prioritizing transparency, simplicity, and ease of deployment.
```

**Why this works**:
- Provides higher perspective immediately
- Makes connections to broader context
- Offers interpretation (not just facts)
- Readable "in the bath" - no computer needed

#### CardGrid for Conceptual Organization

```mdx
<CardGrid>
  <Card title="File-Based Storage" icon="document">
    Collections are folders, items are files. No database, no hidden
    state. Everything is visible and accessible with standard Unix tools.
  </Card>
  <Card title="Pluggable Architecture" icon="puzzle">
    Each subsystem uses plugins. Customization without forking.
  </Card>
</CardGrid>
```

**Why this works**:
- Organizes concepts, not tasks
- Visual structure supports understanding
- Describes "what" and "why", not "how"

#### Tradeoffs Discussion

```mdx
### What This Costs

**Performance at Scale**: File-based storage is slower than optimized
database queries for large collections. Opening 10,000 individual files
to find events in a date range performs worse than a SQL query with
proper indexes.

**Concurrency Limitations**: The `.Radicale.lock` file prevents
concurrent writes. Under heavy concurrent load, this creates a bottleneck.
```

**Why this works**:
- Explanations benefit from informed opinions
- Discusses tradeoffs honestly
- Helps reader understand decisions, not make them
- No specific instructions or commands

#### When This Matters Section

```mdx
## When This Architecture Fits

Understanding Radicale's architecture helps evaluate fit for
specific use cases:

### Good Fit Scenarios

**Personal Calendar Servers**: The file-based design makes backup,
migration, and debugging trivial.

### Poor Fit Scenarios

**Large Enterprise Deployment**: Hundreds or thousands of concurrent
users stress the locking mechanism.
```

**Why this works**:
- Connects concepts to practical implications
- Helps reader make decisions with understanding
- No instructions, just informed perspective

**Boundary Maintenance**: This is NOT a how-to because:
- Doesn't say "do this"
- Provides understanding, not solutions
- Discusses concepts and relationships
- Reader gains mental models, not task completion

---

## Component Usage Patterns

### By Diátaxis Type

#### Tutorials: Steps, Code, Aside (note only)

```mdx
<Steps>
1. **Action with Result**

   ```bash
   command
   ```

   **You should see:**
   ```
   output
   ```

   <Aside type="note">
   Brief context only
   </Aside>
</Steps>
```

**Why**:
- Steps enforce sequential progression
- Aside (note) for minimal context
- Never use tip/caution (implies choice/danger)

#### How-To: Tabs, Aside (tip/caution/danger), Code

```mdx
<Tabs>
  <TabItem label="Recommended">
    Solution A
  </TabItem>
  <TabItem label="Alternative">
    Solution B
  </TabItem>
</Tabs>

<Aside type="caution">
Real-world warning about edge case
</Aside>
```

**Why**:
- Tabs acknowledge multiple valid approaches
- Caution/danger appropriate for real problems
- Tip useful for practical advice

#### Reference: Tables, LinkCard, Code (syntax only)

```mdx
| Parameter | Type | Description |
|-----------|------|-------------|
| option    | type | what it does|

<LinkCard
  title="Related Reference"
  description="Another reference page"
  href="/reference/other/"
/>
```

**Why**:
- Tables for structured lookup
- LinkCard for navigation without narrative
- No Aside (too opinionated for reference)

#### Explanation: Card/CardGrid, Aside (note/tip), No Code

```mdx
<CardGrid>
  <Card title="Concept A" icon="icon">
    What this means and why it matters
  </Card>
</CardGrid>

<Aside type="note">
Informed opinion or connection
</Aside>
```

**Why**:
- Cards organize concepts visually
- Aside for opinions (acceptable in explanations)
- Code only if illustrating concept, never for tasks

---

## Common Violations and Fixes

### Violation 1: Explanation in Tutorial

**Bad** (tutorials/first-server.mdx):
```mdx
The reason Radicale uses file-based storage is because it provides
transparency and simplicity. Database backends would require additional
dependencies and complexity. This architectural decision reflects the
project's philosophy of...
```

**Why it's bad**: Breaks learning flow. Tutorial mental state is doing and seeing results, not understanding architectural philosophy.

**Fix**:
```mdx
This configuration stores calendar data in your home directory.

<Aside type="note">
Calendar items are stored as files you can backup with standard tools.
</Aside>
```

Move deep explanation to `/explanations/architecture/`.

### Violation 2: Instructions in Reference

**Bad** (reference/configuration.mdx):
```mdx
To configure authentication, first open your config file and then
add the [auth] section. You should set the type option to htpasswd
for password-based authentication.
```

**Why it's bad**: Reference should describe, not instruct. This is tutorial/how-to language.

**Fix**:
```mdx
### `[auth]`

Controls authentication mechanism.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `type` | string | `denyall` | Authentication backend |
```

Move instructions to `/how-to/auth/htpasswd/`.

### Violation 3: Tool Perspective in How-To

**Bad** (how-to/auth/htpasswd.mdx):
```mdx
When the authentication module receives a request, it parses the
Authorization header and extracts credentials. The htpasswd backend
then loads the password file and iterates through entries...
```

**Why it's bad**: How-to guides are from user perspective. Describing machinery internals isn't helpful for task completion.

**Fix**:
```mdx
1. Add the authentication section to your configuration:

   ```ini
   [auth]
   type = htpasswd
   htpasswd_filename = /etc/radicale/users
   ```

2. Test that authentication works:

   ```bash
   curl -u username:password http://localhost:5232/
   ```
```

Move machinery explanation to `/explanations/architecture/` or `/explanations/security/`.

### Violation 4: Specific Instructions in Explanation

**Bad** (explanations/architecture.mdx):
```mdx
To enable file-based storage, set the following options in your
configuration file:

```ini
[storage]
type = multifilesystem
filesystem_folder = /var/lib/radicale
```

Then restart the server with systemctl restart radicale.
```

**Why it's bad**: Explanations discuss concepts, not tasks. Step-by-step instructions belong elsewhere.

**Fix**:
```mdx
The file-based storage decision creates cascading consequences.
Each calendar item becomes an individual file. This makes backup
obvious (copy files) but creates performance implications under
heavy concurrent load.

The tradeoff reflects a philosophical choice: transparency over
theoretical maximum throughput.
```

Move instructions to `/how-to/deployment/` or `/tutorials/first-server/`.

### Violation 5: Choice in Tutorial

**Bad** (tutorials/first-server.mdx):
```mdx
Now install Radicale. You can use either pip or your system
package manager:

<Tabs>
  <TabItem label="pip">
    pip3 install radicale
  </TabItem>
  <TabItem label="apt">
    apt install radicale
  </TabItem>
</Tabs>

Choose the method that works best for your environment.
```

**Why it's bad**: Tutorials need one reliable path. Offering choices creates uncertainty and decision paralysis during learning.

**Fix**:
```mdx
Install Radicale using pip:

```bash
pip3 install --user radicale
```

**You should see:**
```
Successfully installed radicale-3.5.10
```
```

If users need other installation methods, put that in a how-to guide: `/how-to/installation/package-managers/`.

---

## Frontmatter Examples

### Tutorial Frontmatter

```yaml
---
title: Build Your First Calendar Server
description: Create a working Radicale server from scratch in 15 minutes
diataxis_type: tutorial
sidebar:
  order: 1
  badge:
    text: 15 min
    variant: success
---
```

**Key elements**:
- Title: Action-oriented (Build, Create, Set Up)
- Description: Outcome statement with time estimate
- Badge variant: `success` (green, achievement-oriented)

### How-To Frontmatter

```yaml
---
title: Configure htpasswd Authentication
description: Secure your server with file-based password authentication
diataxis_type: how-to
sidebar:
  order: 1
  badge:
    text: Task
    variant: note
---
```

**Key elements**:
- Title: Task verb phrase (Configure, Deploy, Troubleshoot)
- Description: Problem statement
- Badge variant: `note` (blue, informational)

### Reference Frontmatter

```yaml
---
title: Configuration Options
description: Complete reference of all Radicale configuration parameters
diataxis_type: reference
sidebar:
  order: 1
  badge:
    text: Lookup
    variant: caution
---
```

**Key elements**:
- Title: Noun phrase (Options, Commands, API)
- Description: Neutral, comprehensive
- Badge variant: `caution` (orange, attention-required)

### Explanation Frontmatter

```yaml
---
title: Radicale Architecture
description: Understanding the design principles and structure of Radicale
diataxis_type: explanation
sidebar:
  order: 1
  badge:
    text: Concept
    variant: tip
---
```

**Key elements**:
- Title: Concept noun phrase
- Description: "Understanding..." or "How X works"
- Badge variant: `tip` (purple, conceptual)

---

## Quality Checklist

### Tutorial Quality

- [ ] Every step produces visible output
- [ ] "You should see" after each command
- [ ] No choices offered (single path)
- [ ] Minimal explanation (move to separate explanation pages)
- [ ] Builds something concrete
- [ ] Time estimate provided
- [ ] Prerequisites clearly stated
- [ ] "What You've Learned" reflection at end

### How-To Quality

- [ ] Starts with problem statement
- [ ] Written from user perspective (not machinery)
- [ ] Addresses edge cases and variations
- [ ] Multiple approaches shown when applicable
- [ ] Real-world warnings included
- [ ] Assumes user competence
- [ ] Verification step included
- [ ] Links to related tasks

### Reference Quality

- [ ] Neutral tone (no "you" language)
- [ ] Systematic coverage
- [ ] Tables for structured information
- [ ] Complete parameter documentation
- [ ] Syntax examples without instruction
- [ ] Organized by product structure
- [ ] No opinions or recommendations
- [ ] Links to how-to guides for tasks

### Explanation Quality

- [ ] Provides higher perspective
- [ ] Makes connections between concepts
- [ ] Discusses tradeoffs openly
- [ ] Includes informed opinions
- [ ] No step-by-step instructions
- [ ] Readable without computer
- [ ] Answers "why" and "how it relates"
- [ ] Links to related concepts

---

## Migration Strategy

### Converting Existing Docs

When you have existing documentation to classify:

1. **Read the first paragraph**: Does it start with:
   - "In this tutorial, you'll build..." → Tutorial
   - "To do X, follow these steps..." → How-to
   - "The [component] is/provides..." → Reference
   - "Understanding how/why X..." → Explanation

2. **Check for boundary violations**:
   - Explanation sections in tutorials → Extract to explanation page
   - Instructions in reference → Move to how-to page
   - Deep theory in how-to → Link to explanation
   - Multiple paths in tutorial → Keep one, move others to how-to

3. **Apply appropriate components**:
   - Tutorial: Add `<Steps>`, verify "you should see" pattern
   - How-to: Add `<Tabs>` for alternatives, `<Aside type="caution">` for warnings
   - Reference: Convert to tables, remove instructional language
   - Explanation: Add `<CardGrid>` for concepts, remove code examples

4. **Update frontmatter**:
   - Add `diataxis_type`
   - Choose appropriate sidebar badge variant
   - Adjust title to match type conventions

---

## Next Steps for Documentation

### Immediate Actions

1. **Audit existing pages** against templates in this document
2. **Identify boundary violations** using the examples above
3. **Extract explanations** from tutorial/how-to content
4. **Systematize reference** pages with consistent table structure
5. **Add Components** to enhance existing content

### Long-term Improvements

1. **Tutorial Series**: Create learning paths (beginner → intermediate → advanced)
2. **How-to Index**: Organize by problem domain (auth, deployment, monitoring)
3. **Reference Completeness**: Ensure all configuration, CLI, API documented
4. **Explanation Depth**: Add more "why" and "when" content for advanced users

### Measuring Success

- **Functional Quality**: Accurate, complete, consistent (test against product)
- **Deep Quality**: Feels good to use, has flow, fits human needs (test with users)
- **Type Purity**: Each page clearly fits one type (use compass tool)
- **User Satisfaction**: Can users accomplish goals? Do they understand? Can they find facts?

Remember: Diátaxis serves users, not documentation authors. The framework exists to create documentation that truly helps the person on the other side of the screen.
