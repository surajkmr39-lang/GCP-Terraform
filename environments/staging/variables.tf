# Staging Environment Variables
variable "project_id" {
  description = "The GCP project ID"
  type        = string
}

variable "region" {
  description = "The GCP region for resources"
  type        = string
  default     = "us-central1"
}

variable "zone" {
  description = "The GCP zone for resources"
  type        = string
  default     = "us-central1-c"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "staging"
}

variable "subnet_cidr" {
  description = "CIDR block for the subnet"
  type        = string
  default     = "10.2.1.0/24"
}

variable "machine_type" {
  description = "Machine type for the VM instance"
  type        = string
  default     = "e2-standard-2"  # Medium size for staging
}

variable "vm_image" {
  description = "The VM image to use"
  type        = string
  default     = "ubuntu-os-cloud/ubuntu-2204-lts"
}

variable "disk_size" {
  description = "Boot disk size in GB"
  type        = number
  default     = 30  # Medium disk for staging
}

variable "ssh_user" {
  description = "SSH username"
  type        = string
  default     = "ubuntu"
}

variable "ssh_public_key" {
  description = "SSH public key"
  type        = string
  default     = ""
}

variable "ssh_source_ranges" {
  description = "CIDR blocks allowed for SSH access"
  type        = list(string)
  default     = ["0.0.0.0/0"]
}

variable "github_repository" {
  description = "GitHub repository for workload identity"
  type        = string
  default     = ""
}

variable "startup_script" {
  description = "Startup script for the VM"
  type        = string
  default     = ""
}

variable "team" {
  description = "Team responsible for the resources"
  type        = string
  default     = "platform"
}

variable "cost_center" {
  description = "Cost center for billing"
  type        = string
  default     = "engineering"
}