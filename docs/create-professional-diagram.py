#!/usr/bin/env python3
"""
Professional GCP Infrastructure Architecture Diagram Generator
Creates a presentation-ready diagram matching the original design
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.lines as mlines

# Set up the figure with white background
fig, ax = plt.subplots(figsize=(20, 12))
ax.set_xlim(0, 20)
ax.set_ylim(0, 12)
ax.axis('off')
fig.patch.set_facecolor('white')

# Color scheme
gcp_blue = '#4285F4'
gcp_green = '#34A853'
gcp_yellow = '#FBBC04'
gcp_red = '#EA4335'
purple = '#9C27B0'
orange = '#FF9800'
light_gray = '#F5F5F5'
dark_gray = '#333333'

# Title
title_box = FancyBboxPatch((1, 10.5), 18, 1.2, boxstyle="round,pad=0.1", 
                           facecolor=light_gray, edgecolor=dark_gray, linewidth=2)
ax.add_patch(title_box)
ax.text(10, 11.3, 'Google Cloud Platform - Development Environment', 
        fontsize=20, fontweight='bold', ha='center', va='center')
ax.text(10, 10.8, 'Infrastructure Architecture | Project: praxis-gear-483220-k4', 
        fontsize=12, ha='center', va='center', style='italic', color='gray')

# ============= LEFT SIDE: Internet & Security =============

# Internet Box
internet_box = FancyBboxPatch((0.5, 8), 3, 1.5, boxstyle="round,pad=0.1",
                              facecolor='#E3F2FD', edgecolor=gcp_blue, linewidth=2)
ax.add_patch(internet_box)
ax.text(2, 9.2, '🌐 Internet', fontsize=11, fontweight='bold', ha='center')
ax.text(2, 8.8, 'External Traffic', fontsize=9, ha='center')
ax.text(2, 8.5, 'HTTPS/SSH Access', fontsize=9, ha='center')

# Security & Firewall Box
security_box = FancyBboxPatch((0.5, 4.5), 3, 3, boxstyle="round,pad=0.1",
                              facecolor='#FFF3E0', edgecolor=orange, linewidth=2)
ax.add_patch(security_box)
ax.text(2, 7.2, '🔒 Security & Firewall', fontsize=11, fontweight='bold', 
        ha='center', color='white',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=orange, edgecolor=orange))

security_items = [
    ('• SSH Access', 'Port 22'),
    ('• HTTP/HTTPS', 'Ports 80, 443'),
    ('• Internal', 'All ports'),
    ('• Health Checks', 'GCP ranges')
]
y_pos = 6.7
for item, detail in security_items:
    ax.text(0.7, y_pos, item, fontsize=9, fontweight='bold')
    ax.text(2.8, y_pos, detail, fontsize=8, ha='right', color='gray')
    y_pos -= 0.4

ax.text(2, 5.2, 'Network Tags:', fontsize=9, fontweight='bold', ha='center')
ax.text(2, 4.9, 'ssh-allowed', fontsize=8, ha='center', 
        bbox=dict(boxstyle='round,pad=0.2', facecolor='lightgray'))
ax.text(2, 4.6, 'http-allowed', fontsize=8, ha='center',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='lightgray'))

# Workload Identity Box
wif_box = FancyBboxPatch((0.5, 1.5), 3, 2.5, boxstyle="round,pad=0.1",
                         facecolor='#F3E5F5', edgecolor=purple, linewidth=2)
ax.add_patch(wif_box)
ax.text(2, 3.7, '🔐 Workload Identity', fontsize=11, fontweight='bold', 
        ha='center', color='white',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=purple, edgecolor=purple))

wif_details = [
    ('Pool ID:', 'dev-pool'),
    ('Provider:', 'GitHub Actions'),
    ('Repository:', 'Configured'),
    ('Status:', '✓ Active')
]
y_pos = 3.2
for label, value in wif_details:
    ax.text(0.7, y_pos, label, fontsize=9, fontweight='bold')
    ax.text(2.8, y_pos, value, fontsize=8, ha='right')
    y_pos -= 0.35

ax.text(2, 1.9, '🔑 No Stored Keys', fontsize=9, fontweight='bold', ha='center',
        color='white', bbox=dict(boxstyle='round,pad=0.3', facecolor=gcp_green))

# ============= CENTER: GCP Infrastructure =============

# Main GCP Project Box
gcp_box = FancyBboxPatch((4, 1.5), 11.5, 8.5, boxstyle="round,pad=0.1",
                         facecolor='white', edgecolor=gcp_blue, linewidth=3)
ax.add_patch(gcp_box)

# GCP Project Header
project_header = FancyBboxPatch((4.2, 9.5), 11.1, 0.6, boxstyle="round,pad=0.05",
                                facecolor=gcp_blue, edgecolor=gcp_blue)
ax.add_patch(project_header)
ax.text(9.75, 9.8, 'Google Cloud Project: praxis-gear-483220-k4', 
        fontsize=12, fontweight='bold', ha='center', color='white')

# VPC Network Box
vpc_box = FancyBboxPatch((4.5, 2), 10.5, 7, boxstyle="round,pad=0.1",
                         facecolor='#E8F5E9', edgecolor=gcp_green, linewidth=2)
ax.add_patch(vpc_box)

# VPC Header
vpc_header = FancyBboxPatch((4.7, 8.5), 10.1, 0.5, boxstyle="round,pad=0.05",
                            facecolor=gcp_green, edgecolor=gcp_green)
ax.add_patch(vpc_header)
ax.text(9.75, 8.75, '🌐 VPC Network: dev-vpc', fontsize=11, fontweight='bold', 
        ha='center', color='white')

# Subnet Box
subnet_box = FancyBboxPatch((5, 2.5), 9.5, 5.5, boxstyle="round,pad=0.1",
                            facecolor='#FFF9C4', edgecolor=gcp_yellow, linewidth=2)
ax.add_patch(subnet_box)

# Subnet Header
subnet_header = FancyBboxPatch((5.2, 7.5), 9.1, 0.4, boxstyle="round,pad=0.05",
                               facecolor=gcp_yellow, edgecolor=gcp_yellow)
ax.add_patch(subnet_header)
ax.text(9.75, 7.7, '📡 Subnet: dev-subnet (10.0.1.0/24)', fontsize=10, 
        fontweight='bold', ha='center')

# Cloud Router
router_box = FancyBboxPatch((5.5, 6.5), 2, 0.8, boxstyle="round,pad=0.05",
                            facecolor='white', edgecolor=gcp_blue, linewidth=2)
ax.add_patch(router_box)
ax.text(6.5, 6.9, '🔄 Cloud Router', fontsize=9, fontweight='bold', ha='center')
ax.text(6.5, 6.6, 'dev-router', fontsize=8, ha='center', color='gray')

# Cloud NAT
nat_box = FancyBboxPatch((8.5, 6.5), 2, 0.8, boxstyle="round,pad=0.05",
                         facecolor='white', edgecolor=gcp_yellow, linewidth=2)
ax.add_patch(nat_box)
ax.text(9.5, 6.9, '🌐 Cloud NAT', fontsize=9, fontweight='bold', ha='center')
ax.text(9.5, 6.6, 'dev-nat', fontsize=8, ha='center', color='gray')

# VM Instance Box
vm_box = FancyBboxPatch((6.5, 3.5), 6, 2.5, boxstyle="round,pad=0.1",
                        facecolor='white', edgecolor=gcp_red, linewidth=3)
ax.add_patch(vm_box)

# VM Header
vm_header = FancyBboxPatch((6.7, 5.6), 5.6, 0.35, boxstyle="round,pad=0.05",
                           facecolor=gcp_red, edgecolor=gcp_red)
ax.add_patch(vm_header)
ax.text(9.5, 5.78, '💻 Compute Engine Instance', fontsize=10, fontweight='bold', 
        ha='center', color='white')

# VM Details
vm_details = [
    'dev-vm | e2-medium',
    'Ubuntu 22.04 LTS',
    'Internal: 10.0.1.2',
    'External: 34.173.255.107'
]
y_pos = 5.1
for detail in vm_details:
    ax.text(9.5, y_pos, detail, fontsize=8, ha='center')
    y_pos -= 0.3

# Docker Badge
docker_badge = FancyBboxPatch((8.5, 3.7), 2, 0.3, boxstyle="round,pad=0.05",
                              facecolor=gcp_blue, edgecolor=gcp_blue)
ax.add_patch(docker_badge)
ax.text(9.5, 3.85, '🐳 Docker Ready', fontsize=8, fontweight='bold', 
        ha='center', color='white')

# Service Account Box
sa_box = FancyBboxPatch((5.5, 2.7), 8, 0.6, boxstyle="round,pad=0.05",
                        facecolor='#E1F5FE', edgecolor=gcp_blue, linewidth=2)
ax.add_patch(sa_box)
ax.text(9.5, 3.15, '🔐 Service Account: dev-vm-sa', fontsize=9, 
        fontweight='bold', ha='center')
ax.text(9.5, 2.9, 'Workload Identity Enabled', fontsize=8, ha='center', color='gray')

# ============= RIGHT SIDE: Infrastructure Metrics =============

# Metrics box
metrics_box = FancyBboxPatch((16, 1.5), 3.5, 8.5, boxstyle="round,pad=0.1",
                             facecolor='#263238', edgecolor='#263238', linewidth=2)
ax.add_patch(metrics_box)

# Metrics Header
ax.text(17.75, 9.5, '📊 Infrastructure Metrics', fontsize=11, fontweight='bold', 
        ha='center', color='white')

# Metrics
metrics = [
    ('• Resources:', '15 Created', 'white'),
    ('• Modules:', '4 Deployed', 'white'),
    ('• Security:', 'Compliant', gcp_green),
    ('• Cost/Month:', '~$18-24', gcp_yellow),
    ('• Uptime:', '99.9% SLA', gcp_green)
]

y_pos = 8.8
for label, value, color in metrics:
    ax.text(16.3, y_pos, label, fontsize=9, fontweight='bold', color='white')
    ax.text(19.2, y_pos, value, fontsize=9, ha='right', color=color)
    y_pos -= 0.6

# Deployment Info
ax.text(17.75, 5.5, 'Deployed via Terraform', fontsize=9, fontweight='bold', 
        ha='center', color='white',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#37474F'))
ax.text(17.75, 5, 'Infrastructure as Code', fontsize=8, ha='center', 
        color='lightgray', style='italic')
ax.text(17.75, 4.6, 'Version Controlled', fontsize=8, ha='center', 
        color='lightgray', style='italic')

# ============= ARROWS =============

# Internet to VM
arrow1 = FancyArrowPatch((3.5, 8.75), (6.5, 5.5), 
                        arrowstyle='->', mutation_scale=20, linewidth=2, 
                        color=gcp_blue, linestyle='--')
ax.add_patch(arrow1)

# Security to VM
arrow2 = FancyArrowPatch((3.5, 6), (6.5, 4.5),
                        arrowstyle='->', mutation_scale=20, linewidth=2,
                        color=orange, linestyle='--')
ax.add_patch(arrow2)

# WIF to Service Account
arrow3 = FancyArrowPatch((3.5, 2.5), (5.5, 3),
                        arrowstyle='->', mutation_scale=20, linewidth=2,
                        color=purple, linestyle='--')
ax.add_patch(arrow3)

# Router to NAT
arrow4 = FancyArrowPatch((7.5, 6.9), (8.5, 6.9),
                        arrowstyle='->', mutation_scale=15, linewidth=2,
                        color=gcp_blue)
ax.add_patch(arrow4)

# ============= FOOTER =============

footer_box = FancyBboxPatch((1, 0.3), 18, 0.6, boxstyle="round,pad=0.05",
                            facecolor='#263238', edgecolor='#263238')
ax.add_patch(footer_box)
ax.text(2, 0.6, '© 2026 Infrastructure Deployment', fontsize=9, color='white')
ax.text(18, 0.6, 'Generated: Terraform Enterprise', fontsize=9, 
        ha='right', color='lightgray')

# Save the diagram
plt.tight_layout()
plt.savefig('gcp-professional-architecture.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
print("✅ Professional architecture diagram generated!")
print("📊 File: gcp-professional-architecture.png")
