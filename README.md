# Message Decorators — Starter

## Your task
1. Keep `PlainMessage` unchanged.
2. Introduce a Decorator that is still a `Message` and wraps another `Message`.
3. Implement `UrgentDecorator`.
4. Implement `TimestampDecorator`.
5. Stack both around one message.
6. Add/update one focused test.
7. Explain whether order matters and one complexity cost.

Use a deterministic timestamp approach so tests remain stable.


## Local setup

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

Windows PowerShell:
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

## Course conventions

- Python is only the implementation language for the exercise; the design roles are language-agnostic.
- Use an explicit object-oriented design.
- Keep one main class per source file.

