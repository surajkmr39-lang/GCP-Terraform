# 🚀 GCP Infrastructure with Terraform

[![Terraform](https://img.shields.io/badge/Terraform-1.0+-623CE4?logo=terraform&logoColor=white)](https://terraform.io)
[![Google Cloud](https://img.shields.io/badge/Google%20Cloud-4285F4?logo=google-cloud&logoColor=white)](https://cloud.google.com)
[![Deployed](https://img.shields.io/badge/Status-Deployed-success)](https://github.com/surajkmr39-lang/GCP-Terraform)

**Enterprise-grade Google Cloud Platform infrastructure deployed using Terraform with modular architecture, security hardening, and workload identity federation.**

**Author**: Suraj Kumar  
**Project**: praxis-gear-483220-k4  
**Environment**: Development (Active)

## 📋 Project Overview

This project demonstrates a fully deployed and operational secure, scalable development environment on Google Cloud Platform using Infrastructure as Code principles. The implementation follows enterprise best practices with comprehensive security features and cost optimization.

### 🎯 Key Features

- **Modular Architecture**: 4 reusable Terraform modules (15 resources deployed)
- **Security First**: Shielded VMs, Workload Identity Federation, VPC security
- **Cost Optimized**: ~$18-24/month for complete environment
- **Enterprise Ready**: Compliance with security standards
- **CI/CD Integration**: GitHub Actions with Workload Identity Federation
- **State Management**: Local state with workspace separation

## 🏗️ Architecture

```
🌐 Internet → 🛡️ Firewall → 🔄 Cloud NAT → 📡 VPC → 💻 VM Instance (34.173.115.82)
                                                    ↓
                              🔐 Service Account ← 🔑 Workload Identity (github-pool)
```

### Infrastructure Components (15 Resources Active)

| Component | Resource | Configuration | Status |
|-----------|----------|---------------|---------|
| **Network** | VPC + Subnet | `dev-vpc` with `10.0.1.0/24` | ✅ Active |
| **Compute** | VM Instance | `dev-vm` (e2-medium) Ubuntu 22.04 | ✅ Running |
| **Security** | Firewall Rules | SSH, HTTP/HTTPS, Internal, Health Check | ✅ Active |
| **Identity** | Service Account | `dev-vm-sa@praxis-gear-483220-k4.iam.gserviceaccount.com` | ✅ Active |
| **WIF** | Identity Pool | `github-pool` for GitHub Actions | ✅ Configured |
| **Networking** | Cloud NAT | Secure outbound internet access | ✅ Active |

### Live Resource Details
- **VM External IP**: `34.173.115.82`
- **VM Internal IP**: `10.0.1.2`
- **SSH Command**: `gcloud compute ssh dev-vm --zone=us-central1-a --project=praxis-gear-483220-k4`

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

## 🚀 Quick Start

### Prerequisites

1. **Google Cloud SDK**
   ```bash
   gcloud auth login
   gcloud config set project your-project-id
   ```

2. **Terraform >= 1.0**
   ```bash
   terraform --version
   ```

3. **Required APIs**
   ```bash
   gcloud services enable compute.googleapis.com
   gcloud services enable iam.googleapis.com
   gcloud services enable iamcredentials.googleapis.com
   gcloud services enable cloudresourcemanager.googleapis.com
   ```

### Deployment

1. **Clone Repository**
   ```bash
   git clone https://github.com/surajkmr39-lang/GCP-Terraform.git
   cd GCP-Terraform
   ```

2. **Configure Environment**
   ```bash
   cp terraform.tfvars.example terraform.tfvars
   # Edit terraform.tfvars with your project details
   ```

3. **Deploy Infrastructure**
   ```bash
   terraform init
   terraform workspace new dev
   terraform plan
   terraform apply
   ```

4. **Verify Deployment**
   ```bash
   terraform state list    # List all resources
   terraform output        # Show resource details
   ```

## 🔐 Security Features

### VM Security
- **Shielded VM**: Secure boot, vTPM, integrity monitoring
- **OS Login**: Centralized SSH key management
- **Metadata Security**: Block project SSH keys
- **Service Account**: Minimal required permissions

### Network Security
- **Private Subnet**: No direct internet access
- **Cloud NAT**: Controlled outbound access
- **Firewall Rules**: Least privilege access
- **VPC Flow Logs**: Network monitoring

### Identity Security
- **Workload Identity**: No stored service account keys
- **IAM Roles**: Principle of least privilege
- **GitHub Integration**: Secure CI/CD authentication

## 💰 Cost Analysis

| Resource | Monthly Cost | 
|----------|-------------|
| VM Instance (e2-medium) | $13-16 |
| Persistent Disk (20GB SSD) | $3 |
| External IP | $3 |
| Cloud NAT | $1-2 |
| Network Egress | $1-3 |
| **Total** | **$18-24/month** |

### Cost Optimization
- Use preemptible instances for dev (-60% cost)
- Implement auto-shutdown schedules
- Monitor network egress usage
- Use committed use discounts for production

## 🛠️ Usage Examples

### Infrastructure Management
```bash
# Check deployment status
terraform state list                    # List all deployed resources
terraform output                        # Show resource details
terraform workspace show               # Current workspace

# Validate configuration
terraform validate                      # Check syntax
terraform plan                         # Check for drift

# Access deployed VM
gcloud compute ssh dev-vm --zone=us-central1-a --project=praxis-gear-483220-k4
```

### State Management
```bash
# Workspace operations
terraform workspace list               # Show available workspaces
terraform workspace select dev        # Switch to dev workspace

# Resource inspection
terraform state show module.compute.google_compute_instance.vm
terraform state show module.iam.google_iam_workload_identity_pool.pool
```

### Environment Operations
```bash
# Development environment
terraform plan                         # Plan changes
terraform apply                        # Apply changes
terraform destroy                      # Destroy infrastructure (if needed)

# Generate architecture diagram
python architecture-diagram.py        # Creates visual diagram
```

## 🔧 Customization

### VM Configuration
Edit `terraform.tfvars`:
```hcl
machine_type = "e2-standard-2"         # Upgrade VM size
vm_image     = "ubuntu-os-cloud/ubuntu-2204-lts"
disk_size    = 50                      # Increase disk size
```

### Network Configuration
```hcl
subnet_cidr = "10.1.1.0/24"           # Change subnet range
region      = "us-west1"               # Different region
zone        = "us-west1-a"             # Different zone
```

### Security Configuration
```hcl
github_repository = "your-org/your-repo"  # Enable workload identity
ssh_source_ranges = ["YOUR_IP/32"]        # Restrict SSH access
```

### Apply Changes
```bash
terraform plan    # Review changes
terraform apply   # Apply modifications
```

## 📊 Monitoring & Maintenance

### Health Checks
- VM instance status and performance
- Network connectivity and throughput
- Service account permissions audit
- Cost and usage monitoring

### Monitoring Commands
```bash
# Check resource status
terraform state list                    # List managed resources
terraform output                        # Show resource details
gcloud compute instances list           # Verify VM status
gcloud iam service-accounts list        # Check service accounts
```

### Maintenance Tasks
- **Daily**: Monitor resource status via GCP Console
- **Weekly**: Review costs and usage in GCP Billing
- **Monthly**: Security updates and patches
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

## 📚 Documentation

### Core Documentation
- **[Project Structure](info/PROJECT-STRUCTURE.md)** - Detailed project organization
- **[Deployment Guide](info/DEPLOYMENT-STATUS-SUMMARY.md)** - Current deployment status
- **[State Management](info/TERRAFORM-STATE-COMMANDS.md)** - Terraform state operations
- **[Authentication Labs](labs/README.md)** - 5-phase authentication practice series

### Technical Guides
- **[CI/CD Pipeline](info/CICD-PIPELINE-GUIDE.md)** - GitHub Actions workflows
- **[Workload Identity](info/WIF-QUICK-REFERENCE.md)** - WIF setup and configuration
- **[Git Commands](info/GIT-COMMANDS-EXPLAINED.md)** - Git operations reference

### Architecture
- **[Architecture Diagram](gcp-architecture-diagram.png)** - Visual infrastructure overview
- **[Diagram Generator](architecture-diagram.py)** - Python script to generate diagrams

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

## 🐛 Troubleshooting

### Common Issues

**Terraform Init Fails**
```bash
rm -rf .terraform/
terraform init
```

**Authentication Issues**
```bash
gcloud auth list
gcloud auth application-default login
```

**API Not Enabled**
```bash
gcloud services enable compute.googleapis.com
gcloud services enable iam.googleapis.com
```

**SSH Connection Issues**
```bash
gcloud compute firewall-rules list
gcloud compute instances list
```

### Verification Commands
```bash
# Verify deployment
terraform state list        # Should show all resources
terraform output            # Should show resource details
terraform validate          # Check configuration
```

## 📞 Support & Contact

- **Repository**: https://github.com/surajkmr39-lang/GCP-Terraform
- **Issues**: [GitHub Issues](https://github.com/surajkmr39-lang/GCP-Terraform/issues)
- **Author**: Suraj Kumar
- **Email**: surajkmr39.lang@gmail.com

### Project Stats
- **Status**: Fully Deployed & Operational
- **Resources**: 15 GCP resources managed
- **Architecture**: Modular Terraform design
- **Security**: Enterprise-grade with WIF
- **Cost**: ~$18-24/month

---

**Created by**: Suraj Kumar  
**Last Updated**: January 2026  

**🚀 Infrastructure as Code | 🔐 Security First | 💰 Cost Optimized**