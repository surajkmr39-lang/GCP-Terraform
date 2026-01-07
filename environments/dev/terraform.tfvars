# Development environment configuration
# Your actual project ID from Google Cloud Console
project_id = "praxis-gear-483220-k4"
region     = "us-central1"
zone       = "us-central1-a"

environment = "dev"
subnet_cidr = "10.0.1.0/24"

# VM Configuration
machine_type = "e2-medium"
vm_image     = "ubuntu-os-cloud/ubuntu-2204-lts"
disk_size    = 20

# SSH Configuration
ssh_user           = "suraj"
ssh_public_key     = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDwWxUffp8iud6qnj7Wa/ocx48LLY9py5QaJrVllNG/y2iS7ePS9lTDinI/lCieeRN6zaf6OYRwxOL8mzyK4xUNf/7jy8ZE3aKV7ToH65tEV9ZsdzZMzouIaV2pU0URbNCtDlrr31p/fj55G68If36yZoHxoteFF8ADFC/HeFx7pYlV7PQq8okLDCrn0VCOyvWlJNHvfPEisKx9VOArchnVfoHZIoRYMc/IO9walmlKKtTht5aKIMUuNd2z7dS1REYFyXkt7X6GYtjB3rleIi5To3UF0me1J+TcSjf2w7kCO583/aUYwA/Ju+yxnPyemujKTytDSflZpBuHlawBB9mVAiuGDmiq8nlHewiyCixF71FOZhdqEs7Y3Frr8BlC2tUeVU8bAEBginFhl2Kg3QV8OADSPKqR93A60T1dxfUahlrYgPzMiM6eU8EIt0oVCG8JjOBnPTUnZQqIpkp+9qQMB2/uwo1EndrufVz44pQEq5EWRbHWSH3yfQWge4thpIfA8WE09EBzV0fnH4W3dxxyLgeGkrngEvL/plYZzGki6MjZT19leknxbU0+uq9VDn8tUEQ584BKRAl+dkicX/9yy+Q8hvFZZ6y9Cz/tTS0oC3c3Q2jbGgOwaOm8ooOWZ0xegeR9w7sNkfh7u4RZuH5KPPZRdrXKAqA0Fj2v7tmTQw=="
ssh_source_ranges  = ["0.0.0.0/0"]  # You can restrict this to your IP for better security

# Workload Identity (Optional - for GitHub Actions)
github_repository = ""  # Leave empty if not using GitHub Actions

# Tags
team        = "praxis-gear"
cost_center = "development"