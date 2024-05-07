.PHONY: init-dev
# Init environment for development
init-dev:
	@make poetry-install && \
	make pre-commit-install

.PHONY: run-app-reload
run-app:
	@uvicorn main:app --reload


# [pre-commit]-[BEGIN]
.PHONY: pre-commit-install
# Install pre-commit.
pre-commit-install:
	@pre-commit install

.PHONY: pre-commit-run-all
# Run tools for all files.
pre-commit-run-all:
	@pre-commit run --all-files

.PHONY: pre-commit-autoupdate
# Update "rev" version of all pre-commit hooks.
pre-commit-autoupdate:
	@pre-commit autoupdate
# [pre-commit]-[END]


# [poetry]-[BEGIN]
.PHONY: poetry-install
# Install the current dependencies.
poetry-install:
	@poetry install --no-root --sync

.PHONY: poetry-export-requirements
# Export the current dependencies to requirements.txt.
poetry-export-requirements:
	@poetry export --format requirements.txt --output requirements.txt --without-hashes

.PHONY: activate-shell
# Activate poetry shell:
activate-shell:
	@poetry shell

# [poetry]-[END]


# [extra_python]-[BEGIN]
.PHONY: install-pipx
# Install pipx.
# Note: Reloading shell is needed after this action.
install-pipx:
	@python3.12 -m ensurepip &&\
	python3.12 -m pip install --upgrade pip &&\
	python3.12 -m pip install --user pipx &&\
	python3.12 -m pipx ensurepath

.PHONY: install-poetry
# Install poetry.
# Note: Reloading shell is needed after this action.
install-poetry:
	@pipx install poetry &&\
	pipx upgrade poetry &&\
	poetry self add poetry-plugin-export ;\
	poetry self add poetry-plugin-up

.PHONY: install-pre-commit
# Install pre-commit.
install-pre-commit:
	@pipx install pre-commit &&\
	pipx upgrade pre-commit
# [extra_python]-[END]
