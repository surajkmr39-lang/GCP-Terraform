# 📋 GCP Infrastructure Deployment Checklist

**Author**: Suraj Kumar  
**Project**: praxis-gear-483220-k4  
**Environment**: Development  
**Date**: January 2026

## 🎯 Project Information
- **Project ID**: `praxis-gear-483220-k4`
- **Environment**: Development
- **Region**: `us-central1`
- **Deployment Method**: Terraform Infrastructure as Code

---

## ✅ Pre-Deployment Checklist

### 🔧 Prerequisites Setup
- [ ] **Google Cloud SDK Installed**
  ```bash
  gcloud --version
  ```
- [ ] **Terraform Installed** (>= 1.0)
  ```bash
  terraform --version
  ```
- [ ] **Project Access Verified**
  ```bash
  gcloud auth login
  gcloud config set project praxis-gear-483220-k4
  ```
- [ ] **Billing Account Enabled**
  - Verify billing is active in GCP Console
  - Check billing alerts are configured

### 🔌 API Enablement
- [ ] **Compute Engine API**
  ```bash
  gcloud services enable compute.googleapis.com
  ```
- [ ] **Identity and Access Management (IAM) API**
  ```bash
  gcloud services enable iam.googleapis.com
  ```
- [ ] **IAM Service Account Credentials API**
  ```bash
  gcloud services enable iamcredentials.googleapis.com
  ```
- [ ] **Cloud Resource Manager API**
  ```bash
  gcloud services enable cloudresourcemanager.googleapis.com
  ```

### 🔐 Security & Access
- [ ] **SSH Key Generated**
  ```bash
  ssh-keygen -t rsa -b 4096 -C "suraj@praxis-gear-483220-k4"
  ```
- [ ] **SSH Key Added to Configuration**
  - Public key copied to `terraform.tfvars`
  - Key format verified (starts with `ssh-rsa`)
- [ ] **IAM Permissions Verified**
  - Editor or Owner role on project
  - Service Account Admin role (if needed)

---

## 🏗️ Deployment Execution Checklist

### 📁 Project Structure Verification
- [ ] **Root Module Files Present**
  - [ ] `main.tf` - Root orchestration
  - [ ] `variables.tf` - Variable definitions
  - [ ] `outputs.tf` - Output definitions
- [ ] **Module Structure Complete**
  - [ ] `modules/network/` - VPC and networking
  - [ ] `modules/security/` - Firewall rules
  - [ ] `modules/iam/` - Service accounts and identity
  - [ ] `modules/compute/` - VM instances
- [ ] **Environment Configuration**
  - [ ] `environments/dev/terraform.tfvars` - Dev settings
  - [ ] Project ID correctly set
  - [ ] SSH key properly configured

### 🚀 Terraform Deployment Steps

#### Step 1: Initialize Terraform
- [ ] **Run Initialization**
  ```bash
  terraform init
  ```
- [ ] **Verify Success**
  - [ ] Providers downloaded successfully
  - [ ] Modules initialized
  - [ ] `.terraform/` directory created
  - [ ] Lock file created

#### Step 2: Create Workspace
- [ ] **Create Dev Workspace**
  ```bash
  terraform workspace new dev
  ```
- [ ] **Verify Workspace**
  ```bash
  terraform workspace list
  ```

#### Step 3: Plan Deployment
- [ ] **Generate Plan**
  ```bash
  terraform plan -var-file="environments/dev/terraform.tfvars"
  ```
- [ ] **Review Plan Output**
  - [ ] 15 resources to be created
  - [ ] No unexpected changes
  - [ ] Resource dependencies correct
  - [ ] Network configuration accurate

#### Step 4: Apply Infrastructure
- [ ] **Deploy Infrastructure**
  ```bash
  terraform apply -var-file="environments/dev/terraform.tfvars"
  ```
- [ ] **Monitor Deployment**
  - [ ] Network module deploys first
  - [ ] Security rules created
  - [ ] IAM resources configured
  - [ ] Compute instance launched

---

## 🔍 Post-Deployment Verification

### 🌐 Network Verification
- [ ] **VPC Network Created**
  - [ ] Name: `dev-vpc`
  - [ ] Mode: Custom (no auto-subnets)
- [ ] **Subnet Configuration**
  - [ ] Name: `dev-subnet`
  - [ ] CIDR: `10.0.1.0/24`
  - [ ] Region: `us-central1`
  - [ ] Private Google Access: Enabled
- [ ] **Cloud NAT & Router**
  - [ ] Router: `dev-router` created
  - [ ] NAT: `dev-nat` configured
  - [ ] Outbound internet access working

### 🔥 Security Verification
- [ ] **Firewall Rules Active**
  - [ ] SSH access (port 22) - `dev-allow-ssh`
  - [ ] HTTP/HTTPS (ports 80/443) - `dev-allow-http-https`
  - [ ] Internal communication - `dev-allow-internal`
  - [ ] Health checks - `dev-allow-health-check`
- [ ] **Network Tags Applied**
  - [ ] `ssh-allowed` on VM
  - [ ] `http-allowed` on VM
  - [ ] `health-check` on VM

### 🔐 IAM & Security Verification
- [ ] **Service Account Created**
  - [ ] Name: `dev-vm-sa`
  - [ ] Email: `dev-vm-sa@praxis-gear-483220-k4.iam.gserviceaccount.com`
- [ ] **IAM Bindings Applied**
  - [ ] Compute Viewer role
  - [ ] Storage Object Viewer role
  - [ ] Logging Writer role
  - [ ] Monitoring Metric Writer role
