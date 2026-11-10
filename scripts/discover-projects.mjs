import { readdir, stat, writeFile } from 'node:fs/promises';
import path from 'node:path';

const root = process.cwd();
const skip = new Set(['.git', '.github', '.vercel', 'node_modules', 'renders', 'snapshots', 'sourcing']);
const projects = [];

async function walk(dir, rel = '') {
  let entries;
  try { entries = await readdir(dir, { withFileTypes: true }); } catch { return; }
  for (const entry of entries) {
    if (entry.name.startsWith('.') || skip.has(entry.name)) continue;
    const full = path.join(dir, entry.name);
    const nextRel = rel ? path.join(rel, entry.name) : entry.name;
    if (!entry.isDirectory()) continue;
    const videoIndex = path.join(full, 'video', 'index.html');
    try {
      await stat(videoIndex);
      // Vercel is a preview host; the music bed is regenerated only in GitHub Actions.
      // Remove the missing bed track from the deployed preview so the player can boot silently.
      const html = await (await import('node:fs/promises')).readFile(videoIndex, 'utf8');
      const previewHtml = html.replace(/<head>/i, '<head><script src=\"/runtime.js\"></script>').replace(/\s*<audio id=\"mix-fx\"[^>]*><\/audio>/g, '');
      if (previewHtml !== html) await (await import('node:fs/promises')).writeFile(videoIndex, previewHtml);
      projects.push({ id: nextRel.replaceAll(path.sep, '/'), label: nextRel.replaceAll(path.sep, ' / '), preview: `${nextRel.replaceAll(path.sep, '/')}/video/` });
      continue;
    } catch {}
    await walk(full, nextRel);
  }
}

await walk(root);
projects.sort((a, b) => a.label.localeCompare(b.label));
await writeFile(path.join(root, 'projects.json'), JSON.stringify({ generatedAt: new Date().toISOString(), projects }, null, 2) + '\n');
console.log(`discovered ${projects.length} video projects`);
