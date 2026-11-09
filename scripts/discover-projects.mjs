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
