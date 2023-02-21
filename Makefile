SHELL=/bin/bash
LINT_PATHS=setup.py aml_rl/ #test/

check-codestyle:
	# Sort imports
	isort --check ${LINT_PATHS}
	# Reformat using black
	black --check -l 127 ${LINT_PATHS}

lint:
	flake8 ${LINT_PATHS} --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 ${LINT_PATHS} --count  --ignore=E501 --exit-zero --statistics
