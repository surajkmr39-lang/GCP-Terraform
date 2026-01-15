# 🔍 Workload Identity Federation - Validation & Education Guide

**Author**: Suraj Kumar  
**Purpose**: Validate WIF setup and educate team members  
**Project**: GCP Terraform Infrastructure

## 🎯 Quick Validation Checklist

Use this checklist to quickly verify if WIF is working in your project:

- [ ] WIF Pool exists
- [ ] WIF Provider is configured
- [ ] Service Account has proper IAM bindings
- [ ] Attribute mapping is correct
- [ ] Attribute conditions are set
- [ ] GitHub repository variable is configured
- [ ] Can generate test tokens

## 📋 Step 1: Check Current WIF Status

Run these commands to see your current WIF setup:

```bash
# 1. List all Workload Identity Pools
gcloud iam workload-identity-pools list --location=global --project=praxis-gear-483220-k4

# 2. Check if dev-pool exists
gcloud iam workload-identity-pools describe dev-pool \
    --location=global \
    --project=praxis-gear-483220-k4

# 3. List providers in the pool
gcloud iam workload-identity-pools providers list \
    --workload-identity-pool=dev-pool \
    --location=global \
    --project=praxis-gear-483220-k4
```

**Expected Output**:
```
NAME: dev-pool
STATE: ACTIVE
DISPLAY_NAME: dev Workload Identity Pool
```

## 🔍 Step 2: Examine Your Terraform WIF Configuration

Let's look at what your Terraform code is doing:

```bash
# View the IAM module that creates WIF
Get-Content modules/iam/main.tf
```

**Key Components to Identify**:

### **Component 1: Workload Identity Pool**
```hcl
resource "google_iam_workload_identity_pool" "pool" {
  workload_identity_pool_id = "${var.environment}-pool"  # Creates "dev-pool"
  display_name              = "${var.environment} Workload Identity Pool"
  description               = "Workload Identity Pool for ${var.environment} environment"
  project                   = var.project_id
}
```

**What this does**: Creates a container for external identities

### **Component 2: GitHub Provider** (Conditional)
```hcl
resource "google_iam_workload_identity_pool_provider" "github_provider" {
  count = var.github_repository != "" ? 1 : 0  # Only creates if github_repository is set
  
  workload_identity_pool_id          = google_iam_workload_identity_pool.pool.workload_identity_pool_id
  workload_identity_pool_provider_id = "github-provider"
  
  # Maps GitHub token claims to GCP attributes
  attribute_mapping = {
    "google.subject"       = "assertion.sub"
    "attribute.actor"      = "assertion.actor"
    "attribute.repository" = "assertion.repository"
    "attribute.ref"        = "assertion.ref"
  }

  # Security: Only allow specific repository
  attribute_condition = "assertion.repository == '${var.github_repository}'"

  # GitHub OIDC configuration
  oidc {
    issuer_uri = "https://token.actions.githubusercontent.com"
  }
}
```

**What this does**: Configures GitHub as a trusted identity provider

### **Component 3: IAM Binding**
```hcl
resource "google_service_account_iam_binding" "workload_identity_binding" {
  count = var.github_repository != "" ? 1 : 0
  
  service_account_id = google_service_account.vm_service_account.name
  role               = "roles/iam.workloadIdentityUser"

  members = [
    "principalSet://iam.googleapis.com/${google_iam_workload_identity_pool.pool.name}/attribute.repository/${var.github_repository}"
  ]
}
```

**What this does**: Grants GitHub Actions permission to impersonate the service account

## 🧪 Step 3: Check if WIF is Active or Dormant

```bash
# Check your current github_repository setting
Get-Content environments/dev/terraform.tfvars | Select-String "github_repository"
```

**Scenario A: WIF is DORMANT** (Most likely your current state)
```hcl
github_repository = ""  # Empty string
```
**Status**: 
- ✅ WIF Pool exists
- ❌ GitHub Provider NOT created (count = 0)
- ❌ IAM Binding NOT created (count = 0)

