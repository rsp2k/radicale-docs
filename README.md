# Radicale Documentation

Starlight-based documentation site for [Radicale](https://github.com/Kozea/Radicale), showcasing industry-leading RFC compliance (85-98%) and providing world-class documentation experience.

## Project Overview

This is a **separate documentation repository** built with [Astro](https://astro.build) and [Starlight](https://starlight.astro.build), organized using the [Diataxis framework](https://diataxis.fr/) for optimal user experience.

### Why Separate Repo?

- **Diataxis Organization**: Strict separation of tutorials, how-tos, reference, and explanations
- **Starlight Features**: Full-text search, mobile-responsive, dark mode, component library
- **Independent Deployment**: Documentation can be updated without releasing new Radicale versions
- **RFC Showcase**: Dedicated section highlighting 85-98% compliance across major standards

## Quick Start

### Development Environment

```bash
# Clone the repository
git clone https://github.com/rsp2k/radicale-docs.git
cd radicale-docs

# Copy environment variables
cp .env.example .env

# Start development server (Docker)
make dev

# Access at https://radicale-docs.local (via Caddy reverse proxy)
```

### Production Build

```bash
# Build for production
make build

# Run production container
make prod
```

## Project Structure

```
radicale-docs/
├── src/
│   ├── content/
│   │   ├── docs/               # All documentation markdown files
│   │   │   ├── getting-started/
│   │   │   ├── tutorials/      # Learning-oriented (Diataxis)
│   │   │   ├── how-to/         # Task-oriented (Diataxis)
│   │   │   ├── reference/      # Information-oriented (Diataxis)
│   │   │   ├── rfc-compliance/ # RFC showcase
│   │   │   └── explanations/   # Understanding-oriented (Diataxis)
│   │   └── config.ts           # Content collections schema
│   ├── components/             # Custom Astro components
│   ├── styles/                 # Global styles
│   └── assets/                 # Images, logos, etc.
├── scripts/                    # Migration and validation scripts
├── astro.config.mjs            # Astro configuration
├── docker-compose.yml          # Dev + prod services
├── Dockerfile                  # Multi-stage build
└── Makefile                    # Common operations
```

## Diataxis Framework

This documentation strictly follows [Diataxis](https://diataxis.fr/) principles:

- **Tutorials** (`/tutorials/`): Learning by doing - step-by-step lessons for beginners
- **How-To Guides** (`/how-to/`): Task-oriented - solve specific problems
- **Reference** (`/reference/`): Information-oriented - technical descriptions
- **Explanations** (`/explanations/`): Understanding-oriented - conceptual background

Each documentation type serves a different user mental state and must not be mixed.

## Development Workflow

### Make Commands

```bash
make dev      # Start development server with hot reload
make build    # Build Docker images
make prod     # Run production server
make stop     # Stop all containers
make logs     # View container logs
make clean    # Remove containers and build artifacts
```

### Adding Content

1. Create markdown file in appropriate Diataxis directory
2. Add frontmatter with `diataxis_type`:

```yaml
---
title: Your Page Title
description: Brief description
diataxis_type: tutorial  # or: how-to, reference, explanation
---
```

3. Update `astro.config.mjs` sidebar if needed
4. Test with `make dev`

### Custom Components

Located in `src/components/`:

- **RFCTable.astro**: Display RFC compliance matrix
- **ConfigOption.astro**: Document configuration options
- More components will be added during migration

## RFC Compliance Showcase

This documentation highlights Radicale's exceptional standards compliance:

| RFC | Title | Compliance | Status |
|-----|-------|------------|--------|
| RFC 3253 | WebDAV Versioning (DeltaV) | 80% | ✅ Complete write operations |
| RFC 4791 | CalDAV | 90% | ✅ Core complete |
| RFC 6352 | CardDAV | 90% | ✅ Core complete |
| RFC 6638 | CalDAV Scheduling | 95% | ✅ Near-complete |
| RFC 6047 | iMIP Email Scheduling | 98% | ✅ Full bidirectional |
| RFC 5546 | iTIP | 95% | ✅ Core methods complete |

See `/rfc-compliance/` section for detailed breakdowns.

## Migration Status

### Phase 1: Infrastructure ✅ Complete
- [x] Repository setup
- [x] Docker configuration
- [x] Starlight configuration
- [x] Content collections schema
- [x] Initial commit

### Phase 2: Structure (Week 2)
- [ ] Create directory structure for all Diataxis sections
- [ ] Set up content collections for each section
- [ ] Configure navigation and sidebar

### Phase 3: Components (Week 3)
- [ ] RFCTable component
- [ ] ConfigOption component
- [ ] MethodCard component
- [ ] SequenceDiagram component

### Phase 4-6: Content Migration (Weeks 4-6)
- [ ] Extract and migrate 10,000+ lines from ADVANCED-FEATURES.md
- [ ] Migrate SCHEDULING.md content
- [ ] Migrate DOCUMENTATION.md content
- [ ] Write 5 tutorials from scratch
- [ ] Create 20+ how-to guides
- [ ] Write 8+ explanation articles

### Phase 7: Testing & Deployment (Week 7)
- [ ] Build verification
- [ ] Link checking
- [ ] CI/CD pipeline setup
- [ ] Production deployment

## Technical Details

### Docker Configuration

**Multi-stage build:**
1. **Base**: uv-based Python image with Node.js
2. **Development**: Hot reload with volume mounts
3. **Builder**: Production build stage
4. **Production**: Nginx serving static files

### Caddy Reverse Proxy

Development server configured for Caddy with:
- HMR WebSocket support (no connection drops)
- Proper flush intervals and timeouts
- TLS termination at proxy level

### HMR Configuration

Vite dev server configured for reverse proxy:
```javascript
vite: {
  server: {
    host: '0.0.0.0',
    hmr: {
      host: process.env.HMR_HOST || 'radicale-docs.local',
      protocol: 'wss',
      clientPort: 443
    }
  }
}
```

## Contributing

### Content Guidelines

1. **Respect Diataxis boundaries** - Don't mix tutorial, how-to, reference, and explanation content
2. **Use consistent voice** - Match the tone of existing docs in each section
3. **Test examples** - All code examples must be tested and working
4. **Link to RFCs** - Reference relevant RFCs when discussing standards compliance

### Anti-Patterns to Avoid

Run `scripts/check-diataxis.py` to detect common anti-patterns:
- Tutorials with branches ("you can also...")
- How-tos with learning content ("let's understand...")
- Reference with prescriptive language ("you should...")
- Explanations with instructions ("run this command...")

## Resources

- [Astro Documentation](https://docs.astro.build)
- [Starlight Documentation](https://starlight.astro.build)
- [Diataxis Framework](https://diataxis.fr/)
- [Radicale Main Repository](https://github.com/Kozea/Radicale)

## License

This documentation is part of the Radicale project and is licensed under the GNU General Public License v3.0.
