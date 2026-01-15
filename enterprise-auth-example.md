# Enterprise GCP Authentication Strategy

## Environment Separation

### Development Environment
```hcl
# terraform/environments/dev/main.tf
provider "google" {
  project = "company-dev-12345"
  impersonate_service_account = "terraform-dev@company-dev-12345.iam.gserviceaccount.com"
}
```

### Staging Environment  
```hcl
# terraform/environments/staging/main.tf
provider "google" {
  project = "company-staging-67890"
  impersonate_service_account = "terraform-staging@company-staging-67890.iam.gserviceaccount.com"
}
```

### Production Environment
```hcl
# terraform/environments/prod/main.tf
provider "google" {
  project = "company-prod-11111"
  # Uses WIF in CI/CD only, no local access
}
```

## Developer Workflow

### 1. Initial Setup (One-time)
```bash
# Install company CLI tool
company-cli auth login

# This sets up:
# - Time-limited access (8 hours)
# - Automatic service account impersonation
# - Environment-specific permissions
```

### 2. Daily Development
```bash
# Refresh credentials (expires every 8 hours)
company-cli auth refresh

# Deploy to dev (automatic impersonation)
terraform plan -var-file="environments/dev/terraform.tfvars"
terraform apply -var-file="environments/dev/terraform.tfvars"
```

### 3. CI/CD Pipeline (GitHub Actions)
```yaml
name: Deploy Infrastructure
on:
  push:
    branches: [main]

jobs:
  deploy-staging:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
      contents: read
    
    steps:
    - uses: actions/checkout@v3
    
    - uses: 'google-github-actions/auth@v1'
      with:
        workload_identity_provider: 'projects/123/locations/global/workloadIdentityPools/staging-pool/providers/github'
        service_account: 'terraform-staging@company-staging-67890.iam.gserviceaccount.com'
    
    - name: Deploy to Staging
      run: |
        terraform init
        terraform plan -var-file="environments/staging/terraform.tfvars"
        terraform apply -auto-approve -var-file="environments/staging/terraform.tfvars"

  deploy-production:
    needs: deploy-staging
    runs-on: ubuntu-latest
    environment: production  # Requires manual approval
    
    steps:
    - uses: 'google-github-actions/auth@v1'
      with:
        workload_identity_provider: 'projects/456/locations/global/workloadIdentityPools/prod-pool/providers/github'
        service_account: 'terraform-prod@company-prod-11111.iam.gserviceaccount.com'
    
    - name: Deploy to Production
      run: |
        terraform init
        terraform plan -var-file="environments/prod/terraform.tfvars"
        # Production requires manual approval in GitHub
        terraform apply -auto-approve -var-file="environments/prod/terraform.tfvars"
```

## Security Controls

### 1. Time-Limited Access
```bash
# Credentials expire every 8 hours
# Developers must re-authenticate daily
company-cli auth status
# Output: "Expires in 3h 45m"
```

### 2. Environment Isolation
```bash
# Developers can only access dev/staging
# Production requires special approval
gcloud projects list --filter="name:company-dev-* OR name:company-staging-*"
```

### 3. Audit Logging
```bash
# All Terraform operations logged
# Automatic alerts for production changes
# Weekly access reviews
```

### 4. Break-Glass Access
```bash
# Emergency production access
company-cli emergency-access request \
  --environment=production \
  --reason="Critical outage - ticket INC-12345" \
  --duration=2h
```

## Terraform Backend Configuration

### Remote State with Encryption
```hcl
terraform {
  backend "gcs" {
    bucket = "company-terraform-state-prod"
    prefix = "infrastructure/prod"
    
    # Encryption at rest
    encryption_key = "projects/company-security/locations/global/keyRings/terraform/cryptoKeys/state"
    
    # Access logging
    access_logs_bucket = "company-audit-logs"
  }
}
```