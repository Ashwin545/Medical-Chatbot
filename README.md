Build a Complete Medical Chatbot with LLMs, LangChain, Pinecone, Flask & AWS

## Overview

This repository is a starter scaffold for a medical chatbot project. The current repository structure includes:

- `app.py` - main application entrypoint
- `src/` - helper modules and prompt logic
- `research/` - notebook experiments
- `template.sh` - file scaffolding script
- `requirements.txt` - dependency list
- `.env` - environment variables file

## Setup

### 1. Create the standard repository files

On Windows with Git Bash:

```bash
cd "/c/Users/kumar.KUMAR/Desktop/Medical Chatbot/Medical-Chatbot"
bash template.sh
```

If you are in PowerShell and don’t have Bash available, use these commands instead:

```powershell
New-Item -ItemType Directory -Path src, research -Force
New-Item -ItemType File -Path \
	src\__init__.py, \
	src\helper.py, \
	src\prompt.py, \
	.env, \
	setup.py, \
	app.py, \
	research\trials.ipynb, \
	requirements.txt -Force
```

### 2. Install Python dependencies

After `requirements.txt` is populated, install dependencies with:

```bash
python -m pip install -r requirements.txt
```

### 3. Prepare environment variables

Add any required keys and settings to `.env`. This repository currently uses a `.env` file pattern, but specific variables must be added as the app is developed.

## Run

Run the main app from the repo root:

```bash
python app.py
```

If you later convert the app to Flask, the standard command will be:

```bash
flask run
```

## Project conventions

- `src/` is intended for reusable modules such as helper functions and prompt builders.
- `template.sh` is a scaffold helper, not required once files exist.
- `requirements.txt` should be kept current with all installed Python dependencies.

## Notes

- Currently the repository files are placeholders. Implement `app.py`, `src/helper.py`, and `src/prompt.py` before running the project.
- Use `git status` to track which scaffolded files are already present.

