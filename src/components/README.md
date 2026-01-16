# Custom Starlight Components

This directory contains custom Astro components designed specifically for the Radicale documentation site. All components follow Starlight design patterns and are built with accessibility, responsiveness, and dark mode support.

## Components

### RFCTable.astro

Displays RFC compliance information in a structured table with visual progress bars and status badges.

**Features:**
- Visual compliance percentage bars with color coding
- Status badges (full, partial, minimal, planned)
- Clickable RFC links
- Mobile-responsive (stacks on small screens)
- Dark mode support

**Usage:**
```astro
import RFCTable from '../../components/RFCTable.astro';

<RFCTable
  caption="Optional description of the table"
  items={[
    {
      rfc: "4791",
      title: "CalDAV",
      compliance: 95,
      status: "full",
      notes: "Complete implementation",
      link: "/rfc-compliance/4791-caldav/"  // Optional
    }
  ]}
/>
```

**Props:**
- `items` (required): Array of RFC items
  - `rfc` (string): RFC number
  - `title` (string): RFC title/name
  - `compliance` (number): Compliance percentage (0-100)
  - `status` ('full' | 'partial' | 'minimal' | 'planned'): Implementation status
  - `notes` (string, optional): Additional notes
  - `link` (string, optional): Link to detailed documentation
- `caption` (string, optional): Table description

---

### ConfigOption.astro

Documents configuration options with structured metadata, examples, and notes.

**Features:**
- Displays section and option name with anchor links
- Type and default value metadata
- Support for required/deprecated/version badges
- Markdown support in description, example, and notes slots
- Syntax highlighting for code examples
- Deprecation notices

**Usage:**
```astro
import ConfigOption from '../../components/ConfigOption.astro';

<ConfigOption
  section="auth"
  name="type"
  type="string"
  defaultValue="denyall"
  required={true}
  version="3.5"
  deprecated={false}
  deprecationNote="Migration instructions if deprecated"
>
  <Fragment slot="description">
    Description with **markdown** support
  </Fragment>
  <Fragment slot="example">
    ```ini
    [auth]
    type = htpasswd
    ```
  </Fragment>
  <Fragment slot="notes">
    Additional notes and warnings
  </Fragment>
</ConfigOption>
```

**Props:**
- `section` (required): Configuration section name
- `name` (required): Option name
- `type` (required): 'string' | 'integer' | 'boolean' | 'float' | 'list'
- `defaultValue` (string, optional): Default value
- `required` (boolean): Whether option is required
- `version` (string, optional): Version when option was introduced
- `deprecated` (boolean): Whether option is deprecated
- `deprecationNote` (string, optional): Deprecation explanation

**Slots:**
- `description` (optional): Main description of the option
- `example` (optional): Code examples
- `notes` (optional): Implementation notes and warnings

---

### MethodCard.astro

Displays HTTP/WebDAV method information in a visually distinct card format.

**Features:**
- Method name with monospace font
- HTTP method and standard badges
- RFC reference with link to spec
- Visual variants for read/write/special operations
- Support for unimplemented methods
- Request/response details in side-by-side layout

**Usage:**
```astro
import MethodCard from '../../components/MethodCard.astro';

<MethodCard
  method="PROPFIND"
  httpMethod="POST"
  standard="WebDAV"
  rfc="4918"
  variant="read"
  implemented={true}
  since="1.0"
>
  <Fragment slot="description">
    Method description
  </Fragment>
  <Fragment slot="request">
    Request details and parameters
  </Fragment>
  <Fragment slot="response">
    Response format and status codes
  </Fragment>
  <Fragment slot="example">
    ```xml
    <!-- Code example -->
    ```
  </Fragment>
  <Fragment slot="notes">
    Implementation notes
  </Fragment>
</MethodCard>
```

**Props:**
- `method` (required): Method name (e.g., "PROPFIND")
- `httpMethod` (optional): 'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATCH' | 'OPTIONS' | 'HEAD'
- `standard` (optional): 'HTTP' | 'WebDAV' | 'CalDAV' | 'CardDAV' (default: 'WebDAV')
- `rfc` (string, optional): RFC number for automatic linking
- `variant` (optional): 'default' | 'read' | 'write' | 'special' (adds colored left border)
- `implemented` (boolean): Whether method is implemented (default: true)
- `since` (string, optional): Version when method was implemented

**Slots:**
- `description` (optional): Method description
- `request` (optional): Request details
- `response` (optional): Response details
- `example` (optional): Code examples
- `notes` (optional): Implementation notes

---

### SequenceDiagram.astro

Renders sequence diagrams using Mermaid.js for visualizing protocol flows and interactions.

**Features:**
- Automatic theme detection (light/dark mode)
- Re-renders on theme change
- Mobile-responsive with horizontal scrolling
- Loading state indicator
- Multiple diagram types supported via Mermaid syntax

