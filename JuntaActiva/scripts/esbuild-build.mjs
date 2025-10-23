import path from 'path';
import { fileURLToPath } from 'url';
import fs from 'fs/promises';
import esbuild from 'esbuild';
import postcss from 'postcss';
import tailwindcss from 'tailwindcss';
import autoprefixer from 'autoprefixer';
import { execFile } from 'child_process';
import { promisify } from 'util';
const execFileAsync = promisify(execFile);

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const projectRoot = path.resolve(__dirname, '..');

const distDir = path.join(projectRoot, 'dist');
const clientIndex = path.join(projectRoot, 'client', 'index.html');

function aliasPlugin(aliases) {
  const exts = ['.tsx', '.ts', '.jsx', '.js', '.json'];
  return {
    name: 'alias-plugin',
    setup(build) {
      for (const [alias, target] of Object.entries(aliases)) {
        // use alias as provided (including trailing slash) so we don't match
        // unrelated package names like '@tanstack/...'
        const prefix = alias;
        const escaped = prefix.replace(/[.*+?^${}()|[\\]\\]/g, '\\$&');
        const filter = new RegExp('^' + escaped);
        build.onResolve({ filter }, async args => {
          const rest = args.path.slice(prefix.length);
          const base = path.resolve(projectRoot, target);
          for (const ext of exts) {
            const candidate = path.join(base, rest + ext);
            try {
              await fs.access(candidate);
              return { path: candidate };
            } catch (_) {}
          }
          try {
            const direct = path.join(base, rest);
            await fs.access(direct);
            return { path: direct };
          } catch (_) {}
          for (const ext of exts) {
            const idx = path.join(base, rest, 'index' + ext);
            try {
              await fs.access(idx);
              return { path: idx };
            } catch (_) {}
          }
          return { path: path.join(base, rest) };
        });
      }
    }
  };
}

async function ensureDistIndex() {
  await fs.mkdir(distDir, { recursive: true });
  const indexHtml = await fs.readFile(clientIndex, 'utf8');
  await fs.writeFile(path.join(distDir, 'index.html'), indexHtml, 'utf8');
  // copy favicon if present
  try {
    await fs.copyFile(path.join(projectRoot, 'client', 'favicon.ico'), path.join(distDir, 'favicon.ico'));
  } catch (_) {}
  // copy fallback.css if present so built site has fallback styles
  try {
    await fs.copyFile(path.join(projectRoot, 'client', 'fallback.css'), path.join(distDir, 'fallback.css'));
  } catch (_) {}
}

