# 🚀 How to Run WIF Status Check

## Quick Start (3 Simple Steps)

### Step 1: Open PowerShell in Your Project Directory

```powershell
# Navigate to your project
cd C:\GCP-Terraform-7th-Jan-2026
```

### Step 2: Run the Script

```powershell
# Run the WIF status check script
.\Check-WIF-Status.ps1
```

That's it! The script will automatically check your WIF configuration.

---

## 📊 What the Script Checks

The script validates 4 key components:

1. **Workload Identity Pool** - Checks if `github-pool` exists and is ACTIVE
2. **GitHub Provider** - Verifies the GitHub OIDC provider is configured
3. **Provider Configuration** - Shows issuer URI and security conditions
4. **Service Accounts** - Lists all service accounts in your project

---

## ✅ Your Current Results

Based on the last run, your WIF is **FULLY OPERATIONAL**:

```
✅ Pool: github-pool (ACTIVE)
✅ Provider: github (ACTIVE)
✅ Issuer: https://token.actions.githubusercontent.com
✅ Security: Only allows repository "surajkmr39-lang/GCP-Terraform"
✅ Service Account: galaxy@praxis-gear-483220-k4.iam.gserviceaccount.com
```

---

## 🎯 Alternative Ways to Run

### Method 1: Direct Execution (Recommended)
```powershell
.\Check-WIF-Status.ps1
```

### Method 2: With Execution Policy Bypass
```powershell
PowerShell -ExecutionPolicy Bypass -File .\Check-WIF-Status.ps1
```

### Method 3: From Any Directory
```powershell
PowerShell -ExecutionPolicy Bypass -File "C:\GCP-Terraform-7th-Jan-2026\Check-WIF-Status.ps1"
```

---

## 🔍 Manual Validation Commands

If you prefer to check manually, use these commands:

```powershell
# Check WIF Pool
gcloud iam workload-identity-pools describe github-pool --location=global --project=praxis-gear-483220-k4

# Check GitHub Provider
gcloud iam workload-identity-pools providers describe github --workload-identity-pool=github-pool --location=global --project=praxis-gear-483220-k4

# List Service Accounts
gcloud iam service-accounts list --project=praxis-gear-483220-k4

# Get Full Provider Details
gcloud iam workload-identity-pools providers describe github --workload-identity-pool=github-pool --location=global --project=praxis-gear-483220-k4 --format=yaml
```

---

## 📋 Expected Output

When WIF is working correctly, you should see:

```
========================================
  WIF Status Check - Quick Validation
========================================

[1/4] Checking Workload Identity Pool...
  ✅ Status: ACTIVE
  ✅ Pool: github-pool

[2/4] Checking GitHub Provider...
  ✅ Status: ACTIVE
  ✅ Provider: github

[3/4] Checking Provider Configuration...
  Issuer URI: https://token.actions.githubusercontent.com
  Attribute Condition: assertion.repository == "surajkmr39-lang/GCP-Terraform"

[4/4] Checking Service Accounts...
  ✅ galaxy@praxis-gear-483220-k4.iam.gserviceaccount.com (GitHub Actions)
  ✅ demo-service-account@praxis-gear-483220-k4.iam.gserviceaccount.com (Terraform)
```

---

## 🎓 Using This for Education/Demonstration

### For Team Demos:

1. **Open PowerShell** in your project directory
2. **Run the script**: `.\Check-WIF-Status.ps1`
3. **Explain each section** as it appears:
   - "This checks our WIF pool exists..."
   - "This verifies GitHub is configured as a provider..."
   - "This shows our security condition - only our repo can authenticate..."
   - "These are the service accounts that can be used..."

### For Interviews:

Show the script output and explain:
- "I implemented WIF for keyless GitHub Actions authentication"
- "The script validates all components are configured correctly"
- "We use attribute-based access control to restrict by repository"
- "No service account keys are stored anywhere"

---

## 🔧 Troubleshooting

### Issue: "Script cannot be loaded"

**Solution**:
```powershell
# Run with execution policy bypass
PowerShell -ExecutionPolicy Bypass -File .\Check-WIF-Status.ps1
```

### Issue: "gcloud command not found"

**Solution**:
```powershell
# Verify gcloud is installed
gcloud --version

# If not installed, download from: https://cloud.google.com/sdk/docs/install
```

### Issue: "Permission denied" errors

**Solution**:
```powershell
# Re-authenticate
gcloud auth login
gcloud auth application-default login
```

### Issue: "Pool not found"

**Possible Causes**:
- Wrong project ID
- WIF not deployed yet
- Need to run `terraform apply`

**Solution**:
```powershell
# Check current project
gcloud config get-value project

# Deploy infrastructure if needed
terraform apply -var-file="environments/dev/terraform.tfvars"
```

---

## 📚 Related Files

- **Check-WIF-Status.ps1** - The main status check script (this one!)
- **WIF-COMPLETE-SETUP-SUMMARY.md** - Complete WIF documentation
- **WIF-QUICK-REFERENCE.md** - Quick reference for daily use
- **WIF-VALIDATION-REPORT.md** - Detailed validation report

---

## 🎯 Quick Commands Cheat Sheet

```powershell
# Run WIF status check
.\Check-WIF-Status.ps1

# Check WIF pool only
gcloud iam workload-identity-pools describe github-pool --location=global --project=praxis-gear-483220-k4

# Check GitHub provider only
gcloud iam workload-identity-pools providers describe github --workload-identity-pool=github-pool --location=global --project=praxis-gear-483220-k4

# List all WIF pools
gcloud iam workload-identity-pools list --location=global --project=praxis-gear-483220-k4

# Get provider in YAML format (detailed)
gcloud iam workload-identity-pools providers describe github --workload-identity-pool=github-pool --location=global --project=praxis-gear-483220-k4 --format=yaml
```

---

## ✅ Success Indicators

Your WIF is working correctly if you see:

- ✅ Pool status: ACTIVE
- ✅ Provider status: ACTIVE
- ✅ Issuer URI: https://token.actions.githubusercontent.com
- ✅ Attribute condition includes your repository name
- ✅ Service account `galaxy@...` exists

---

**🎉 Your WIF is fully operational and ready for GitHub Actions!**

Next step: Create a GitHub Actions workflow using the configuration shown in the script output.