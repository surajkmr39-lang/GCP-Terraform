# 🚀 GCP Migration Complete End-to-End Guide

**Author**: Suraj Kumar

## 📋 Table of Contents
1. [Migration Overview](#migration-overview)
2. [Pre-Migration Assessment](#pre-migration-assessment)
3. [Landing Zone Design](#landing-zone-design)
4. [Migration Phases](#migration-phases)
5. [Real-Time Use Cases](#real-time-use-cases)
6. [Post-Migration Steps](#post-migration-steps)
7. [Monitoring & Optimization](#monitoring--optimization)
8. [Troubleshooting](#troubleshooting)

---

## 🎯 Migration Overview

### What is GCP Migration?
GCP Migration is the process of moving applications, data, and infrastructure from on-premises or other cloud providers to Google Cloud Platform while ensuring minimal downtime, data integrity, and cost optimization.

### Migration Types
- **Lift and Shift (Rehost)**: Move as-is with minimal changes
- **Replatform**: Minor optimizations for cloud
- **Refactor**: Redesign for cloud-native architecture
- **Rebuild**: Complete rewrite using cloud services
- **Replace**: Switch to SaaS alternatives

### Key Success Factors
✅ Comprehensive assessment and planning  
✅ Proper landing zone setup  
✅ Phased migration approach  
✅ Continuous monitoring and optimization  
✅ Team training and change management  

---

## 🔍 Pre-Migration Assessment

### 1. Infrastructure Discovery

#### Current State Analysis
```bash
# Infrastructure inventory script
#!/bin/bash
echo "=== Infrastructure Discovery ==="
echo "Servers: $(nmap -sn 192.168.1.0/24 | grep -c "Nmap scan report")"
echo "Databases: $(netstat -tuln | grep -c ":3306\|:5432\|:1433")"
echo "Applications: $(ps aux | grep -c "java\|python\|node")"
echo "Storage: $(df -h | awk 'NR>1 {sum+=$2} END {print sum"GB"}')"
```

#### Application Portfolio Assessment
| Application | Criticality | Dependencies | Migration Strategy | Timeline |
|-------------|-------------|--------------|-------------------|----------|
| Web Frontend | High | Database, API | Replatform | Phase 1 |
| Database | Critical | All apps | Lift & Shift | Phase 1 |
| Analytics | Medium | Data warehouse | Refactor | Phase 2 |
| Legacy ERP | Low | File shares | Replace | Phase 3 |

### 2. Technical Assessment

#### Network Architecture Review
```yaml
# Current network mapping
current_network:
  on_premises:
    - subnet: "192.168.1.0/24"
      services: ["web", "app", "db"]
    - subnet: "192.168.2.0/24" 
      services: ["storage", "backup"]
  
  cloud_target:
    - region: "us-central1"
      vpc: "production-vpc"
      subnets:
        - "10.0.1.0/24"  # web tier
        - "10.0.2.0/24"  # app tier
        - "10.0.3.0/24"  # data tier
```

#### Security Assessment
```bash
# Security audit checklist
security_audit:
  - identity_management: "Active Directory integration"
  - access_controls: "RBAC implementation needed"
  - data_encryption: "At rest and in transit"
  - compliance: "SOC2, GDPR, HIPAA requirements"
  - network_security: "Firewall rules, VPN setup"
```

### 3. Cost Analysis

#### Current vs Target Cost Comparison
```python
# Cost calculation script
current_costs = {
    "servers": 15000,      # Monthly server costs
    "storage": 3000,       # Storage costs
    "network": 2000,       # Network/bandwidth
    "licenses": 8000,      # Software licenses
    "maintenance": 5000    # Support and maintenance
}

gcp_projected = {
    "compute": 8000,       # GCE instances
    "storage": 2000,       # Cloud Storage
    "network": 1500,       # VPC and egress
    "managed_services": 4000,  # Cloud SQL, etc.
    "support": 2000        # Google Cloud Support
}

savings = sum(current_costs.values()) - sum(gcp_projected.values())
print(f"Projected monthly savings: ${savings}")
```
---

## 🏗️ Landing Zone Design

### What is a Landing Zone?
A landing zone is a well-architected, multi-account GCP environment that provides a secure, scalable foundation for deploying workloads and applications.

### Core Components

#### 1. Organization Structure
```
Organization (company.com)
├── Security Folder
│   ├── Security Project (logging, monitoring)
│   └── Identity Project (IAM, groups)
├── Shared Services Folder
│   ├── Network Hub Project
│   └── DNS Project
├── Production Folder
│   ├── Prod App Project
│   └── Prod Data Project
├── Non-Production Folder
│   ├── Dev Project
│   ├── Test Project
│   └── Staging Project
└── Sandbox Folder
    └── Individual developer projects
```

#### 2. Network Architecture
```yaml
# Landing zone network design
network_architecture:
  hub_and_spoke:
    hub_vpc: "shared-vpc-hub"
    regions: ["us-central1", "us-east1"]
    
  spoke_vpcs:
    production:
      name: "prod-vpc"
      cidr: "10.0.0.0/16"
      subnets:
        - name: "prod-web"
          cidr: "10.0.1.0/24"
        - name: "prod-app" 
          cidr: "10.0.2.0/24"
        - name: "prod-data"
          cidr: "10.0.3.0/24"
    
    non_production:
      name: "nonprod-vpc"
      cidr: "10.1.0.0/16"
      subnets:
        - name: "dev-subnet"
          cidr: "10.1.1.0/24"
        - name: "test-subnet"
          cidr: "10.1.2.0/24"
```

#### 3. Security Framework
```bash
# Security baseline implementation
security_controls:
  - organization_policies: "Restrict public IPs, enforce encryption"
  - iam_hierarchy: "Principle of least privilege"
  - audit_logging: "All admin and data access"
  - network_security: "Private Google Access, Cloud NAT"
  - data_protection: "Customer-managed encryption keys"
```

### Landing Zone Terraform Implementation

#### Organization Setup
```hcl
# organization.tf
resource "google_folder" "security" {
  display_name = "Security"
  parent       = "organizations/${var.org_id}"
}

resource "google_folder" "shared_services" {
  display_name = "Shared Services"
  parent       = "organizations/${var.org_id}"
}

resource "google_folder" "production" {
  display_name = "Production"
  parent       = "organizations/${var.org_id}"
}

resource "google_folder" "non_production" {
  display_name = "Non-Production"
  parent       = "organizations/${var.org_id}"
}

# Organization policies
resource "google_org_policy_policy" "restrict_public_ips" {
  name   = "organizations/${var.org_id}/policies/compute.vmExternalIpAccess"
  parent = "organizations/${var.org_id}"

  spec {
    rules {
      deny_all = true
    }
  }
}
```

#### Network Hub Implementation
```hcl
# network-hub.tf
resource "google_compute_network" "hub_vpc" {
  name                    = "shared-vpc-hub"
  auto_create_subnetworks = false
  project                 = var.network_project_id
}

resource "google_compute_subnetwork" "hub_subnet" {
  name          = "hub-subnet"
  ip_cidr_range = "10.100.0.0/24"
  region        = var.region
  network       = google_compute_network.hub_vpc.id
  project       = var.network_project_id

  secondary_ip_range {
    range_name    = "gke-pods"
    ip_cidr_range = "10.101.0.0/16"
  }

  secondary_ip_range {
    range_name    = "gke-services"
    ip_cidr_range = "10.102.0.0/16"
  }
}

# VPC Peering for spoke networks
resource "google_compute_network_peering" "hub_to_prod" {
  name         = "hub-to-prod"
  network      = google_compute_network.hub_vpc.self_link
  peer_network = google_compute_network.prod_vpc.self_link
}
```

---

## 📅 Migration Phases

### Phase 1: Foundation (Weeks 1-4)

#### Week 1-2: Landing Zone Setup
```bash
# Landing zone deployment script
#!/bin/bash
echo "Deploying GCP Landing Zone..."

# 1. Create organization structure
gcloud organizations add-iam-policy-binding $ORG_ID \
    --member="user:admin@company.com" \
    --role="roles/resourcemanager.organizationAdmin"

# 2. Deploy network infrastructure
cd terraform/landing-zone
terraform init
terraform plan -var="org_id=$ORG_ID"
terraform apply -auto-approve

# 3. Configure security baseline
cd ../security
terraform init && terraform apply -auto-approve

echo "Landing zone deployment complete!"
```

#### Week 3-4: Connectivity Setup
```yaml
# VPN connection configuration
vpn_setup:
  on_premises:
    gateway_ip: "203.0.113.1"
    bgp_asn: 65001
    
  gcp_side:
    vpn_gateway: "prod-vpn-gateway"
    cloud_router: "prod-router"
    bgp_asn: 65002
    
  tunnels:
    - name: "tunnel-1"
      shared_secret: "{{ vault_secret }}"
      ike_version: 2
```

### Phase 2: Pilot Migration (Weeks 5-8)

#### Application Selection Criteria
```python
# Pilot application scoring
pilot_criteria = {
    "low_complexity": 3,      # Simple architecture
    "minimal_dependencies": 3, # Few external dependencies  
    "non_critical": 2,        # Can tolerate downtime
    "good_documentation": 2,   # Well documented
    "team_availability": 2     # Team available for migration
}

# Score applications 1-3 for each criteria
applications = {
    "blog_website": [3, 3, 3, 2, 3],      # Total: 14 - Good pilot
    "internal_wiki": [3, 2, 3, 2, 2],     # Total: 12 - Good pilot  
    "payment_system": [1, 1, 1, 3, 2],    # Total: 8 - Not suitable
    "reporting_tool": [2, 3, 2, 2, 3]     # Total: 12 - Good pilot
}
```

#### Pilot Migration Steps
```bash
# Pilot migration automation
#!/bin/bash
PILOT_APP="blog-website"

echo "Starting pilot migration for $PILOT_APP"

# 1. Create GCP resources
gcloud compute instances create $PILOT_APP-vm \
    --zone=us-central1-a \
    --machine-type=e2-medium \
    --subnet=prod-web \
    --no-address \
    --image-family=ubuntu-2004-lts \
    --image-project=ubuntu-os-cloud

# 2. Setup database
gcloud sql instances create $PILOT_APP-db \
    --database-version=MYSQL_8_0 \
    --tier=db-f1-micro \
    --region=us-central1 \
    --network=prod-vpc \
    --no-assign-ip

# 3. Migrate data
gsutil -m cp -r gs://migration-bucket/data/* gs://$PILOT_APP-storage/

# 4. Deploy application
gcloud compute ssh $PILOT_APP-vm --command="
    sudo apt update && sudo apt install -y docker.io
    sudo docker run -d -p 80:8080 --name app $PILOT_APP:latest
"

echo "Pilot migration complete!"
```

### Phase 3: Production Migration (Weeks 9-16)

#### Migration Wave Planning
```yaml
migration_waves:
  wave_1:
    timeline: "Weeks 9-10"
    applications: ["web-frontend", "api-gateway"]
    strategy: "Blue-Green deployment"
    rollback_plan: "DNS switch back"
    
  wave_2:
    timeline: "Weeks 11-12" 
    applications: ["user-service", "notification-service"]
    strategy: "Rolling deployment"
    rollback_plan: "Load balancer switch"
    
  wave_3:
    timeline: "Weeks 13-14"
    applications: ["database-cluster", "data-warehouse"]
    strategy: "Maintenance window"
    rollback_plan: "Database restore"
    
  wave_4:
    timeline: "Weeks 15-16"
    applications: ["analytics", "reporting"]
    strategy: "Parallel run"
    rollback_plan: "Traffic redirect"
```

#### Production Migration Automation
```python
# Production migration orchestrator
import subprocess
import time
from datetime import datetime

class MigrationOrchestrator:
    def __init__(self, wave_config):
        self.wave_config = wave_config
        self.migration_log = []
    
    def execute_wave(self, wave_name):
        wave = self.wave_config[wave_name]
        
        print(f"Starting {wave_name} migration...")
        self.log_event(f"Wave {wave_name} started")
        
        for app in wave['applications']:
            try:
                self.migrate_application(app, wave['strategy'])
                self.log_event(f"Successfully migrated {app}")
            except Exception as e:
                self.log_event(f"Failed to migrate {app}: {str(e)}")
                self.execute_rollback(app, wave['rollback_plan'])
                raise
    
    def migrate_application(self, app_name, strategy):
        if strategy == "blue-green":
            self.blue_green_deployment(app_name)
        elif strategy == "rolling":
            self.rolling_deployment(app_name)
        elif strategy == "maintenance":
            self.maintenance_window_migration(app_name)
    
    def blue_green_deployment(self, app_name):
        # Create green environment
        subprocess.run([
            "gcloud", "compute", "instance-groups", "managed", "create",
            f"{app_name}-green", "--template", f"{app_name}-template",
            "--size", "3", "--zone", "us-central1-a"
        ])
        
        # Wait for health checks
        time.sleep(300)
        
        # Switch traffic
        subprocess.run([
            "gcloud", "compute", "backend-services", "update",
            f"{app_name}-backend", "--instance-group", f"{app_name}-green"
        ])
        
        # Cleanup blue environment after validation
        time.sleep(600)  # 10 minutes validation
        subprocess.run([
            "gcloud", "compute", "instance-groups", "managed", "delete",
            f"{app_name}-blue", "--zone", "us-central1-a"
        ])
```

---

## 🎯 Real-Time Use Cases

### Use Case 1: E-commerce Platform Migration

#### Scenario
- **Company**: Online retailer with 1M+ users
- **Current**: On-premises VMware infrastructure
- **Challenge**: Black Friday traffic spikes, scaling issues
- **Timeline**: 6 months migration window

#### Architecture Transformation
```yaml
# Before (On-premises)
current_architecture:
  web_tier:
    servers: 4
    type: "Physical servers"
    load_balancer: "F5 BigIP"
    
  app_tier:
    servers: 8
    type: "VMware VMs"
    middleware: "Tomcat"
    
  data_tier:
    database: "Oracle RAC"
    storage: "SAN storage"
    backup: "Tape backup"

# After (GCP)
target_architecture:
  web_tier:
    service: "Cloud Load Balancing"
    compute: "GKE cluster (3-50 nodes)"
    cdn: "Cloud CDN"
    
  app_tier:
    service: "Cloud Run"
    scaling: "Auto-scaling 0-1000 instances"
    
  data_tier:
    database: "Cloud SQL (HA)"
    storage: "Cloud Storage"
    backup: "Automated backups"
```

#### Migration Steps
```bash
# E-commerce migration script
#!/bin/bash

echo "=== E-commerce Platform Migration ==="

# Phase 1: Setup GCP infrastructure
echo "Setting up GCP infrastructure..."
gcloud container clusters create ecommerce-cluster \
    --num-nodes=3 \
    --enable-autoscaling \
    --min-nodes=3 \
    --max-nodes=50 \
    --zone=us-central1-a

# Phase 2: Migrate database
echo "Migrating database..."
gcloud sql instances create ecommerce-db \
    --database-version=MYSQL_8_0 \
    --tier=db-n1-highmem-4 \
    --region=us-central1 \
    --availability-type=REGIONAL

# Phase 3: Deploy applications
echo "Deploying applications..."
kubectl apply -f k8s-manifests/

# Phase 4: Setup monitoring
echo "Setting up monitoring..."
gcloud services enable monitoring.googleapis.com
kubectl apply -f monitoring/

echo "Migration complete!"
```

### Use Case 2: Financial Services Migration

#### Scenario
- **Company**: Regional bank
- **Current**: Mainframe + Windows servers
- **Challenge**: Regulatory compliance, disaster recovery
- **Timeline**: 12 months phased approach

#### Compliance Requirements
```yaml
compliance_framework:
  regulations: ["PCI-DSS", "SOX", "FFIEC"]
  
  security_controls:
    - data_encryption: "AES-256 at rest and in transit"
    - access_controls: "Multi-factor authentication"
    - audit_logging: "Immutable audit trails"
    - network_isolation: "Private VPCs, no internet access"
    - backup_retention: "7 years for financial records"
    
  gcp_services:
    - security: "Cloud KMS, Cloud HSM"
    - compliance: "Cloud Audit Logs, Cloud Asset Inventory"
    - networking: "Private Google Access, VPC Service Controls"
    - data_protection: "Cloud DLP, Binary Authorization"
```

#### Migration Architecture
```hcl
# Financial services secure architecture
resource "google_compute_network" "banking_vpc" {
  name                    = "banking-secure-vpc"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "core_banking" {
  name          = "core-banking-subnet"
  ip_cidr_range = "10.0.1.0/24"
  region        = "us-central1"
  network       = google_compute_network.banking_vpc.id
  
  # No external IP addresses allowed
  private_ip_google_access = true
}

# VPC Service Controls perimeter
resource "google_access_context_manager_service_perimeter" "banking_perimeter" {
  parent = "accessPolicies/${var.access_policy_id}"
  name   = "accessPolicies/${var.access_policy_id}/servicePerimeters/banking_perimeter"
  title  = "Banking Services Perimeter"
  
  status {
    restricted_services = [
      "storage.googleapis.com",
      "bigquery.googleapis.com",
      "sql-component.googleapis.com"
    ]
    
    resources = [
      "projects/${var.core_banking_project}",
      "projects/${var.data_warehouse_project}"
    ]
  }
}
```

### Use Case 3: Healthcare Platform Migration

#### Scenario
- **Company**: Healthcare provider network
- **Current**: Legacy .NET applications
- **Challenge**: HIPAA compliance, patient data security
- **Timeline**: 18 months with zero downtime requirement

#### HIPAA Compliance Architecture
```yaml
hipaa_architecture:
  data_classification:
    phi_data: "Patient Health Information"
    pii_data: "Personally Identifiable Information"
    public_data: "General healthcare information"
    
  security_zones:
    dmz_zone:
      purpose: "Public-facing web applications"
      encryption: "TLS 1.3"
      access: "Internet-facing load balancer"
      
    application_zone:
      purpose: "Healthcare applications"
      encryption: "Application-level encryption"
      access: "Private load balancer only"
      
    data_zone:
      purpose: "PHI/PII databases"
      encryption: "Customer-managed keys"
      access: "Private subnet, no internet"
      
  audit_requirements:
    - access_logging: "All data access logged"
    - retention: "6 years minimum"
    - monitoring: "Real-time anomaly detection"
    - reporting: "Monthly compliance reports"
```

#### Zero-Downtime Migration Strategy
```python
# Healthcare zero-downtime migration
class HealthcareMigration:
    def __init__(self):
        self.migration_phases = [
            "database_replication",
            "application_deployment", 
            "traffic_gradual_shift",
            "legacy_system_decommission"
        ]
    
    def execute_zero_downtime_migration(self):
        # Phase 1: Setup database replication
        self.setup_database_replication()
        
        # Phase 2: Deploy applications in parallel
        self.deploy_parallel_environment()
        
        # Phase 3: Gradual traffic shift (1%, 5%, 25%, 50%, 100%)
        traffic_percentages = [1, 5, 25, 50, 100]
        for percentage in traffic_percentages:
            self.shift_traffic(percentage)
            self.monitor_health_metrics(duration=3600)  # 1 hour monitoring
            
            if not self.validate_system_health():
                self.rollback_traffic()
                raise Exception("Health check failed, rolling back")
        
        # Phase 4: Decommission legacy systems
        self.decommission_legacy_systems()
    
    def setup_database_replication(self):
        # Setup Cloud SQL replica from on-premises
        subprocess.run([
            "gcloud", "sql", "instances", "create", "healthcare-replica",
            "--master-instance-name", "on-prem-master",
            "--replica-type", "READ",
            "--tier", "db-custom-8-32768"
        ])
    
    def shift_traffic(self, percentage):
        # Update load balancer weights
        subprocess.run([
            "gcloud", "compute", "backend-services", "update",
            "healthcare-backend",
            f"--backend", f"gcp-backend,balancing-mode=RATE,max-rate-per-instance={percentage}"
        ])
```

---

## ✅ Post-Migration Steps

### 1. Performance Optimization

#### Resource Right-Sizing
```bash
# GCP resource optimization script
#!/bin/bash

echo "=== Post-Migration Optimization ==="

# Analyze compute usage
gcloud compute instances list --format="table(
    name,
    zone,
    machineType.scope(machineTypes):label=MACHINE_TYPE,
    status
)" > compute_inventory.csv

# Get CPU utilization metrics
gcloud logging read "
    resource.type=gce_instance AND
    metric.type=compute.googleapis.com/instance/cpu/utilization
" --limit=1000 --format=json > cpu_metrics.json

# Analyze and recommend right-sizing
python3 << EOF
import json
import pandas as pd

# Load metrics
with open('cpu_metrics.json') as f:
    metrics = json.load(f)

# Analyze utilization patterns
for instance in metrics:
    avg_cpu = instance.get('avg_cpu', 0)
    if avg_cpu < 20:
        print(f"RECOMMENDATION: Downsize {instance['instance_name']}")
    elif avg_cpu > 80:
        print(f"RECOMMENDATION: Upsize {instance['instance_name']}")
EOF
```

#### Cost Optimization
```python
# Cost optimization recommendations
import google.cloud.billing.budgets_v1 as budgets

class CostOptimizer:
    def __init__(self, project_id):
        self.project_id = project_id
        self.recommendations = []
    
    def analyze_costs(self):
        # Committed Use Discounts analysis
        self.check_cud_opportunities()
        
        # Preemptible instances analysis  
        self.check_preemptible_opportunities()
        
        # Storage class optimization
        self.optimize_storage_classes()
        
        # Unused resources cleanup
        self.identify_unused_resources()
    
    def check_cud_opportunities(self):
        # Analyze consistent workloads for CUD
        consistent_workloads = self.get_consistent_workloads()
        
        for workload in consistent_workloads:
            if workload['runtime_hours'] > 17520:  # 70% of year
                savings = workload['cost'] * 0.57  # Up to 57% savings
                self.recommendations.append({
                    'type': 'Committed Use Discount',
                    'resource': workload['name'],
                    'potential_savings': savings,
                    'action': f"Purchase 1-year CUD for {workload['machine_type']}"
                })
    
    def optimize_storage_classes(self):
        # Analyze access patterns for storage optimization
        storage_buckets = self.get_storage_usage()
        
        for bucket in storage_buckets:
            if bucket['access_frequency'] < 1:  # Less than once per month
                savings = bucket['cost'] * 0.4  # 40% savings with Coldline
                self.recommendations.append({
                    'type': 'Storage Class Optimization',
                    'resource': bucket['name'],
                    'potential_savings': savings,
                    'action': 'Move to Coldline Storage'
                })
```

### 2. Security Hardening

#### Security Baseline Implementation
```bash
# Post-migration security hardening
#!/bin/bash

echo "=== Security Hardening ==="

# Enable security services
gcloud services enable securitycenter.googleapis.com
gcloud services enable cloudasset.googleapis.com
gcloud services enable binaryauthorization.googleapis.com

# Configure organization policies
gcloud resource-manager org-policies set-policy org-policy-restrict-public-ip.yaml
gcloud resource-manager org-policies set-policy org-policy-require-os-login.yaml

# Setup Cloud Security Command Center
gcloud scc sources create --organization=$ORG_ID \
    --display-name="Custom Security Scanner" \
    --description="Post-migration security validation"

# Enable audit logging
cat > audit-policy.yaml << EOF
auditConfigs:
- service: allServices
  auditLogConfigs:
  - logType: ADMIN_READ
  - logType: DATA_READ
  - logType: DATA_WRITE
EOF

gcloud logging sinks create security-audit-sink \
    bigquery.googleapis.com/projects/$PROJECT_ID/datasets/security_audit \
    --log-filter='protoPayload.serviceName="compute.googleapis.com" OR protoPayload.serviceName="storage.googleapis.com"'
```

#### Vulnerability Assessment
```python
# Automated vulnerability scanning
from google.cloud import securitycenter
from google.cloud import asset_v1

class SecurityAssessment:
    def __init__(self, org_id):
        self.org_id = org_id
        self.security_client = securitycenter.SecurityCenterClient()
        self.asset_client = asset_v1.AssetServiceClient()
    
    def run_comprehensive_scan(self):
        # Asset inventory
        assets = self.get_asset_inventory()
        
        # Vulnerability scanning
        vulnerabilities = self.scan_vulnerabilities()
        
        # Configuration assessment
        misconfigurations = self.assess_configurations()
        
        # Generate security report
        self.generate_security_report(assets, vulnerabilities, misconfigurations)
    
    def scan_vulnerabilities(self):
        # Container image scanning
        self.scan_container_images()
        
        # OS package scanning
        self.scan_os_packages()
        
        # Web application scanning
        self.scan_web_applications()
    
    def assess_configurations(self):
        findings = []
        
        # Check for public IP addresses
        public_ips = self.find_public_ip_instances()
        if public_ips:
            findings.append({
                'severity': 'HIGH',
                'category': 'Network Security',
                'finding': f'{len(public_ips)} instances with public IPs',
                'recommendation': 'Use Cloud NAT for outbound connectivity'
            })
        
        # Check for overprivileged service accounts
        overprivileged_sas = self.find_overprivileged_service_accounts()
        if overprivileged_sas:
            findings.append({
                'severity': 'MEDIUM', 
                'category': 'IAM Security',
                'finding': f'{len(overprivileged_sas)} overprivileged service accounts',
                'recommendation': 'Apply principle of least privilege'
            })
        
        return findings
```

### 3. Monitoring and Alerting Setup

#### Comprehensive Monitoring Stack
```yaml
# monitoring-stack.yaml
monitoring_configuration:
  infrastructure_monitoring:
    - compute_instances: "CPU, Memory, Disk, Network"
    - kubernetes_clusters: "Node health, Pod status, Resource usage"
    - databases: "Connection count, Query performance, Replication lag"
    - load_balancers: "Request rate, Error rate, Latency"
    
  application_monitoring:
    - custom_metrics: "Business KPIs, Transaction rates"
    - distributed_tracing: "Request flow across services"
    - error_tracking: "Application errors and exceptions"
    - performance_monitoring: "Response times, Throughput"
    
  security_monitoring:
    - audit_logs: "Admin activities, Data access"
    - network_security: "Firewall denies, Suspicious traffic"
    - identity_security: "Failed logins, Privilege escalations"
    - compliance_monitoring: "Policy violations, Configuration drift"
```

#### Alerting Configuration
```python
# Automated alerting setup
from google.cloud import monitoring_v3

class AlertingSetup:
    def __init__(self, project_id):
        self.project_id = project_id
        self.client = monitoring_v3.AlertPolicyServiceClient()
    
    def create_critical_alerts(self):
        alerts = [
            {
                'name': 'High CPU Usage',
                'condition': 'compute.googleapis.com/instance/cpu/utilization > 0.8',
                'duration': '300s',
                'severity': 'CRITICAL'
            },
            {
                'name': 'Database Connection Failures',
                'condition': 'cloudsql.googleapis.com/database/network/connections > 80',
                'duration': '60s', 
                'severity': 'CRITICAL'
            },
            {
                'name': 'Application Error Rate',
                'condition': 'logging.googleapis.com/user/error_rate > 0.05',
                'duration': '120s',
                'severity': 'HIGH'
            }
        ]
        
        for alert_config in alerts:
            self.create_alert_policy(alert_config)
    
    def create_alert_policy(self, config):
        project_name = f"projects/{self.project_id}"
        
        policy = monitoring_v3.AlertPolicy(
            display_name=config['name'],
            conditions=[
                monitoring_v3.AlertPolicy.Condition(
                    display_name=config['name'],
                    condition_threshold=monitoring_v3.AlertPolicy.Condition.MetricThreshold(
                        filter=f'metric.type="{config["condition"].split()[0]}"',
                        comparison=monitoring_v3.ComparisonType.COMPARISON_GREATER_THAN,
                        threshold_value=float(config['condition'].split()[-1]),
                        duration={"seconds": int(config['duration'][:-1])}
                    )
                )
            ],
            notification_channels=[
                f"projects/{self.project_id}/notificationChannels/{self.get_notification_channel()}"
            ]
        )
        
        self.client.create_alert_policy(
            name=project_name,
            alert_policy=policy
        )
```

### 4. Backup and Disaster Recovery

#### Automated Backup Strategy
```bash
# Comprehensive backup setup
#!/bin/bash

echo "=== Setting up Backup and DR ==="

# Database backups
gcloud sql instances patch $DB_INSTANCE \
    --backup-start-time=02:00 \
    --enable-bin-log \
    --retained-backups-count=30

# Compute Engine snapshots
gcloud compute disks snapshot $DISK_NAME \
    --zone=$ZONE \
    --snapshot-names=$DISK_NAME-$(date +%Y%m%d-%H%M%S) \
    --storage-location=$REGION

# Cloud Storage versioning and lifecycle
gsutil versioning set on gs://$BACKUP_BUCKET
gsutil lifecycle set backup-lifecycle.json gs://$BACKUP_BUCKET

# Create backup lifecycle policy
cat > backup-lifecycle.json << EOF
{
  "lifecycle": {
    "rule": [
      {
        "action": {"type": "SetStorageClass", "storageClass": "NEARLINE"},
        "condition": {"age": 30}
      },
      {
        "action": {"type": "SetStorageClass", "storageClass": "COLDLINE"}, 
        "condition": {"age": 90}
      },
      {
        "action": {"type": "Delete"},
        "condition": {"age": 2555}  # 7 years
      }
    ]
  }
}
EOF
```

#### Disaster Recovery Testing
```python
# DR testing automation
class DisasterRecoveryTesting:
    def __init__(self, primary_region, dr_region):
        self.primary_region = primary_region
        self.dr_region = dr_region
        self.test_results = []
    
    def run_dr_test(self):
        print("Starting DR test...")
        
        # Test 1: Database failover
        db_failover_time = self.test_database_failover()
        
        # Test 2: Application recovery
        app_recovery_time = self.test_application_recovery()
        
        # Test 3: Data consistency validation
        data_consistency = self.validate_data_consistency()
        
        # Test 4: Network connectivity
        network_connectivity = self.test_network_connectivity()
        
        # Generate DR test report
        self.generate_dr_report({
            'database_failover_time': db_failover_time,
            'application_recovery_time': app_recovery_time,
            'data_consistency': data_consistency,
            'network_connectivity': network_connectivity
        })
    
    def test_database_failover(self):
        start_time = time.time()
        
        # Simulate primary database failure
        subprocess.run([
            "gcloud", "sql", "instances", "patch", "primary-db",
            "--activation-policy", "NEVER"
        ])
        
        # Promote replica to primary
        subprocess.run([
            "gcloud", "sql", "instances", "promote-replica", "replica-db"
        ])
        
        # Test connectivity to new primary
        while not self.test_db_connectivity("replica-db"):
            time.sleep(10)
        
        failover_time = time.time() - start_time
        return failover_time
```

---

## 📊 Monitoring & Optimization

### Performance Monitoring Dashboard
```python
# Custom monitoring dashboard
from google.cloud import monitoring_dashboard_v1

class MigrationDashboard:
    def __init__(self, project_id):
        self.project_id = project_id
        self.client = monitoring_dashboard_v1.DashboardsServiceClient()
    
    def create_migration_dashboard(self):
        dashboard_config = {
            "displayName": "Post-Migration Performance Dashboard",
            "mosaicLayout": {
                "tiles": [
                    self.create_cpu_utilization_tile(),
                    self.create_memory_utilization_tile(),
                    self.create_network_throughput_tile(),
                    self.create_application_latency_tile(),
                    self.create_error_rate_tile(),
                    self.create_cost_tracking_tile()
                ]
            }
        }
        
        project_name = f"projects/{self.project_id}"
        dashboard = monitoring_dashboard_v1.Dashboard(dashboard_config)
        
        self.client.create_dashboard(
            parent=project_name,
            dashboard=dashboard
        )
    
    def create_cpu_utilization_tile(self):
        return {
            "width": 6,
            "height": 4,
            "widget": {
                "title": "CPU Utilization",
                "xyChart": {
                    "dataSets": [{
                        "timeSeriesQuery": {
                            "timeSeriesFilter": {
                                "filter": 'metric.type="compute.googleapis.com/instance/cpu/utilization"',
                                "aggregation": {
                                    "alignmentPeriod": "60s",
                                    "perSeriesAligner": "ALIGN_MEAN"
                                }
                            }
                        }
                    }]
                }
            }
        }
```

### Cost Tracking and Optimization
```sql
-- BigQuery cost analysis queries
-- Daily cost breakdown by service
SELECT
  DATE(usage_start_time) as usage_date,
  service.description as service_name,
  SUM(cost) as daily_cost,
  SUM(usage.amount) as usage_amount,
  usage.unit as usage_unit
FROM `project.billing_export.gcp_billing_export_v1_XXXXXX`
WHERE DATE(usage_start_time) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY usage_date, service_name, usage_unit
ORDER BY usage_date DESC, daily_cost DESC;

-- Cost comparison: pre vs post migration
WITH pre_migration AS (
  SELECT 
    'Pre-Migration' as period,
    AVG(cost) as avg_daily_cost
  FROM `project.billing_export.gcp_billing_export_v1_XXXXXX`
  WHERE DATE(usage_start_time) BETWEEN '2024-01-01' AND '2024-03-31'
),
post_migration AS (
  SELECT
    'Post-Migration' as period, 
    AVG(cost) as avg_daily_cost
  FROM `project.billing_export.gcp_billing_export_v1_XXXXXX`
  WHERE DATE(usage_start_time) >= '2024-04-01'
)
SELECT * FROM pre_migration
UNION ALL
SELECT * FROM post_migration;
```

---

## 🔧 Troubleshooting

### Common Migration Issues

#### Issue 1: Network Connectivity Problems
```bash
# Network troubleshooting toolkit
#!/bin/bash

echo "=== Network Connectivity Troubleshooting ==="

# Check VPC configuration
gcloud compute networks list
gcloud compute networks subnets list --network=$VPC_NAME

# Test connectivity between subnets
gcloud compute ssh test-vm-1 --command="ping -c 4 10.0.2.10"

# Check firewall rules
gcloud compute firewall-rules list --filter="network:$VPC_NAME"

# Verify Cloud NAT configuration
gcloud compute routers nats list --router=$ROUTER_NAME --region=$REGION

# Test external connectivity
gcloud compute ssh test-vm --command="curl -I https://www.google.com"
```

#### Issue 2: Performance Degradation
```python
# Performance analysis toolkit
class PerformanceAnalyzer:
    def __init__(self, project_id):
        self.project_id = project_id
        
    def analyze_performance_issues(self):
        # CPU bottlenecks
        cpu_issues = self.check_cpu_bottlenecks()
        
        # Memory pressure
        memory_issues = self.check_memory_pressure()
        
        # Disk I/O problems
        disk_issues = self.check_disk_performance()
        
        # Network latency
        network_issues = self.check_network_latency()
        
        return {
            'cpu': cpu_issues,
            'memory': memory_issues, 
            'disk': disk_issues,
            'network': network_issues
        }
    
    def check_cpu_bottlenecks(self):
        # Query CPU metrics from Cloud Monitoring
        query = '''
        fetch gce_instance
        | metric 'compute.googleapis.com/instance/cpu/utilization'
        | filter (metric.instance_name =~ '.*')
        | group_by [resource.instance_id], [value_utilization_mean: mean(value.utilization)]
        | every 1m
        '''
        
        # Identify instances with high CPU usage
        high_cpu_instances = []
        # Implementation would query monitoring API
        
        return high_cpu_instances
```

#### Issue 3: Data Consistency Problems
```bash
# Data validation toolkit
#!/bin/bash

echo "=== Data Consistency Validation ==="

# Database record count comparison
SOURCE_COUNT=$(mysql -h $SOURCE_DB -e "SELECT COUNT(*) FROM users;" | tail -1)
TARGET_COUNT=$(gcloud sql connect $TARGET_DB --user=root --quiet << EOF
SELECT COUNT(*) FROM users;
EOF
)

echo "Source DB records: $SOURCE_COUNT"
echo "Target DB records: $TARGET_COUNT"

if [ "$SOURCE_COUNT" -eq "$TARGET_COUNT" ]; then
    echo "✅ Record counts match"
else
    echo "❌ Record count mismatch detected"
fi

# File integrity checks
gsutil -m cp gs://$SOURCE_BUCKET/checksums.txt .
gsutil -m cp gs://$TARGET_BUCKET/checksums.txt .

if diff checksums.txt checksums_target.txt > /dev/null; then
    echo "✅ File checksums match"
else
    echo "❌ File integrity issues detected"
fi
```

### Migration Rollback Procedures
```python
# Automated rollback system
class MigrationRollback:
    def __init__(self, migration_id):
        self.migration_id = migration_id
        self.rollback_steps = []
        
    def execute_rollback(self, rollback_reason):
        print(f"Initiating rollback for migration {self.migration_id}")
        print(f"Reason: {rollback_reason}")
        
        # Step 1: Stop new traffic to GCP
        self.redirect_traffic_to_source()
        
        # Step 2: Restore database from backup
        self.restore_database_backup()
        
        # Step 3: Validate source system health
        self.validate_source_system()
        
        # Step 4: Clean up GCP resources (optional)
        self.cleanup_gcp_resources()
        
        print("Rollback completed successfully")
    
    def redirect_traffic_to_source(self):
        # Update DNS records to point back to source
        subprocess.run([
            "gcloud", "dns", "record-sets", "transaction", "start",
            "--zone", "migration-zone"
        ])
        
        subprocess.run([
            "gcloud", "dns", "record-sets", "transaction", "remove",
            "--zone", "migration-zone",
            "--name", "app.company.com.",
            "--type", "A",
            "--ttl", "300",
            "34.102.136.180"  # GCP IP
        ])
        
        subprocess.run([
            "gcloud", "dns", "record-sets", "transaction", "add",
            "--zone", "migration-zone", 
            "--name", "app.company.com.",
            "--type", "A",
            "--ttl", "300",
            "203.0.113.10"  # Source IP
        ])
        
        subprocess.run([
            "gcloud", "dns", "record-sets", "transaction", "execute",
            "--zone", "migration-zone"
        ])
```

---

## 📋 Migration Checklist

### Pre-Migration Checklist
- [ ] Complete infrastructure assessment
- [ ] Identify all dependencies and integrations
- [ ] Design target architecture
- [ ] Set up GCP landing zone
- [ ] Configure network connectivity (VPN/Interconnect)
- [ ] Establish security baseline
- [ ] Create migration timeline and wave plan
- [ ] Set up monitoring and alerting
- [ ] Prepare rollback procedures
- [ ] Train migration team

### During Migration Checklist
- [ ] Execute pilot migration
- [ ] Validate pilot results
- [ ] Begin production migration waves
- [ ] Monitor system performance continuously
- [ ] Validate data integrity after each wave
- [ ] Update DNS and load balancer configurations
- [ ] Test application functionality
- [ ] Verify security controls
- [ ] Document any issues and resolutions
- [ ] Communicate status to stakeholders

### Post-Migration Checklist
- [ ] Validate all applications are functional
- [ ] Confirm data consistency and integrity
- [ ] Optimize resource sizing and costs
- [ ] Implement security hardening
- [ ] Set up comprehensive monitoring
- [ ] Configure backup and disaster recovery
- [ ] Conduct security assessment
- [ ] Train operations team on GCP tools
- [ ] Update documentation and runbooks
- [ ] Decommission source infrastructure
- [ ] Conduct lessons learned session
- [ ] Plan for continuous optimization

---

## 🎯 Success Metrics

### Technical Metrics
- **Availability**: 99.9%+ uptime
- **Performance**: <2s application response time
- **Security**: Zero security incidents
- **Data Integrity**: 100% data consistency

### Business Metrics  
- **Cost Reduction**: 20-40% infrastructure cost savings
- **Scalability**: Auto-scaling to handle 10x traffic spikes
- **Time to Market**: 50% faster deployment cycles
- **Compliance**: 100% regulatory compliance maintained

### Operational Metrics
- **Migration Timeline**: On-time delivery
- **Downtime**: <4 hours total planned downtime
- **Team Productivity**: 30% reduction in operational overhead
- **Innovation**: Faster adoption of new cloud services

---

**🚀 This comprehensive guide provides the foundation for successful GCP migration with enterprise-grade practices, real-world use cases, and proven methodologies.**