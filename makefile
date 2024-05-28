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
	@cd docs/v$(FEATURE_VERSION) && asciidoctor -o index.html index.adoc
