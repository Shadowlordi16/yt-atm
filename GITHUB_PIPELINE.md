# Vercel + GitHub render pipeline

Vercel hosts the online HyperFrames preview. GitHub Actions performs the expensive MP4 render. They are separate systems.

The workflow is manual so a push does not render every video. In GitHub, open **Actions → Render video → Run workflow**, then enter a project path such as `blockbuster` or `football-channel/episodes/coutinho`.

The workflow builds, lints, renders at 24 fps, regenerates the audio bed, normalizes audio to YouTube loudness, and uploads `final.mp4` as an artifact for three days. Download the artifact from the completed workflow run, then upload it in YouTube Studio.

Vercel deployments only rebuild the hosted preview when you push source changes. They do not run the MP4 render and do not consume GitHub Actions minutes. GitHub standard runners are free for this public repository.

Do not commit private credentials or unrelated personal files. Finished MP4s and generated audio beds are ignored by Git because they are regenerated or stored as temporary artifacts.
