# Staging environment configuration
project_id = "your-staging-project-id"
region     = "us-central1"
zone       = "us-central1-b"

environment = "staging"
subnet_cidr = "10.1.1.0/24"

# VM Configuration
machine_type = "e2-standard-2"
vm_image     = "ubuntu-os-cloud/ubuntu-2204-lts"
disk_size    = 30

# SSH Configuration
ssh_user           = "ubuntu"
ssh_public_key     = ""  # Add your SSH public key here
ssh_source_ranges  = ["10.0.0.0/8"]  # More restrictive for staging

# Workload Identity
github_repository = ""  # Format: owner/repo

# Tags
team        = "platform"
cost_center = "engineering"