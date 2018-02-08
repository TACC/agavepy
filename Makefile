
docs:
	python build/swagger_to_rst.py && \
	cd docs && \
	make definitions && \
	make schemas && \
	make html && \
	cd ../

clean:
	rm -rf schemas definitions

.PHONY: docs clean
