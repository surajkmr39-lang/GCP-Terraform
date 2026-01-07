# Production environment configuration
project_id = "your-prod-project-id"
region     = "us-east1"
zone       = "us-east1-a"

environment = "prod"
subnet_cidr = "10.2.1.0/24"

# VM Configuration
machine_type = "e2-standard-4"
vm_image     = "ubuntu-os-cloud/ubuntu-2204-lts"
disk_size    = 50

# SSH Configuration
ssh_user           = "ubuntu"
ssh_public_key     = ""  # Add your SSH public key here
ssh_source_ranges  = ["10.0.0.0/8"]  # Restrict to corporate network

# Workload Identity
github_repository = ""  # Format: owner/repo

# Tags
team        = "platform"
cost_center = "engineering"