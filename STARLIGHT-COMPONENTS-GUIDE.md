# Starlight Components for Diátaxis Documentation

Quick reference guide for using Starlight's built-in components while maintaining Diátaxis boundaries.

## Component Import

All components import from `@astrojs/starlight/components`:

```mdx
import { Steps, Aside, Card, CardGrid, LinkCard, Tabs, TabItem } from '@astrojs/starlight/components';
```

---

## Steps Component

**Use in**: Tutorials only
**Purpose**: Sequential learning progression with visible feedback

### Syntax

```mdx
<Steps>

1. **First step with action**

   Description and command:

   ```bash
   command
   ```

   **You should see:**
   ```
   expected output
   ```

2. **Second step with action**

   Continue pattern...

</Steps>
```

### Key Features

- Automatically numbers steps
- Can nest any Markdown or components
- Supports multiple paragraphs and code blocks per step
- Use `**You should see:**` pattern for feedback

### Do's and Don'ts

✅ **Do**:
- Every step produces visible output
- Use bold for step titles: `**Install Radicale**`
- Include verification after each major action
- Keep steps focused on doing, not explaining

❌ **Don't**:
- Use in how-to guides (they need branching paths)
- Use in reference (no sequential instructions)
- Use in explanations (no step-by-step tasks)
- Skip verification steps

### Example

```mdx
<Steps>

1. **Create configuration directory**

   ```bash
   mkdir -p ~/.config/radicale
   ```

   **You should see:**
   No output means success. Verify it was created:

   ```bash
   ls -la ~/.config/radicale
   ```

2. **Create configuration file**

   ```bash
   cat > ~/.config/radicale/config << 'EOF'
   [server]
   hosts = 127.0.0.1:5232
   EOF
   ```

</Steps>
```

---

## Aside Component

**Use in**: All types (but different purposes by type)
**Purpose**: Callouts for notes, tips, warnings, and dangers

### Syntax

```mdx
<Aside type="note">
Content here
</Aside>

<Aside type="tip">
Content here
</Aside>

<Aside type="caution">
Content here
</Aside>

<Aside type="danger">
Content here
</Aside>
```

### Visual Appearance

- **note**: Blue, informational
- **tip**: Purple, helpful suggestions
- **caution**: Orange, warnings
- **danger**: Red, critical warnings

### Usage by Diátaxis Type

#### Tutorials: `note` only

```mdx
<Aside type="note">
The `--user` flag installs in your home directory, avoiding system-wide changes.
</Aside>
```

**Why**: Tutorials minimize explanation. Brief contextual notes only. Never use tip/caution/danger - they imply choices or failures.

#### How-To Guides: All types

```mdx
<Aside type="tip">
Use bcrypt encryption for production environments.
</Aside>

<Aside type="caution">
If you're using SELinux, set the correct file context.
</Aside>

<Aside type="danger">
Plain text passwords are insecure. Only use for local testing.
</Aside>
```

**Why**: How-to guides handle real-world complexity. Warnings and tips serve practical problem-solving.

#### Reference: Avoid

```mdx
<!-- DON'T use Aside in reference docs -->
```

**Why**: Reference should be neutral. Asides imply opinion or judgment. If you need to highlight something, use a table row or separate subsection.

#### Explanations: `note` and `tip`

```mdx
<Aside type="note">
This locking mechanism reflects a philosophical choice: prefer correctness
over theoretical maximum throughput.
</Aside>

<Aside type="tip">
If you need database-level performance, consider alternatives like DAViCal.
Understanding these tradeoffs helps evaluate fit.
</Aside>
```

**Why**: Explanations benefit from informed opinions. Note and tip appropriate for perspective and connections. Avoid caution/danger - explanations don't give instructions.

---

## Card and CardGrid Components

**Use in**: Explanations primarily, splash pages
**Purpose**: Organize concepts visually

### Syntax

```mdx
<CardGrid>
  <Card title="Concept Title" icon="icon-name">
    Description of concept and why it matters.
  </Card>
  <Card title="Another Concept" icon="icon-name">
    Description of another concept.
  </Card>
</CardGrid>
```

### Available Icons

Common icons suitable for documentation:

- `star` - highlights, important features
- `rocket` - performance, speed, launch
- `document` - files, documentation
- `puzzle` - architecture, plugins, components
- `random` - stateless, distributed, chaos
- `open-book` - learning, education
- `approve-check` - verification, success
- `information` - details, info
- `warning` - caution, attention
- `error` - problems, failures

Full icon list: https://starlight.astro.build/reference/icons/

### Usage by Diátaxis Type

#### Explanations: Primary use case

