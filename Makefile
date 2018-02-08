
docs: deps
	python build/swagger_to_rst.py && \
	cd docs && \
	make definitions && \
	make schemas && \
	make html && \
	cd ../

deps:
	mkdir -p schemas && \
	mkdir -p definitions

clean:
	rm -rf schemas definitions

tests:
	py.test agavepy/tests/test_agave_basic.py

.PHONY: docs clean deps
