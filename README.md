# testGithubCI
Testing github CI/CD. Learning strategy based off Claude. Will be deleted after testing done.

---

# GitHub CI/CD Crash Course — 3-Day Lesson Plan

> **Before you start:** Have a GitHub account and a simple project repo ready (a basic Python or Node script with at least one test file is enough). All videos are free on YouTube. Budget 5–7 hours per day including hands-on time. (this project)

---

## Day 1 — Foundations: workflows, triggers & first CI pipeline

### Morning · Core concepts (watch first, no skipping)

DONE: *~1.5 hrs · Build the mental model before touching YAML*

DONE: **Video 1: GitHub Actions Tutorial – Basic Concepts & CI/CD Pipeline (TechWorld with Nana)**
- [x] Duration: ~32 min
- [x] Link: https://www.youtube.com/watch?v=R8_veQiYBjI
- [x] Covers workflows, jobs, steps, runners, triggers. Best conceptual intro available.

**Video 2: GitHub Actions CI/CD — Everything you need to know to get started (Fireship)**
- [x]  Duration: ~12 min
- [x] Link: https://www.youtube.com/watch?v=mFFXuXjVgkU
- [x] Dense, fast overview. Watch after Nana to solidify the event model.

**Exercises:**
- [x] Sketch the workflow anatomy on paper: `event → workflow → job → step → action`
- [x] Identify 3 triggers you'd use in a real project
- [x] Write real project.

---

### Afternoon · First hands-on pipeline

*~2.5 hrs · Follow along in your own repo*

**Video: CI/CD Tutorial – Automated Testing & Automated Deployments (Tom Shaw)**
- Duration: ~45 min
- Link: https://www.youtube.com/watch?v=YLtlz88zrLg
- Has a companion starter repo. Covers push trigger, test job, and deploy job end-to-end.
- Companion repo: https://github.com/IAmTomShaw/github-actions-demo-project

**Exercises:**
- Fork the companion repo and run the workflow yourself
- Break a test intentionally — watch the pipeline fail, then fix it
- Add a second job that echoes "deploy complete" and depends on the test job using `needs:`

---

### Evening · Secrets, env vars & the marketplace

*~1 hr · Critical concepts before Day 2*

**Video: GitHub Actions – From BEGINNER to PRO (DevOps Journey) — Secrets & Env vars section**
- Duration: ~25 min (jump to secrets chapter)
- Link: https://www.youtube.com/watch?v=Xwpi0ITkL3U
- Covers the Actions marketplace, repository secrets, and the env context.

**Exercises:**
- Add a repository secret and reference it in a workflow step
- Browse the Actions Marketplace — find and use one community action you didn't already know

**Topics covered today:**
`on: push/pull_request` · `jobs & steps` · `runs-on` · `uses: actions/checkout` · `needs:` · `secrets context` · `env context`

---

## Day 2 — Intermediate: matrices, caching, Docker & real pipelines

### Morning · Matrix strategy & build optimisation

*~2 hrs · Parallel jobs, caching deps, artifact passing*

**Video: Mastering GitHub Actions CI/CD – Complete Guide (Dec 2025)**
- Duration: ~2.5 hrs (watch at 1.25×)
- Link: https://www.youtube.com/watch?v=G3z0s7OdzFQ
- Beginner-friendly, covers matrix builds, caching, and artifacts.

**Exercises:**
- Write a matrix job that runs tests across 3 Node or Python versions simultaneously
- Add `actions/cache` to your pipeline and verify a cache hit on the second run
- Upload a build artifact and download it in a downstream job

---

### Afternoon · Docker build & push pipeline

*~2 hrs · Core real-world pattern — build image, push to registry*

**Video: GitHub Actions Tutorial – Basic Concepts & CI/CD Pipeline with Docker (TechWorld with Nana)**
- Duration: ~1 hr
- Link: https://www.youtube.com/watch?v=R8_veQiYBjI
- Covers Docker build + push to DockerHub. Companion to the Day 1 Nana video.

**Exercises:**
- Build a Docker image in Actions and push to DockerHub or GHCR (GitHub Container Registry)
- Tag the image with the git SHA using `${{ github.sha }}`
- Add a branch filter so the push only happens on `main`

---

### Evening · Conditionals, expressions & workflow control

*~1 hr · `if:`, skipping steps, `always()`, `failure()`*

