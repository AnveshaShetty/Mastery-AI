# Team plan (16 days: 21 Nov - 6 Dec 2026)

Daily check-in: ____ (pick a time, 10 min). Swap owners freely, just update this file.

## Split
| Area | Owner | Files |
|---|---|---|
| Tutor brain: prompts, diagnose/explain/check/grade logic, language quality | **Anvesha** | tutor/prompts.py, tutor/engine.py, tests/ |
| Product shell: UI, storage, progress view, deployment | **Pratham** | app/app.py, tutor/storage.py, deploy config |
| Shared | Both | README, docs/AI_TOOLS.md, content/topics.json, demo video |

## Git rules
- `main` always runs. Work on branches: `anvesha/prompts`, `pratham/ui`.
- Small commits, pull before you push, review each other's PRs (AI-written code too).

## Timeline
**Days 1-2 (21-22 Nov): end-to-end path**
- [ ] Both sign in to dashboard; repo created and public
- [ ] Both run the app locally (API key works)
- [ ] Pick v1 subject + fill content/topics.json  (Anvesha)
- [ ] Full loop runs for one topic  (both)

**Days 3-6: make it good**
- [ ] A: tune prompts, check question quality, test Kannada/Hindi output
- [ ] P: better UI, progress/mastery history page
- [ ] Both: claim partner perks you will use (Keploy star, Olostep, n8n)

**Days 7-10: differentiators**
- [ ] A: re-explain strategy, difficulty adaptation, misconception tracking
- [ ] P: deploy a live link; add progress chart
- [ ] Optional: Olostep for grounded sources; n8n for revision reminders

**Days 11-13: real users**
- [ ] Test with 5-10 classmates; record before/after scores
- [ ] Fix top 5 issues

**Days 14-16: ship**
- [ ] README final, AI_TOOLS.md final, screenshots
- [ ] Demo video; pitch deck (optional); LinkedIn/X post tagging Olostep (if used)
- [ ] Submit before the deadline, with buffer time

## Risks
- Wrong explanations: stick to one subject, give the model reference notes in topics.json, review outputs manually
- API cost/limits: cache questions, keep prompts short
- Scope creep: no new features after day 13
