# Cloudflare Workers

Use these defaults for new Workers projects. Keep an existing deployment setup
unless asked to migrate.

- **CLI and config:** Use the [Cloudflare CLI (`cf`)](https://developers.cloudflare.com/cf/)
  v1 release candidate or newer with
  [`cloudflare.config.ts`](https://developers.cloudflare.com/cf/projects/cloudflare-config/),
  not Wrangler with `wrangler.config.ts`.

- **Vite (including Vite+):** Add `cloudflare()` from
  [`@cloudflare/vite-plugin`](https://developers.cloudflare.com/workers/vite-plugin/)
  to `vite.config.ts` so development runs in the Workers runtime. Use
  [plugin v2.0.0-rc.0 or newer](https://developers.cloudflare.com/changelog/product/cf/)
  with the `cf` 1.0 RC, and keep the Worker configuration in
  `cloudflare.config.ts`.
