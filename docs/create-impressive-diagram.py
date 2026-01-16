#!/usr/bin/env python3
"""
Impressive GCP Infrastructure Architecture Diagram
Clean, professional, presentation-ready with large fonts
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import matplotlib.lines as mlines

# Create large figure for presentation
fig, ax = plt.subplots(figsize=(24, 14))
ax.set_xlim(0, 24)
ax.set_ylim(0, 14)
ax.axis('off')
fig.patch.set_facecolor('white')

# Professional color palette
gcp_blue = '#4285F4'
gcp_green = '#34A853'
gcp_yellow = '#FBBC04'
gcp_red = '#EA4335'
purple = '#9C27B0'
orange = '#FF6F00'
dark_blue = '#1A73E8'
light_bg = '#F8F9FA'
dark_text = '#202124'

# ============= TITLE SECTION =============
title_box = FancyBboxPatch((1, 12), 22, 1.5, boxstyle="round,pad=0.15", 
                           facecolor=light_bg, edgecolor=dark_blue, linewidth=3)
ax.add_patch(title_box)

# GCP Logo placeholder
logo_circle = Circle((2.5, 12.75), 0.4, facecolor=gcp_blue, edgecolor='white', linewidth=2)
ax.add_patch(logo_circle)
ax.text(2.5, 12.75, 'GCP', fontsize=14, fontweight='bold', ha='center', va='center', color='white')

ax.text(12, 13, 'Google Cloud Platform - Development Environment', 
        fontsize=26, fontweight='bold', ha='center', va='center', color=dark_text)
ax.text(12, 12.4, 'Infrastructure Architecture | Project: praxis-gear-483220-k4', 
        fontsize=14, ha='center', va='center', style='italic', color='gray')

# ============= LEFT PANEL: EXTERNAL & SECURITY =============

# Internet Section
internet_box = FancyBboxPatch((0.5, 9.5), 4, 2, boxstyle="round,pad=0.15",
                              facecolor='#E8F4FD', edgecolor=gcp_blue, linewidth=3)
ax.add_patch(internet_box)
ax.text(2.5, 11, 'Internet', fontsize=16, fontweight='bold', ha='center', color=dark_blue)
ax.text(2.5, 10.5, 'External Traffic', fontsize=13, ha='center')
ax.text(2.5, 10.1, 'HTTPS/SSH Access', fontsize=13, ha='center')

# Security & Firewall Section
security_box = FancyBboxPatch((0.5, 5), 4, 4, boxstyle="round,pad=0.15",
                              facecolor='#FFF8E1', edgecolor=orange, linewidth=3)
ax.add_patch(security_box)

# Security header
sec_header = FancyBboxPatch((0.7, 8.5), 3.6, 0.5, boxstyle="round,pad=0.1",
                            facecolor=orange, edgecolor=orange)
ax.add_patch(sec_header)
ax.text(2.5, 8.75, 'Security & Firewall', fontsize=15, fontweight='bold', 
        ha='center', color='white')

# Security rules with better spacing
rules = [
    ('SSH Access', 'Port 22'),
    ('HTTP/HTTPS', 'Ports 80, 443'),
    ('Internal', 'All ports'),
    ('Health Checks', 'GCP ranges')
]
y_pos = 8
for rule, detail in rules:
    ax.text(0.9, y_pos, '•', fontsize=18, fontweight='bold', color=orange)
    ax.text(1.3, y_pos, rule, fontsize=13, fontweight='bold')
    ax.text(4, y_pos, detail, fontsize=12, ha='right', color='gray')
    y_pos -= 0.6

ax.text(2.5, 5.8, 'Network Tags:', fontsize=13, fontweight='bold', ha='center')
tag1 = FancyBboxPatch((1.2, 5.2), 2.6, 0.35, boxstyle="round,pad=0.05",
                      facecolor='lightgray', edgecolor='gray', linewidth=1)
ax.add_patch(tag1)
ax.text(2.5, 5.37, 'ssh-allowed', fontsize=12, ha='center', fontweight='bold')

# Workload Identity Section
wif_box = FancyBboxPatch((0.5, 1.5), 4, 3, boxstyle="round,pad=0.15",
                         facecolor='#F3E5F5', edgecolor=purple, linewidth=3)
ax.add_patch(wif_box)

wif_header = FancyBboxPatch((0.7, 4), 3.6, 0.5, boxstyle="round,pad=0.1",
                            facecolor=purple, edgecolor=purple)
ax.add_patch(wif_header)
ax.text(2.5, 4.25, 'Workload Identity', fontsize=15, fontweight='bold', 
        ha='center', color='white')

wif_info = [
    ('Pool ID:', 'dev-pool'),
    ('Provider:', 'GitHub Actions'),
    ('Repository:', 'Configured'),
    ('Status:', 'Active')
]
y_pos = 3.5
for label, value in wif_info:
    ax.text(0.9, y_pos, label, fontsize=13, fontweight='bold')
    ax.text(4, y_pos, value, fontsize=12, ha='right', color=gcp_green if value == 'Active' else 'gray')
    y_pos -= 0.45

# No Keys badge
no_keys = FancyBboxPatch((1, 1.8), 3, 0.4, boxstyle="round,pad=0.1",
                         facecolor=gcp_green, edgecolor=gcp_green)
ax.add_patch(no_keys)
ax.text(2.5, 2, 'No Stored Keys', fontsize=13, fontweight='bold', ha='center', color='white')

# ============= CENTER: GCP INFRASTRUCTURE =============

# Main GCP Container
gcp_main = FancyBboxPatch((5, 1.5), 13.5, 10, boxstyle="round,pad=0.2",
                          facecolor='white', edgecolor=gcp_blue, linewidth=4)
ax.add_patch(gcp_main)

# GCP Project Header
gcp_header = FancyBboxPatch((5.3, 11), 12.9, 0.6, boxstyle="round,pad=0.1",
                            facecolor=gcp_blue, edgecolor=gcp_blue)
ax.add_patch(gcp_header)
ax.text(11.75, 11.3, 'Google Cloud Project: praxis-gear-483220-k4', 
        fontsize=16, fontweight='bold', ha='center', color='white')

# VPC Network Container
vpc_box = FancyBboxPatch((5.5, 2), 12.5, 8.5, boxstyle="round,pad=0.15",
                         facecolor='#E8F5E9', edgecolor=gcp_green, linewidth=3)
ax.add_patch(vpc_box)

vpc_header = FancyBboxPatch((5.8, 10), 11.9, 0.5, boxstyle="round,pad=0.1",
                            facecolor=gcp_green, edgecolor=gcp_green)
ax.add_patch(vpc_header)
ax.text(11.75, 10.25, 'VPC Network: dev-vpc', fontsize=15, fontweight='bold', 
        ha='center', color='white')

# Subnet Container
subnet_box = FancyBboxPatch((6, 2.5), 11.5, 7, boxstyle="round,pad=0.15",
                            facecolor='#FFFDE7', edgecolor=gcp_yellow, linewidth=3)
ax.add_patch(subnet_box)

subnet_header = FancyBboxPatch((6.3, 9), 10.9, 0.45, boxstyle="round,pad=0.08",
                               facecolor=gcp_yellow, edgecolor=gcp_yellow)
ax.add_patch(subnet_header)
ax.text(11.75, 9.22, 'Subnet: dev-subnet (10.0.1.0/24)', fontsize=14, 
        fontweight='bold', ha='center', color=dark_text)

# Cloud Router
router_box = FancyBboxPatch((6.5, 7.5), 3, 1.2, boxstyle="round,pad=0.1",
                            facecolor='white', edgecolor=gcp_blue, linewidth=3)
ax.add_patch(router_box)
ax.text(8, 8.3, 'Cloud Router', fontsize=14, fontweight='bold', ha='center', color=gcp_blue)
ax.text(8, 7.85, 'dev-router', fontsize=12, ha='center', color='gray')

# Cloud NAT
nat_box = FancyBboxPatch((10.5, 7.5), 3, 1.2, boxstyle="round,pad=0.1",
                         facecolor='white', edgecolor=gcp_yellow, linewidth=3)
ax.add_patch(nat_box)
ax.text(12, 8.3, 'Cloud NAT', fontsize=14, fontweight='bold', ha='center', color=gcp_yellow)
ax.text(12, 7.85, 'dev-nat', fontsize=12, ha='center', color='gray')

# VM Instance - Main Feature
vm_box = FancyBboxPatch((7.5, 3.5), 8, 3.5, boxstyle="round,pad=0.15",
                        facecolor='white', edgecolor=gcp_red, linewidth=4)
ax.add_patch(vm_box)

vm_header = FancyBboxPatch((7.8, 6.5), 7.4, 0.5, boxstyle="round,pad=0.1",
                           facecolor=gcp_red, edgecolor=gcp_red)
ax.add_patch(vm_header)
ax.text(11.5, 6.75, 'Compute Engine Instance', fontsize=15, fontweight='bold', 
        ha='center', color='white')

# VM Details with better layout
vm_details = [
    ('Instance:', 'dev-vm'),
    ('Type:', 'e2-medium'),
    ('OS:', 'Ubuntu 22.04 LTS'),
    ('Internal IP:', '10.0.1.2'),
    ('External IP:', '34.173.255.107')
]
y_pos = 5.9
for label, value in vm_details:
    ax.text(8, y_pos, label, fontsize=13, fontweight='bold')
    ax.text(15, y_pos, value, fontsize=12, ha='right', color='gray')
    y_pos -= 0.45

# Docker badge
docker_badge = FancyBboxPatch((9.5, 3.8), 4, 0.45, boxstyle="round,pad=0.1",
                              facecolor=gcp_blue, edgecolor=gcp_blue)
ax.add_patch(docker_badge)
ax.text(11.5, 4.02, 'Docker Ready', fontsize=13, fontweight='bold', 
        ha='center', color='white')

# Service Account
sa_box = FancyBboxPatch((6.5, 2.7), 10, 0.7, boxstyle="round,pad=0.1",
                        facecolor='#E1F5FE', edgecolor=gcp_blue, linewidth=2)
ax.add_patch(sa_box)
ax.text(11.5, 3.2, 'Service Account: dev-vm-sa', fontsize=13, 
        fontweight='bold', ha='center', color=gcp_blue)
ax.text(11.5, 2.9, 'Workload Identity Enabled', fontsize=11, ha='center', color='gray')

# ============= RIGHT PANEL: METRICS =============

metrics_box = FancyBboxPatch((19, 1.5), 4.5, 10, boxstyle="round,pad=0.15",
                             facecolor='#263238', edgecolor='#263238', linewidth=3)
ax.add_patch(metrics_box)

# Metrics header
ax.text(21.25, 11, 'Infrastructure', fontsize=16, fontweight='bold', 
        ha='center', color='white')
ax.text(21.25, 10.5, 'Metrics', fontsize=16, fontweight='bold', 
        ha='center', color='white')

# Separator line
ax.plot([19.5, 23], [10.2, 10.2], color='white', linewidth=2, alpha=0.3)

# Metrics with icons and colors
metrics_data = [
    ('Resources', '15 Created', gcp_green),
    ('Modules', '4 Deployed', gcp_blue),
    ('Security', 'Compliant', gcp_green),
    ('Cost/Month', '$18-24', gcp_yellow),
    ('Uptime', '99.9% SLA', gcp_green)
]

y_pos = 9.5
for label, value, color in metrics_data:
    # Metric label
    ax.text(19.5, y_pos, label, fontsize=14, fontweight='bold', color='white')
    # Metric value with colored background
    value_box = FancyBboxPatch((19.5, y_pos - 0.5), 3.5, 0.35, 
                               boxstyle="round,pad=0.05",
                               facecolor=color, edgecolor=color, alpha=0.3)
    ax.add_patch(value_box)
    ax.text(21.25, y_pos - 0.32, value, fontsize=13, fontweight='bold', 
            ha='center', color=color)
    y_pos -= 1.2

# Deployment info
ax.plot([19.5, 23], [3.5, 3.5], color='white', linewidth=2, alpha=0.3)

deploy_box = FancyBboxPatch((19.5, 2.5), 3.5, 0.8, boxstyle="round,pad=0.1",
                            facecolor='#37474F', edgecolor='#37474F')
ax.add_patch(deploy_box)
ax.text(21.25, 3, 'Deployed via', fontsize=13, ha='center', color='white')
ax.text(21.25, 2.7, 'Terraform', fontsize=14, fontweight='bold', ha='center', color=gcp_blue)

ax.text(21.25, 2.1, 'Infrastructure as Code', fontsize=11, ha='center', 
        color='lightgray', style='italic')
ax.text(21.25, 1.8, 'Version Controlled', fontsize=11, ha='center', 
        color='lightgray', style='italic')

# ============= ARROWS & CONNECTIONS =============

# Internet to VM (blue dashed)
arrow1 = FancyArrowPatch((4.5, 10.5), (7.5, 5.5), 
                        arrowstyle='->', mutation_scale=30, linewidth=3, 
                        color=gcp_blue, linestyle='--', alpha=0.7)
ax.add_patch(arrow1)
ax.text(5.5, 8, 'Traffic', fontsize=11, color=gcp_blue, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=gcp_blue))

# Security to VM (orange dashed)
arrow2 = FancyArrowPatch((4.5, 7), (7.5, 5),
                        arrowstyle='->', mutation_scale=30, linewidth=3,
                        color=orange, linestyle='--', alpha=0.7)
ax.add_patch(arrow2)
ax.text(5.5, 6, 'Rules', fontsize=11, color=orange, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=orange))

# WIF to Service Account (purple dashed)
arrow3 = FancyArrowPatch((4.5, 2.8), (6.5, 3),
                        arrowstyle='->', mutation_scale=30, linewidth=3,
                        color=purple, linestyle='--', alpha=0.7)
ax.add_patch(arrow3)
ax.text(5.2, 2.5, 'Auth', fontsize=11, color=purple, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=purple))

# Router to NAT (solid arrow)
arrow4 = FancyArrowPatch((9.5, 8.1), (10.5, 8.1),
                        arrowstyle='->', mutation_scale=25, linewidth=3,
                        color=gcp_blue)
ax.add_patch(arrow4)

# ============= FOOTER =============

footer_box = FancyBboxPatch((1, 0.3), 22, 0.8, boxstyle="round,pad=0.1",
                            facecolor='#263238', edgecolor='#263238')
ax.add_patch(footer_box)
ax.text(2, 0.7, '© 2026 Infrastructure Deployment', fontsize=13, 
        color='white', fontweight='bold')
ax.text(22, 0.7, 'Generated: Terraform Enterprise', fontsize=13, 
        ha='right', color='lightgray')

# Save high-quality diagram
plt.tight_layout()
plt.savefig('gcp-impressive-architecture.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
print("✅ Impressive architecture diagram created!")
print("📊 File: gcp-impressive-architecture.png")
print("🎨 High resolution (300 DPI) - Perfect for presentations!")
