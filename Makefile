# the things that don't have output files or run every time
.PHONY: help all install test dev coverage clean \
		pre-commit update-pre-commit


# SOURCE_FILES := $(shell find . -type f -name '*.py')


all: dev coverage  ## builds everything

install: .venv/.installed  ## installs the venv and the project packages

dev: .venv/.installed-dev pre-commit  ## prepare local repo and venv for dev

test: .venv/.installed-dev  ## run the project's tests
	build/test.sh

coverage: .venv/.installed-dev build/coverage.sh  ## build the html coverage report
	build/coverage.sh

docs: .docs/index.html ## build the documentation

clean:  ## delete caches and the venv
	build/clean.sh

pre-commit: .git/hooks/pre-commit  ## install pre-commit into the git repo

update-pre-commit: build/update-pre-commit.sh  ## autoupdate pre-commit
	build/update-pre-commit.sh

dist: build/dist.sh ## build the distributable files
	build/dist.sh

release: build/release.sh ## publish to pypi
	build/release.sh

# Caching doesn't work if we depend on PHONY targets

.docs/index.html: .venv/.installed-dev build/docs.sh mkdocs.yml $(shell find . -name '*.md')
	build/docs.sh

.venv/.installed: */pyproject.toml .venv/bin/activate build/install.sh $(shell find uh-halp -name '*.py')
	build/install.sh

.venv/.installed-dev: */pyproject.toml .venv/bin/activate build/install-dev.sh
	build/install-dev.sh

.venv/bin/activate:
	build/venv.sh

.git/hooks/pre-commit: build/install-pre-commit.sh
	build/install-pre-commit.sh


help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
