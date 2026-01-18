#!/usr/bin/env python3
"""
Professional GCP Infrastructure Architecture Diagram
Enterprise-grade visualization of Terraform-provisioned infrastructure
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch, Rectangle, Circle, Polygon
import numpy as np

# Set up the figure with professional styling
plt.style.use('default')
fig, ax = plt.subplots(1, 1, figsize=(20, 14))
ax.set_xlim(0, 20)
ax.set_ylim(0, 14)
ax.axis('off')
fig.patch.set_facecolor('white')

# Professional GCP Color Palette
gcp_blue = '#4285F4'
gcp_green = '#34A853'
gcp_yellow = '#FBBC04'
gcp_red = '#EA4335'
gcp_orange = '#FF6D01'
gcp_purple = '#9C27B0'

# Professional grays and backgrounds
cloud_gray = '#F8F9FA'
border_gray = '#DADCE0'
text_primary = '#202124'
text_secondary = '#5F6368'
accent_blue = '#1A73E8'
success_green = '#137333'
warning_orange = '#F29900'
error_red = '#D93025'

# Background gradient effect
background = Rectangle((0, 0), 20, 14, facecolor=cloud_gray, alpha=0.3)
ax.add_patch(background)

# Professional Header with Company Branding
header_box = FancyBboxPatch((1, 12.5), 18, 1.2, 
                           boxstyle="round,pad=0.15", 
                           facecolor='white', 
                           edgecolor=border_gray, linewidth=2)
ax.add_patch(header_box)

# Title with professional typography
ax.text(10, 13.4, 'Enterprise Multi-Environment GCP Infrastructure', 
        fontsize=22, fontweight='bold', ha='center', color=text_primary,
        family='sans-serif')
ax.text(10, 12.9, 'Development • Staging • Production | Project: praxis-gear-483220-k4', 
        fontsize=14, ha='center', color=text_secondary, style='italic')

# Add GCP logo placeholder (represented as colored circle)
gcp_logo = Circle((2, 13.1), 0.3, facecolor=gcp_blue, edgecolor='white', linewidth=2)
ax.add_patch(gcp_logo)
ax.text(2, 13.1, 'GCP', fontsize=10, fontweight='bold', ha='center', va='center', color='white')

# Internet/External Zone
internet_zone = FancyBboxPatch((0.5, 10), 4, 2, 
                              boxstyle="round,pad=0.15", 
                              facecolor='#E8F0FE', 
                              edgecolor=gcp_blue, linewidth=2)
ax.add_patch(internet_zone)
ax.text(2.5, 11.5, 'Internet', fontsize=14, fontweight='bold', ha='center', color=gcp_blue)
ax.text(2.5, 11.1, 'External Traffic', fontsize=10, ha='center', color=text_secondary)
ax.text(2.5, 10.8, 'HTTPS/SSH Access', fontsize=10, ha='center', color=text_secondary)

# Main GCP Project Container
project_container = FancyBboxPatch((5.5, 0.5), 13.5, 11.5, 
                                  boxstyle="round,pad=0.2", 
                                  facecolor='white', 
                                  edgecolor=gcp_blue, linewidth=3)
ax.add_patch(project_container)

# Project header
project_header = FancyBboxPatch((6, 11), 12.5, 0.8, 
                               boxstyle="round,pad=0.1", 
                               facecolor=gcp_blue, 
                               edgecolor=gcp_blue, linewidth=1)
ax.add_patch(project_header)
ax.text(12.25, 11.4, 'Google Cloud Project: praxis-gear-483220-k4', 
        fontsize=16, fontweight='bold', ha='center', color='white')

# Region indicator
region_badge = FancyBboxPatch((16.5, 10.2), 2, 0.5, 
                             boxstyle="round,pad=0.05", 
                             facecolor=gcp_green, 
                             edgecolor=gcp_green, linewidth=1)
ax.add_patch(region_badge)
ax.text(17.5, 10.45, 'us-central1', fontsize=10, fontweight='bold', ha='center', color='white')

# VPC Network Container
vpc_container = FancyBboxPatch((6, 1.5), 12, 9, 
                              boxstyle="round,pad=0.15", 
                              facecolor='#F8FCF8', 
                              edgecolor=gcp_green, linewidth=2)
ax.add_patch(vpc_container)

# VPC Header
vpc_header = FancyBboxPatch((6.5, 9.8), 11, 0.6, 
                           boxstyle="round,pad=0.05", 
                           facecolor=gcp_green, 
                           edgecolor=gcp_green, linewidth=1)
ax.add_patch(vpc_header)
ax.text(12, 10.1, 'VPC Network: development-vpc', 
        fontsize=14, fontweight='bold', ha='center', color='white')

# Subnet Container
subnet_container = FancyBboxPatch((7, 2.5), 10, 6.8, 
                                 boxstyle="round,pad=0.1", 
                                 facecolor='white', 
                                 edgecolor=gcp_yellow, linewidth=2)
ax.add_patch(subnet_container)

# Subnet Header
subnet_header = FancyBboxPatch((7.5, 8.8), 9, 0.5, 
                              boxstyle="round,pad=0.05", 
                              facecolor=gcp_yellow, 
                              edgecolor=gcp_yellow, linewidth=1)
ax.add_patch(subnet_header)
ax.text(12, 9.05, 'Subnet: development-subnet (10.10.0.0/16)', 
        fontsize=12, fontweight='bold', ha='center', color='white')

# Network Infrastructure Components
# Cloud Router
router_box = FancyBboxPatch((8, 7.5), 2.5, 1, 
                           boxstyle="round,pad=0.1", 
                           facecolor='#E8F5E8', 
                           edgecolor=gcp_green, linewidth=2)
ax.add_patch(router_box)
router_icon = Circle((8.5, 8), 0.2, facecolor=gcp_green, edgecolor='white', linewidth=1)
ax.add_patch(router_icon)
ax.text(9.7, 8.1, 'Cloud Router', fontsize=11, fontweight='bold', ha='center', color=gcp_green)
ax.text(9.7, 7.8, 'development-router', fontsize=9, ha='center', color=text_secondary)

# Cloud NAT
nat_box = FancyBboxPatch((11.5, 7.5), 2.5, 1, 
                        boxstyle="round,pad=0.1", 
                        facecolor='#FFF8E1', 
                        edgecolor=gcp_yellow, linewidth=2)
ax.add_patch(nat_box)
nat_icon = Circle((12, 8), 0.2, facecolor=gcp_yellow, edgecolor='white', linewidth=1)
ax.add_patch(nat_icon)
ax.text(13.2, 8.1, 'Cloud NAT', fontsize=11, fontweight='bold', ha='center', color=gcp_yellow)
ax.text(13.2, 7.8, 'development-nat', fontsize=9, ha='center', color=text_secondary)

# VM Instance - Main Component
vm_container = FancyBboxPatch((8.5, 4.5), 5, 2.5, 
                             boxstyle="round,pad=0.15", 
                             facecolor='#FFF3E0', 
                             edgecolor=gcp_red, linewidth=3)
ax.add_patch(vm_container)

# VM Icon
vm_icon = FancyBboxPatch((9, 6.2), 0.8, 0.6, 
                        boxstyle="round,pad=0.05", 
                        facecolor=gcp_red, 
                        edgecolor='white', linewidth=2)
ax.add_patch(vm_icon)
ax.text(9.4, 6.5, 'VM', fontsize=16, ha='center', va='center')

ax.text(11.5, 6.5, 'Compute Engine Instance', fontsize=13, fontweight='bold', ha='center', color=gcp_red)
ax.text(11.5, 6.1, 'development-vm | e2-medium', fontsize=11, fontweight='bold', ha='center', color=text_primary)
ax.text(11.5, 5.8, 'Ubuntu 22.04 LTS', fontsize=10, ha='center', color=text_secondary)
ax.text(11.5, 5.5, 'Internal: 10.10.0.2', fontsize=10, ha='center', color=text_secondary)
ax.text(11.5, 5.2, 'External: Dynamic IP', fontsize=10, ha='center', color=text_secondary)

# Docker badge
docker_badge = FancyBboxPatch((10.5, 4.7), 2, 0.3, 
                             boxstyle="round,pad=0.05", 
                             facecolor=gcp_blue, 
                             edgecolor=gcp_blue, linewidth=1)
ax.add_patch(docker_badge)
ax.text(11.5, 4.85, 'Docker Ready', fontsize=9, fontweight='bold', ha='center', color='white')

# Service Account
sa_container = FancyBboxPatch((8, 3), 6, 0.8, 
                             boxstyle="round,pad=0.1", 
                             facecolor='#E3F2FD', 
                             edgecolor=gcp_blue, linewidth=2)
ax.add_patch(sa_container)
sa_icon = Circle((8.5, 3.4), 0.15, facecolor=gcp_blue, edgecolor='white', linewidth=1)
ax.add_patch(sa_icon)
ax.text(11, 3.5, 'Service Account: development-vm-sa', fontsize=11, fontweight='bold', ha='center', color=gcp_blue)
ax.text(11, 3.2, 'Workload Identity Enabled', fontsize=9, ha='center', color=text_secondary)

# Security & IAM Panel
security_panel = FancyBboxPatch((0.5, 6), 4.5, 3.5, 
                               boxstyle="round,pad=0.15", 
                               facecolor='white', 
                               edgecolor=gcp_orange, linewidth=2)
ax.add_patch(security_panel)

# Security header
security_header = FancyBboxPatch((1, 9), 3.5, 0.4, 
                                boxstyle="round,pad=0.05", 
                                facecolor=gcp_orange, 
                                edgecolor=gcp_orange, linewidth=1)
ax.add_patch(security_header)
ax.text(2.75, 9.2, 'Security & Firewall', fontsize=12, fontweight='bold', ha='center', color='white')

# Firewall rules
firewall_rules = [
    ('SSH Access', 'Port 22', success_green),
    ('HTTP/HTTPS', 'Ports 80, 443', success_green),
    ('Internal', 'All ports', success_green),
    ('Health Checks', 'GCP ranges', success_green)
]

y_pos = 8.5
for rule, port, color in firewall_rules:
    rule_indicator = Circle((1.2, y_pos), 0.08, facecolor=color, edgecolor='white', linewidth=1)
    ax.add_patch(rule_indicator)
    ax.text(1.5, y_pos, f'{rule}', fontsize=10, fontweight='bold', va='center', color=text_primary)
    ax.text(4.2, y_pos, f'{port}', fontsize=9, va='center', color=text_secondary, ha='right')
    y_pos -= 0.4

# Tags section
ax.text(2.75, 6.8, 'Network Tags:', fontsize=10, fontweight='bold', ha='center', color=text_primary)
tags = ['ssh-allowed', 'http-allowed', 'health-check']
tag_y = 6.5
for tag in tags:
    tag_badge = FancyBboxPatch((1.5, tag_y-0.1), 2.5, 0.2, 
                              boxstyle="round,pad=0.02", 
                              facecolor='#F1F3F4', 
                              edgecolor=border_gray, linewidth=1)
    ax.add_patch(tag_badge)
    ax.text(2.75, tag_y, tag, fontsize=8, ha='center', color=text_secondary)
    tag_y -= 0.3

# Workload Identity Panel
wi_panel = FancyBboxPatch((0.5, 2), 4.5, 3.5, 
                         boxstyle="round,pad=0.15", 
                         facecolor='white', 
                         edgecolor=gcp_purple, linewidth=2)
ax.add_patch(wi_panel)

# WI header
wi_header = FancyBboxPatch((1, 5), 3.5, 0.4, 
                          boxstyle="round,pad=0.05", 
                          facecolor=gcp_purple, 
                          edgecolor=gcp_purple, linewidth=1)
ax.add_patch(wi_header)
ax.text(2.75, 5.2, 'Workload Identity', fontsize=12, fontweight='bold', ha='center', color='white')

# WI details
wi_details = [
    ('Pool ID:', 'github-pool'),
    ('Provider:', 'GitHub Actions'),
    ('Repository:', 'surajkmr39-lang/GCP-Terraform'),
    ('Status:', 'Active')
]

y_pos = 4.5
for label, value in wi_details:
    ax.text(1.2, y_pos, label, fontsize=10, fontweight='bold', va='center', color=text_primary)
    ax.text(4.2, y_pos, value, fontsize=10, va='center', color=text_secondary, ha='right')
    y_pos -= 0.3

# Security badge
security_badge = FancyBboxPatch((1.5, 2.3), 2.5, 0.3, 
                               boxstyle="round,pad=0.05", 
                               facecolor=success_green, 
                               edgecolor=success_green, linewidth=1)
ax.add_patch(security_badge)
ax.text(2.75, 2.45, 'No Stored Keys', fontsize=9, fontweight='bold', ha='center', color='white')

# Professional connection lines with proper routing
def draw_professional_connection(start, end, color, style='solid', linewidth=2):
    if style == 'dashed':
        linestyle = '--'
    else:
        linestyle = '-'
    
    # Create curved connection
    mid_x = (start[0] + end[0]) / 2
    mid_y = max(start[1], end[1]) + 0.3
    
    # Draw connection with bezier curve effect
    connection = ConnectionPatch(start, end, "data", "data",
                               arrowstyle="->", shrinkA=8, shrinkB=8, 
                               mutation_scale=20, fc=color, ec=color, 
                               linewidth=linewidth, linestyle=linestyle,
                               connectionstyle="arc3,rad=0.1")
    ax.add_patch(connection)

# Network connections
draw_professional_connection((4.5, 11), (8, 8), gcp_blue, linewidth=3)  # Internet to Router
draw_professional_connection((10.5, 8), (11.5, 8), gcp_green, linewidth=2)  # Router to NAT
draw_professional_connection((12, 7.5), (11, 6.8), gcp_yellow, linewidth=2)  # NAT to VM

# Security connections
draw_professional_connection((4.5, 7.5), (8.5, 6.5), gcp_orange, 'dashed', linewidth=2)  # Security to VM

# Identity connections
draw_professional_connection((4.5, 3.5), (8, 3.4), gcp_purple, 'dashed', linewidth=2)  # WI to SA

# Professional metrics and status panel
metrics_panel = FancyBboxPatch((15.5, 1), 4, 5, 
                              boxstyle="round,pad=0.15", 
                              facecolor='white', 
                              edgecolor=border_gray, linewidth=2)
ax.add_patch(metrics_panel)

# Metrics header
metrics_header = FancyBboxPatch((16, 5.5), 3, 0.4, 
                               boxstyle="round,pad=0.05", 
                               facecolor=text_primary, 
                               edgecolor=text_primary, linewidth=1)
ax.add_patch(metrics_header)
ax.text(17.5, 5.7, 'Multi-Environment Setup', fontsize=11, fontweight='bold', ha='center', color='white')

# Environment status indicators
env_items = [
    ('Development:', '10.10.0.0/16', success_green),
    ('Staging:', '10.20.0.0/16', warning_orange),
    ('Production:', '10.30.0.0/16', error_red),
    ('State Storage:', 'Remote GCS', success_green),
    ('CI/CD Ready:', 'All Envs', success_green)
]

y_pos = 5
for label, value, color in env_items:
    status_dot = Circle((16.3, y_pos), 0.08, facecolor=color, edgecolor='white', linewidth=1)
    ax.add_patch(status_dot)
    ax.text(16.6, y_pos, label, fontsize=9, fontweight='bold', va='center', color=text_primary)
    ax.text(19.2, y_pos, value, fontsize=9, va='center', color=color, ha='right', fontweight='bold')
    y_pos -= 0.4

# Deployment info
deployment_info = FancyBboxPatch((16, 1.5), 3, 1, 
                                boxstyle="round,pad=0.1", 
                                facecolor='#F8F9FA', 
                                edgecolor=border_gray, linewidth=1)
ax.add_patch(deployment_info)
ax.text(17.5, 2.2, 'Enterprise Architecture', fontsize=10, fontweight='bold', ha='center', color=text_primary)
ax.text(17.5, 1.9, 'Multi-Environment Ready', fontsize=9, ha='center', color=text_secondary)
ax.text(17.5, 1.6, 'Remote State Management', fontsize=9, ha='center', color=text_secondary)

# Footer with professional branding
footer = FancyBboxPatch((1, 0.1), 18, 0.6, 
                       boxstyle="round,pad=0.1", 
                       facecolor=text_primary, 
                       edgecolor=text_primary, linewidth=1)
ax.add_patch(footer)
ax.text(2, 0.4, '© 2026 Infrastructure Deployment', fontsize=10, color='white', fontweight='bold')
ax.text(18, 0.4, 'Generated: Terraform Enterprise', fontsize=10, color='white', ha='right')

plt.tight_layout()
plt.savefig('gcp-architecture-diagram.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none', pad_inches=0.2)
plt.savefig('gcp-architecture-diagram.pdf', bbox_inches='tight', 
            facecolor='white', edgecolor='none', pad_inches=0.2)

print("✅ Enterprise Multi-Environment Architecture Diagram Created:")
print("   📊 gcp-architecture-diagram.png (High Resolution)")
print("   📄 gcp-architecture-diagram.pdf (Vector Format)")
print("\n🏗️ Enterprise Infrastructure Components:")
print("   • Multi-Environment Setup (Development/Staging/Production)")
print("   • Enterprise CIDR Blocks (/16 networks)")
print("   • Remote State Management with GCS")
print("   • Workload Identity Federation (keyless authentication)")
print("   • Comprehensive security and compliance")
print("   • CI/CD ready for all environments")
print("\n🌍 Environment Configuration:")
print("   • Development: 10.10.0.0/16 (e2-medium)")
print("   • Staging: 10.20.0.0/16 (e2-standard-2)")
print("   • Production: 10.30.0.0/16 (e2-standard-4)")
print("   • State Storage: gs://praxis-gear-483220-k4-terraform-state/")

plt.show()
