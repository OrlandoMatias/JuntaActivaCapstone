import fs from 'fs/promises';
import fsSync from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const cssPath = fileURLToPath(new URL('../dist/main.css', import.meta.url));

(async () => {
  try {
    const content = await fs.readFile(cssPath, 'utf8');
    const hasTailwind = /@tailwind|@apply/.test(content);
    console.log('inspect-css: path=', cssPath);
    console.log('inspect-css: contains @tailwind/@apply?', hasTailwind);
    console.log('--- file head (first 120 lines) ---');
    console.log(content.split('\n').slice(0, 120).join('\n'));
  } catch (e) {
    console.error('inspect-css: error reading file', e && (e.message || e));
    // If the file doesn't exist, show dist directory to help debug
    try {
      const distDir = path.dirname(cssPath);
      console.log('\ninspect-css: listing', distDir);
      const entries = fsSync.readdirSync(distDir, { withFileTypes: true });
      for (const ent of entries) {
        console.log(ent.isDirectory() ? '[DIR] ' : '      ', ent.name);
      }
    } catch (e2) {
      console.error('inspect-css: could not list dist directory', e2 && (e2.message || e2));
    }
    process.exit(1);
  }
})();