```mdx
## Core Design Principles

<CardGrid>
  <Card title="File-Based Storage" icon="document">
    Collections are folders, items are files. No database, no hidden state.
  </Card>
  <Card title="Pluggable Architecture" icon="puzzle">
    Each subsystem uses plugins. Customization without forking.
  </Card>
</CardGrid>
```

**Why**: Organizes conceptual information visually. Helps readers build mental models.

#### Splash Pages: Feature highlights

```mdx
<CardGrid>
  <Card title="RFC Compliant" icon="approve-check">
    85-98% compliance across major CalDAV/CardDAV standards.
  </Card>
  <Card title="Lightweight" icon="rocket">
    Easy to install and configure. Perfect for personal use.
  </Card>
</CardGrid>
```

#### Tutorials, How-To, Reference: Avoid

**Why**: These types are task/information oriented. Cards organize concepts, not tasks or data.

---

## LinkCard Component

**Use in**: Reference primarily, any type for navigation
**Purpose**: Link to related documentation with description

### Syntax

```mdx
<LinkCard
  title="Page Title"
  description="Brief description of what you'll find there"
  href="/path/to/page/"
/>
```

### Usage by Diátaxis Type

#### Reference: Related references

```mdx
## Related Documentation

<LinkCard
  title="CLI Commands"
  description="Command-line options and flags reference"
  href="/reference/cli/"
/>

<LinkCard
  title="HTTP Methods"
  description="CalDAV/CardDAV HTTP method reference"
  href="/reference/http-methods/"
/>
```

#### All Types: Cross-type navigation

```mdx
## Next Steps

<LinkCard
  title="Deploy with Caddy"
  description="How-to guide for production deployment"
  href="/how-to/deployment/caddy/"
/>

<LinkCard
  title="Understanding Architecture"
  description="Learn why Radicale uses file-based storage"
  href="/explanations/architecture/"
/>
```

**Why**: LinkCard provides context for navigation. Useful when moving between Diátaxis types.

---

## Tabs and TabItem Components

**Use in**: How-to guides primarily
**Purpose**: Present multiple valid solution paths

### Syntax

```mdx
<Tabs>
  <TabItem label="Option 1">
    Content for first option
  </TabItem>
  <TabItem label="Option 2">
    Content for second option
  </TabItem>
  <TabItem label="Option 3">
    Content for third option
  </TabItem>
</Tabs>
```

### Usage by Diátaxis Type

#### How-To Guides: Primary use case

```mdx
### Creating the Password File

<Tabs>
  <TabItem label="htpasswd (recommended)">
    ```bash
    htpasswd -c -B /etc/radicale/users alice
    ```
  </TabItem>

  <TabItem label="Python bcrypt">
    ```python
    import bcrypt
    # ... code
    ```
  </TabItem>

  <TabItem label="Plain text (testing only)">
    <Aside type="danger">
    Plain text passwords are insecure.
    </Aside>

    ```bash
    echo "alice:password" > /etc/radicale/users
    ```
  </TabItem>
</Tabs>
```

**Why**: How-to guides serve real-world problems. Multiple valid approaches exist. Tabs let users choose appropriate method for their context.

#### Tutorials: AVOID

**Why**: Tutorials need one reliable path. Offering choices creates uncertainty during learning. Users can't yet evaluate which option to choose.

**Alternative**: Pick the most reliable method for tutorials. Move alternatives to how-to guides.

#### Reference: Rare, syntax variants only

```mdx
<Tabs>
  <TabItem label="INI Format">
    ```ini
    [section]
    option = value
    ```
  </TabItem>

  <TabItem label="Environment Variable">
    ```bash
    export RADICALE_SECTION_OPTION=value
    ```
  </TabItem>
</Tabs>
```

**Why**: Only use when documenting equivalent syntaxes. Not for recommendations or choices.

#### Explanations: AVOID

**Why**: Explanations discuss concepts, not specific implementations. No need for alternative code paths.

---

## Code Blocks

**Use in**: All types (but different purposes)
**Purpose**: Display commands, configuration, or code

### Basic Syntax

````mdx
```bash
command --flag value
```

```ini
[section]
option = value
```

```python
def function():
    pass
```
````

### With Filename

````mdx
```ini title="/etc/radicale/config"
[server]
hosts = 127.0.0.1:5232
```
````

### With Line Highlighting

````mdx
```python {3-5}
def example():
    print("line 1")
    # These lines are highlighted
    result = calculate()
    return result
    print("line 6")
```
````

### Usage by Diátaxis Type

#### Tutorials: Complete, working examples

````mdx
```bash
# Complete command that works
curl -X PUT 'http://127.0.0.1:5232/personal/test.ics' \
  -H 'Content-Type: text/calendar' \
  -d 'BEGIN:VCALENDAR
VERSION:2.0
...
END:VCALENDAR'
```
````

