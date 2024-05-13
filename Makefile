# Build Docker image
build-image:
	docker build -t fastapi-words .

# Run image in new container
run-image:
	docker run -p 8000:8000 fastapi-words

# Force remove all containers(running and stoped) !!! Be careful using this
remove-force-all-containers:
	docker rm -f $(sudo docker ps -aq)

# Make all prepares to start dev
init-dev:
	pip install poetry && \
	poetry install && \
	poetry shell && \
	pre-commit install

# Run pre-commit hooks
pre-commit-run-all:
	poetry shell && \
	pre-commit run --all-files

# Update versions of pre-commit hooks
pre-commit-autoupdate:
	pre-commit autoupdate
