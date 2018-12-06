GIT_BRANCH := $(shell git rev-parse --abbrev-ref HEAD 2>/dev/null)
GIT_BRANCH_CLEAN := $(shell echo $(GIT_BRANCH) | sed -e "s/[^[:alnum:]]/-/g")
DOCKER_IMAGE := agavepy$(if $(GIT_BRANCH_CLEAN),:$(GIT_BRANCH_CLEAN))

DOCKER_BUILD_ARGS ?= --force-rm
DOCKERFILE ?= dev.Dockerfile

DOCKER_MOUNT := -v "$(CURDIR)":/agavepy
DOCKER_FLAGS := docker run --rm -it $(DOCKER_MOUNT)

DOCKER_RUN_AGAVECLI := $(DOCKER_FLAGS) "$(DOCKER_IMAGE)"


.PHONY: authors build clean deps docs install shell tests


authors:
	git log --format='%aN <%aE>' | sort -u --ignore-case | grep -v 'users.noreply.github.com' > AUTHORS && \
	git add AUTHORS && \
	git commit AUTHORS -m 'Updating AUTHORS' || true

build: # Build development container.
	docker build $(DOCKER_BUILD_ARGS) -f "$(DOCKERFILE)" -t "$(DOCKER_IMAGE)" .

clean:
	rm -rf agavepy.egg-info build dist .cache
	rm -rf schema openapi
	rm -rf agavepy/__pycache__/
	rm -rf agavepy/tenants/*.pyc agavepy/tenants/__pycache__/
	rm -rf agavepy/clients/*.pyc agavepy/clients/__pycache__/
	rm -rf agavepy/tokens/*.pyc agavepy/tokens/__pycache__/
	rm -rf agavepy/files/*.pyc agavepy/files/__pycache__/
	rm -rf agavepy/utils/*.pyc agavepy/utils/__pycache__/
	rm -rf agavepy/tests/__pycache__/
	rm -rf agavepy/*.pyc
	rm -rf tests/__pycache__/
	rm -rf tests/*.pyc
	rm -rf .pytest_cache/

clean-docs:
	make -C docs/ clean


docs:
	pip install sphinx-rtd-theme>=0.4.0
	make -C docs/ html


install:
	python setup.py install

install-py2:
	python2 setup.py install

shell: build # Start a shell inside the build environment.
	$(DOCKER_RUN_AGAVECLI) bash

tests:
	pytest -vv --cache-clear tests/

tests-py2:
	python2 -m pytest -vv tests
