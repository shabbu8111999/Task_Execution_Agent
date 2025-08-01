import os
import logging
from pathlib import Path

logging.basicConfig(level = logging.INFO, format = ('[%(asctime)s]: %(message)s:'))


project_name = "taskExecutor"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/routes.py",
    f"{project_name}/agent_controller.py",
    f"{project_name}/utils.py",
    f"{project_name}/config.py",
    "agent/__init__.py",
    "agent/base_tools.py",
    "agent/execution_agent.py",
    "agent/memory_store.py",
    "data/user_uploads/",
    "logs/execution.log",
    "templates/index.html",
    "static/style.css",
    "requirements.txt",
    "app.py",
    "setup.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created Directory {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (not os.path.getsize(filepath) == 0):
        with open (filepath, "w") as f:
            pass
        logging.info(f"Created empty file {filepath}")
    else:
        logging.info(f"{filepath} already exists")
