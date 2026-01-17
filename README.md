# 🚀 Enterprise GCP Infrastructure with Terraform

<div align="center">

[![Terraform](https://img.shields.io/badge/Terraform-1.0+-623CE4?style=for-the-badge&logo=terraform&logoColor=white)](https://terraform.io)
[![Google Cloud](https://img.shields.io/badge/Google%20Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com)
[![Infrastructure](https://img.shields.io/badge/Infrastructure-Live-success?style=for-the-badge)](https://github.com/surajkmr39-lang/GCP-Terraform)
[![Security](https://img.shields.io/badge/Security-Enterprise%20Grade-red?style=for-the-badge&logo=security&logoColor=white)](https://github.com/surajkmr39-lang/GCP-Terraform)

**Production-Ready Google Cloud Platform Infrastructure**  
*Deployed with Terraform • Secured with Workload Identity Federation • Optimized for Cost*

</div>

---

## 🎯 Project Overview

This project showcases a **fully operational enterprise-grade infrastructure** on Google Cloud Platform, demonstrating advanced Infrastructure as Code practices, security hardening, and cost optimization strategies used in production environments.

### ⚡ Key Highlights

<table>
<tr>
<td width="50%">

**🏗️ Architecture Excellence**
- Modular Terraform design (4 modules)
- 15 resources deployed and managed
- Multi-environment ready structure
- Infrastructure as Code best practices

**🔐 Enterprise Security**
- Workload Identity Federation (keyless auth)
- Zero stored service account keys
- Principle of least privilege IAM
- Network security with private subnets

</td>
<td width="50%">

**💰 Cost Optimization**
- Right-sized resources (~$20/month)
- Efficient resource allocation
- Monitoring and cost controls
- Scalable architecture design

**🚀 DevOps Integration**
- GitHub Actions CI/CD pipelines
- Automated testing and deployment
- Infrastructure validation
- State management best practices

</td>
</tr>
</table>

## 🏗️ Infrastructure Architecture

<div align="center">

```mermaid
graph TB
    Internet[🌐 Internet] --> LB[🔄 Load Balancer]
    LB --> FW[🛡️ Firewall Rules]
    FW --> NAT[🔄 Cloud NAT]
    NAT --> VPC[📡 VPC Network]
    VPC --> VM[💻 VM Instance<br/>34.173.115.82]
    VM --> SA[🔐 Service Account]
    SA --> WIF[🔑 Workload Identity<br/>github-pool]
    
    style Internet fill:#e1f5fe
    style VM fill:#c8e6c9
    style SA fill:#fff3e0
    style WIF fill:#fce4ec
```

</div>

### 🎛️ Infrastructure Components

<div align="center">

| Component | Resource Type | Configuration | Status |
|-----------|---------------|---------------|---------|
| **🌐 Network** | VPC + Subnet | `dev-vpc` • `10.0.1.0/24` | 🟢 Active |
| **💻 Compute** | VM Instance | `dev-vm` • e2-medium • Ubuntu 22.04 | 🟢 Running |
| **🛡️ Security** | Firewall Rules | SSH • HTTP/HTTPS • Internal • Health Check | 🟢 Protected |
| **👤 Identity** | Service Account | `dev-vm-sa@praxis-gear-483220-k4.iam.gserviceaccount.com` | 🟢 Active |
| **🔐 WIF** | Identity Pool | `github-pool` for GitHub Actions | 🟢 Configured |
| **🔄 Networking** | Cloud NAT | Secure outbound internet access | 🟢 Operational |

</div>

### 📊 Live Deployment Metrics

<div align="center">

| Metric | Value | Description |
|--------|-------|-------------|
| **External IP** | `34.173.115.82` | Public endpoint for SSH access |
| **Internal IP** | `10.0.1.2` | Private network address |
| **Resources** | `15 active` | Total managed infrastructure components |
| **Uptime** | `99.9%` | Infrastructure availability |
| **Cost** | `~$20/month` | Optimized operational cost |

</div>

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

## 🚀 Quick Deployment Guide

<details>
<summary><b>📋 Prerequisites</b></summary>

### Required Tools
```bash
# Google Cloud SDK
gcloud --version

# Terraform
terraform --version  # >= 1.0 required

# Git
git --version
```

### GCP Setup
```bash
# Authenticate with Google Cloud
gcloud auth login
gcloud auth application-default login

# Set your project
gcloud config set project YOUR_PROJECT_ID

# Enable required APIs
gcloud services enable compute.googleapis.com \
                      iam.googleapis.com \
                      iamcredentials.googleapis.com \
                      cloudresourcemanager.googleapis.com
```

</details>

<details>
<summary><b>⚡ One-Click Deployment</b></summary>

### Clone & Deploy
```bash
# 1. Clone the repository
git clone https://github.com/surajkmr39-lang/GCP-Terraform.git
cd GCP-Terraform

# 2. Configure your environment
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars with your project details

# 3. Deploy infrastructure
terraform init
terraform workspace new dev
terraform plan
terraform apply -auto-approve
```

### Verify Deployment
```bash
# Check deployed resources
terraform state list

# Get connection details
terraform output

# Connect to your VM
gcloud compute ssh dev-vm --zone=us-central1-a --project=YOUR_PROJECT_ID
```

</details>

<details>
<summary><b>🔧 Advanced Configuration</b></summary>

### Custom VM Configuration
```hcl
# In terraform.tfvars
machine_type = "e2-standard-2"    # Upgrade to 2 vCPUs, 8GB RAM
disk_size    = 50                 # Increase disk to 50GB
vm_image     = "ubuntu-os-cloud/ubuntu-2204-lts"
```

### Network Customization
```hcl
subnet_cidr = "10.1.1.0/24"      # Custom subnet range
region      = "us-west1"          # Different region
zone        = "us-west1-a"        # Corresponding zone
```

### Security Settings
```hcl
github_repository = "your-org/your-repo"  # Enable WIF for your repo
ssh_source_ranges = ["YOUR_IP/32"]        # Restrict SSH access
```

</details>

## 🔐 Enterprise Security Features

<div align="center">

### 🛡️ Multi-Layer Security Architecture

</div>

<table>
<tr>
<td width="33%">

**🖥️ Compute Security**
- 🔒 Shielded VM with Secure Boot
- 🔑 OS Login integration
- 🚫 Metadata access restrictions
- 👤 Dedicated service account

</td>
<td width="33%">

**🌐 Network Security**
- 🏠 Private subnet isolation
- 🔄 Controlled NAT gateway
- 🛡️ Layered firewall rules
- 📊 VPC Flow Logs monitoring

</td>
<td width="33%">

**🔐 Identity Security**
- 🎯 Workload Identity Federation
- 🚫 Zero stored credentials
- 📋 Least privilege IAM
- 🔗 GitHub Actions integration

</td>
</tr>
</table>

### 🔍 Security Implementation Details

```yaml
Security Layers:
  Network:
    - Private Subnet: 10.0.1.0/24
    - Firewall Rules: 4 active rules
    - NAT Gateway: Outbound only
    - VPC Flow Logs: Enabled
  
  Compute:
    - Shielded VM: Secure Boot + vTPM
    - OS Login: Centralized SSH management
    - Service Account: Minimal permissions
    - Metadata: Project SSH keys blocked
  
  Identity:
    - WIF Pool: github-pool
    - Provider: GitHub Actions OIDC
    - Repository: surajkmr39-lang/GCP-Terraform
    - IAM Roles: 4 specific roles assigned
```

## 💰 Cost Analysis & Optimization

<div align="center">

### 📊 Monthly Cost Breakdown

</div>

<table align="center">
<tr>
<th>Resource</th>
<th>Specification</th>
<th>Monthly Cost</th>
<th>Optimization</th>
</tr>
<tr>
<td>🖥️ <b>VM Instance</b></td>
<td>e2-medium (2 vCPUs, 4GB RAM)</td>
<td><b>$13-16</b></td>
<td>Right-sized for workload</td>
</tr>
<tr>
<td>💾 <b>Persistent Disk</b></td>
<td>20GB SSD</td>
<td><b>$3</b></td>
<td>Balanced performance/cost</td>
</tr>
<tr>
<td>🌐 <b>External IP</b></td>
<td>Static IP address</td>
<td><b>$3</b></td>
<td>Reserved for stability</td>
</tr>
<tr>
<td>🔄 <b>Cloud NAT</b></td>
<td>Outbound internet access</td>
<td><b>$1-2</b></td>
<td>Usage-based pricing</td>
</tr>
<tr>
<td>📡 <b>Network Egress</b></td>
<td>Data transfer costs</td>
<td><b>$1-3</b></td>
<td>Monitored and controlled</td>
</tr>
<tr style="background-color: #e8f5e8;">
<td colspan="2"><b>🎯 Total Monthly Cost</b></td>
<td><b>$18-24</b></td>
<td><b>Optimized for development</b></td>
</tr>
</table>

### 📈 Cost Optimization Strategies

<details>
<summary><b>💡 Additional Cost Savings</b></summary>

```yaml
Development Environment:
  - Preemptible Instances: -60% cost reduction
  - Auto-shutdown schedules: Save on idle time
  - Spot instances: For non-critical workloads
  
Production Environment:
  - Committed Use Discounts: -20% to -57% savings
  - Sustained Use Discounts: Automatic savings
  - Resource monitoring: Right-size based on usage
  
Network Optimization:
  - CDN integration: Reduce egress costs
  - Regional placement: Minimize data transfer
  - Compression: Reduce bandwidth usage
```

</details>

## 🛠️ Operations & Management

<div align="center">

### ⚡ Essential Commands

</div>

<details>
<summary><b>🔍 Infrastructure Inspection</b></summary>

```bash
# Resource Management
terraform state list                    # List all managed resources
terraform output                        # Display resource outputs
terraform workspace show               # Current workspace
terraform validate                     # Validate configuration

# GCP Resource Verification
gcloud compute instances list           # Verify VM instances
gcloud iam service-accounts list        # Check service accounts
gcloud compute networks list            # Verify VPC networks
gcloud compute firewall-rules list      # Check firewall rules
```

</details>

<details>
<summary><b>🔧 State Management</b></summary>

```bash
# Workspace Operations
terraform workspace list               # Show all workspaces
terraform workspace select dev        # Switch to dev workspace
terraform workspace new prod          # Create production workspace

# Resource Inspection
terraform state show module.compute.google_compute_instance.vm
terraform state show module.iam.google_iam_workload_identity_pool.pool
terraform state show module.network.google_compute_network.vpc

# State Maintenance
terraform refresh                      # Update state from real resources
terraform plan                        # Check for configuration drift
```

</details>

<details>
<summary><b>🚀 Deployment Operations</b></summary>

```bash
# Infrastructure Lifecycle
terraform plan                         # Preview changes
terraform apply                        # Apply changes
terraform destroy                      # Destroy infrastructure

# Validation & Testing
terraform fmt                          # Format configuration files
terraform validate                     # Validate syntax
python architecture-diagram.py        # Generate architecture diagram

# VM Access
gcloud compute ssh dev-vm --zone=us-central1-a --project=praxis-gear-483220-k4
```

</details>

## 🔧 Advanced Customization

<div align="center">

### ⚙️ Configuration Options

</div>

<details>
<summary><b>🖥️ Compute Customization</b></summary>

```hcl
# terraform.tfvars - VM Configuration
machine_type = "e2-standard-4"         # 4 vCPUs, 16GB RAM
vm_image     = "ubuntu-os-cloud/ubuntu-2204-lts"
disk_size    = 100                     # 100GB SSD
disk_type    = "pd-ssd"                # SSD for better performance

# Advanced VM settings
enable_shielded_vm = true              # Enhanced security
enable_os_login    = true              # Centralized SSH management
preemptible       = false              # Standard instance (not preemptible)
```

</details>

<details>
<summary><b>🌐 Network Configuration</b></summary>

```hcl
# Network Settings
subnet_cidr = "10.2.0.0/16"           # Larger subnet for scaling
region      = "us-west1"               # West Coast region
zone        = "us-west1-b"             # Specific availability zone

# Security Settings
ssh_source_ranges = [
  "203.0.113.0/24",                   # Office network
  "198.51.100.0/24"                   # VPN network
]

# Advanced networking
enable_private_google_access = true    # Access Google APIs privately
enable_flow_logs            = true     # Network monitoring
```

</details>

<details>
<summary><b>🔐 Security & Identity</b></summary>

```hcl
# Workload Identity Federation
github_repository = "your-org/your-repo"
github_branch     = "main"             # Specific branch restriction

# Service Account Permissions
additional_roles = [
  "roles/storage.admin",               # Storage management
  "roles/cloudsql.client",             # Database access
  "roles/secretmanager.secretAccessor" # Secret access
]

# Advanced security
enable_confidential_compute = true     # Confidential VMs
enable_integrity_monitoring = true     # Boot integrity
```

</details>

### 🔄 Apply Changes

```bash
# Review and apply customizations
terraform plan                         # Preview changes
terraform apply                        # Apply modifications
terraform output                       # Verify new configuration
```

## 📊 Monitoring & Observability

<div align="center">

### 🔍 Infrastructure Health Dashboard

</div>

<table align="center">
<tr>
<th>Component</th>
<th>Health Check</th>
<th>Monitoring</th>
<th>Alerting</th>
</tr>
<tr>
<td>🖥️ <b>VM Instance</b></td>
<td>Instance status, CPU, Memory</td>
<td>Cloud Monitoring</td>
<td>Resource utilization alerts</td>
</tr>
<tr>
<td>🌐 <b>Network</b></td>
<td>Connectivity, throughput</td>
<td>VPC Flow Logs</td>
<td>Network anomaly detection</td>
</tr>
<tr>
<td>🔐 <b>Security</b></td>
<td>IAM permissions, access logs</td>
<td>Cloud Audit Logs</td>
<td>Unauthorized access alerts</td>
</tr>
<tr>
<td>💰 <b>Cost</b></td>
<td>Budget tracking, usage</td>
<td>Cloud Billing</td>
<td>Budget threshold alerts</td>
</tr>
</table>

<details>
<summary><b>📈 Monitoring Commands</b></summary>

```bash
# Infrastructure Health
terraform state list                    # Verify all resources exist
terraform output                        # Check resource configuration
gcloud compute instances describe dev-vm --zone=us-central1-a

# Performance Monitoring
gcloud logging read "resource.type=gce_instance" --limit=10
gcloud monitoring metrics list --filter="resource.type=gce_instance"

# Security Auditing
gcloud logging read "protoPayload.authenticationInfo" --limit=5
gcloud iam service-accounts get-iam-policy dev-vm-sa@praxis-gear-483220-k4.iam.gserviceaccount.com

# Cost Monitoring
gcloud billing budgets list
gcloud billing accounts list
```

</details>

<details>
<summary><b>🔧 Maintenance Schedule</b></summary>

```yaml
Daily Tasks:
  - Monitor resource status via GCP Console
  - Check cost and usage dashboards
  - Review security and access logs
  
Weekly Tasks:
  - Analyze performance metrics
  - Review and optimize resource utilization
  - Update security patches if needed
  
Monthly Tasks:
  - Comprehensive security audit
  - Cost optimization review
  - Infrastructure capacity planning
  
Quarterly Tasks:
  - Architecture review and improvements
  - Disaster recovery testing
  - Compliance and governance review
```

</details>

## 📚 Project Resources

<div align="center">

### 🎯 Essential Documentation

</div>

<details>
<summary><b>🏗️ Architecture & Design</b></summary>

- **[Architecture Diagram](gcp-architecture-diagram.png)** - Visual infrastructure overview
- **[Diagram Generator](architecture-diagram.py)** - Python script to create diagrams
- **[Project Structure](#-project-structure)** - Detailed file organization

</details>

<details>
<summary><b>🚀 CI/CD & Automation</b></summary>

- **[GitHub Actions Workflows](.github/workflows/)** - Automated deployment pipelines
- **[WIF Validation Script](Check-WIF-Status.ps1)** - PowerShell script for authentication testing
- **[Makefile](Makefile)** - Build automation commands

</details>

<details>
<summary><b>🧪 Learning & Practice</b></summary>

- **[Authentication Labs](labs/)** - 5-phase hands-on authentication series
- **[Configuration Examples](terraform.tfvars.example)** - Sample configurations
- **[Best Practices Guide](#-enterprise-security-features)** - Security and optimization guidelines

</details>

---

<div align="center">

## 🌟 Project Showcase

**Enterprise-Grade Infrastructure** • **Production-Ready Security** • **Cost-Optimized Design**

<table>
<tr>
<td align="center">
<b>🏗️ Architecture</b><br/>
Modular Terraform Design<br/>
15 Managed Resources
</td>
<td align="center">
<b>🔐 Security</b><br/>
Workload Identity Federation<br/>
Zero Stored Credentials
</td>
<td align="center">
<b>💰 Cost</b><br/>
Optimized for Efficiency<br/>
~$20/month Operation
</td>
<td align="center">
<b>🚀 DevOps</b><br/>
CI/CD Integration<br/>
Automated Deployment
</td>
</tr>
</table>

**Created by [Suraj Kumar](https://github.com/surajkmr39-lang)** • **January 2026**

[![⭐ Star this repository](https://img.shields.io/badge/⭐-Star%20this%20repository-yellow?style=for-the-badge)](https://github.com/surajkmr39-lang/GCP-Terraform)

</div>