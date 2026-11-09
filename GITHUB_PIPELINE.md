# GitHub render pipeline

The workflow is manual so a push does not render every video. In GitHub, open **Actions → Render video → Run workflow**, then enter a project path such as `blockbuster` or `football-channel/episodes/coutinho`.

The workflow builds, lints, renders at 24 fps, normalizes audio to YouTube loudness, and uploads `final.mp4` as an artifact for three days. Download the artifact from the completed workflow run, then upload it in YouTube Studio.

This repository is public, so standard GitHub-hosted runners are free. Do not commit private credentials or unrelated personal files. Artifacts are temporary here to avoid filling the account storage quota.
