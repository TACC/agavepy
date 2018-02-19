
authors:
	git log --format='%aN <%aE>' | sort -u --ignore-case | grep -v 'users.noreply.github.com' > AUTHORS && \
	git add AUTHORS && \
	git commit AUTHORS -m 'Updating AUTHORS' || true

docs: deps
	python scripts/swagger_to_rst.py && \
	cd docs && \
	make static-clean && \
	make openapi && \
	make schema && \
	make html && \
	cd ../

deps:
	mkdir -p schema && \
	mkdir -p openapi

clean:
	rm -rf agavepy.egg-info build dist .cache && \
	rm -rf schema openapi && \
	cd docs && \
	make clean

tests:
	py.test agavepy/tests/test_agave_basic.py

.PHONY: docs clean deps authors
