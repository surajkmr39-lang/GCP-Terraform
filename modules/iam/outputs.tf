output "vm_service_account_email" {
  description = "Email of the VM service account"
  value       = google_service_account.vm_service_account.email
}

output "vm_service_account_id" {
  description = "ID of the VM service account"
  value       = google_service_account.vm_service_account.id
}

output "workload_identity_pool_name" {
  description = "Name of the workload identity pool"
  value       = google_iam_workload_identity_pool.pool.name
}

output "workload_identity_pool_id" {
  description = "ID of the workload identity pool"
  value       = google_iam_workload_identity_pool.pool.workload_identity_pool_id
}

output "workload_identity_provider_name" {
  description = "Name of the workload identity provider"
  value       = var.github_repository != "" ? google_iam_workload_identity_pool_provider.github_provider[0].name : null
}

output "workload_identity_provider_id" {
  description = "ID of the workload identity provider"
  value       = var.github_repository != "" ? google_iam_workload_identity_pool_provider.github_provider[0].workload_identity_pool_provider_id : null
}