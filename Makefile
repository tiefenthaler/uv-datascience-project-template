.PHONY: help
help:
	@echo "Available commands:"
	@echo "check-template-sync - Check for inconsistencies between root and template configuration files."

.PHONY: check-template-sync
check-template-sync: # Check for inconsistencies between root and template configuration files
	@echo "🚀 Checking for file inconsistencies..."
	@uv run python scripts/check_template_sync.py

.PHONY: upgrade-dependencies
upgrade-dependencies: # Upgrade python packages to latest version within the pyproject.toml file
	@echo "🔄 Upgrading python dependencies in pyproject.toml..."
	@uv run python scripts/uv_upgrade_dependencies.py
