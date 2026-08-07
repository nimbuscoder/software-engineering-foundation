.PHONY: docs build serve deploy

docs:
	python scripts/split_for_mkdocs.py

build: docs
	mkdocs build --strict

serve: docs
	mkdocs serve

deploy: docs
	mkdocs gh-deploy --force