**Usage:**
```astro
import SequenceDiagram from '../../components/SequenceDiagram.astro';

<SequenceDiagram
  title="Diagram Title"
  caption="Optional explanation of the flow"
  theme="default"
  height="auto"
>
  participant Client
  participant Server

  Client->>Server: Request
  Server-->>Client: Response

  Note over Client,Server: Additional context
</SequenceDiagram>
```

**Props:**
- `title` (string, optional): Diagram title
- `caption` (string, optional): Caption/explanation below diagram
- `theme` (optional): 'default' | 'dark' | 'forest' | 'neutral' (auto-detects Starlight theme)
- `height` (string, optional): Fixed height (e.g., "400px"), default is "auto"

**Mermaid Syntax:**
The component content should be valid Mermaid sequence diagram syntax (without the `sequenceDiagram` declaration):

```
participant Name
participant Another as "Display Name"

Name->>Another: Solid line with arrow
Name-->>Another: Dotted line with arrow
Name-xAnother: Solid line with cross
Name--xAnother: Dotted line with cross

activate Name
Name->>Another: Message
deactivate Name

Note left of Name: Note text
Note right of Another: Note text
Note over Name,Another: Spanning note

loop Every minute
    Name->>Another: Periodic message
end

alt Successful case
    Name->>Another: Success
else Failure case
    Name->>Another: Error
end
```

**Dependencies:**
- Loads Mermaid.js from CDN (v11+)
- No build-time dependencies required

---

## Design Principles

### Starlight Integration

All components use Starlight's design system:
- CSS custom properties for colors (`--sl-color-*`)
- Typography scale (`--sl-text-*`)
- Font families (`--sl-font`, `--sl-font-mono`)
- Spacing and layout patterns
- Component styling conventions

### Accessibility

Components follow WCAG 2.1 AA guidelines:
- Semantic HTML structure
- Proper heading hierarchy
- Keyboard navigation support
- Screen reader friendly
- High contrast mode support
- Focus indicators
- Reduced motion support

### Responsive Design

Mobile-first approach:
- Flexible layouts using CSS Grid and Flexbox
- Breakpoints at 640px, 768px, and 1024px
- Touch-friendly interactive elements
- Horizontal scrolling for wide content
- Stacking layouts on small screens

### Dark Mode

All components support both light and dark themes:
- Use Starlight's theme system
- Automatic theme detection
- Smooth transitions between themes
- Readable contrast in both modes
- No reliance on hardcoded colors

### Performance

Components are optimized for speed:
- Minimal JavaScript (only SequenceDiagram uses external library)
- CSS-only animations and transitions
- Lazy loading for heavy dependencies
- Efficient rendering with Astro's static generation
- Print-friendly styles

## File Structure

```
src/components/
├── README.md              # This file
├── RFCTable.astro         # RFC compliance table
├── ConfigOption.astro     # Configuration documentation
├── MethodCard.astro       # HTTP method cards
└── SequenceDiagram.astro  # Mermaid sequence diagrams
```

## Testing

Test all components using the showcase page:
```
src/content/docs/test.mdx
```

View locally:
```bash
npm run dev
# Visit http://localhost:4321/test/
```

## Best Practices

### Import Organization

Import components at the top of your MDX files:
```astro
---
title: Page Title
---

import RFCTable from '../../components/RFCTable.astro';
import ConfigOption from '../../components/ConfigOption.astro';
```

### Component Spacing

Components automatically include appropriate vertical spacing. Avoid adding extra wrapper divs unless necessary.

### Prop Validation

TypeScript interfaces enforce prop types. Use the correct types to avoid build errors.

### Slot Content

Use `<Fragment slot="name">` for named slots to keep markup clean:
```astro
<ConfigOption>
  <Fragment slot="description">
    Content here
  </Fragment>
</ConfigOption>
```

### Code Examples

Use proper syntax highlighting in example slots:
```astro
<Fragment slot="example">
  ```ini
  [section]
  option = value
  ```
</Fragment>
```

### Accessibility

- Always provide descriptive text for links
- Use semantic heading levels
- Include alt text for images (if added to components)
- Test with keyboard navigation
- Verify screen reader compatibility

## Browser Support

Components are tested and supported in:
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Android)

## Troubleshooting

### Mermaid Diagrams Not Rendering

- Check browser console for errors
- Verify Mermaid syntax is valid
- Ensure CDN is accessible
- Try clearing browser cache

### Components Not Styled Correctly

- Verify Starlight CSS is loaded
- Check for conflicting styles
- Inspect CSS custom properties
- Test in both light and dark modes

### TypeScript Errors

- Ensure props match interface definitions
- Check for required vs optional props
- Verify correct prop types
- Run `npm run check` for validation

## Contributing

When adding new components:

1. Follow existing component patterns
2. Use Starlight CSS variables
3. Include TypeScript interfaces
4. Add dark mode support
5. Ensure mobile responsiveness
6. Test accessibility
7. Document in this README
8. Add examples to test.mdx

## Resources

- [Starlight Documentation](https://starlight.astro.build/)
- [Astro Components Guide](https://docs.astro.build/en/core-concepts/astro-components/)
- [Mermaid.js Documentation](https://mermaid.js.org/)
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
