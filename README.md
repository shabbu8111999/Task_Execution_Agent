# Task_Execution_Agent

## These are the steps for venv and the setup for the project

### Step-1: Created a Github Repo and also cloned it in the Project Folder
```bash
git clone https://github.com/shabbu8111999/Task_Execution_Agent.git
```

### Step-2: After Clonning launched my VS Code and Initialized my uv command for the Environment

For VS Code in your Terminal
```bash
code .
```

UV Initialize
```bash
uv init
```

From UV Created the Python Enivornment
```bash
uv venv venv
```

Activate your venv with this command
```bash
venv\Scripts\activate
```

### Step-3: Now after creating env manually created a template.py file and in that mentioned my file names which is mandatory with the help of code and run this via uv
```bash
uv run template.py
```

### Step-4: Then created a setup.py files and also added libraries which are needed in requirements.txt and run this by
```bash
uv pip install -r requirements.txt
```