# 🚀 WIF Quick Reference Card

**Your Project**: praxis-gear-483220-k4  
**Status**: ✅ FULLY OPERATIONAL

---

## 📋 Your WIF Configuration (Copy-Paste Ready)

### Workload Identity Provider
```
projects/251838763754/locations/global/workloadIdentityPools/github-pool/providers/github
```

### Service Account
```
galaxy@praxis-gear-483220-k4.iam.gserviceaccount.com
```

### Repository
```
surajkmr39-lang/GCP-Terraform
```

---

## ⚡ Quick Validation Commands

```bash
# Check WIF Pool
gcloud iam workload-identity-pools describe github-pool --location=global --project=praxis-gear-483220-k4

# Check GitHub Provider
gcloud iam workload-identity-pools providers describe github --workload-identity-pool=github-pool --location=global --project=praxis-gear-483220-k4

# List Service Accounts
gcloud iam service-accounts list --project=praxis-gear-483220-k4

# View Provider Configuration
gcloud iam workload-identity-pools providers describe github --workload-identity-pool=github-pool --location=global --project=praxis-gear-483220-k4 --format=yaml
```

---

## 🔧 GitHub Actions Workflow (Minimal)

```yaml
name: Deploy with WIF

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      id-token: write  # REQUIRED for WIF
      
    steps:
    - uses: actions/checkout@v4
    
    - uses: google-github-actions/auth@v2
      with:
        workload_identity_provider: 'projects/251838763754/locations/global/workloadIdentityPools/github-pool/providers/github'
        service_account: 'galaxy@praxis-gear-483220-k4.iam.gserviceaccount.com'
    
    - uses: google-github-actions/setup-gcloud@v2
    
    - run: |
        gcloud auth list
        terraform init
        terraform apply -auto-approve
```

---

## 🎯 30-Second Explanation

"We use Workload Identity Federation so GitHub Actions can deploy to GCP without storing any service account keys. GitHub gives us an OIDC token, GCP validates it's from our repository, and exchanges it for a 1-hour GCP token. Zero stored credentials, automatic expiration, full audit trail."

---

## 🔍 Troubleshooting

### Issue: "Failed to generate access token"
```bash
# Check provider exists
gcloud iam workload-identity-pools providers list --workload-identity-pool=github-pool --location=global

# Check attribute condition
gcloud iam workload-identity-pools providers describe github --workload-identity-pool=github-pool --location=global --format="value(attributeCondition)"
```

### Issue: "Permission denied"
```bash
# Check service account IAM (need appropriate permissions)
gcloud projects get-iam-policy praxis-gear-483220-k4 --flatten="bindings[].members" --filter="bindings.members:galaxy@praxis-gear-483220-k4.iam.gserviceaccount.com"
```

### Issue: "Invalid token"
- Verify `id-token: write` permission in workflow
- Check repository name matches exactly
- Verify provider is ACTIVE

---

## 📊 Security Checklist

- [x] No service account keys exist
- [x] Repository restriction enabled
- [x] Tokens expire after 1 hour
- [x] Audit logging enabled
- [ ] Branch restrictions (optional)
- [ ] User restrictions (optional)
- [ ] Monitoring alerts (optional)

---

## 🎓 Key Concepts

**WIF Pool**: Trust boundary for external identities  
**Provider**: Configuration for specific identity system (GitHub)  
**Attribute Mapping**: Maps external token claims to GCP attributes  
**Attribute Condition**: Security filter (e.g., specific repository only)  
**IAM Binding**: Grants external identity permission to impersonate SA

---

## 📚 Documentation Links

- [WIF Overview](https://cloud.google.com/iam/docs/workload-identity-federation)
- [GitHub Actions Integration](https://github.com/google-github-actions/auth)
- [Your Complete Guide](./WIF-COMPLETE-SETUP-SUMMARY.md)
- [Validation Report](./WIF-VALIDATION-REPORT.md)

---

**Last Updated**: January 15, 2026  
**Status**: Production Ready ✅