**Scenario B: WIF is ACTIVE**
```hcl
github_repository = "surajkmr39-lang/GCP-Terraform"  # Set to your repo
```
**Status**:
- ✅ WIF Pool exists
- ✅ GitHub Provider created
- ✅ IAM Binding created

## 🚀 Step 4: Activate WIF (Demonstration)

Let's activate WIF to demonstrate how it works:

```bash
# 1. Backup current configuration
Copy-Item "environments/dev/terraform.tfvars" "environments/dev/terraform.tfvars.backup"

# 2. Check if you have a GitHub repository
# If not, create one at: https://github.com/new
# Name it: GCP-Terraform (or any name you prefer)

# 3. Update terraform.tfvars
# Edit environments/dev/terraform.tfvars and change:
# github_repository = "your-github-username/your-repo-name"
```

**Example**:
```hcl
# Before (Dormant)
github_repository = ""

# After (Active)
github_repository = "surajkmr39-lang/GCP-Terraform"
```

```bash
# 4. Apply the changes
terraform plan -var-file="environments/dev/terraform.tfvars"
terraform apply -var-file="environments/dev/terraform.tfvars"

# 5. Verify GitHub provider was created
gcloud iam workload-identity-pools providers list \
    --workload-identity-pool=dev-pool \
    --location=global \
    --project=praxis-gear-483220-k4
```

## 🔍 Step 5: Detailed WIF Inspection

Once WIF is active, inspect all components:

```bash
# 1. Get complete WIF provider details
gcloud iam workload-identity-pools providers describe github-provider \
    --workload-identity-pool=dev-pool \
    --location=global \
    --project=praxis-gear-483220-k4 \
    --format=yaml

# 2. Check attribute mapping
gcloud iam workload-identity-pools providers describe github-provider \
    --workload-identity-pool=dev-pool \
    --location=global \
    --project=praxis-gear-483220-k4 \
    --format="yaml(attributeMapping)"

# 3. Check attribute condition (security filter)
gcloud iam workload-identity-pools providers describe github-provider \
    --workload-identity-pool=dev-pool \
    --location=global \
    --project=praxis-gear-483220-k4 \
    --format="yaml(attributeCondition)"

# 4. Check service account IAM policy
gcloud iam service-accounts get-iam-policy \
    dev-vm-sa@praxis-gear-483220-k4.iam.gserviceaccount.com \
    --format=yaml
```

## 📊 Step 6: Visual Explanation for Education

Create this visual diagram to explain WIF to others:

