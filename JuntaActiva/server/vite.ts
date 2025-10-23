import express, { type Express } from "express";
import fs from "fs";
import path from "path";
import { createServer as createViteServer, createLogger } from "vite";
import { type Server } from "http";
import viteConfig from "../vite.config";
import { nanoid } from "nanoid";

const viteLogger = createLogger();

export function log(message: string, source = "express") {
  const formattedTime = new Date().toLocaleTimeString("en-US", {
    hour: "numeric",
    minute: "2-digit",
    second: "2-digit",
    hour12: true,
  });

  console.log(`${formattedTime} [${source}] ${message}`);
}

export async function setupVite(app: Express, server: Server) {
  const serverOptions = {
    middlewareMode: true,
    hmr: { server },
    allowedHosts: true as const,
  };

  const vite = await createViteServer({
    ...viteConfig,
    configFile: false,
    customLogger: {
      ...viteLogger,
      error: (msg, options) => {
        viteLogger.error(msg, options);
        process.exit(1);
      },
    },
    server: serverOptions,
    appType: "custom",
  });

  app.use(vite.middlewares);
  // diagnostic: log that vite middleware was attached
  log('Vite dev middleware attached', 'vite');

  // diagnostic middleware — log requests to /src to inspect how they are handled
  app.use((req, res, next) => {
    if (req.path.startsWith('/src')) {
      res.on('finish', () => {
        log(`REQ ${req.method} ${req.path} -> ${res.statusCode}; Content-Type: ${res.getHeader('Content-Type')}`, 'vite-req');
      });
    }
    next();
  });
  app.use("*", async (req, res, next) => {
    const url = req.originalUrl;

    try {
      const clientTemplate = path.resolve(
        import.meta.dirname,
        "..",
        "client",
        "index.html",
      );

      // always reload the index.html file from disk incase it changes
      let template = await fs.promises.readFile(clientTemplate, "utf-8");
      // ensure a base href is present so relative imports like "src/main.tsx"
      // resolve to the server root. This prevents requests like
      // /JuntaActiva/client/src/main.tsx when the page is opened at
      // /JuntaActiva/client/index.html
      if (!/\<base\s+href=/.test(template)) {
        template = template.replace(/<head(>|\s[^>]*>)/i, (m) => `${m}\n    <base href="/" />`);
      }
      // index.html now references the script as a relative path 'src/main.tsx'
      // replace that exact string and add a cache-busting query so the browser reloads
      template = template.replace(
        `src=\"src/main.tsx\"`,
        `src=\"src/main.tsx?v=${nanoid()}\"`,
      );
  // Use '/' as the URL used for transform to avoid Vite resolving the path
  // with repository filesystem segments (which can produce incorrect resolved ids
  // like /JuntaActiva/client/src/...). Using '/' tells Vite to rewrite imports
  // relative to the dev server root.
  log(`transformIndexHtml incoming url: ${url}`, 'vite');
  const page = await vite.transformIndexHtml('/', template);
  // diagnostic: log a short preview of the transformed page to inspect injected paths
  log(`transformed index.html preview:\n${page.split('\n').slice(0,6).join('\n')}`, 'vite');
  res.status(200).set({ "Content-Type": "text/html" }).end(page);
    } catch (e) {
      vite.ssrFixStacktrace(e as Error);
      next(e);
    }
  });
}

export function serveStatic(app: Express) {
  // build output is configured to go to <repo root>/dist/public
  // import.meta.dirname here is <repo root>/server, so resolve up one level
  const distPath = path.resolve(import.meta.dirname, "..", "dist", "public");

  if (!fs.existsSync(distPath)) {
    throw new Error(
      `Could not find the build directory: ${distPath}, make sure to build the client first`,
    );
  }

  app.use(express.static(distPath));

  // fall through to index.html if the file doesn't exist
  app.use("*", (_req, res) => {
    res.sendFile(path.resolve(distPath, "index.html"));
  });
}
