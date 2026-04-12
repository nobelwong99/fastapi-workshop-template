# 102 Workshop — Web API Development using Python

A hands-on workshop by **TM Technology Sdn Bhd** teaching Web API development with Python and FastAPI.

## What you'll build

By the end of the workshop you'll have a working **Task Manager API** with:
- Full CRUD endpoints (Create, Read, Update, Delete)
- Pydantic data models for validation
- Persistent storage via a local JSON file
- Proper HTTP status codes and error handling
- Filtering and search via query parameters

## Getting started (GitHub Codespaces)

1. Click **Code → Codespaces → Create codespace on main**.
2. Wait for the container to build (installs Python 3.12, FastAPI, Jupyter, etc. automatically).
3. Open a terminal and verify:
   ```bash
   python -V      # Python 3.12.x
   pip list       # should list fastapi, uvicorn, jupyter
   ```

## Running the FastAPI server

```bash
uvicorn main:app --reload
```

Open the forwarded port `8000` and append `/docs` to view the interactive Swagger UI.

## Workshop files

| File | Purpose |
|---|---|
| `main.py` | Your FastAPI app — starts with just a root endpoint, you build the rest |
| `tasks.ipynb` | Jupyter notebook for **Task 1a** (functions) and **Task 1b** (dicts/lists) |
| `data.json` | Local "database" for persistent storage (Day 2) |
| `requirements.txt` | Python dependencies |
| `.devcontainer/devcontainer.json` | Codespaces configuration |

## Workshop schedule

- **Day 1** — Python functions, API & web server intro, FastAPI setup, Pydantic, basic CRUD
- **Day 2** — Persistent storage, error handling & status codes, path/query parameters, filtering
- **Day 3** — Build your own API project, presentations

## Working with the notebook

Open `tasks.ipynb` in VS Code. The Jupyter and Google Colab extensions are pre-installed in the devcontainer, so you can run cells directly with `Shift + Enter`. Use this notebook for ad-hoc Python experimentation throughout the workshop.

## Useful links

- FastAPI docs: <https://fastapi.tiangolo.com/>
- Pydantic docs: <https://docs.pydantic.dev/>
- Postman: <https://www.postman.com/>