```
┌─────────────────────────────────────────────────────────────────┐
│                    WORKLOAD IDENTITY FEDERATION                  │
│                         (How It Works)                           │
└─────────────────────────────────────────────────────────────────┘

Step 1: GitHub Actions Workflow Runs
┌──────────────────┐
│  GitHub Actions  │
│   Workflow Run   │
└────────┬─────────┘
         │
         │ 1. GitHub generates OIDC token
         │    Token contains:
         │    - repository: "surajkmr39-lang/GCP-Terraform"
         │    - ref: "refs/heads/main"
         │    - actor: "surajkmr39-lang"
         │
         ▼
┌──────────────────────────────────────────┐
│   GitHub OIDC Token (JWT)                │
│   {                                      │
│     "iss": "https://token.actions...",  │
│     "sub": "repo:owner/repo:ref:...",   │
│     "repository": "owner/repo",         │
│     "ref": "refs/heads/main",           │
│     "actor": "username"                 │
│   }                                      │
└────────┬─────────────────────────────────┘
         │
         │ 2. Send token to GCP WIF endpoint
         │
         ▼
┌──────────────────────────────────────────┐
│   GCP Workload Identity Pool             │
│   (dev-pool)                             │
│                                          │
│   ┌────────────────────────────┐        │
│   │  GitHub Provider           │        │
│   │  - Validates token         │        │
│   │  - Checks issuer           │        │
│   │  - Maps attributes         │        │
│   └────────────────────────────┘        │
└────────┬─────────────────────────────────┘
         │
         │ 3. Attribute Mapping
         │    google.subject = assertion.sub
         │    attribute.repository = assertion.repository
         │
         │ 4. Attribute Condition Check
         │    assertion.repository == "surajkmr39-lang/GCP-Terraform" ✓
         │
         ▼
┌──────────────────────────────────────────┐
│   IAM Binding Check                      │
│                                          │
│   Does principalSet have permission to   │
│   impersonate dev-vm-sa?                 │
│                                          │
│   Role: roles/iam.workloadIdentityUser   │
└────────┬─────────────────────────────────┘
         │
         │ 5. If all checks pass...
         │
         ▼
┌──────────────────────────────────────────┐
│   GCP Issues Access Token                │
│   - For: dev-vm-sa@...                   │
│   - Duration: 1 hour                     │
│   - Scope: cloud-platform                │
└────────┬─────────────────────────────────┘
         │
         │ 6. GitHub Actions uses token
         │
         ▼
┌──────────────────────────────────────────┐
│   Access GCP Resources                   │
│   - Deploy infrastructure                │
│   - Manage compute instances             │
│   - Access storage                       │
└──────────────────────────────────────────┘

🔐 Security Benefits:
✅ No service account keys stored anywhere
✅ Tokens expire after 1 hour
✅ Full audit trail (who, what, when)
✅ Attribute-based access control
✅ Easy to revoke access
```

## 🎓 Step 7: Create Educational Demo Script

Create this PowerShell script to demonstrate WIF:

```powershell
# Save as: WIF-Demo-Script.ps1

Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║   Workload Identity Federation - Live Demonstration       ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan

Write-Host "`n📋 PART 1: Current WIF Status" -ForegroundColor Yellow
Write-Host "─────────────────────────────────────────────────────────────"

# Check WIF Pool
Write-Host "`n1️⃣  Checking Workload Identity Pool..." -ForegroundColor Green
$pool = gcloud iam workload-identity-pools describe dev-pool --location=global --project=praxis-gear-483220-k4 --format="value(name,state)" 2>$null

if ($pool) {
    Write-Host "   ✅ WIF Pool exists: dev-pool" -ForegroundColor Green
    Write-Host "   State: ACTIVE" -ForegroundColor Green
} else {
    Write-Host "   ❌ WIF Pool not found" -ForegroundColor Red
}

# Check GitHub Provider
Write-Host "`n2️⃣  Checking GitHub Provider..." -ForegroundColor Green
$provider = gcloud iam workload-identity-pools providers list --workload-identity-pool=dev-pool --location=global --project=praxis-gear-483220-k4 --format="value(name)" 2>$null

if ($provider) {
    Write-Host "   ✅ GitHub Provider exists: github-provider" -ForegroundColor Green
    
    # Get provider details
    Write-Host "`n   📝 Provider Configuration:" -ForegroundColor Cyan
    $issuer = gcloud iam workload-identity-pools providers describe github-provider --workload-identity-pool=dev-pool --location=global --project=praxis-gear-483220-k4 --format="value(oidc.issuerUri)"
    Write-Host "   Issuer: $issuer" -ForegroundColor White
    
    $condition = gcloud iam workload-identity-pools providers describe github-provider --workload-identity-pool=dev-pool --location=global --project=praxis-gear-483220-k4 --format="value(attributeCondition)"
    Write-Host "   Condition: $condition" -ForegroundColor White
} else {
    Write-Host "   ⚠️  GitHub Provider not configured" -ForegroundColor Yellow
    Write-Host "   Reason: github_repository variable is empty" -ForegroundColor Yellow
}

# Check Service Account IAM
Write-Host "`n3️⃣  Checking Service Account IAM Bindings..." -ForegroundColor Green
$iamPolicy = gcloud iam service-accounts get-iam-policy dev-vm-sa@praxis-gear-483220-k4.iam.gserviceaccount.com --format=json | ConvertFrom-Json

