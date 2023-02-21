SHELL=/bin/bash
LINT_PATHS=aml_rl/ tests/ setup.py

lint:
	flake8 ${LINT_PATHS} --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 ${LINT_PATHS} --count  --ignore=E501 --exit-zero --statistics
