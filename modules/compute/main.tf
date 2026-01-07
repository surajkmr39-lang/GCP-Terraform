# Compute module - VM instances
resource "google_compute_instance" "vm" {
  name         = "${var.environment}-vm"
  machine_type = var.machine_type
  zone         = var.zone
  project      = var.project_id

  tags = ["ssh-allowed", "http-allowed", "health-check"]

  boot_disk {
    initialize_params {
      image = var.vm_image
      size  = var.disk_size
      type  = "pd-ssd"
      labels = var.tags
    }
  }

  network_interface {
    network    = var.network_name
    subnetwork = var.subnet_name

    # Assign external IP for dev environment
    access_config {
      // Ephemeral public IP
    }
  }

  # Use the service account with workload identity
  service_account {
    email  = var.service_account_email
    scopes = ["cloud-platform"]
  }

  metadata = merge(
    {
      ssh-keys               = var.ssh_public_key != "" ? "${var.ssh_user}:${var.ssh_public_key}" : ""
      enable-oslogin         = "TRUE"
      block-project-ssh-keys = "TRUE"
    },
    var.metadata
  )

  metadata_startup_script = var.startup_script

  labels = var.tags

  # Shielded VM configuration
  shielded_instance_config {
    enable_secure_boot          = true
    enable_vtpm                 = true
    enable_integrity_monitoring = true
  }

  # Allow stopping for maintenance
  allow_stopping_for_update = true

  lifecycle {
    ignore_changes = [
      metadata["ssh-keys"]
    ]
  }
}