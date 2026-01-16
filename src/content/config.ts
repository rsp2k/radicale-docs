import { defineCollection, z } from 'astro:content';
import { docsSchema } from '@astrojs/starlight/schema';

const docsCollection = defineCollection({
  type: 'content',
  schema: docsSchema({
    extend: z.object({
      // Additional frontmatter for Diataxis framework
      diataxis_type: z.enum(['tutorial', 'how-to', 'reference', 'explanation']).optional(),
      // RFC compliance tracking
      rfc_numbers: z.array(z.number()).optional(),
      compliance_level: z.number().min(0).max(100).optional(),
    }),
  }),
});

export const collections = {
  docs: docsCollection,
};
