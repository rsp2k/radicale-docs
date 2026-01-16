import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  site: 'https://docs.radicale.org',

  // Disable telemetry per user preferences
  telemetry: false,

  // Disable dev toolbar per user preferences
  devToolbar: { enabled: false },

  // HMR configuration for Caddy reverse proxy
  vite: {
    server: {
      host: '0.0.0.0',
      hmr: {
        host: process.env.HMR_HOST || 'radicale-docs.local',
        protocol: 'wss',
        clientPort: 443
      }
    }
  },

  integrations: [
    starlight({
      title: 'Radicale',
      description: 'CalDAV and CardDAV server documentation',

      logo: {
        src: './src/assets/radicale-logo.svg',
      },

      social: [
        {
          icon: 'github',
          label: 'GitHub',
          href: 'https://github.com/Kozea/Radicale',
        },
      ],

      sidebar: [
        {
          label: 'Getting Started',
          items: [
            { label: 'Introduction', link: '/getting-started/' },
            { label: 'Quick Start', link: '/getting-started/quick-start/' },
            { label: 'Installation', link: '/getting-started/installation/' },
          ],
        },
        {
          label: 'Tutorials',
          badge: { text: 'Learn', variant: 'success' },
          items: [
            { label: 'Your First Calendar Server', link: '/tutorials/first-server/' },
            { label: 'Adding Scheduling', link: '/tutorials/scheduling/' },
            { label: 'Setting Up Metrics', link: '/tutorials/metrics/' },
            { label: 'Enabling Versioning', link: '/tutorials/versioning/' },
            { label: 'WebSocket Sync', link: '/tutorials/websocket/' },
          ],
        },
        {
          label: 'How-To Guides',
          badge: { text: 'Tasks', variant: 'note' },
          items: [
            { label: 'Authentication', collapsed: true, items: [
              { label: 'htpasswd', link: '/how-to/auth/htpasswd/' },
              { label: 'LDAP', link: '/how-to/auth/ldap/' },
              { label: 'OAuth2', link: '/how-to/auth/oauth2/' },
            ]},
            { label: 'Deployment', collapsed: true, items: [
              { label: 'Caddy Reverse Proxy', link: '/how-to/deployment/caddy/' },
              { label: 'Nginx Reverse Proxy', link: '/how-to/deployment/nginx/' },
              { label: 'WSGI Servers', link: '/how-to/deployment/wsgi/' },
            ]},
            { label: 'Scheduling', collapsed: true, items: [
              { label: 'Email Delivery', link: '/how-to/scheduling/email/' },
              { label: 'IMAP Polling', link: '/how-to/scheduling/imap/' },
              { label: 'Resource Calendars', link: '/how-to/scheduling/resources/' },
            ]},
            { label: 'Monitoring', collapsed: true, items: [
              { label: 'Prometheus Integration', link: '/how-to/monitoring/prometheus/' },
              { label: 'Grafana Dashboard', link: '/how-to/monitoring/grafana/' },
            ]},
            { label: 'Versioning', collapsed: true, items: [
              { label: 'Enable Git Versioning', link: '/how-to/versioning/enable/' },
              { label: 'Version Labels', link: '/how-to/versioning/labels/' },
              { label: 'Activities', link: '/how-to/versioning/activities/' },
            ]},
            { label: 'Troubleshooting', collapsed: true, items: [
              { label: 'Authentication Issues', link: '/how-to/troubleshooting/auth/' },
              { label: 'Scheduling Problems', link: '/how-to/troubleshooting/scheduling/' },
              { label: 'Versioning Issues', link: '/how-to/troubleshooting/versioning/' },
            ]},
          ],
        },
        {
          label: 'Reference',
          badge: { text: 'Lookup', variant: 'caution' },
          items: [
            { label: 'Configuration', link: '/reference/configuration/' },
            { label: 'HTTP Methods', link: '/reference/http-methods/' },
            { label: 'Properties', link: '/reference/properties/' },
            { label: 'Metrics', link: '/reference/metrics/' },
            { label: 'Storage Layout', link: '/reference/storage/' },
            { label: 'CLI Commands', link: '/reference/cli/' },
          ],
        },
        {
          label: 'RFC Compliance',
          badge: { text: '85-98%', variant: 'success' },
          items: [
            { label: 'Overview', link: '/rfc-compliance/' },
            { label: 'RFC 3253 - DeltaV', link: '/rfc-compliance/3253-deltav/' },
            { label: 'RFC 4791 - CalDAV', link: '/rfc-compliance/4791-caldav/' },
            { label: 'RFC 6352 - CardDAV', link: '/rfc-compliance/6352-carddav/' },
            { label: 'RFC 6638 - Scheduling', link: '/rfc-compliance/6638-scheduling/' },
            { label: 'RFC 6047 - iMIP', link: '/rfc-compliance/6047-imip/' },
            { label: 'Extended RFCs', link: '/rfc-compliance/extended/' },
          ],
        },
        {
          label: 'Explanations',
          badge: { text: 'Understand', variant: 'tip' },
          items: [
            { label: 'Architecture', link: '/explanations/architecture/' },
            { label: 'How CalDAV Works', link: '/explanations/caldav/' },
            { label: 'How Scheduling Works', link: '/explanations/scheduling/' },
            { label: 'Versioning Concepts', link: '/explanations/versioning/' },
            { label: 'Security Model', link: '/explanations/security/' },
            { label: 'When to Use Versioning', link: '/explanations/when-versioning/' },
            { label: 'Choosing Auth Method', link: '/explanations/choosing-auth/' },
          ],
        },
      ],

      customCss: [
        './src/styles/custom.css',
      ],

      components: {
        // Custom component overrides if needed
      },
    }),
  ],
});
