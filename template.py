import os 
from pathlib import Path

package_name = "db_connect"

LIST_OF_FILES = [
    
    ".github/workflows/.ci.yaml",
    ".github/workflows/.python-publish.yaml",
    "src/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/mongo_crud.py",
    f"src/{package_name}/sql_crud.py",
    "tests/unit/__init__.py",
    "tests/unit/test_mongo_crud.py",
    "tests/unit/test_sql_crud.py",
    "tests/integration/__init__.py",
    "tests/integration/integration.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb",
    
]


for filepath in LIST_OF_FILES:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file