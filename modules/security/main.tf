# Security module - Firewall rules
resource "google_compute_firewall" "allow_ssh" {
  name    = "${var.environment}-allow-ssh"
  network = var.network_name
  project = var.project_id

  allow {
    protocol = "tcp"
    ports    = ["22"]
  }

  source_ranges = var.ssh_source_ranges
  target_tags   = ["ssh-allowed"]
  
  description = "Allow SSH access to instances with ssh-allowed tag"
}

resource "google_compute_firewall" "allow_http_https" {
  name    = "${var.environment}-allow-http-https"
  network = var.network_name
  project = var.project_id

  allow {
    protocol = "tcp"
    ports    = ["80", "443"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["http-allowed"]
  
  description = "Allow HTTP/HTTPS access to instances with http-allowed tag"
}

resource "google_compute_firewall" "allow_internal" {
  name    = "${var.environment}-allow-internal"
  network = var.network_name
  project = var.project_id

  allow {
    protocol = "tcp"
    ports    = ["0-65535"]
  }

  allow {
    protocol = "udp"
    ports    = ["0-65535"]
  }

  allow {
    protocol = "icmp"
  }

  source_ranges = [var.subnet_cidr]
  
  description = "Allow internal communication within the subnet"
}

# Health check firewall rule
resource "google_compute_firewall" "allow_health_check" {
  name    = "${var.environment}-allow-health-check"
  network = var.network_name
  project = var.project_id

  allow {
    protocol = "tcp"
  }

  source_ranges = ["130.211.0.0/22", "35.191.0.0/16"]
  target_tags   = ["health-check"]
  
  description = "Allow Google Cloud health checks"
}