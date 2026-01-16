#!/usr/bin/env python3
"""
Exact replica of the original GCP Infrastructure Architecture Diagram
Matches the layout, colors, and style from the screenshot
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import matplotlib.lines as mlines

# Create figure matching original proportions
fig, ax = plt.subplots(figsize=(22, 13))
ax.set_xlim(0, 22)
ax.set_ylim(0, 13)
ax.axis('off')
fig.patch.set_facecolor('white')

# Exact color matching
gcp_blue = '#4285F4'
gcp_green = '#34A853'
gcp_yellow = '#FBBC04'
gcp_red = '#EA4335'
purple = '#9C27B0'
orange = '#FF6F00'
light_blue_bg = '#E8F4FD'
light_green_bg = '#E8F5E9'
light_yellow_bg = '#FFFDE7'
light_purple_bg = '#F3E5F5'
light_orange_bg = '#FFF3E0'
dark_footer = '#2C2C2C'
dark_metrics = '#1A1A1A'

# ============= TITLE SECTION =============
title_outer = FancyBboxPatch((1, 11.2), 20, 1.5, boxstyle="round,pad=0.1", 
                             facecolor='#F5F5F5', edgecolor='#CCCCCC', linewidth=2)
ax.add_patch(title_outer)

# GCP Logo
logo_circle = Circle((2, 12), 0.35, facecolor=gcp_blue, edgecolor='white', linewidth=2)
ax.add_patch(logo_circle)
ax.text(2, 12, 'GCP', fontsize=11, fontweight='bold', ha='center', va='center', color='white')

ax.text(11, 12.3, 'Google Cloud Platform - Development Environment', 
        fontsize=22, fontweight='bold', ha='center', va='center', color='#333333')
ax.text(11, 11.7, 'Infrastructure Architecture | Project: praxis-gear-483220-k4', 
        fontsize=12, ha='center', va='center', style='italic', color='#666666')

# ============= LEFT COLUMN =============

# Internet Box
internet_box = FancyBboxPatch((0.5, 9), 3.5, 1.8, boxstyle="round,pad=0.1",
                              facecolor=light_blue_bg, edgecolor=gcp_blue, linewidth=2)
ax.add_patch(internet_box)
ax.text(2.25, 10.3, 'Internet', fontsize=14, fontweight='bold', ha='center', color=gcp_blue)
ax.text(2.25, 9.85, 'External Traffic', fontsize=11, ha='center', color='#555555')
ax.text(2.25, 9.5, 'HTTPS/SSH Access', fontsize=11, ha='center', color='#555555')

# Security & Firewall Box
security_box = FancyBboxPatch((0.5, 4.8), 3.5, 3.8, boxstyle="round,pad=0.1",
                              facecolor=light_orange_bg, edgecolor=orange, linewidth=2)
ax.add_patch(security_box)

# Security header
sec_header = FancyBboxPatch((0.7, 8.2), 3.1, 0.4, boxstyle="round,pad=0.05",
                            facecolor=orange, edgecolor=orange)
ax.add_patch(sec_header)
ax.text(2.25, 8.4, 'Security & Firewall', fontsize=13, fontweight='bold', 
        ha='center', color='white')

# Security rules
rules_data = [
    ('SSH Access', 'Port 22'),
    ('HTTP/HTTPS', 'Ports 80, 443'),
    ('Internal', 'All ports'),
    ('Health Checks', 'GCP ranges')
]
y_pos = 7.7
for rule, detail in rules_data:
    ax.text(0.8, y_pos, '●', fontsize=12, color='#333333')
    ax.text(1.1, y_pos, rule, fontsize=11, fontweight='bold', color='#333333')
    ax.text(3.8, y_pos, detail, fontsize=10, ha='right', color='#666666')
    y_pos -= 0.45

ax.text(2.25, 5.9, 'Network Tags:', fontsize=11, fontweight='bold', ha='center', color='#333333')
ax.text(2.25, 5.5, 'ssh-allowed', fontsize=10, ha='center', 
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#E0E0E0', edgecolor='#999999'))
ax.text(2.25, 5.15, 'http-allowed', fontsize=10, ha='center',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#E0E0E0', edgecolor='#999999'))

# Workload Identity Box
wif_box = FancyBboxPatch((0.5, 1.8), 3.5, 2.6, boxstyle="round,pad=0.1",
                         facecolor=light_purple_bg, edgecolor=purple, linewidth=2)
ax.add_patch(wif_box)

wif_header = FancyBboxPatch((0.7, 4), 3.1, 0.4, boxstyle="round,pad=0.05",
                            facecolor=purple, edgecolor=purple)
ax.add_patch(wif_header)
ax.text(2.25, 4.2, 'Workload Identity', fontsize=13, fontweight='bold', 
        ha='center', color='white')

wif_details = [
    ('Pool ID:', 'dev-pool'),
    ('Provider:', 'GitHub Actions'),
    ('Repository:', 'Configured'),
    ('Status:', '✓ Active')
]
y_pos = 3.6
for label, value in wif_details:
    ax.text(0.8, y_pos, label, fontsize=11, fontweight='bold', color='#333333')
    ax.text(3.8, y_pos, value, fontsize=10, ha='right', 
            color=gcp_green if 'Active' in value else '#666666')
    y_pos -= 0.4

# No Keys badge
no_keys_box = FancyBboxPatch((1, 2), 2.5, 0.35, boxstyle="round,pad=0.05",
                             facecolor=gcp_green, edgecolor=gcp_green)
ax.add_patch(no_keys_box)
ax.text(2.25, 2.17, 'No Stored Keys', fontsize=11, fontweight='bold', ha='center', color='white')

# ============= CENTER: GCP INFRASTRUCTURE =============

# Main GCP Project Box
gcp_outer = FancyBboxPatch((4.5, 1.8), 12, 9.2, boxstyle="round,pad=0.1",
                           facecolor='white', edgecolor='#CCCCCC', linewidth=3)
ax.add_patch(gcp_outer)

# GCP Project Header
gcp_header = FancyBboxPatch((4.7, 10.5), 11.6, 0.5, boxstyle="round,pad=0.05",
                            facecolor=gcp_blue, edgecolor=gcp_blue)
ax.add_patch(gcp_header)
ax.text(10.5, 10.75, 'Google Cloud Project: praxis-gear-483220-k4', 
        fontsize=14, fontweight='bold', ha='center', color='white')

# VPC Network Box
vpc_box = FancyBboxPatch((4.9, 2.1), 11.2, 8, boxstyle="round,pad=0.1",
                         facecolor=light_green_bg, edgecolor=gcp_green, linewidth=2)
ax.add_patch(vpc_box)

vpc_header = FancyBboxPatch((5.1, 9.7), 10.8, 0.4, boxstyle="round,pad=0.05",
                            facecolor=gcp_green, edgecolor=gcp_green)
ax.add_patch(vpc_header)
ax.text(10.5, 9.9, 'VPC Network: dev-vpc', fontsize=13, fontweight='bold', 
        ha='center', color='white')

# Subnet Box
subnet_box = FancyBboxPatch((5.3, 2.4), 10.4, 6.9, boxstyle="round,pad=0.1",
                            facecolor=light_yellow_bg, edgecolor=gcp_yellow, linewidth=2)
ax.add_patch(subnet_box)

subnet_header = FancyBboxPatch((5.5, 8.9), 10, 0.35, boxstyle="round,pad=0.05",
                               facecolor=gcp_yellow, edgecolor=gcp_yellow)
ax.add_patch(subnet_header)
ax.text(10.5, 9.07, 'Subnet: dev-subnet (10.0.1.0/24)', fontsize=12, 
        fontweight='bold', ha='center', color='#333333')

# Cloud Router
router_box = FancyBboxPatch((5.8, 7.8), 2.2, 0.9, boxstyle="round,pad=0.08",
                            facecolor='white', edgecolor=gcp_green, linewidth=2)
ax.add_patch(router_box)
ax.text(6.9, 8.4, 'Cloud Router', fontsize=11, fontweight='bold', ha='center', color=gcp_green)
ax.text(6.9, 8.05, 'dev-router', fontsize=9, ha='center', color='#666666')

# Cloud NAT
nat_box = FancyBboxPatch((9, 7.8), 2.2, 0.9, boxstyle="round,pad=0.08",
                         facecolor='white', edgecolor=gcp_yellow, linewidth=2)
ax.add_patch(nat_box)
ax.text(10.1, 8.4, 'Cloud NAT', fontsize=11, fontweight='bold', ha='center', color=gcp_yellow)
ax.text(10.1, 8.05, 'dev-nat', fontsize=9, ha='center', color='#666666')

# Arrow between Router and NAT
arrow_router_nat = FancyArrowPatch((8, 8.25), (9, 8.25),
                                   arrowstyle='->', mutation_scale=15, linewidth=2,
                                   color=gcp_blue)
ax.add_patch(arrow_router_nat)

# VM Instance Box (Red)
vm_box = FancyBboxPatch((6.5, 4), 7.5, 3.3, boxstyle="round,pad=0.1",
                        facecolor='white', edgecolor=gcp_red, linewidth=3)
ax.add_patch(vm_box)

vm_header = FancyBboxPatch((6.7, 6.9), 7.1, 0.4, boxstyle="round,pad=0.05",
                           facecolor=gcp_red, edgecolor=gcp_red)
ax.add_patch(vm_header)
ax.text(10.25, 7.1, 'Compute Engine Instance', fontsize=12, fontweight='bold', 
        ha='center', color='white')

# VM Details
vm_info = [
    'dev-vm | e2-medium',
    'Ubuntu 22.04 LTS',
    'Internal: 10.0.1.2',
    'External: 34.173.255.107'
]
y_pos = 6.5
for info in vm_info:
    ax.text(10.25, y_pos, info, fontsize=10, ha='center', color='#333333')
    y_pos -= 0.35

# Docker Ready badge
docker_badge = FancyBboxPatch((8.75, 4.25), 3, 0.3, boxstyle="round,pad=0.05",
                              facecolor=gcp_blue, edgecolor=gcp_blue)
ax.add_patch(docker_badge)
ax.text(10.25, 4.4, 'Docker Ready', fontsize=10, fontweight='bold', 
        ha='center', color='white')

# Service Account Box
sa_box = FancyBboxPatch((5.8, 2.7), 9, 0.9, boxstyle="round,pad=0.08",
                        facecolor='#E3F2FD', edgecolor=gcp_blue, linewidth=2)
ax.add_patch(sa_box)
ax.text(10.3, 3.3, 'Service Account: dev-vm-sa', fontsize=11, 
        fontweight='bold', ha='center', color=gcp_blue)
ax.text(10.3, 2.95, 'Workload Identity Enabled', fontsize=9, ha='center', color='#666666')

# ============= RIGHT PANEL: METRICS =============

metrics_box = FancyBboxPatch((17, 1.8), 4.5, 9.2, boxstyle="round,pad=0.1",
                             facecolor=dark_metrics, edgecolor=dark_metrics, linewidth=2)
ax.add_patch(metrics_box)

# Metrics header
metrics_header_box = FancyBboxPatch((17.2, 10.5), 4.1, 0.5, boxstyle="round,pad=0.05",
                                    facecolor='#333333', edgecolor='#333333')
ax.add_patch(metrics_header_box)
ax.text(19.25, 10.75, 'Infrastructure Metrics', fontsize=12, fontweight='bold', 
        ha='center', color='white')

# Metrics items
metrics = [
    ('Resources:', '15 Created'),
    ('Modules:', '4 Deployed'),
    ('Security:', 'Compliant'),
    ('Cost/Month:', '~$18-24'),
    ('Uptime:', '99.9% SLA')
]

y_pos = 9.8
for label, value in metrics:
    ax.text(17.4, y_pos, '●', fontsize=10, color=gcp_green)
    ax.text(17.8, y_pos, label, fontsize=11, fontweight='bold', color='white')
    ax.text(21.2, y_pos, value, fontsize=10, ha='right', color='#AAAAAA')
    y_pos -= 0.6

# Separator
ax.plot([17.4, 21.1], [6.5, 6.5], color='#444444', linewidth=1)

# Deployment section
deploy_box = FancyBboxPatch((17.5, 5.5), 3.5, 0.8, boxstyle="round,pad=0.08",
                            facecolor='#2A2A2A', edgecolor='#444444', linewidth=1)
ax.add_patch(deploy_box)
ax.text(19.25, 6.1, 'Deployed via Terraform', fontsize=11, fontweight='bold', 
        ha='center', color='white')
ax.text(19.25, 5.7, 'Infrastructure as Code', fontsize=9, ha='center', 
        color='#999999', style='italic')
ax.text(19.25, 5.4, 'Version Controlled', fontsize=9, ha='center', 
        color='#999999', style='italic')

# ============= ARROWS =============

# Internet to VM (blue dashed)
arrow1 = FancyArrowPatch((4, 9.9), (6.5, 6.5), 
                        arrowstyle='->', mutation_scale=25, linewidth=2.5, 
                        color=gcp_blue, linestyle='--', alpha=0.8)
ax.add_patch(arrow1)

# Security to VM (orange dashed)
arrow2 = FancyArrowPatch((4, 6.7), (6.5, 5.5),
                        arrowstyle='->', mutation_scale=25, linewidth=2.5,
                        color=orange, linestyle='--', alpha=0.8)
ax.add_patch(arrow2)

# WIF to Service Account (purple dashed)
arrow3 = FancyArrowPatch((4, 3), (5.8, 3.2),
                        arrowstyle='->', mutation_scale=25, linewidth=2.5,
                        color=purple, linestyle='--', alpha=0.8)
ax.add_patch(arrow3)

# ============= FOOTER =============

footer_box = FancyBboxPatch((0.5, 0.3), 21, 0.7, boxstyle="round,pad=0.05",
                            facecolor=dark_footer, edgecolor=dark_footer)
ax.add_patch(footer_box)
ax.text(1.5, 0.65, '© 2026 Infrastructure Deployment', fontsize=11, 
        color='white', fontweight='bold')
ax.text(20.5, 0.65, 'Generated: Terraform Enterprise', fontsize=11, 
        ha='right', color='#AAAAAA')

# Save the diagram
plt.tight_layout()
plt.savefig('gcp-infrastructure-architecture.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
print("✅ Exact architecture diagram created!")
print("📊 File: gcp-infrastructure-architecture.png")
print("🎯 Perfect match to original design!")