**Key**: Must be copy-paste-able. Must work. No placeholders.

#### How-To Guides: Practical snippets

````mdx
```ini
[auth]
type = htpasswd
htpasswd_filename = /etc/radicale/users
htpasswd_encryption = bcrypt
```
````

**Key**: Focused on solving the problem. May have placeholders if explained.

#### Reference: Syntax illustration

````mdx
```ini
[section]
option = value
```
````

**Key**: Illustrates format only. Minimal, neutral examples.

#### Explanations: Rare, conceptual only

````mdx
```
Request → Auth Plugin → Rights Plugin → Storage Plugin → Response
```
````

**Key**: ASCII diagrams or pseudocode to illustrate concepts. Avoid executable code.

---

## Tables

**Use in**: Reference primarily
**Purpose**: Structured parameter/option documentation

### Syntax

```mdx
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Value A  | Value B  | Value C  |
| Value D  | Value E  | Value F  |
```

### Standard Reference Table Format

```mdx
| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `option_name` | string | `default_value` | Neutral description of what it controls |
```

### Usage by Diátaxis Type

#### Reference: Primary use case

```mdx
### `[server]` Section

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `hosts` | string | `127.0.0.1:5232` | Addresses and ports to bind |
| `timeout` | integer | `30` | Socket timeout in seconds |
```

#### How-To Guides: Quick reference within tasks

```mdx
### Encryption Options

| Method | Security | Speed | Library Required |
|--------|----------|-------|------------------|
| bcrypt | High | Slow | `bcrypt` |
| sha512 | Medium | Fast | Built-in |
| plain | None | Fast | Built-in |
```

**Why**: Helps users choose appropriate option for their context.

#### Tutorials: Avoid

**Why**: Tables are for information lookup, not sequential learning.

#### Explanations: Comparative only

```mdx
| Design Choice | Radicale | Enterprise CalDAV |
|---------------|----------|-------------------|
| Storage | Files | Database |
| Complexity | Low | High |
| Scale | Personal | Enterprise |
```

**Why**: Illustrates conceptual differences, not technical specifications.

---

## Component Combinations

### Tutorial Pattern: Steps + Aside + Code

```mdx
<Steps>

1. **Action**

   ```bash
   command
   ```

   **You should see:**
   ```
   output
   ```

   <Aside type="note">
   Brief context
   </Aside>

</Steps>
```

### How-To Pattern: Tabs + Aside + Code

```mdx
<Tabs>
  <TabItem label="Method A">
    ```bash
    command_a
    ```
  </TabItem>
  <TabItem label="Method B">
    ```bash
    command_b
    ```
  </TabItem>
</Tabs>

<Aside type="caution">
Real-world warning about edge case
</Aside>
```

### Reference Pattern: Table + Code + LinkCard

```mdx
### Section Name

| Option | Type | Description |
|--------|------|-------------|
| name   | type | description |

**Example:**

```ini
[section]
option = value
```

<LinkCard
  title="Related Reference"
  href="/reference/other/"
/>
```

### Explanation Pattern: CardGrid + Aside

```mdx
## Conceptual Section

<CardGrid>
  <Card title="Concept A" icon="icon">
    Description
  </Card>
  <Card title="Concept B" icon="icon">
    Description
  </Card>
</CardGrid>

<Aside type="note">
Informed opinion connecting the concepts
</Aside>
```

---

## Anti-Patterns to Avoid

### 1. Steps in How-To Guides

❌ **Don't**:
```mdx
<Steps>
1. Configure authentication
2. Test authentication
3. Enable authentication
</Steps>
```

✅ **Do**:
```mdx
### Configure Authentication

1. Open your configuration file:
   ```bash
   nano /etc/radicale/config
   ```

2. Add the authentication section:
   ```ini
   [auth]
   type = htpasswd
   ```

### Alternative: Using LDAP

If you need enterprise directory integration...
```

**Why**: Steps imply single path. How-to guides need flexibility for branching solutions.

### 2. Tabs in Tutorials

❌ **Don't**:
```mdx
<Tabs>
  <TabItem label="Method 1">...</TabItem>
  <TabItem label="Method 2">...</TabItem>
</Tabs>
```

✅ **Do**:
```mdx
Install using pip:

```bash
pip3 install radicale
```
```

**Why**: Tutorials build confidence through reliable success. Choices create uncertainty.

### 3. Aside in Reference

❌ **Don't**:
```mdx
| Option | Description |
|--------|-------------|
| timeout | Socket timeout |

<Aside type="tip">
You should increase timeout for slow networks.
</Aside>
```

