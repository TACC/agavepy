# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = python -msphinx
SPHINXPROJ    = AgavePy
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile static-clean

static-clean: openapi-clean schema-clean
	true

openapi: openapi-clean
	mkdir -p _static/openapi/ && \
	cp -R ../openapi/* _static/openapi/

openapi-clean:
	rm -rf _static/openapi/*

schema: schema-clean
	mkdir -p _static/schema/ && \
	cp -R ../schema/* _static/schema/

schema-clean:
	rm -rf _static/schema/*

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)