# Makefile for Terraform operations
.PHONY: help init plan apply destroy clean validate format lint

# Default environment
ENV ?= dev

# Colors for output
RED    := \033[31m
GREEN  := \033[32m
YELLOW := \033[33m
BLUE   := \033[34m
RESET  := \033[0m

help: ## Show this help message
	@echo "$(BLUE)Available commands:$(RESET)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-15s$(RESET) %s\n", $$1, $$2}'

init: ## Initialize Terraform
	@echo "$(BLUE)Initializing Terraform...$(RESET)"
	terraform init

validate: ## Validate Terraform configuration
	@echo "$(BLUE)Validating Terraform configuration...$(RESET)"
	terraform validate

format: ## Format Terraform files
	@echo "$(BLUE)Formatting Terraform files...$(RESET)"
	terraform fmt -recursive

lint: ## Lint Terraform files with tflint
	@echo "$(BLUE)Linting Terraform files...$(RESET)"
	@if command -v tflint >/dev/null 2>&1; then \
		tflint --recursive; \
	else \
		echo "$(YELLOW)tflint not installed. Skipping...$(RESET)"; \
	fi

plan: ## Plan Terraform changes for specified environment
	@echo "$(BLUE)Planning Terraform changes for $(ENV) environment...$(RESET)"
	terraform workspace select $(ENV) || terraform workspace new $(ENV)
	terraform plan -var-file="environments/$(ENV)/terraform.tfvars"

apply: ## Apply Terraform changes for specified environment
	@echo "$(BLUE)Applying Terraform changes for $(ENV) environment...$(RESET)"
	terraform workspace select $(ENV) || terraform workspace new $(ENV)
	terraform apply -var-file="environments/$(ENV)/terraform.tfvars"

destroy: ## Destroy Terraform resources for specified environment
	@echo "$(RED)Destroying Terraform resources for $(ENV) environment...$(RESET)"
	@read -p "Are you sure you want to destroy $(ENV) environment? [y/N] " confirm && [ "$$confirm" = "y" ]
	terraform workspace select $(ENV)
	terraform destroy -var-file="environments/$(ENV)/terraform.tfvars"

output: ## Show Terraform outputs for specified environment
	@echo "$(BLUE)Terraform outputs for $(ENV) environment:$(RESET)"
	terraform workspace select $(ENV)
	terraform output

clean: ## Clean Terraform temporary files
	@echo "$(BLUE)Cleaning Terraform temporary files...$(RESET)"
	rm -rf .terraform/
	rm -f .terraform.lock.hcl
	rm -f terraform.tfstate*

# Environment-specific shortcuts
dev-plan: ## Plan for dev environment
	@$(MAKE) plan ENV=dev

dev-apply: ## Apply for dev environment
	@$(MAKE) apply ENV=dev

staging-plan: ## Plan for staging environment
	@$(MAKE) plan ENV=staging

staging-apply: ## Apply for staging environment
	@$(MAKE) apply ENV=staging

prod-plan: ## Plan for prod environment
	@$(MAKE) plan ENV=prod

prod-apply: ## Apply for prod environment
	@$(MAKE) apply ENV=prod