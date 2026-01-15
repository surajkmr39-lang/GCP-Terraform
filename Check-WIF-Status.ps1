# WIF Status Check Script
# Simple and reliable version

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  WIF Status Check - Quick Validation  " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$project = "praxis-gear-483220-k4"

# Check 1: WIF Pool
Write-Host "[1/4] Checking Workload Identity Pool..." -ForegroundColor Yellow
try {
    $poolOutput = gcloud iam workload-identity-pools describe github-pool --location=global --project=$project --format="value(name,state)" 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  Status: ACTIVE" -ForegroundColor Green
        Write-Host "  Pool: github-pool" -ForegroundColor Green
    } else {
        Write-Host "  Status: NOT FOUND" -ForegroundColor Red
    }
} catch {
    Write-Host "  Error checking pool: $_" -ForegroundColor Red
}

Write-Host ""

# Check 2: GitHub Provider
Write-Host "[2/4] Checking GitHub Provider..." -ForegroundColor Yellow
try {
    $providerOutput = gcloud iam workload-identity-pools providers describe github --workload-identity-pool=github-pool --location=global --project=$project --format="value(name,state)" 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  Status: ACTIVE" -ForegroundColor Green
        Write-Host "  Provider: github" -ForegroundColor Green
    } else {
        Write-Host "  Status: NOT FOUND" -ForegroundColor Red
    }
} catch {
    Write-Host "  Error checking provider: $_" -ForegroundColor Red
}

Write-Host ""

# Check 3: Provider Configuration
Write-Host "[3/4] Checking Provider Configuration..." -ForegroundColor Yellow
try {
    Write-Host "  Issuer URI:" -ForegroundColor Cyan
    gcloud iam workload-identity-pools providers describe github --workload-identity-pool=github-pool --location=global --project=$project --format="value(oidc.issuerUri)"
    
    Write-Host "  Attribute Condition:" -ForegroundColor Cyan
    gcloud iam workload-identity-pools providers describe github --workload-identity-pool=github-pool --location=global --project=$project --format="value(attributeCondition)"
} catch {
    Write-Host "  Error getting configuration: $_" -ForegroundColor Red
}

Write-Host ""

# Check 4: Service Accounts
Write-Host "[4/4] Checking Service Accounts..." -ForegroundColor Yellow
try {
    Write-Host "  Available Service Accounts:" -ForegroundColor Cyan
    gcloud iam service-accounts list --project=$project --format="table(email,displayName)"
} catch {
    Write-Host "  Error listing service accounts: $_" -ForegroundColor Red
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "           Status Check Complete        " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Summary
Write-Host "SUMMARY:" -ForegroundColor Yellow
Write-Host "  Your WIF Configuration:" -ForegroundColor Cyan
Write-Host "  - Pool: github-pool" -ForegroundColor White
Write-Host "  - Provider: github" -ForegroundColor White
Write-Host "  - Project: $project" -ForegroundColor White
Write-Host ""
Write-Host "  For GitHub Actions, use:" -ForegroundColor Cyan
Write-Host "  workload_identity_provider: 'projects/251838763754/locations/global/workloadIdentityPools/github-pool/providers/github'" -ForegroundColor White
Write-Host "  service_account: 'galaxy@praxis-gear-483220-k4.iam.gserviceaccount.com'" -ForegroundColor White
Write-Host ""
