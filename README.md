# taxi-squad-tracker

# Quick Start
1. Install poetry `sudo apt get poetry`
2. Run `poetry install`
3. Run `python3 generate_config.py`
4. Update config.yml with appropriate data for your league
5. Run `poetry run track`

# Dev Setup
- Run `poetry run pre-commit install`
- If using VS Code, change Python Interpreter to the interpreter inside of project .venv folder

# Common Issues
If using VS Code for development. Git Commit will not work properly unless 
`"terminal.integrated.inheritEnv": true}`
is added to ~/.vscode-server/data/Machine/settings.json