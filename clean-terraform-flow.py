#!/usr/bin/env python3
"""
Clean Terraform Flow Diagram - Based on Reference Style
Author: Suraj Kumar

Creates a clean, simple flowchart exactly like the reference image:
- Clean purple/blue gradient boxes
- Simple vertical flow
- Clear, readable text
- Professional rounded corners
- Cyan arrows
- Perfect for presentations
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import matplotlib.patches as patches

# Configure for clean presentation
plt.rcParams.update({
    'font.family': 'Arial',
    'font.size': 16,
    'font.weight': 'bold',
    'figure.facecolor': 'white'
})

# Create figure - vertical layout like reference
fig = plt.figure(figsize=(12, 20))
ax = fig.add_subplot(111)
ax.set_xlim(0, 12)
ax.set_ylim(0, 20)
ax.axis('off')
fig.patch.set_facecolor('white')

# Colors matching the reference style
COLORS = {
    'purple': '#8B5CF6',     # Purple like reference
    'cyan': '#06B6D4',       # Cyan arrows like reference
    'white': '#FFFFFF',      # White text
    'light_bg': '#F8FAFC'    # Light background
}

def create_rounded_box(x, y, width, height, text, is_oval=False):
    """Create rounded box exactly like reference"""
    if is_oval:
        # Oval shape for Start/Stop
        box = FancyBboxPatch((x, y), width, height,
                            boxstyle="round,pad=0.3",
                            facecolor=COLORS['purple'],
                            edgecolor='none',
                            alpha=0.9)
    else:
        # Rectangle with rounded corners
        box = FancyBboxPatch((x, y), width, height,
                            boxstyle="round,pad=0.1",
                            facecolor=COLORS['purple'],
                            edgecolor='none',
                            alpha=0.9)
    
    ax.add_patch(box)
    
    # Add text
    ax.text(x + width/2, y + height/2, text,
            ha='center', va='center',
            fontsize=18, fontweight='bold',
            color=COLORS['white'])

def create_arrow(start_x, start_y, end_x, end_y):
    """Create cyan arrow like reference"""
    arrow = patches.FancyArrowPatch((start_x, start_y), (end_x, end_y),
                                   arrowstyle='->', mutation_scale=30,
                                   color=COLORS['cyan'], linewidth=6,
                                   alpha=0.8)
    ax.add_patch(arrow)

# START - Oval shape like reference
create_rounded_box(4, 18.5, 4, 1, 'Start', is_oval=True)

# Arrow down
create_arrow(6, 18.5, 6, 17.7)

# STEP 1: Configuration
create_rounded_box(2, 16.5, 8, 1.2, 'Load terraform.tfvars and variables.tf')

# Arrow down
create_arrow(6, 16.5, 6, 15.5)

# STEP 2: Provider Setup
create_rounded_box(2, 14.3, 8, 1.2, 'Initialize GCP Provider')

# Arrow down
create_arrow(6, 14.3, 6, 13.3)

# STEP 3: Main Module
create_rounded_box(2, 12.1, 8, 1.2, 'Execute main.tf - Call Modules')

# Arrow down
create_arrow(6, 12.1, 6, 11.1)

# STEP 4: Network Module
create_rounded_box(2, 9.9, 8, 1.2, 'Create Network (VPC, Subnet, NAT)')

# Arrow down
create_arrow(6, 9.9, 6, 8.9)

# STEP 5: Security Module
create_rounded_box(2, 7.7, 8, 1.2, 'Create Security (Firewall Rules)')

# Arrow down
create_arrow(6, 7.7, 6, 6.7)

# STEP 6: IAM Module
create_rounded_box(2, 5.5, 8, 1.2, 'Create IAM (Service Accounts)')

# Arrow down
create_arrow(6, 5.5, 6, 4.5)

# STEP 7: Compute Module
create_rounded_box(2, 3.3, 8, 1.2, 'Create Compute (VM Instances)')

# Arrow down
create_arrow(6, 3.3, 6, 2.3)

# STEP 8: Outputs
create_rounded_box(2, 1.1, 8, 1.2, 'Generate outputs.tf (IPs, SSH)')

# Arrow down
create_arrow(6, 1.1, 6, 0.3)

# STOP - Oval shape like reference
create_rounded_box(4, -0.5, 4, 1, 'Stop', is_oval=True)

# Add title at the top
ax.text(6, 19.7, 'TERRAFORM INFRASTRUCTURE DEPLOYMENT FLOW', 
        ha='center', va='center', fontsize=20, fontweight='bold', 
        color=COLORS['purple'])

# Add execution info on the side
info_box = FancyBboxPatch((0.2, 8), 1.5, 8,
                         boxstyle="round,pad=0.1",
                         facecolor=COLORS['light_bg'],
                         edgecolor=COLORS['purple'],
                         linewidth=2,
                         alpha=0.7)
ax.add_patch(info_box)

ax.text(0.95, 15, 'EXECUTION\nORDER', ha='center', va='top', 
        fontsize=12, fontweight='bold', color=COLORS['purple'])

execution_steps = [
    '1. Config',
    '2. Provider', 
    '3. Network',
    '4. Security',
    '5. IAM',
    '6. Compute',
    '7. Outputs'
]

for i, step in enumerate(execution_steps):
    ax.text(0.95, 13.5 - i*1.5, step, ha='center', va='center',
            fontsize=10, fontweight='bold', color=COLORS['purple'])

# Add timing info on the right side
timing_box = FancyBboxPatch((10.3, 8), 1.5, 8,
                           boxstyle="round,pad=0.1",
                           facecolor=COLORS['light_bg'],
                           edgecolor=COLORS['purple'],
                           linewidth=2,
                           alpha=0.7)
ax.add_patch(timing_box)

ax.text(11.05, 15, 'TIMING\n(seconds)', ha='center', va='top', 
        fontsize=12, fontweight='bold', color=COLORS['purple'])

timings = ['5s', '10s', '60s', '30s', '45s', '90s', '5s']

for i, timing in enumerate(timings):
    ax.text(11.05, 13.5 - i*1.5, timing, ha='center', va='center',
            fontsize=10, fontweight='bold', color=COLORS['purple'])

# Add summary at bottom
summary_box = FancyBboxPatch((1, -2), 10, 1.2,
                            boxstyle="round,pad=0.1",
                            facecolor=COLORS['light_bg'],
                            edgecolor=COLORS['purple'],
                            linewidth=2,
                            alpha=0.7)
ax.add_patch(summary_box)

ax.text(6, -1.4, 'TOTAL: 15+ Resources | 3-5 Minutes | Cost: $18-24/month', 
        ha='center', va='center', fontsize=14, fontweight='bold', 
        color=COLORS['purple'])

# Author signature
ax.text(11.5, -2.8, 'Suraj Kumar\nTerraform Specialist', 
        fontsize=12, ha='right', va='bottom',
        color=COLORS['purple'], fontweight='bold')

# Save with high quality
plt.tight_layout()
plt.savefig('clean-terraform-flow.png', dpi=400, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.savefig('clean-terraform-flow.pdf', dpi=400, bbox_inches='tight',
            facecolor='white', edgecolor='none')

print("✅ CLEAN TERRAFORM FLOW DIAGRAM CREATED!")
print("=" * 50)
print("📁 Files Generated:")
print("   ✅ clean-terraform-flow.png (400 DPI)")
print("   ✅ clean-terraform-flow.pdf (Vector)")
print("\n🎯 PERFECT REFERENCE STYLE:")
print("   ✅ Clean purple boxes like reference")
print("   ✅ Cyan arrows like reference")
print("   ✅ Simple vertical flow")
print("   ✅ Rounded corners")
print("   ✅ Clear, readable text")
print("   ✅ Professional presentation quality")
print("   ✅ Execution timing included")

plt.show()