$wifBinding = $iamPolicy.bindings | Where-Object { $_.role -eq "roles/iam.workloadIdentityUser" }

if ($wifBinding) {
    Write-Host "   ✅ Workload Identity binding exists" -ForegroundColor Green
    Write-Host "   Members:" -ForegroundColor Cyan
    $wifBinding.members | ForEach-Object {
        Write-Host "   - $_" -ForegroundColor White
    }
} else {
    Write-Host "   ⚠️  No Workload Identity binding found" -ForegroundColor Yellow
}

# Check Terraform Configuration
Write-Host "`n📋 PART 2: Terraform Configuration" -ForegroundColor Yellow
Write-Host "─────────────────────────────────────────────────────────────"

Write-Host "`n4️⃣  Checking Terraform Variables..." -ForegroundColor Green
$tfvarsContent = Get-Content "environments/dev/terraform.tfvars" | Select-String "github_repository"

if ($tfvarsContent) {
    Write-Host "   Configuration: $tfvarsContent" -ForegroundColor White
    
    if ($tfvarsContent -match 'github_repository\s*=\s*""') {
        Write-Host "   ⚠️  Status: WIF is DORMANT (github_repository is empty)" -ForegroundColor Yellow
        Write-Host "   💡 To activate: Set github_repository = 'your-username/your-repo'" -ForegroundColor Cyan
    } else {
        Write-Host "   ✅ Status: WIF is ACTIVE" -ForegroundColor Green
    }
}

# Summary
Write-Host "`n📊 SUMMARY" -ForegroundColor Yellow
Write-Host "─────────────────────────────────────────────────────────────"

if ($pool -and $provider -and $wifBinding) {
    Write-Host "✅ WIF is FULLY CONFIGURED and ACTIVE" -ForegroundColor Green
    Write-Host "   Ready for GitHub Actions integration" -ForegroundColor Green
} elseif ($pool -and !$provider) {
    Write-Host "⚠️  WIF is PARTIALLY CONFIGURED (Dormant)" -ForegroundColor Yellow
    Write-Host "   Pool exists but provider not created" -ForegroundColor Yellow
    Write-Host "   Action: Set github_repository in terraform.tfvars" -ForegroundColor Cyan
} else {
    Write-Host "❌ WIF is NOT CONFIGURED" -ForegroundColor Red
    Write-Host "   Action: Deploy Terraform infrastructure" -ForegroundColor Cyan
}

Write-Host "`n╔════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║              Demo Complete                                 ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
```

Run the demo:
```bash
PowerShell -ExecutionPolicy Bypass -File WIF-Demo-Script.ps1
```

## 🧪 Step 8: Test WIF with GitHub Actions (Optional)

If you want to fully test WIF, create a simple GitHub Actions workflow:

```yaml
# Save as: .github/workflows/test-wif.yml

name: Test Workload Identity Federation

on:
  workflow_dispatch:  # Manual trigger only

jobs:
  test-wif:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      id-token: write  # Required for WIF
      
    steps:
    - name: Checkout
      uses: actions/checkout@v4
      
    - name: Authenticate to Google Cloud
      id: auth
      uses: google-github-actions/auth@v2
      with:
        workload_identity_provider: 'projects/YOUR_PROJECT_NUMBER/locations/global/workloadIdentityPools/dev-pool/providers/github-provider'
        service_account: 'dev-vm-sa@praxis-gear-483220-k4.iam.gserviceaccount.com'
        
    - name: Set up Cloud SDK
      uses: google-github-actions/setup-gcloud@v2
      
    - name: Test GCP Access
      run: |
        echo "Testing WIF authentication..."
        gcloud auth list
        gcloud config get-value project
        gcloud compute instances list --limit=5
        echo "✅ WIF is working!"
