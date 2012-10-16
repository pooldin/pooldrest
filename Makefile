# Magical make incantations...
.DEFAULT_GOAL := deps
.PHONY: build clean deps dist run run-test shell ipy bpy tests upload

RUN=foreman run
SETUP=$(RUN) python setup.py
MANAGE=$(RUN) python manage.py


build:
	@$(SETUP) build

clean:
	@find . -name "*.py[co]" -exec rm -rf {} \;
	@$(SETUP) clean
	@rm -rf dist build

deps:
	@$(SETUP) dev

dist: clean
	@$(SETUP) sdist

run:
	@foreman start -f dev/Procfile

run-test:
	@foreman start

shell:
	@$(MANAGE) shell

ipy:
	@$(MANAGE) shell -i

bpy:
	@$(MANAGE) shell -b

tests:
	@python manage.py tests

upload: clean
	@$(SETUP) sdist upload -r pooldin