async function processCss() {
  const cssIn = path.join(projectRoot, 'client', 'src', 'index.css');
  const cssOut = path.join(distDir, 'main.css');
  const input = await fs.readFile(cssIn, 'utf8');
  // dynamically import Tailwind plugins (ESM-safe)
  const [{ default: tailwindcssAnimate }, { default: tailwindTypography }] = await Promise.all([
    import('tailwindcss-animate').catch(() => ({ default: undefined })),
    import('@tailwindcss/typography').catch(() => ({ default: undefined })),
  ]);

  const twConfig = {
    darkMode: 'class',
    content: ['./client/index.html', './client/src/**/*.{js,jsx,ts,tsx}'],
    theme: {
      extend: {
        borderRadius: {
          lg: '.5625rem',
          md: '.375rem',
          sm: '.1875rem',
        },
        colors: {
          background: 'hsl(var(--background) / <alpha-value>)',
          foreground: 'hsl(var(--foreground) / <alpha-value>)',
          border: 'hsl(var(--border) / <alpha-value>)',
          input: 'hsl(var(--input) / <alpha-value>)',
          card: {
            DEFAULT: 'hsl(var(--card) / <alpha-value>)',
            foreground: 'hsl(var(--card-foreground) / <alpha-value>)',
            border: 'hsl(var(--card-border) / <alpha-value>)',
          },
          popover: {
            DEFAULT: 'hsl(var(--popover) / <alpha-value>)',
            foreground: 'hsl(var(--popover-foreground) / <alpha-value>)',
            border: 'hsl(var(--popover-border) / <alpha-value>)',
          },
          primary: {
            DEFAULT: 'hsl(var(--primary) / <alpha-value>)',
            foreground: 'hsl(var(--primary-foreground) / <alpha-value>)',
            border: 'var(--primary-border)',
          },
          secondary: {
            DEFAULT: 'hsl(var(--secondary) / <alpha-value>)',
            foreground: 'hsl(var(--secondary-foreground) / <alpha-value>)',
            border: 'var(--secondary-border)',
          },
          muted: {
            DEFAULT: 'hsl(var(--muted) / <alpha-value>)',
            foreground: 'hsl(var(--muted-foreground) / <alpha-value>)',
            border: 'var(--muted-border)',
          },
          accent: {
            DEFAULT: 'hsl(var(--accent) / <alpha-value>)',
            foreground: 'hsl(var(--accent-foreground) / <alpha-value>)',
            border: 'var(--accent-border)',
          },
          destructive: {
            DEFAULT: 'hsl(var(--destructive) / <alpha-value>)',
            foreground: 'hsl(var(--destructive-foreground) / <alpha-value>)',
            border: 'var(--destructive-border)',
          },
          ring: 'hsl(var(--ring) / <alpha-value>)',
          chart: {
            '1': 'hsl(var(--chart-1) / <alpha-value>)',
            '2': 'hsl(var(--chart-2) / <alpha-value>)',
            '3': 'hsl(var(--chart-3) / <alpha-value>)',
            '4': 'hsl(var(--chart-4) / <alpha-value>)',
            '5': 'hsl(var(--chart-5) / <alpha-value>)',
          },
          sidebar: {
            ring: 'hsl(var(--sidebar-ring) / <alpha-value>)',
            DEFAULT: 'hsl(var(--sidebar) / <alpha-value>)',
            foreground: 'hsl(var(--sidebar-foreground) / <alpha-value>)',
            border: 'hsl(var(--sidebar-border) / <alpha-value>)',
          },
          'sidebar-primary': {
            DEFAULT: 'hsl(var(--sidebar-primary) / <alpha-value>)',
            foreground: 'hsl(var(--sidebar-primary-foreground) / <alpha-value>)',
            border: 'var(--sidebar-primary-border)',
          },
          'sidebar-accent': {
            DEFAULT: 'hsl(var(--sidebar-accent) / <alpha-value>)',
            foreground: 'hsl(var(--sidebar-accent-foreground) / <alpha-value>)',
            border: 'var(--sidebar-accent-border)',
          },
          status: {
            online: 'rgb(34 197 94)',
            away: 'rgb(245 158 11)',
            busy: 'rgb(239 68 68)',
            offline: 'rgb(156 163 175)',
          },
        },
        fontFamily: {
          sans: ['var(--font-sans)'],
          serif: ['var(--font-serif)'],
          mono: ['var(--font-mono)'],
        },
      },
    },
    plugins: [tailwindcssAnimate || (()=>{}), tailwindTypography || (()=>{})],
  };

  const result = await postcss([
    tailwindcss(twConfig),
    autoprefixer,
  ]).process(input, { from: cssIn });
  await fs.writeFile(cssOut, result.css, 'utf8');
  console.log('postcss: wrote', cssOut);
  if (/@tailwind|@apply/.test(result.css)) {
    console.log('postcss: tailwind directives still present — running tailwind CLI fallback');
    const cliPath = path.join(projectRoot, 'node_modules', 'tailwindcss', 'lib', 'cli.js');
    const outPath = path.join(distDir, 'main.css');
    const backupPath = path.join(distDir, `main.css.before.${Date.now()}`);
    try {
      try { await fs.copyFile(outPath, backupPath); console.log('tailwind: backed up previous CSS to', backupPath); } catch (_) {}
      await fs.access(cliPath);
      const { stdout, stderr } = await execFileAsync('node', [cliPath, '-i', './client/src/index.css', '-o', './dist/main.css', '--minify', '--content', './client/index.html', '--content', './client/src/**/*.{js,jsx,ts,tsx}'], { cwd: projectRoot, windowsHide: true });
      if (stdout) console.log('tailwind (node) stdout:', stdout.trim());
      if (stderr) console.error('tailwind (node) stderr:', stderr.trim());
      console.log('tailwind CLI: wrote dist/main.css (via node cli.js)');
      try {
        const beforeStat = await fs.stat(backupPath).catch(()=>null);
        const afterStat = await fs.stat(outPath).catch(()=>null);
        console.log('tailwind: sizes — before=', beforeStat ? beforeStat.size : 'none', 'after=', afterStat ? afterStat.size : 'none');
      } catch (_) {}
    } catch (err) {
      console.log('tailwind node CLI failed or not present:', err && (err.message || err));
      try {
        const localBin = path.join(projectRoot, 'node_modules', '.bin', process.platform === 'win32' ? 'tailwindcss.cmd' : 'tailwindcss');
        await fs.access(localBin);
        try {
          const { stdout, stderr } = await execFileAsync(localBin, ['-i', './client/src/index.css', '-o', './dist/main.css', '--minify', '--content', './client/index.html', '--content', './client/src/**/*.{js,jsx,ts,tsx}'], { cwd: projectRoot, windowsHide: true });
          if (stdout) console.log('tailwind (local) stdout:', stdout.trim());
          if (stderr) console.error('tailwind (local) stderr:', stderr.trim());
          console.log('tailwind CLI: wrote dist/main.css (via local bin)');
        } catch (errLocal) {
          console.log('local tailwind binary failed:', errLocal && (errLocal.message || errLocal));
          try {
            const { stdout, stderr } = await execFileAsync('cmd.exe', ['/c', 'npx', 'tailwindcss', '-i', './client/src/index.css', '-o', './dist/main.css', '--minify', '--content', './client/index.html', '--content', './client/src/**/*.{js,jsx,ts,tsx}'], { cwd: projectRoot, windowsHide: true });
            if (stdout) console.log('tailwind (cmd) stdout:', stdout.trim());
            if (stderr) console.error('tailwind (cmd) stderr:', stderr.trim());
            console.log('tailwind CLI: wrote dist/main.css (via cmd.exe /c npx)');
          } catch (errCmd) {
            console.error('tailwind CLI final fallback failed:', errCmd && (errCmd.message || errCmd) || 'unknown error');
          }
        }
      } catch (errBin) {
        console.error('no tailwind CLI available (node cli, local bin) and npx fallback failed:', errBin && (errBin.message || errBin));
      }
    }
  }
}

async function build() {
  await ensureDistIndex();

  const aliases = {
    '@assets/': 'attached_assets/',
    '@/': 'client/src/',
    '@shared/': 'shared/',
  };

  await esbuild.build({
    entryPoints: [path.join(projectRoot, 'client', 'src', 'main.tsx')],
    bundle: true,
    minify: true,
    outfile: path.join(distDir, 'main.js'),
    sourcemap: true,
    loader: { '.tsx': 'tsx', '.ts': 'ts', '.jpg': 'file', '.png': 'file', '.svg': 'file', '.woff2': 'file', '.css': 'css' },
    jsx: 'automatic',
    plugins: [aliasPlugin(aliases)],
    absWorkingDir: projectRoot,
  });

  await processCss();
  // ensure fallback.css is copied into dist
  try {
    await fs.copyFile(path.join(projectRoot, 'client', 'fallback.css'), path.join(distDir, 'fallback.css'));
  } catch (_) {}

  console.log('esbuild: build complete -> dist/main.js');
}

build().catch(err => {
  console.error(err);
  process.exit(1);
});
