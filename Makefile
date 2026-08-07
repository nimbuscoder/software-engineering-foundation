.PHONY: prepare serve build

prepare:
	python scripts/prepare_jekyll.py

serve: prepare
	bundle exec jekyll serve --livereload

build: prepare
	bundle exec jekyll build
