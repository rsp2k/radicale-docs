# Custom Starlight Components for Radicale Documentation

This document provides an overview of the custom components created for the Radicale documentation site.

## Created Components

### 1. RFCTable.astro
**Location:** `/home/rpm/claude/radicale/radicale-docs/src/components/RFCTable.astro`

A comprehensive table component for displaying RFC compliance information.

**Features:**
- Visual compliance progress bars with color-coded percentages
- Status badges (full, partial, minimal, planned)
- RFC links to detailed documentation
- Mobile-responsive with stacking layout
- Dark mode support
- Print-friendly styling

**Example Usage:**
```astro
<RFCTable
  caption="Core CalDAV and CardDAV protocol support"
  items={[
    {
      rfc: "4791",
      title: "CalDAV",
      compliance: 95,
      status: "full",
      notes: "All core features supported",
      link: "/rfc-compliance/4791-caldav/"
    }
  ]}
/>
```

---

### 2. ConfigOption.astro
**Location:** `/home/rpm/claude/radicale/radicale-docs/src/components/ConfigOption.astro`

Structured documentation component for configuration options.

**Features:**
- Section and option name with automatic anchor links
- Type and default value metadata display
- Required, version, and deprecated badges
- Markdown support in description, examples, and notes
- Syntax highlighting for code examples
- Deprecation notices with migration guidance
- Highlight on target (anchor navigation)

**Example Usage:**
```astro
<ConfigOption
  section="auth"
  name="type"
  type="string"
  defaultValue="denyall"
  required={true}
  version="3.5"
>
  <Fragment slot="description">
    Authentication backend to use. Options: htpasswd, ldap, oauth2, none, denyall
  </Fragment>
  <Fragment slot="example">
    ```ini
    [auth]
    type = htpasswd
    htpasswd_filename = /etc/radicale/users
    ```
  </Fragment>
  <Fragment slot="notes">
    - The default denyall prevents unauthorized access
    - Always use strong password hashing
  </Fragment>
</ConfigOption>
```

---

### 3. MethodCard.astro
**Location:** `/home/rpm/claude/radicale/radicale-docs/src/components/MethodCard.astro`

Card component for documenting HTTP and WebDAV methods.

**Features:**
- Method name in monospace font
- HTTP method and standard badges (WebDAV, CalDAV, CardDAV)
- RFC reference with automatic linking
- Visual variants (read/write/special with colored borders)
- Unimplemented method support (dashed border)
- Side-by-side request/response layout
- Hover effects and transitions

**Example Usage:**
```astro
<MethodCard
  method="PROPFIND"
  httpMethod="POST"
  standard="WebDAV"
  rfc="4918"
  variant="read"
  since="1.0"
>
  <Fragment slot="description">
    Retrieves properties defined on a resource or collection
  </Fragment>
  <Fragment slot="request">
    - XML body with property names to retrieve
    - Depth header: 0, 1, or infinity
  </Fragment>
  <Fragment slot="response">
    - 207 Multi-Status with requested properties
  </Fragment>
</MethodCard>
```

---

### 4. SequenceDiagram.astro
**Location:** `/home/rpm/claude/radicale/radicale-docs/src/components/SequenceDiagram.astro`

Mermaid.js-powered sequence diagram component for visualizing protocol flows.

**Features:**
- Automatic Starlight theme detection (light/dark)
- Re-renders on theme change
- Mobile-responsive with horizontal scrolling
- Loading state indicator
- CDN-based Mermaid.js (no build dependencies)
- Support for all Mermaid sequence diagram features

**Example Usage:**
```astro
<SequenceDiagram
  title="CalDAV Calendar Creation"
  caption="Client creates a new calendar and adds an event"
>
  participant Client
  participant Server
  participant Storage

  Client->>Server: MKCALENDAR /calendars/user/work/
  Server->>Storage: Create collection
  Storage-->>Server: Collection created
  Server-->>Client: 201 Created
</SequenceDiagram>
```