- [ ] **Workload Identity Pool**
  - [ ] Pool ID: `dev-pool`
  - [ ] GitHub provider configured (if applicable)

### 💻 Compute Verification
- [ ] **VM Instance Running**
  - [ ] Name: `dev-vm`
  - [ ] Machine type: `e2-medium`
  - [ ] Zone: `us-central1-a`
  - [ ] Status: RUNNING
- [ ] **Network Configuration**
  - [ ] Internal IP: `10.0.1.2`
  - [ ] External IP: `34.173.255.107`
  - [ ] Subnet: `dev-subnet`
- [ ] **Security Features**
  - [ ] Shielded VM enabled
  - [ ] Secure boot active
  - [ ] vTPM enabled
  - [ ] Integrity monitoring active
  - [ ] OS Login enabled

---

## 🧪 Connectivity Testing

### 🔌 SSH Connection Test
- [ ] **SSH via gcloud**
  ```bash
  gcloud compute ssh dev-vm --zone=us-central1-a --project=praxis-gear-483220-k4
  ```
- [ ] **Direct SSH Test**
  ```bash
  ssh -i ~/.ssh/id_rsa suraj@34.173.255.107
  ```
- [ ] **Connection Successful**
  - [ ] Login prompt appears
  - [ ] User authentication works
  - [ ] Shell access granted

### 🐳 Application Testing
- [ ] **Docker Functionality**
  ```bash
  sudo docker run hello-world
  ```
- [ ] **System Updates**
  ```bash
  sudo apt update && sudo apt upgrade -y
  ```
- [ ] **Network Connectivity**
  ```bash
  ping google.com
  curl -I https://www.google.com
  ```

---

## 📊 Resource Inventory Verification

### 📋 Created Resources Checklist
- [ ] **Network Resources (4)**
  - [ ] `google_compute_network.vpc`
  - [ ] `google_compute_subnetwork.subnet`
  - [ ] `google_compute_router.router`
  - [ ] `google_compute_router_nat.nat`

- [ ] **Security Resources (4)**
  - [ ] `google_compute_firewall.allow_ssh`
  - [ ] `google_compute_firewall.allow_http_https`
  - [ ] `google_compute_firewall.allow_internal`
  - [ ] `google_compute_firewall.allow_health_check`

- [ ] **IAM Resources (6)**
  - [ ] `google_service_account.vm_service_account`
  - [ ] `google_iam_workload_identity_pool.pool`
  - [ ] `google_project_iam_member.vm_sa_compute_viewer`
  - [ ] `google_project_iam_member.vm_sa_storage_viewer`
  - [ ] `google_project_iam_member.vm_sa_logging_writer`
  - [ ] `google_project_iam_member.vm_sa_monitoring_writer`

- [ ] **Compute Resources (1)**
  - [ ] `google_compute_instance.vm`

**Total Resources: 15** ✅

---

## 💰 Cost Monitoring Setup

### 📈 Budget Alerts
- [ ] **Monthly Budget Set**
  - [ ] Budget amount: $50/month
  - [ ] Alert thresholds: 50%, 90%, 100%
  - [ ] Email notifications configured

### 💸 Cost Optimization
- [ ] **Resource Labeling**
  - [ ] Environment: `dev`
  - [ ] Team: `praxis-gear`
  - [ ] Cost center: `development`
  - [ ] Managed by: `terraform`
- [ ] **Scheduled Shutdown** (Optional)
  - [ ] VM auto-shutdown configured
  - [ ] Development hours defined

---

## 🔄 Maintenance & Updates

### 📅 Regular Tasks
- [ ] **Weekly Security Updates**
  ```bash
  sudo apt update && sudo apt upgrade -y
  ```
- [ ] **Monthly Terraform Updates**
  ```bash
  terraform providers lock -upgrade
  ```
- [ ] **Quarterly Cost Review**
  - [ ] Analyze usage patterns
  - [ ] Optimize resource sizing
  - [ ] Review unused resources

### 📝 Documentation Updates
- [ ] **Infrastructure Changes Documented**
- [ ] **Runbook Updated**
- [ ] **Team Knowledge Shared**

---

## 🚨 Troubleshooting Checklist

### ❌ Common Issues & Solutions

#### Terraform Init Fails
- [ ] Check internet connectivity
- [ ] Verify Terraform version
- [ ] Clear `.terraform/` directory and retry

#### Plan/Apply Fails
- [ ] Verify GCP authentication
- [ ] Check API enablement
- [ ] Validate project permissions
- [ ] Review quota limits

#### SSH Connection Issues
- [ ] Verify firewall rules
- [ ] Check VM status
- [ ] Validate SSH key format
- [ ] Test network connectivity

#### Resource Creation Errors
- [ ] Check regional availability
- [ ] Verify resource quotas
- [ ] Review IAM permissions
- [ ] Validate resource naming

---

## ✅ Deployment Sign-off

### 👥 Stakeholder Approval
- [ ] **Technical Lead Review**: _________________ Date: _______
- [ ] **Security Team Approval**: _________________ Date: _______
- [ ] **Operations Team Handoff**: _________________ Date: _______

### 📋 Final Verification
- [ ] All checklist items completed
- [ ] Infrastructure fully functional
- [ ] Documentation updated
- [ ] Team trained on new environment
- [ ] Monitoring and alerting configured
- [ ] Backup and disaster recovery planned

---

**🎉 Deployment Status: COMPLETE**

*Infrastructure successfully deployed and verified on: _______________*

*Deployed by: _______________*

*Next review date: _______________*