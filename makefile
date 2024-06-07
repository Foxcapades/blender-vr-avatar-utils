PLUGIN_NAME = fxcpds_vr_avatar_utils
PLUGIN_VERSION = $(shell grep '"version"' src/$(PLUGIN_NAME)/__init__.py | sed 's/.\+\([0-9]\+\), *\([0-9]\+\), *\([0-9]\+\).\+/\1.\2.\3/g')
FEATURE_VERSION = $(shell grep '"version"' src/$(PLUGIN_NAME)/__init__.py | sed 's/.\+\([0-9]\+\), *\([0-9]\+\), *\([0-9]\+\).\+/\1.\2.0/g')
ZIP_NAME = fxcpds-vr-avatar-utils-v$(PLUGIN_VERSION).zip

ROOT_DIR = "$(PWD)"
BUILD_DIR = "$(ROOT_DIR)/build"
STAGING_DIR = "$(BUILD_DIR)/staging"
ARCHIVE_DIR = "$(BUILD_DIR)/release"

.ONESHELL:
.SHELLFLAGS += -e

.PHONY: build
build: clean build-docker
	@mkdir -p $(STAGING_DIR) $(ARCHIVE_DIR)
	@cd src
	@cp --parents -t "$(STAGING_DIR)" $$(find fxcpds_vr_avatar_utils -type f -name '*.py')
	@cd ..
	@docker run --rm -v "$(BUILD_DIR):/tmp/workspace" fxcpds-py3-11:latest pyminify --in-place staging/
	@cp -rt "$(STAGING_DIR)"/fxcpds_vr_avatar_utils assets
	@cd "$(STAGING_DIR)"
	@zip -r "$(ZIP_NAME)" fxcpds_vr_avatar_utils
	@mv "$(ZIP_NAME)" $(ARCHIVE_DIR)

.PHONY: clean
clean:
	@rm -rf "$(BUILD_DIR)"

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

.PHONY: build-docker
build-docker:
	@docker inspect -f='1' fxcpds-py3-11:latest >/dev/null 2>&1 || docker build -f dockerfile -t fxcpds-py3-11:latest .
