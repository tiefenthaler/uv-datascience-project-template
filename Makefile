.PHONY: help
help:
	@echo "Available commands:"
	@echo "  check-template-sync - Check for inconsistencies between root and template configuration files."

.PHONY: check-template-sync
check-template-sync:
	@echo "🚀 Checking for file inconsistencies..."
	@uv run python scripts/check_template_sync.py
