import fs from 'node:fs';
import path from 'node:path';

function validProject(project) {
  return typeof project === 'string' && /^[A-Za-z0-9_./-]+$/.test(project) && !project.includes('..');
}

export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ error: 'POST required' });
  const project = req.body?.project;
  if (!validProject(project)) return res.status(400).json({ error: 'Invalid project path' });
  const projectRoot = path.join(process.cwd(), project, 'video', 'index.html');
  if (!fs.existsSync(projectRoot)) return res.status(404).json({ error: 'Video project not found' });
  if (!process.env.GITHUB_TOKEN) return res.status(500).json({ error: 'GITHUB_TOKEN is not configured in Vercel' });

  const response = await fetch('https://api.github.com/repos/Shadowlordi16/yt-atm/actions/workflows/render-video.yml/dispatches', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${process.env.GITHUB_TOKEN}`,
      Accept: 'application/vnd.github+json',
      'X-GitHub-Api-Version': '2022-11-28',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ ref: 'main', inputs: { project, output_name: `${project.replaceAll('/', '-')}-final` } })
  });
  if (!response.ok) return res.status(502).json({ error: `GitHub dispatch failed (${response.status})` });
  return res.status(202).json({ ok: true, project, actionsUrl: 'https://github.com/Shadowlordi16/yt-atm/actions' });
}