```

## 📚 Step 9: Educational Talking Points

Use these points when explaining WIF to others:

### **🎯 What Problem Does WIF Solve?**
"Before WIF, we had to create service account keys (JSON files) and store them in GitHub Secrets. This was risky because:
- Keys never expire
- If leaked, attackers have permanent access
- Hard to track who's using what key
- Manual rotation required"

### **🔐 How WIF Solves It**
"With WIF, GitHub Actions uses its own identity token. GCP validates this token and exchanges it for a temporary GCP token. No keys stored anywhere!"

### **🏗️ The Three Components**
1. **Workload Identity Pool**: "Think of this as a 'trust boundary' - it defines which external systems we trust"
2. **Provider**: "This is the specific configuration for GitHub - how to validate GitHub tokens"
3. **IAM Binding**: "This grants the external identity permission to act as our service account"

### **🎭 The Token Exchange Flow**
"When GitHub Actions runs:
1. GitHub gives it an OIDC token proving 'I am workflow X from repo Y'
2. GitHub Actions sends this to GCP
3. GCP checks: Is this from the right repo? Right branch? Right user?
4. If yes, GCP gives back a 1-hour GCP access token
5. GitHub Actions uses that to deploy infrastructure"

### **✅ Security Benefits**
- "No stored credentials anywhere"
- "Tokens expire after 1 hour"
- "We can restrict by repository, branch, even specific users"
- "Full audit trail - we know exactly who did what"
- "Easy to revoke - just remove the IAM binding"

## 🎬 Step 10: Live Demonstration Checklist

When demonstrating to others, follow this sequence:

```
☐ 1. Show current Terraform code (modules/iam/main.tf)
     - Point out the conditional creation (count = ...)
     - Explain each resource

☐ 2. Run the demo script (WIF-Demo-Script.ps1)
     - Show current status
     - Explain what each check means

☐ 3. Show terraform.tfvars
     - Point out github_repository variable
     - Explain dormant vs active state

☐ 4. If activating WIF:
     - Update github_repository
     - Run terraform plan
     - Show what will be created
     - Run terraform apply
     - Re-run demo script to show changes

☐ 5. Show GCP Console
     - Navigate to IAM & Admin > Workload Identity Federation
     - Show the pool and provider visually
     - Show service account IAM bindings

☐ 6. Explain the security benefits
     - Compare to service account keys
     - Show audit logs (if available)

☐ 7. Q&A Session
     - Answer questions
     - Show relevant documentation
```

## 📊 Validation Outputs Reference

### **Healthy WIF Setup**
```bash
# Pool exists
NAME: dev-pool
STATE: ACTIVE

# Provider exists
NAME: github-provider
STATE: ACTIVE

# IAM binding exists
role: roles/iam.workloadIdentityUser
members:
- principalSet://iam.googleapis.com/.../attribute.repository/your-repo
```

### **Dormant WIF Setup** (Your current state)
```bash
# Pool exists
NAME: dev-pool
STATE: ACTIVE

# Provider does NOT exist
Listed 0 items.

# IAM binding does NOT exist
(no workloadIdentityUser role)
```

## 🎓 Quiz for Validation

Test understanding with these questions:

1. **Q**: Why does the GitHub provider have `count = var.github_repository != "" ? 1 : 0`?
   **A**: To conditionally create the provider only when github_repository is set, avoiding unnecessary resources.

2. **Q**: What does the attribute_condition do?
   **A**: It restricts which GitHub repositories can use this WIF provider, adding a security layer.

3. **Q**: Why is `id-token: write` permission needed in GitHub Actions?
   **A**: GitHub Actions needs this permission to generate OIDC tokens for WIF authentication.

4. **Q**: How long do WIF tokens last?
   **A**: 1 hour by default, then they expire automatically.

5. **Q**: Can we use WIF for local development?
   **A**: No, WIF is designed for external systems like CI/CD. For local development, use ADC or impersonation.

---

**🎉 You now have everything needed to validate and educate others about WIF!**

Run the demo script, follow the talking points, and use the visual diagrams to make WIF concepts clear to your team.