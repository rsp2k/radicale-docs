# syntax=docker/dockerfile:1
FROM ghcr.io/astral-sh/uv:0.5.13-python3.12-bookworm-slim AS base

# Disable Astro telemetry
ENV ASTRO_TELEMETRY_DISABLED=1

# Node.js installation
FROM base AS node-base
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

# Development stage
FROM node-base AS development
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 4321
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]

# Build stage
FROM node-base AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Production stage with nginx
FROM nginx:alpine AS production
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