✅ **Do**:
```mdx
| Option | Type | Default | Description |
|--------|------|---------|-------------|
| timeout | integer | 30 | Socket timeout in seconds. Increase for slow networks. |
```

**Why**: Reference should be neutral. Put recommendations in description or link to how-to guide.

### 4. Instructions in Explanation CardGrid

❌ **Don't**:
```mdx
<Card title="File-Based Storage" icon="document">
  To enable file-based storage, set `type = multifilesystem` in your config.
</Card>
```

✅ **Do**:
```mdx
<Card title="File-Based Storage" icon="document">
  Collections are folders, items are files. This design prioritizes
  transparency over raw performance.
</Card>
```

**Why**: Explanations discuss concepts, not tasks. Instructions belong in tutorials or how-to guides.

---

## Component Decision Tree

### Should I use Steps?

- Is this a tutorial? **YES** → Use Steps
- Is this showing sequential learning? **YES** → Use Steps
- Is this a how-to with branching paths? **NO** → Use numbered list + Tabs
- Is this reference or explanation? **NO** → Don't use Steps

### Should I use Tabs?

- Are there multiple valid approaches? **YES** → Consider Tabs
- Is this a tutorial? **NO** → Pick one method
- Is this a how-to guide? **YES** → Use Tabs
- Is this reference showing syntax variants? **MAYBE** → Use if clarifying

### Should I use Aside?

- Is this a brief note in context? **YES** → Use `type="note"`
- Is this a practical tip for problem-solving? **YES** → Use `type="tip"`
- Is this a warning about edge case? **YES** → Use `type="caution"`
- Is this a critical security warning? **YES** → Use `type="danger"`
- Is this reference documentation? **NO** → Don't use Aside
- Is this a long explanation? **NO** → Make it a section instead

### Should I use CardGrid?

- Is this organizing concepts? **YES** → Use CardGrid
- Is this a splash/landing page? **YES** → Use CardGrid
- Is this showing features? **YES** → Use CardGrid
- Is this showing tasks or data? **NO** → Use list or table

### Should I use LinkCard?

- Is this navigating to related documentation? **YES** → Use LinkCard
- Is this within a paragraph? **NO** → Use regular link
- Is this a list of many links? **MAYBE** → LinkCard for 2-4 links, list for more

---

## Quick Reference Cheat Sheet

| Component | Tutorial | How-To | Reference | Explanation |
|-----------|----------|--------|-----------|-------------|
| **Steps** | ✅ Primary | ❌ No | ❌ No | ❌ No |
| **Aside (note)** | ✅ Minimal | ✅ Yes | ❌ Rare | ✅ Yes |
| **Aside (tip/caution/danger)** | ❌ No | ✅ Primary | ❌ No | ⚠️ Sparingly |
| **Tabs** | ❌ No | ✅ Primary | ⚠️ Rare | ❌ No |
| **Card/CardGrid** | ❌ No | ❌ No | ❌ No | ✅ Primary |
| **LinkCard** | ✅ Yes | ✅ Yes | ✅ Primary | ✅ Yes |
| **Code blocks** | ✅ Complete | ✅ Practical | ✅ Syntax | ⚠️ Conceptual |
| **Tables** | ❌ No | ⚠️ Comparison | ✅ Primary | ⚠️ Comparison |

Legend:
- ✅ Primary use case
- ⚠️ Use sparingly with care
- ❌ Avoid (boundary violation)

---

## Additional Resources

- **Starlight Components**: https://starlight.astro.build/components/using-components/
- **Starlight Icons**: https://starlight.astro.build/reference/icons/
- **Starlight Frontmatter**: https://starlight.astro.build/reference/frontmatter/
- **Diátaxis Framework**: https://diataxis.fr/

---

## Testing Your Component Usage

### Questions to Ask

1. **Does this component match the mental state?**
   - Tutorial: Learning through doing
   - How-to: Solving a specific problem
   - Reference: Looking up information
   - Explanation: Understanding concepts

2. **Does this component help or hinder the user goal?**
   - Tabs in tutorials hinder (create uncertainty)
   - Steps in how-to guides hinder (too rigid)
   - Asides in reference hinder (break neutrality)

3. **Could this be simpler?**
   - CardGrid for two items? Use simple paragraphs.
   - LinkCard for inline navigation? Use regular link.
   - Aside for one sentence? Integrate into paragraph.

4. **Am I crossing Diátaxis boundaries?**
   - Instructions in explanation? Remove or move to how-to.
   - Explanations in tutorial? Move to explanation page.
   - Opinions in reference? Remove or make neutral.

Remember: Components serve users, not documentation aesthetics. Choose components that genuinely help accomplish the user's goal in their current mental state.
