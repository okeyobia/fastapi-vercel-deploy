# ai-engineer-day1

This project is a FastAPI application configured for deployment with Vercel and managed using `uv` for dependency management.

## Requirements
- Python >= 3.12 (see `.python-version`)
- [uv](https://github.com/astral-sh/uv) (for dependency management)
- [Vercel CLI](https://vercel.com/docs/cli) (for deployment, optional)

## Setup

1. **Ensure Python 3.12 is installed**
	- You can check your version with:
	  ```sh
	  python3.12 --version
	  ```

2. **Create a new virtual environment**
	```sh
	python3.12 -m venv .venv
	source .venv/bin/activate
	```

3. **Install uv (if not already installed)**
	```sh
	pip install uv
	```

4. **Install dependencies with uv**
	```sh
	uv pip install .
	```
	This will install all dependencies specified in `pyproject.toml`.

## Running Locally

```sh
uv pip install .
uvicorn app.main:app --reload
```

## Deployment

This project is configured for deployment on Vercel using the `vercel.json` file. See [Vercel Python documentation](https://vercel.com/docs/frameworks/python) for more details.

## Project Structure

- `app/main.py` — FastAPI application entrypoint
- `pyproject.toml` — Project metadata and dependencies
- `.python-version` — Python version requirement
- `vercel.json` — Vercel deployment configuration
vercel.json
{
    "builds": [
        {
            "src": "app/main.py",
            "use": "@vercel/python"
        }
    ],
    "routes": [
        {
            "src": "/(.*)",
            "dest": "app/main.py"
        }
    ]
}



## Notes
- Make sure your virtual environment uses Python 3.12 or higher to avoid compatibility issues.
- Use `uv` for all dependency management commands for best performance.
