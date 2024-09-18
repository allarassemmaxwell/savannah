.PHONY: lint pylint all

# Run Flake8 to lint the code, excluding the env and migrations folders, and ignoring main_app/apps.py
lint:
	flake8 . --exclude=env,main_app/migrations,main_app/apps.py --count --select=E9,F63,F7,F82 --show-source --statistics --max-complexity=10 --max-line-length=127

# Run Pylint to analyze the code, excluding the env and migrations folders, and ignoring main_app/apps.py
pylint:
	pylint main_app --ignore=env,migrations,main_app/apps.py --disable=C0111,C0115,C0116,R0903,C0415,W0611 --max-line-length=127 --load-plugins pylint_django

# Run all the checks: Flake8 and Pylint
all: lint pylint