---

## Supporting Files

### Custom CSS
**Location:** `/home/rpm/claude/radicale/radicale-docs/src/styles/custom.css`

Enhanced custom styles including:
- Component-specific CSS variables
- Smooth scrolling for anchor links
- Print styles for all components
- Accessibility improvements (focus states, reduced motion)
- Custom scrollbar styling
- High contrast mode support
- Utility classes for layouts

### Component Documentation
**Location:** `/home/rpm/claude/radicale/radicale-docs/src/components/README.md`

Comprehensive documentation covering:
- Detailed component APIs and props
- Usage examples for each component
- Design principles and accessibility features
- Responsive design approach
- Dark mode implementation
- Performance considerations
- Browser support matrix
- Troubleshooting guide

### Test/Showcase Page
**Location:** `/home/rpm/claude/radicale/radicale-docs/src/content/docs/test.mdx`

Live demonstration page featuring:
- Working examples of all four components
- Multiple use cases per component
- Real-world CalDAV/CardDAV scenarios
- Usage guidelines and code snippets
- Accessibility and theming information

## Design System Integration

All components seamlessly integrate with Starlight's design system:

### Color System
- Uses Starlight CSS custom properties (`--sl-color-*`)
- Respects light/dark theme preferences
- Automatic theme detection and switching
- Consistent color coding across components

### Typography
- Matches Starlight's text scale (`--sl-text-*`)
- Uses Starlight font families (`--sl-font`, `--sl-font-mono`)
- Maintains consistent line heights and spacing
- Proper heading hierarchy

### Accessibility
- WCAG 2.1 AA compliant
- Semantic HTML structure
- Keyboard navigation support
- Screen reader friendly
- Focus indicators
- High contrast mode support
- Reduced motion support

### Responsive Design
- Mobile-first approach
- Breakpoints: 640px, 768px, 1024px
- Touch-friendly interactive elements
- Horizontal scrolling for wide content
- Adaptive layouts for all screen sizes

## Build Information

**Build Status:** ✅ Success
- All components compile without errors
- TypeScript interfaces validated
- MDX syntax properly formatted
- Static generation working correctly
- Pagefind search indexing enabled

**Build Output:**
- 13 pages generated
- 2158 words indexed
- 12 searchable pages
- All components rendering correctly

## Usage in Documentation

To use these components in your documentation pages:

1. **Import the component:**
```astro
import RFCTable from '../../components/RFCTable.astro';
```

2. **Use in MDX content:**
```mdx
---
title: Your Page Title
---

import RFCTable from '../../components/RFCTable.astro';

# Your Content

<RFCTable items={[...]} />
```

3. **View the test page:**
Visit `/test/` in your local development server to see all components in action.

## Development Workflow

**Start development server:**
```bash
cd /home/rpm/claude/radicale/radicale-docs
npm run dev
```

**Build for production:**
```bash
npm run build
```

**Preview production build:**
```bash
npm run preview
```

## File Locations Summary

```
radicale-docs/
├── src/
│   ├── components/
│   │   ├── README.md              # Component documentation
│   │   ├── RFCTable.astro         # RFC compliance table
│   │   ├── ConfigOption.astro     # Configuration option docs
│   │   ├── MethodCard.astro       # HTTP method documentation
│   │   └── SequenceDiagram.astro  # Mermaid sequence diagrams
│   ├── content/
│   │   └── docs/
│   │       └── test.mdx           # Component showcase
│   └── styles/
│       └── custom.css             # Enhanced custom styles
├── astro.config.mjs               # Updated with social links fix
└── COMPONENTS.md                  # This file
```

## Next Steps

1. **Review the test page** at `/test/` to see all components in action
2. **Read component documentation** in `src/components/README.md`
3. **Start using components** in your documentation pages
4. **Customize as needed** while maintaining Starlight integration

All components are production-ready and designed to enhance the Radicale documentation experience!