**Video: GitHub Actions: The Full Course – Conditionals & expressions section (playlist)**
- Duration: ~40 min (jump to the conditionals section)
- Link: https://www.youtube.com/playlist?list=PLArH6NjfKsUhvGHrpag7SuPumMzQRhUKY
- Covers `if:`, contexts, and status check functions.

**Exercises:**
- Add a Slack or Discord notification step that only runs on failure using `if: failure()`
- Skip a step based on a custom input or branch name using an expression

**Topics covered today:**
`strategy.matrix` · `actions/cache` · `upload-artifact` · `docker/build-push-action` · `if: failure()` · `github context` · branch filters

---

## Day 3 — Advanced: reusable workflows, OIDC & production patterns

### Morning · Reusable workflows & composite actions

*~2.5 hrs · DRY pipelines, calling workflows across repos*

**Video: GitHub Actions Certification – Full Course (freeCodeCamp / Andrew Brown)**
- Duration: ~4 hrs total (jump to the reusable workflows and composite actions chapters — ~60–90 min combined)
- Link: https://www.youtube.com/watch?v=Tz7FsunBbfQ

**Exercises:**
- Extract your test job into a reusable workflow triggered by `workflow_call`
- Pass an input (e.g. Node version) and a secret into the reusable workflow
- Build a composite action (`action.yml`) that wraps 3 steps into one reusable unit

---

### Afternoon · OIDC — keyless cloud authentication

*~1.5 hrs · Replace static secrets with short-lived tokens*

**Resource 1: GitHub Actions OIDC with AWS – No More Access Keys (Living DevOps)**
- Format: Written guide + hands-on walkthrough
- Link: https://livingdevops.com/aws/step-by-step-guide-to-setting-oidc-for-github-actions-workflows-with-aws-using-terraform/
- Covers IAM OIDC provider setup and role assumption in a workflow.

**Resource 2: GitHub Actions: The Full Course – OIDC chapter (playlist)**
- Duration: ~25 min
- Link: https://www.youtube.com/playlist?list=PLArH6NjfKsUhvGHrpag7SuPumMzQRhUKY
- Shows `id-token: write`, OIDC token structure, and configuring the AWS trust policy.

**Exercises:**
- Configure an IAM OIDC Identity Provider for GitHub in AWS (or Azure if preferred)
- Write a workflow using `aws-actions/configure-aws-credentials` with `role-to-assume` — no static keys
- Lock the IAM trust policy to a specific branch (`ref:refs/heads/main`) in the `sub` claim

---

### Evening · Production hardening & capstone

*~1.5 hrs · Pin actions, concurrency, environments, review gates*

**Video: Complete GitHub Actions Course – Environments & deployment protection rules section**
- Duration: ~30 min (jump to environments chapter)
- Link: https://www.youtube.com/watch?v=Xwpi0ITkL3U
- Covers required reviewers, environment secrets, and deployment gates.

**Exercises:**
- Pin all third-party actions to a commit SHA (not a tag) to prevent supply-chain attacks
- Set up a `production` environment with a required reviewer approval gate
- Add a `concurrency:` block to cancel in-progress runs on new pushes

**Capstone — build this pipeline from scratch:**

```
lint → test (matrix, 3 versions) → docker build → OIDC deploy to staging → manual approval gate → production deploy
```

**Topics covered today:**
`workflow_call` · `composite actions` · `id-token: write` · OIDC trust policy · `environments` · `concurrency:` · SHA pinning

---

## Reference: key concepts by day

| Day | Focus | Must-know syntax |
|-----|-------|-----------------|
| 1 | Workflow anatomy, triggers, secrets | `on:`, `jobs:`, `steps:`, `needs:`, `secrets.X` |
| 2 | Parallelism, Docker, conditionals | `strategy.matrix`, `if: failure()`, `github.sha` |
| 3 | Reuse, keyless auth, production gates | `workflow_call`, `id-token: write`, `concurrency:` |

## Tips

- **Follow along in real time.** Pause and do each exercise before moving to the next section — don't batch the hands-on work to the end.
- **Break things on purpose.** Intentionally failing a pipeline and reading the error output is one of the fastest ways to learn.
- **The capstone is the goal.** If you can build the full Day 3 pipeline from scratch without referencing notes, you've genuinely got the skills.
- **OIDC is worth the afternoon.** Ditching static AWS keys for short-lived tokens is a meaningful security improvement and increasingly expected in professional environments.

