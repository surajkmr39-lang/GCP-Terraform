# Enterprise Terraform Makefile - Real-World Multi-Environment Operations
.PHONY: help init plan apply destroy output clean validate format

# Default environment
ENV ?= development

help:
	@echo "Enterprise Terraform Operations"
	@echo "==============================="
	@echo ""
	@echo "Available environments: development, staging, production"
	@echo ""
	@echo "Environment Operations:"
	@echo "  make init ENV=development        # Initialize environment"
	@echo "  make plan ENV=development        # Plan changes"
	@echo "  make apply ENV=development       # Apply changes"
	@echo "  make output ENV=development      # Show outputs"
	@echo "  make destroy ENV=development     # Destroy infrastructure"
	@echo ""
	@echo "Quick Environment Shortcuts:"
	@echo "  make dev-init           # Initialize development environment"
	@echo "  make dev-plan           # Plan development changes"
	@echo "  make dev-apply          # Apply development changes"
	@echo "  make staging-plan       # Plan staging changes"
	@echo "  make prod-plan          # Plan production changes"
	@echo ""
	@echo "Utilities:"
	@echo "  make validate-all       # Validate all environments"
	@echo "  make format             # Format all Terraform files"
	@echo "  make demo-comparison    # Run state comparison demo"

# Generic environment operations
init:
	@echo "Initializing $(ENV) environment..."
	cd environments/$(ENV) && terraform init

plan:
	@echo "Planning $(ENV) environment..."
	cd environments/$(ENV) && terraform plan

apply:
	@echo "Applying $(ENV) environment..."
	cd environments/$(ENV) && terraform apply

output:
	@echo "Outputs for $(ENV) environment:"
	cd environments/$(ENV) && terraform output

destroy:
	@echo "Destroying $(ENV) environment..."
	cd environments/$(ENV) && terraform destroy

# Development environment shortcuts
dev-init:
	@$(MAKE) init ENV=development

dev-plan:
	@$(MAKE) plan ENV=development

dev-apply:
	@$(MAKE) apply ENV=development

dev-output:
	@$(MAKE) output ENV=development

# Staging environment shortcuts
staging-init:
	@$(MAKE) init ENV=staging

staging-plan:
	@$(MAKE) plan ENV=staging

staging-apply:
	@$(MAKE) apply ENV=staging

staging-output:
	@$(MAKE) output ENV=staging

# Production environment shortcuts
prod-init:
	@$(MAKE) init ENV=production

prod-plan:
	@$(MAKE) plan ENV=production

prod-apply:
	@$(MAKE) apply ENV=production

prod-output:
	@$(MAKE) output ENV=production

# Utility targets
validate-all:
	@echo "Validating all environments..."
	@for env in development staging production; do \
		echo "Validating $$env..."; \
		cd environments/$$env && terraform validate; \
	done

format:
	@echo "Formatting Terraform files..."
	terraform fmt -recursive .

clean:
	@echo "Cleaning temporary files..."
	find . -name ".terraform" -type d -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.tfplan" -delete 2>/dev/null || true

# State management
state-list:
	@echo "State for $(ENV) environment:"
	cd environments/$(ENV) && terraform state list

# Backend and demo operations
setup-backend:
	@echo "Setting up remote backend..."
	./Setup-RemoteBackend.ps1

demo-comparison:
	@echo "Running state management comparison demo..."
	./Demo-StateComparison.ps1

demo-all:
	@echo "Enterprise Multi-Environment Demo"
	@echo "================================="
	@echo "Development Environment:"
	@$(MAKE) state-list ENV=dev || echo "Not initialized"
	@echo ""
	@echo "Staging Environment:"
	@$(MAKE) state-list ENV=staging || echo "Not initialized"
	@echo ""
	@echo "Production Environment:"
	@$(MAKE) state-list ENV=prod || echo "Not initialized"