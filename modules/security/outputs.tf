output "firewall_rules" {
  description = "List of created firewall rules"
  value = {
    ssh        = google_compute_firewall.allow_ssh.name
    http_https = google_compute_firewall.allow_http_https.name
    internal   = google_compute_firewall.allow_internal.name
    health_check = google_compute_firewall.allow_health_check.name
  }
}