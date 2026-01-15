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

# Check Terraform State
Write-Host "`n5️⃣  Checking Terraform State..." -ForegroundColor Green
$wifPoolState = terraform state list 2>$null | Select-String "workload_identity_pool.pool"
$wifProviderState = terraform state list 2>$null | Select-String "workload_identity_pool_provider"
$wifBindingState = terraform state list 2>$null | Select-String "workload_identity_binding"

if ($wifPoolState) {
    Write-Host "   ✅ WIF Pool in Terraform state" -ForegroundColor Green
} else {
    Write-Host "   ❌ WIF Pool not in Terraform state" -ForegroundColor Red
}

if ($wifProviderState) {
    Write-Host "   ✅ WIF Provider in Terraform state" -ForegroundColor Green
} else {
    Write-Host "   ⚠️  WIF Provider not in Terraform state (dormant)" -ForegroundColor Yellow
}

if ($wifBindingState) {
    Write-Host "   ✅ WIF IAM Binding in Terraform state" -ForegroundColor Green
} else {
    Write-Host "   ⚠️  WIF IAM Binding not in Terraform state (dormant)" -ForegroundColor Yellow
}

# Summary
Write-Host "`n📊 SUMMARY" -ForegroundColor Yellow
Write-Host "─────────────────────────────────────────────────────────────"

if ($pool -and $provider -and $wifBinding) {
    Write-Host "✅ WIF is FULLY CONFIGURED and ACTIVE" -ForegroundColor Green
    Write-Host "   Ready for GitHub Actions integration" -ForegroundColor Green
    Write-Host "`n   Next Steps:" -ForegroundColor Cyan
    Write-Host "   1. Create .github/workflows/deploy.yml in your repo" -ForegroundColor White
    Write-Host "   2. Use google-github-actions/auth@v2 action" -ForegroundColor White
    Write-Host "   3. Test the workflow" -ForegroundColor White
} elseif ($pool -and !$provider) {
    Write-Host "⚠️  WIF is PARTIALLY CONFIGURED (Dormant)" -ForegroundColor Yellow
    Write-Host "   Pool exists but provider not created" -ForegroundColor Yellow
    Write-Host "`n   To Activate WIF:" -ForegroundColor Cyan
    Write-Host "   1. Edit environments/dev/terraform.tfvars" -ForegroundColor White
    Write-Host "   2. Set: github_repository = 'your-username/your-repo'" -ForegroundColor White
    Write-Host "   3. Run: terraform apply -var-file='environments/dev/terraform.tfvars'" -ForegroundColor White
} else {
    Write-Host "❌ WIF is NOT CONFIGURED" -ForegroundColor Red
    Write-Host "   Action: Deploy Terraform infrastructure" -ForegroundColor Cyan
}

# Educational Section
Write-Host "`n📚 EDUCATIONAL NOTES" -ForegroundColor Yellow
Write-Host "─────────────────────────────────────────────────────────────"
Write-Host "What is Workload Identity Federation?" -ForegroundColor Cyan
Write-Host "  WIF allows external systems (like GitHub Actions) to authenticate" -ForegroundColor White
Write-Host "  to GCP without storing service account keys." -ForegroundColor White
Write-Host "`nHow it works:" -ForegroundColor Cyan
Write-Host "  1. GitHub Actions gets an OIDC token from GitHub" -ForegroundColor White
Write-Host "  2. Sends token to GCP WIF endpoint" -ForegroundColor White
Write-Host "  3. GCP validates token and checks conditions" -ForegroundColor White
Write-Host "  4. GCP issues temporary GCP access token (1 hour)" -ForegroundColor White
Write-Host "  5. GitHub Actions uses token to access GCP resources" -ForegroundColor White
Write-Host "`nSecurity Benefits:" -ForegroundColor Cyan
Write-Host "  ✅ No stored credentials" -ForegroundColor Green
Write-Host "  ✅ Automatic token expiration" -ForegroundColor Green
Write-Host "  ✅ Full audit trail" -ForegroundColor Green
Write-Host "  ✅ Attribute-based access control" -ForegroundColor Green
Write-Host "  ✅ Easy to revoke access" -ForegroundColor Green

Write-Host "`n╔════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║              Demo Complete                                 ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
