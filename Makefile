
docs: deps
	python build/swagger_to_rst.py && \
	cd docs && \
	make openapi && \
	make schema && \
	make html && \
	cd ../

deps:
	mkdir -p schema && \
	mkdir -p openapi

clean:
	rm -rf schema openapi && \
	cd docs && \
	make clean

tests:
	py.test agavepy/tests/test_agave_basic.py

.PHONY: docs clean deps
