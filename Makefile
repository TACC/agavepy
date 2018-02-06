
docs:
	python build/swagger_to_rst.py && \
	cd docs && \
	make schemas && \
	make html && \
	cd ../

.PHONY: docs
