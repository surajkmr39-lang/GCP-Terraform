# 🚀 GCP Infrastructure with Terraform

[![Terraform](https://img.shields.io/badge/Terraform-1.0+-623CE4?logo=terraform&logoColor=white)](https://terraform.io)
[![Google Cloud](https://img.shields.io/badge/Google%20Cloud-4285F4?logo=google-cloud&logoColor=white)](https://cloud.google.com)
[![Deployed](https://img.shields.io/badge/Status-Deployed-success)](https://github.com/surajkmr39-lang/GCP-Terraform)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**✅ LIVE DEPLOYMENT**: Enterprise-grade Google Cloud Platform infrastructure successfully deployed using Terraform with modular architecture, security hardening, and workload identity federation.

**Author**: Suraj Kumar  
**Project**: praxis-gear-483220-k4  
**Environment**: Development (Active)

## 📋 Project Overview

This project demonstrates a **fully deployed and operational** secure, scalable development environment on Google Cloud Platform using Infrastructure as Code principles. The implementation follows enterprise best practices with comprehensive security features and cost optimization.

### 🎯 Key Features ✅ DEPLOYED

- **✅ Modular Architecture**: 4 reusable Terraform modules (15 resources deployed)
- **✅ Security First**: Shielded VMs, Workload Identity Federation, VPC security
- **✅ Cost Optimized**: ~$18-24/month for complete environment
- **✅ Enterprise Ready**: Compliance with security standards
- **✅ CI/CD Integration**: GitHub Actions with Workload Identity Federation
- **✅ State Management**: Local state with workspace separation
- **✅ Documentation**: Comprehensive guides and interview preparation materials

## 🏗️ Architecture - LIVE DEPLOYMENT

```
🌐 Internet → 🛡️ Firewall → 🔄 Cloud NAT → 📡 VPC → 💻 VM Instance (34.173.115.82)
                                                    ↓
                              🔐 Service Account ← 🔑 Workload Identity (github-pool)
```

### ✅ DEPLOYED Infrastructure Components (15 Resources Active)

| Component | Resource | Configuration | Status |
|-----------|----------|---------------|---------|
| **Network** | VPC + Subnet | `dev-vpc` with `10.0.1.0/24` | ✅ Active |
| **Compute** | VM Instance | `dev-vm` (e2-medium) Ubuntu 22.04 | ✅ Running |
| **Security** | Firewall Rules | SSH, HTTP/HTTPS, Internal, Health Check | ✅ Active |
| **Identity** | Service Account | `dev-vm-sa@praxis-gear-483220-k4.iam.gserviceaccount.com` | ✅ Active |
| **WIF** | Identity Pool | `github-pool` for GitHub Actions | ✅ Configured |
| **Networking** | Cloud NAT | Secure outbound internet access | ✅ Active |

### 🔍 Live Resource Details
- **VM External IP**: `34.173.115.82`
- **VM Internal IP**: `10.0.1.2`
- **SSH Command**: `gcloud compute ssh dev-vm --zone=us-central1-a --project=praxis-gear-483220-k4`
- **Workload Identity Pool**: `projects/251838763754/locations/global/workloadIdentityPools/github-pool`

## 📁 Project Structure - CURRENT ORGANIZATION

```
├── README.md                         # 📖 Project overview (this file)
├── main.tf                           # 🏗️ Root Terraform configuration
├── variables.tf                      # 📝 Variable definitions
├── outputs.tf                        # 📤 Output definitions
├── terraform.tfvars                  # ⚙️ Current environment variables
├── terraform.tfvars.example          # 📋 Example variables file
├── Makefile                          # 🔧 Build automation commands
├── Check-WIF-Status.ps1              # ✅ WIF validation script
├── architecture-diagram.py           # 📊 Generate architecture diagram
├── gcp-architecture-diagram.png      # 🖼️ Generated architecture diagram
├── gcp-architecture-diagram.pdf      # 📄 Architecture diagram (PDF)
├── .github/workflows/                # 🚀 CI/CD pipelines
│   ├── cicd-pipeline.yml            # 🔄 Main CI/CD workflow
│   ├── deploy-infrastructure.yml    # 🚀 Deployment workflow
│   └── test-wif-auth.yml            # 🔐 WIF authentication test
├── modules/                          # 📦 Terraform modules
│   ├── network/                      # 🌐 VPC, subnets, NAT gateway
│   ├── security/                     # 🛡️ Firewall rules
│   ├── iam/                          # 👤 Service accounts, workload identity
│   └── compute/                      # 💻 VM instances
├── environments/                     # 🌍 Environment-specific configs
│   └── dev/terraform.tfvars          # 🔧 Development configuration
├── labs/                             # 🧪 Authentication practice labs
│   ├── README.md                     # 📚 Lab overview and instructions
│   ├── phase-1-adc/                  # 🔑 Application Default Credentials
│   ├── phase-2-service-account-keys/ # 🗝️ Service Account Keys
│   ├── phase-3-impersonation/        # 🎭 Service Account Impersonation
│   ├── phase-4-workload-identity/    # 🔐 Workload Identity Federation
│   └── phase-5-github-actions-wif/   # 🚀 GitHub Actions with WIF
├── info/                             # 📚 Documentation & guides
│   ├── DEPLOYMENT-STATUS-SUMMARY.md  # ✅ Current deployment status
│   ├── TERRAFORM-STATE-COMMANDS.md   # 📋 State management commands
│   ├── TERRAFORM-STATE-STORAGE-EXPLAINED.md # 💾 State storage options
│   ├── INTERVIEW-MASTER-GUIDE.md     # 🎯 Complete interview preparation
│   ├── INTERVIEW-GUIDE-PART1-CONCEPTS.md # 📖 Terraform concepts
│   ├── INTERVIEW-GUIDE-PART2-CODE-WALKTHROUGH.md # 🔍 Code explanation
│   ├── INTERVIEW-GUIDE-PART3-ADVANCED-QUESTIONS.md # 🧠 Advanced topics
│   ├── INTERVIEW-GUIDE-PART4-SCENARIO-QUESTIONS.md # 🎭 Scenario-based
│   ├── INTERVIEW-GUIDE-PART5-PROJECT-DEMO.md # 🎪 Project demonstration
│   ├── INTERVIEW-GUIDE-PART6-QUICK-REFERENCE.md # ⚡ Quick reference
│   ├── GIT-COMMANDS-EXPLAINED.md     # 📝 Git commands explanation
│   ├── GIT-INTERVIEW-COMMANDS.md     # 🔧 Git interview commands
│   ├── STRING-INTERPOLATION-EXPLAINED.md # 🔗 String interpolation guide
│   ├── CICD-PIPELINE-GUIDE.md        # 🚀 CI/CD documentation
│   ├── CICD-DEPLOYMENT-SUCCESS.md    # ✅ Deployment success guide
│   └── WIF-QUICK-REFERENCE.md        # 🔐 WIF reference guide
├── docs/                             # 📄 Additional documentation
└── terraform.tfstate.d/              # 💾 Terraform state files (local)
    └── dev/                          # 🔧 Development workspace state
        ├── terraform.tfstate         # 📊 Current state (15 resources)
        └── terraform.tfstate.backup  # 🔄 State backup
```

## 🚀 Quick Start - VERIFIED WORKING

### Prerequisites ✅ CONFIRMED

1. **Google Cloud SDK** ✅
   ```bash
   # Already configured for project: praxis-gear-483220-k4
   gcloud auth login
   gcloud config set project praxis-gear-483220-k4
   ```

2. **Terraform >= 1.0** ✅
   ```bash
   # Currently using Terraform with local state
   terraform --version
   ```

3. **Required APIs** ✅ ENABLED
   ```bash
   # All APIs already enabled and working:
   # ✅ compute.googleapis.com
   # ✅ iam.googleapis.com  
   # ✅ iamcredentials.googleapis.com
   # ✅ cloudresourcemanager.googleapis.com
   ```

### Current Deployment Status ✅

**Infrastructure is LIVE and OPERATIONAL**:
```bash
# Check current deployment
terraform state list    # Shows 15 deployed resources
terraform output        # Shows live resource details

# Connect to running VM
gcloud compute ssh dev-vm --zone=us-central1-a --project=praxis-gear-483220-k4

# Validate WIF setup
.\Check-WIF-Status.ps1
```

### For New Deployments

1. **Clone Repository**
   ```bash
   git clone https://github.com/surajkmr39-lang/GCP-Terraform.git
   cd GCP-Terraform
   ```

2. **Configure Environment**
   ```bash
   # Copy and edit terraform.tfvars
   cp terraform.tfvars.example terraform.tfvars
   # Update with your project details
   ```

3. **Deploy Infrastructure**
   ```bash
   # Initialize and deploy
   terraform init
   terraform workspace new dev  # or select existing
   terraform plan
   terraform apply
   ```

## 🔐 Security Features - IMPLEMENTED & ACTIVE

### VM Security ✅
- ✅ **Shielded VM**: Secure boot, vTPM, integrity monitoring (ACTIVE)
- ✅ **OS Login**: Centralized SSH key management (CONFIGURED)
- ✅ **Metadata Security**: Block project SSH keys (ENABLED)
- ✅ **Service Account**: `dev-vm-sa@praxis-gear-483220-k4.iam.gserviceaccount.com` (ACTIVE)

### Network Security ✅
- ✅ **Private Subnet**: `10.0.1.0/24` - No direct internet access (DEPLOYED)
- ✅ **Cloud NAT**: Controlled outbound access (ACTIVE)
- ✅ **Firewall Rules**: 4 rules - SSH, HTTP/HTTPS, Internal, Health Check (ACTIVE)
- ✅ **VPC Flow Logs**: Network monitoring (ENABLED)

### Identity Security ✅
- ✅ **Workload Identity**: `github-pool` - No stored service account keys (CONFIGURED)
- ✅ **IAM Roles**: 4 roles - Compute/Storage Viewer, Logging/Monitoring Writer (ASSIGNED)
- ✅ **GitHub Integration**: Secure CI/CD authentication for `surajkmr39-lang/GCP-Terraform` (READY)

## 💰 Cost Analysis - CURRENT DEPLOYMENT

| Resource | Monthly Cost | Status |
|----------|-------------|---------|
| VM Instance (e2-medium) | $13-16 | ✅ Running |
| Persistent Disk (20GB SSD) | $3 | ✅ Attached |
| External IP (34.173.115.82) | $3 | ✅ Assigned |
| Cloud NAT | $1-2 | ✅ Active |
| Network Egress | $1-3 | ✅ Monitored |
| **Total Current Cost** | **$18-24/month** | **✅ LIVE** |

### Cost Optimization Implemented
- ✅ Using e2-medium (cost-effective for development)
- ✅ 20GB SSD (right-sized for current needs)
- ✅ Single environment deployment
- ✅ Efficient resource allocation

### Additional Cost Optimization Options
- Use preemptible instances for dev (-60% cost)
- Implement auto-shutdown schedules
- Monitor network egress usage
- Use committed use discounts for production

## 🛠️ Usage Examples - CURRENT OPERATIONS

### Infrastructure Management
```bash
# Check current deployment status
terraform state list                    # List all 15 deployed resources
terraform output                        # Show live resource details
terraform workspace show               # Current workspace: dev

# Validate configuration
terraform validate                      # Check configuration syntax
terraform plan                         # Check for any drift

# Access deployed VM
gcloud compute ssh dev-vm --zone=us-central1-a --project=praxis-gear-483220-k4

# Validate WIF setup
.\Check-WIF-Status.ps1                 # PowerShell script for WIF validation
```

### State Management
```bash
# Current state location: terraform.tfstate.d/dev/
terraform workspace list               # Show available workspaces
terraform state show module.compute.google_compute_instance.vm  # VM details
terraform state show module.iam.google_iam_workload_identity_pool.pool  # WIF details
```

### Environment Operations
```bash
# Development environment (current)
terraform plan                         # Plan changes
terraform apply                        # Apply changes
terraform destroy                      # Destroy infrastructure (if needed)

# Generate architecture diagram
python architecture-diagram.py        # Creates visual architecture diagram
```

## 🔧 Customization - CURRENT CONFIGURATION

### Current VM Configuration
```hcl
# In terraform.tfvars (active configuration)
project_id = "praxis-gear-483220-k4"
region     = "us-central1"
zone       = "us-central1-a"
environment = "dev"

machine_type = "e2-medium"              # Currently deployed
vm_image     = "ubuntu-os-cloud/ubuntu-2204-lts"  # Active OS
disk_size    = 20                       # Current disk size (GB)
```

### Current Network Configuration
```hcl
# Active network settings
subnet_cidr = "10.0.1.0/24"           # Current subnet range
vpc_name    = "dev-vpc"                # Deployed VPC
subnet_name = "dev-subnet"             # Active subnet
```

### Current Security Configuration
```hcl
# Active WIF configuration
github_repository = "surajkmr39-lang/GCP-Terraform"  # Configured repository
workload_identity_pool = "github-pool"                # Active pool
service_account = "dev-vm-sa@praxis-gear-483220-k4.iam.gserviceaccount.com"
```

### Customization Options
To modify the deployment, update `terraform.tfvars` and run:
```bash
terraform plan    # Review changes
terraform apply   # Apply modifications
```

## 📊 Monitoring & Maintenance - ACTIVE DEPLOYMENT

### Current Health Status ✅
- ✅ **VM Instance**: `dev-vm` running at `34.173.115.82`
- ✅ **Network Connectivity**: VPC and subnet operational
- ✅ **Service Account**: Active with proper permissions
- ✅ **Workload Identity**: `github-pool` configured and ready
- ✅ **Firewall Rules**: 4 rules active and protecting resources
- ✅ **State Management**: 15 resources tracked in local state

### Monitoring Commands
```bash
# Check resource status
terraform state list                    # List all managed resources
terraform output                        # Show current resource details
gcloud compute instances list           # Verify VM status
gcloud iam service-accounts list        # Check service accounts

# Validate WIF setup
.\Check-WIF-Status.ps1                 # PowerShell validation script
```

### Maintenance Tasks
- **Daily**: Monitor resource status via GCP Console
- **Weekly**: Review costs and usage in GCP Billing
- **Monthly**: Security updates and patches via SSH
- **Quarterly**: Infrastructure and security audit

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow Terraform best practices
- Update documentation for any changes
- Test in development environment first
- Use conventional commit messages

## 📚 Documentation - COMPREHENSIVE GUIDES

### 📖 Core Documentation
- **[README.md](README.md)** - This comprehensive project overview
- **[DEPLOYMENT-STATUS-SUMMARY.md](info/DEPLOYMENT-STATUS-SUMMARY.md)** - Current deployment status and live resource details
- **[TERRAFORM-STATE-COMMANDS.md](info/TERRAFORM-STATE-COMMANDS.md)** - Complete guide to Terraform state management
- **[TERRAFORM-STATE-STORAGE-EXPLAINED.md](info/TERRAFORM-STATE-STORAGE-EXPLAINED.md)** - State storage options explained

### 🎯 Interview Preparation (Complete Series)
- **[INTERVIEW-MASTER-GUIDE.md](info/INTERVIEW-MASTER-GUIDE.md)** - Master guide with all interview materials
- **[INTERVIEW-GUIDE-PART1-CONCEPTS.md](info/INTERVIEW-GUIDE-PART1-CONCEPTS.md)** - Terraform concepts and theory
- **[INTERVIEW-GUIDE-PART2-CODE-WALKTHROUGH.md](info/INTERVIEW-GUIDE-PART2-CODE-WALKTHROUGH.md)** - Detailed code explanation
- **[INTERVIEW-GUIDE-PART3-ADVANCED-QUESTIONS.md](info/INTERVIEW-GUIDE-PART3-ADVANCED-QUESTIONS.md)** - Advanced technical questions
- **[INTERVIEW-GUIDE-PART4-SCENARIO-QUESTIONS.md](info/INTERVIEW-GUIDE-PART4-SCENARIO-QUESTIONS.md)** - Real-world scenarios
- **[INTERVIEW-GUIDE-PART5-PROJECT-DEMO.md](info/INTERVIEW-GUIDE-PART5-PROJECT-DEMO.md)** - Project demonstration script
- **[INTERVIEW-GUIDE-PART6-QUICK-REFERENCE.md](info/INTERVIEW-GUIDE-PART6-QUICK-REFERENCE.md)** - Quick reference guide

### 🔧 Technical Guides
- **[GIT-COMMANDS-EXPLAINED.md](info/GIT-COMMANDS-EXPLAINED.md)** - Git commands with explanations
- **[GIT-INTERVIEW-COMMANDS.md](info/GIT-INTERVIEW-COMMANDS.md)** - Git commands for interviews
- **[STRING-INTERPOLATION-EXPLAINED.md](info/STRING-INTERPOLATION-EXPLAINED.md)** - Terraform string interpolation
- **[CICD-PIPELINE-GUIDE.md](info/CICD-PIPELINE-GUIDE.md)** - CI/CD pipeline documentation
- **[WIF-QUICK-REFERENCE.md](info/WIF-QUICK-REFERENCE.md)** - Workload Identity Federation guide

### 🧪 Hands-on Labs
- **[Labs Overview](labs/README.md)** - 5-phase authentication lab series
- **Phase 1**: Application Default Credentials (ADC)
- **Phase 2**: Service Account Keys
- **Phase 3**: Service Account Impersonation  
- **Phase 4**: Workload Identity Federation
- **Phase 5**: GitHub Actions with WIF

## 🐛 Troubleshooting - RESOLVED ISSUES

### ✅ Previously Resolved Issues

**✅ Terraform Init Fails**
```bash
# SOLUTION: Clean and reinitialize
rm -rf .terraform/
terraform init
```

**✅ Authentication Issues (OAuth2 Invalid Grant)**
```bash
# SOLUTION: Refresh ADC credentials
gcloud auth application-default login
```

**✅ WIF Pool Already Exists**
```bash
# SOLUTION: Updated code to use existing github-pool
# Modified modules/iam/main.tf to reference existing resources
```

**✅ Billing Not Enabled**
```bash
# SOLUTION: Enabled billing in GCP Console
# URL: https://console.developers.google.com/billing/enable?project=praxis-gear-483220-k4
```

### Current Status Verification
```bash
# Verify everything is working
terraform state list        # Should show 15 resources
terraform output            # Should show live resource details
.\Check-WIF-Status.ps1      # Should confirm WIF is working
```

### Common Commands for Issues
```bash
# Check API status
gcloud services list --enabled

# Verify authentication
gcloud auth list
gcloud config list

# Check resource status
gcloud compute instances list
gcloud iam service-accounts list
```

## 📞 Support & Resources

- **🐛 Issues**: [GitHub Issues](https://github.com/surajkmr39-lang/GCP-Terraform/issues)
- **💬 Discussions**: [GitHub Discussions](https://github.com/surajkmr39-lang/GCP-Terraform/discussions)
- **📧 Email**: surajkmr39.lang@gmail.com
- **🔗 Repository**: https://github.com/surajkmr39-lang/GCP-Terraform

### 📈 Project Stats
- **✅ Status**: Fully Deployed & Operational
- **📊 Resources**: 15 GCP resources managed
- **💾 State**: Local state with workspace separation
- **🔐 Security**: Enterprise-grade with WIF
- **📚 Documentation**: 20+ comprehensive guides
- **🧪 Labs**: 5-phase authentication practice series

---

**🎯 Created by**: Suraj Kumar  
**📅 Last Updated**: January 2026  
**⭐ If this project helped you, please give it a star!**

**🚀 Infrastructure as Code | 🔐 Security First | 💰 Cost Optimized | ✅ Production Ready**