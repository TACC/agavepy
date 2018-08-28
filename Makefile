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
	make -C docs/ clean

deps:
	mkdir -p schema
	mkdir -p openap

docs: deps
	python scripts/swagger_to_rst.py && \
	cd docs && \
	make static-clean && \
	make openapi && \
	make schema && \
	make html && \
	cd ../

install:
	python setup.py install

shell: build # Start a shell inside the build environment.
	$(DOCKER_RUN_AGAVECLI) bash

tests:
	py.test agavepy/tests/test_agave_basic.py -s
