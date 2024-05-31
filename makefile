PLUGIN_NAME = fxcpds_vr_avatar_utils
PLUGIN_VERSION = $(shell grep '"version"' src/$(PLUGIN_NAME)/__init__.py | sed 's/.\+\([0-9]\+\), *\([0-9]\+\), *\([0-9]\+\).\+/\1.\2.\3/g')
FEATURE_VERSION = $(shell grep '"version"' src/$(PLUGIN_NAME)/__init__.py | sed 's/.\+\([0-9]\+\), *\([0-9]\+\), *\([0-9]\+\).\+/\1.\2.0/g')
ZIP_NAME = fxcpds-vr-avatar-utils-v$(PLUGIN_VERSION).zip

.PHONY: build
build:
	@mkdir -p build
	@cd src && zip -r $(ZIP_NAME) $(PLUGIN_NAME) && mv $(ZIP_NAME) ../build

.PHONY: docs
docs:
	@rm -f docs/index.adoc docs/index.html
	@echo '= Addon Documentation Index' > links.adoc \
	  && echo ':stylesdir: common/css' >> links.adoc \
	  && echo ':stylesheet: slate.css' >> links.adoc \
	  && echo '' >> links.adoc
	@for i in `find docs -type f -name '*.adoc'`; do \
	  dir=`dirname "$$i"`; \
	  asciidoctor -o "$$dir/index.html" "$$i"; \
	  if [ `basename "$$i"` = 'index.adoc' ]; then \
	    version=`basename $$dir`; \
        echo "* link:$$version/index.html[$$version]" >> links.adoc; \
	  fi; \
	done;
	@mv links.adoc docs/index.adoc
	@asciidoctor -o docs/index.html docs/index.adoc

.PHONY: apply-version
apply-version:
	@sed -i 's#:feature-version: .\+#:feature-version: $(FEATURE_VERSION)#' readme.adoc
