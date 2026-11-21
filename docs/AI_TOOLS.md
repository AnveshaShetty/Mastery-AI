# AI tools, models and libraries

Update this file whenever you add or change a tool. Judges read it.

## Models
| Model | Used for |
|---|---|
| Claude (via Anthropic API, model set by `TUTOR_MODEL`) | Diagnostic questions, explanations, check questions, re-explanations |

## AI assistants used while building
| Tool | How we used it |
|---|---|
| Claude (claude.ai) | Planning, project scaffold, prompt drafting, code review |
| _add yours (Copilot, Cursor, etc.)_ | |

## Libraries
| Library | Purpose |
|---|---|
| anthropic | Claude API client |
| streamlit | Web UI |
| pydantic | Data validation (add when needed) |
| python-dotenv | Load API key from `.env` |
| sqlite3 (stdlib) | Attempt history |
| pytest | Tests |

## Partner tools (add only if actually used)
| Partner | Used? | How |
|---|---|---|
| Olostep | TBD | Web data for grounding explanations |
| n8n | TBD | Revision reminders / progress emails |
| Keploy | TBD | API testing |

## Our rule
AI-written code is reviewed by a human before it is merged. We do not claim anything the app doesn't do.
