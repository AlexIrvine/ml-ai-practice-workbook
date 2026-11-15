# Setup (once, about 10 minutes)

1. Install **Python 3.11 or newer** from https://www.python.org/downloads/
   (Windows: tick **Add Python to PATH** in the installer).
2. Install **VS Code** with the *Python* and *Jupyter* extensions, or use JupyterLab
   (installed in step 4).
3. Open a terminal in this folder and create a virtual environment (a private copy of
   Python for this course, so nothing clashes with other projects):

   | | Windows (PowerShell) | macOS / Linux |
   |---|---|---|
   | create | `python -m venv .venv` | `python3 -m venv .venv` |
   | activate | `.venv\Scripts\activate` | `source .venv/bin/activate` |

   If PowerShell refuses to run the activate script, run
   `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, then try again.
4. Install the libraries: `pip install -r requirements.txt`
5. Build the practice database for the SQL drills: `python data/seed_bank_db.py`
6. Open any notebook. In VS Code, click **Select Kernel** (top right) and choose the
   `.venv` Python. In JupyterLab, run `jupyter lab` from this folder (with the
   environment activated) and open the notebook there.

Each new terminal session: activate the environment again (step 3, second row) before
running `jupyter lab` or a script.
