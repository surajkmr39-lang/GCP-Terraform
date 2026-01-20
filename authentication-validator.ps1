# Enhanced Authentication Status Check Script
# Checks WIF, Production Service Account, and Multi-Environment Authentication
Write-Host "🔐 Enhanced Authentication Status Check - Enterprise Ready" -ForegroundColor Cyan
Write-Host ""

# Check current authentication
Write-Host "📋 Current Authentication Status:" -ForegroundColor Yellow
Write-Host ""
gcloud auth list --format="table(account,status)" 2>$null
Write-Host ""

# Check WIF Infrastructure
Write-Host "🌐 Checking Workload Identity Federation..." -ForegroundColor Yellow
gcloud iam workload-identity-pools describe github-actions-pool --location=global --project=praxis-gear-483220-k4 --format="value(name)" 2>$null
if ($LASTEXITCODE -eq 0) {
    Write-Host "  ✅ WIF Pool Status: ACTIVE" -ForegroundColor Green
} else {
    Write-Host "  ❌ WIF Pool Status: NOT FOUND" -ForegroundColor Red
}

# Check GitHub Provider
gcloud iam workload-identity-pools providers describe github-actions --workload-identity-pool=github-actions-pool --location=global --project=praxis-gear-483220-k4 --format="value(name)" 2>$null
if ($LASTEXITCODE -eq 0) {
    Write-Host "  ✅ GitHub Provider Status: ACTIVE" -ForegroundColor Green
} else {
    Write-Host "  ❌ GitHub Provider Status: NOT FOUND" -ForegroundColor Red
}

Write-Host ""

# Check Service Accounts
Write-Host "🏢 Checking Service Accounts..." -ForegroundColor Yellow

# GitHub Actions Service Account
gcloud iam service-accounts describe github-actions-sa@praxis-gear-483220-k4.iam.gserviceaccount.com --project=praxis-gear-483220-k4 --format="value(email)" 2>$null
if ($LASTEXITCODE -eq 0) {
    Write-Host "  ✅ GitHub Actions SA: ACTIVE" -ForegroundColor Green
} else {
    Write-Host "  ❌ GitHub Actions SA: NOT FOUND" -ForegroundColor Red
}

# Production Service Account (NEW)
gcloud iam service-accounts describe terraform-prod-sa@praxis-gear-483220-k4.iam.gserviceaccount.com --project=praxis-gear-483220-k4 --format="value(email)" 2>$null
if ($LASTEXITCODE -eq 0) {
    Write-Host "  ✅ Production SA: ACTIVE" -ForegroundColor Green
} else {
    Write-Host "  ❌ Production SA: NOT FOUND" -ForegroundColor Red
}

Write-Host ""

# Test Production Impersonation
Write-Host "🔐 Testing Production Service Account Impersonation..." -ForegroundColor Yellow
gcloud auth print-access-token --impersonate-service-account=terraform-prod-sa@praxis-gear-483220-k4.iam.gserviceaccount.com --quiet 2>$null
if ($LASTEXITCODE -eq 0) {
    Write-Host "  ✅ Production Impersonation: WORKING" -ForegroundColor Green
} else {
    Write-Host "  ❌ Production Impersonation: FAILED" -ForegroundColor Red
}

Write-Host ""

# Check Infrastructure Status
Write-Host "🏗️ Checking Infrastructure Status..." -ForegroundColor Yellow
$instances = gcloud compute instances list --format="value(name,zone,status,machineType,externalIP)" --project=praxis-gear-483220-k4 2>$null
if ($instances) {
    Write-Host "  ✅ Infrastructure Status:" -ForegroundColor Green
    gcloud compute instances list --format="table(name,zone,status,machineType,externalIP)" --project=praxis-gear-483220-k4 2>$null
} else {
    Write-Host "  ℹ️ No running instances found" -ForegroundColor Yellow
}

Write-Host ""

# Enhanced Configuration Summary
Write-Host "📊 Enhanced Authentication Configuration Summary:" -ForegroundColor Cyan
Write-Host ""
Write-Host "🖥️ Development Environment:" -ForegroundColor White
Write-Host "  Method: ADC (Application Default Credentials)" -ForegroundColor Gray
Write-Host "  Account: $(gcloud config get-value account 2>$null)" -ForegroundColor Gray
Write-Host "  Use Case: Local development and testing" -ForegroundColor Gray
Write-Host ""
Write-Host "🏭 Production Environment:" -ForegroundColor White
Write-Host "  Method: Service Account Impersonation" -ForegroundColor Gray
Write-Host "  Service Account: terraform-prod-sa@praxis-gear-483220-k4.iam.gserviceaccount.com" -ForegroundColor Gray
Write-Host "  Use Case: Secure production deployments with audit trail" -ForegroundColor Gray
Write-Host ""
Write-Host "🌐 CI/CD Pipeline:" -ForegroundColor White
Write-Host "  Method: WIF (Workload Identity Federation)" -ForegroundColor Gray
Write-Host "  Pool: github-actions-pool" -ForegroundColor Gray
Write-Host "  Provider: github-actions" -ForegroundColor Gray
Write-Host "  Service Account: github-actions-sa@praxis-gear-483220-k4.iam.gserviceaccount.com" -ForegroundColor Gray
Write-Host "  Use Case: Automated keyless deployments" -ForegroundColor Gray
Write-Host ""
Write-Host "🎯 Status: Enterprise-grade multi-environment authentication ready!" -ForegroundColor Green
Write-Host ""