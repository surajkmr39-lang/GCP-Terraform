#!/usr/bin/env python3
"""
Complete Terraform Project Understanding Flowcharts
Author: Suraj Kumar

Creates multiple flowcharts to understand:
1. Overall Project Structure
2. File Relationships & Dependencies
3. Variable Flow & Data Passing
4. Module Interactions
5. Resource Creation Process
6. Complete Execution Flow

All in clean, easy-to-understand style
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import matplotlib.patches as patches

# Configure for clean presentation
plt.rcParams.update({
    'font.family': 'Arial',
    'font.size': 14,
    'font.weight': 'bold',
    'figure.facecolor': 'white'
})

# Colors for different types
COLORS = {
    'config': '#8B5CF6',     # Purple for configuration
    'main': '#3B82F6',       # Blue for main orchestration
    'module': '#10B981',     # Green for modules
    'resource': '#F59E0B',   # Orange for resources
    'output': '#EF4444',     # Red for outputs
    'arrow': '#06B6D4',      # Cyan for arrows
    'white': '#FFFFFF',      # White text
    'light_bg': '#F8FAFC'    # Light background
}

def create_flowchart_box(ax, x, y, width, height, text, color, is_oval=False):
    """Create flowchart box"""
    if is_oval:
        box = FancyBboxPatch((x, y), width, height,
                            boxstyle="round,pad=0.3",
                            facecolor=color, edgecolor='none', alpha=0.9)
    else:
        box = FancyBboxPatch((x, y), width, height,
                            boxstyle="round,pad=0.1",
                            facecolor=color, edgecolor='none', alpha=0.9)
    ax.add_patch(box)
    
    ax.text(x + width/2, y + height/2, text,
            ha='center', va='center', fontsize=12, fontweight='bold',
            color=COLORS['white'])

def create_flowchart_arrow(ax, start_x, start_y, end_x, end_y, label=''):
    """Create flowchart arrow"""
    arrow = patches.FancyArrowPatch((start_x, start_y), (end_x, end_y),
                                   arrowstyle='->', mutation_scale=25,
                                   color=COLORS['arrow'], linewidth=4)
    ax.add_patch(arrow)
    
    if label:
        mid_x = (start_x + end_x) / 2
        mid_y = (start_y + end_y) / 2 + 0.2
        ax.text(mid_x, mid_y, label, ha='center', va='center',
                fontsize=10, fontweight='bold', color=COLORS['arrow'])

# ============================================================================
# FLOWCHART 1: PROJECT STRUCTURE OVERVIEW
# ============================================================================

fig1, ax1 = plt.subplots(1, 1, figsize=(14, 16))
ax1.set_xlim(0, 14)
ax1.set_ylim(0, 16)
ax1.axis('off')

# Title
ax1.text(7, 15.5, 'TERRAFORM PROJECT STRUCTURE OVERVIEW', 
         ha='center', va='center', fontsize=18, fontweight='bold', color=COLORS['main'])

# Start
create_flowchart_box(ax1, 5.5, 14, 3, 0.8, 'PROJECT START', COLORS['config'], is_oval=True)
create_flowchart_arrow(ax1, 7, 14, 7, 13.2)

# Configuration Files
create_flowchart_box(ax1, 4, 12.2, 6, 1, 'CONFIGURATION FILES\nterraform.tfvars + variables.tf', COLORS['config'])
create_flowchart_arrow(ax1, 7, 12.2, 7, 11.2)

# Main Orchestrator
create_flowchart_box(ax1, 4, 10.2, 6, 1, 'MAIN ORCHESTRATOR\nmain.tf (calls all modules)', COLORS['main'])
create_flowchart_arrow(ax1, 7, 10.2, 7, 9.2)

# Modules Layer
create_flowchart_box(ax1, 1, 8.2, 3, 1, 'NETWORK\nMODULE', COLORS['module'])
create_flowchart_box(ax1, 4.5, 8.2, 3, 1, 'SECURITY\nMODULE', COLORS['module'])
create_flowchart_box(ax1, 8, 8.2, 3, 1, 'IAM\nMODULE', COLORS['module'])
create_flowchart_box(ax1, 11.5, 8.2, 2.5, 1, 'COMPUTE\nMODULE', COLORS['module'])

# Arrows to modules
create_flowchart_arrow(ax1, 6, 9.2, 2.5, 9.2)
create_flowchart_arrow(ax1, 6.5, 9.2, 6, 9.2)
create_flowchart_arrow(ax1, 7.5, 9.2, 9.5, 9.2)
create_flowchart_arrow(ax1, 8, 9.2, 12.75, 9.2)

# GCP Resources
create_flowchart_box(ax1, 1, 6.5, 3, 1, 'GCP NETWORK\nRESOURCES', COLORS['resource'])
create_flowchart_box(ax1, 4.5, 6.5, 3, 1, 'GCP SECURITY\nRESOURCES', COLORS['resource'])
create_flowchart_box(ax1, 8, 6.5, 3, 1, 'GCP IAM\nRESOURCES', COLORS['resource'])
create_flowchart_box(ax1, 11.5, 6.5, 2.5, 1, 'GCP COMPUTE\nRESOURCES', COLORS['resource'])

# Arrows to resources
create_flowchart_arrow(ax1, 2.5, 8.2, 2.5, 7.5)
create_flowchart_arrow(ax1, 6, 8.2, 6, 7.5)
create_flowchart_arrow(ax1, 9.5, 8.2, 9.5, 7.5)
create_flowchart_arrow(ax1, 12.75, 8.2, 12.75, 7.5)

# Outputs
create_flowchart_arrow(ax1, 2.5, 6.5, 6, 5.5)
create_flowchart_arrow(ax1, 6, 6.5, 6.5, 5.5)
create_flowchart_arrow(ax1, 9.5, 6.5, 7.5, 5.5)
create_flowchart_arrow(ax1, 12.75, 6.5, 8, 5.5)

create_flowchart_box(ax1, 4, 4.5, 6, 1, 'OUTPUTS COLLECTION\noutputs.tf', COLORS['output'])
create_flowchart_arrow(ax1, 7, 4.5, 7, 3.5)

# End
create_flowchart_box(ax1, 5.5, 2.5, 3, 0.8, 'DEPLOYMENT\nCOMPLETE', COLORS['config'], is_oval=True)

# Side information
info_box = FancyBboxPatch((0.2, 1), 2, 4,
                         boxstyle="round,pad=0.1",
                         facecolor=COLORS['light_bg'],
                         edgecolor=COLORS['main'], linewidth=2)
ax1.add_patch(info_box)

ax1.text(1.2, 4.5, 'PROJECT INFO', ha='center', fontsize=12, fontweight='bold', color=COLORS['main'])
ax1.text(1.2, 4, '• 4 Modules', ha='center', fontsize=10, color=COLORS['main'])
ax1.text(1.2, 3.6, '• 15+ Resources', ha='center', fontsize=10, color=COLORS['main'])
ax1.text(1.2, 3.2, '• 3-5 min deploy', ha='center', fontsize=10, color=COLORS['main'])
ax1.text(1.2, 2.8, '• $18-24/month', ha='center', fontsize=10, color=COLORS['main'])
ax1.text(1.2, 2.4, '• us-central1', ha='center', fontsize=10, color=COLORS['main'])
ax1.text(1.2, 2, '• Auto-scaling', ha='center', fontsize=10, color=COLORS['main'])
ax1.text(1.2, 1.6, '• Secure setup', ha='center', fontsize=10, color=COLORS['main'])

plt.tight_layout()
plt.savefig('1-project-structure-overview.png', dpi=400, bbox_inches='tight', facecolor='white')

# ============================================================================
# FLOWCHART 2: FILE RELATIONSHIPS & DEPENDENCIES
# ============================================================================

fig2, ax2 = plt.subplots(1, 1, figsize=(16, 14))
ax2.set_xlim(0, 16)
ax2.set_ylim(0, 14)
ax2.axis('off')

# Title
ax2.text(8, 13.5, 'FILE RELATIONSHIPS & DEPENDENCIES', 
         ha='center', va='center', fontsize=18, fontweight='bold', color=COLORS['main'])

# Configuration files
create_flowchart_box(ax2, 1, 11.5, 3, 1, 'terraform.tfvars\n(Values)', COLORS['config'])
create_flowchart_box(ax2, 5, 11.5, 3, 1, 'variables.tf\n(Definitions)', COLORS['config'])
create_flowchart_box(ax2, 9, 11.5, 3, 1, 'provider.tf\n(GCP Setup)', COLORS['config'])
create_flowchart_box(ax2, 13, 11.5, 2.5, 1, 'locals\n(Computed)', COLORS['config'])

# Arrows to main.tf
create_flowchart_arrow(ax2, 2.5, 11.5, 7, 10.5, 'project_id')
create_flowchart_arrow(ax2, 6.5, 11.5, 7.5, 10.5, 'types')
create_flowchart_arrow(ax2, 10.5, 11.5, 8.5, 10.5, 'auth')
create_flowchart_arrow(ax2, 14.25, 11.5, 9, 10.5, 'tags')

# Main.tf
create_flowchart_box(ax2, 6, 9.5, 4, 1, 'main.tf\n(Orchestrator)', COLORS['main'])

# Module files
create_flowchart_box(ax2, 1, 7.5, 3, 1.5, 'modules/network/\n• main.tf\n• variables.tf\n• outputs.tf', COLORS['module'])
create_flowchart_box(ax2, 4.5, 7.5, 3, 1.5, 'modules/security/\n• main.tf\n• variables.tf\n• outputs.tf', COLORS['module'])
create_flowchart_box(ax2, 8, 7.5, 3, 1.5, 'modules/iam/\n• main.tf\n• variables.tf\n• outputs.tf', COLORS['module'])
create_flowchart_box(ax2, 11.5, 7.5, 3, 1.5, 'modules/compute/\n• main.tf\n• variables.tf\n• outputs.tf', COLORS['module'])

# Arrows from main to modules
create_flowchart_arrow(ax2, 7, 9.5, 2.5, 9)
create_flowchart_arrow(ax2, 7.5, 9.5, 6, 9)
create_flowchart_arrow(ax2, 8.5, 9.5, 9.5, 9)
create_flowchart_arrow(ax2, 9, 9.5, 13, 9)

# Inter-module dependencies
create_flowchart_arrow(ax2, 4, 8.25, 4.5, 8.25, 'vpc_name')
create_flowchart_arrow(ax2, 11, 8.25, 11.5, 8.25, 'sa_email')

# Outputs collection
create_flowchart_arrow(ax2, 2.5, 7.5, 7, 6)
create_flowchart_arrow(ax2, 6, 7.5, 7.5, 6)
create_flowchart_arrow(ax2, 9.5, 7.5, 8.5, 6)
create_flowchart_arrow(ax2, 13, 7.5, 9, 6)

create_flowchart_box(ax2, 6, 5, 4, 1, 'outputs.tf\n(Final Results)', COLORS['output'])

# Dependency explanation
dep_box = FancyBboxPatch((0.5, 2), 15, 2.5,
                        boxstyle="round,pad=0.2",
                        facecolor=COLORS['light_bg'],
                        edgecolor=COLORS['main'], linewidth=2)
ax2.add_patch(dep_box)

ax2.text(8, 4, 'DEPENDENCY RELATIONSHIPS', ha='center', fontsize=14, fontweight='bold', color=COLORS['main'])
ax2.text(1, 3.5, '1. terraform.tfvars provides actual values (project_id = "praxis-gear-483220-k4")', fontsize=11, color=COLORS['main'])
ax2.text(1, 3.1, '2. variables.tf defines types and validation rules', fontsize=11, color=COLORS['main'])
ax2.text(1, 2.7, '3. main.tf distributes variables to modules and manages dependencies', fontsize=11, color=COLORS['main'])
ax2.text(1, 2.3, '4. Network module outputs vpc_name → Security module uses it for firewall rules', fontsize=11, color=COLORS['main'])
ax2.text(1, 1.9, '5. IAM module outputs service_account_email → Compute module uses it for VM', fontsize=11, color=COLORS['main'])

plt.tight_layout()
plt.savefig('2-file-relationships.png', dpi=400, bbox_inches='tight', facecolor='white')

# ============================================================================
# FLOWCHART 3: VARIABLE FLOW & DATA PASSING
# ============================================================================

fig3, ax3 = plt.subplots(1, 1, figsize=(14, 18))
ax3.set_xlim(0, 14)
ax3.set_ylim(0, 18)
ax3.axis('off')

# Title
ax3.text(7, 17.5, 'VARIABLE FLOW & DATA PASSING', 
         ha='center', va='center', fontsize=18, fontweight='bold', color=COLORS['main'])

# Start with terraform.tfvars
create_flowchart_box(ax3, 5, 16, 4, 1, 'terraform.tfvars\nproject_id = "praxis-gear..."', COLORS['config'], is_oval=True)
create_flowchart_arrow(ax3, 7, 16, 7, 15)

# Variables.tf
create_flowchart_box(ax3, 4, 14, 6, 1, 'variables.tf\nvariable "project_id" { type = string }', COLORS['config'])
create_flowchart_arrow(ax3, 7, 14, 7, 13)

# Main.tf receives variables
create_flowchart_box(ax3, 4, 12, 6, 1, 'main.tf\nvar.project_id → modules', COLORS['main'])

# Split to modules
create_flowchart_arrow(ax3, 5.5, 12, 2, 11, 'project_id')
create_flowchart_arrow(ax3, 6.5, 12, 5, 11, 'project_id')
create_flowchart_arrow(ax3, 7.5, 12, 9, 11, 'project_id')
create_flowchart_arrow(ax3, 8.5, 12, 12, 11, 'project_id')

# Module variables
create_flowchart_box(ax3, 0.5, 10, 3, 1, 'network/variables.tf\nvar.project_id', COLORS['module'])
create_flowchart_box(ax3, 4, 10, 3, 1, 'security/variables.tf\nvar.project_id', COLORS['module'])
create_flowchart_box(ax3, 7.5, 10, 3, 1, 'iam/variables.tf\nvar.project_id', COLORS['module'])
create_flowchart_box(ax3, 11, 10, 3, 1, 'compute/variables.tf\nvar.project_id', COLORS['module'])

# Module main.tf uses variables
create_flowchart_arrow(ax3, 2, 10, 2, 9)
create_flowchart_arrow(ax3, 5.5, 10, 5.5, 9)
create_flowchart_arrow(ax3, 9, 10, 9, 9)
create_flowchart_arrow(ax3, 12.5, 10, 12.5, 9)

create_flowchart_box(ax3, 0.5, 8, 3, 1, 'network/main.tf\nproject = var.project_id', COLORS['module'])
create_flowchart_box(ax3, 4, 8, 3, 1, 'security/main.tf\nproject = var.project_id', COLORS['module'])
create_flowchart_box(ax3, 7.5, 8, 3, 1, 'iam/main.tf\nproject = var.project_id', COLORS['module'])
create_flowchart_box(ax3, 11, 8, 3, 1, 'compute/main.tf\nproject = var.project_id', COLORS['module'])

# Resources created
create_flowchart_arrow(ax3, 2, 8, 2, 7)
create_flowchart_arrow(ax3, 5.5, 8, 5.5, 7)
create_flowchart_arrow(ax3, 9, 8, 9, 7)
create_flowchart_arrow(ax3, 12.5, 8, 12.5, 7)

create_flowchart_box(ax3, 0.5, 6, 3, 1, 'GCP VPC\nproject: praxis-gear...', COLORS['resource'])
create_flowchart_box(ax3, 4, 6, 3, 1, 'GCP Firewall\nproject: praxis-gear...', COLORS['resource'])
create_flowchart_box(ax3, 7.5, 6, 3, 1, 'GCP Service Account\nproject: praxis-gear...', COLORS['resource'])
create_flowchart_box(ax3, 11, 6, 3, 1, 'GCP VM Instance\nproject: praxis-gear...', COLORS['resource'])

# Outputs flow back
create_flowchart_arrow(ax3, 2, 6, 2, 5, 'vpc_name')
create_flowchart_arrow(ax3, 12.5, 6, 12.5, 5, 'vm_ip')

create_flowchart_box(ax3, 0.5, 4, 3, 1, 'network/outputs.tf\nvpc_name = vpc.name', COLORS['output'])
create_flowchart_box(ax3, 11, 4, 3, 1, 'compute/outputs.tf\nvm_ip = instance.ip', COLORS['output'])

# Inter-module data flow
create_flowchart_arrow(ax3, 3.5, 4.5, 4, 4.5, 'vpc_name')
ax3.text(3.75, 4.8, 'network_name', ha='center', fontsize=10, color=COLORS['arrow'])

# Final outputs
create_flowchart_arrow(ax3, 2, 4, 6, 3)
create_flowchart_arrow(ax3, 12.5, 4, 8, 3)

create_flowchart_box(ax3, 5, 2, 4, 1, 'Root outputs.tf\nAll module outputs', COLORS['output'])

# Variable flow explanation
var_box = FancyBboxPatch((0.5, 0.2), 13, 1.5,
                        boxstyle="round,pad=0.1",
                        facecolor=COLORS['light_bg'],
                        edgecolor=COLORS['main'], linewidth=2)
ax3.add_patch(var_box)

ax3.text(7, 1.4, 'VARIABLE FLOW EXAMPLE', ha='center', fontsize=12, fontweight='bold', color=COLORS['main'])
ax3.text(7, 1, 'project_id flows: tfvars → variables.tf → main.tf → all modules → all GCP resources', 
         ha='center', fontsize=11, color=COLORS['main'])
ax3.text(7, 0.6, 'vpc_name flows: network module → main.tf → security module (for firewall rules)', 
         ha='center', fontsize=11, color=COLORS['main'])

plt.tight_layout()
plt.savefig('3-variable-flow.png', dpi=400, bbox_inches='tight', facecolor='white')

# ============================================================================
# FLOWCHART 4: MODULE INTERACTIONS
# ============================================================================

fig4, ax4 = plt.subplots(1, 1, figsize=(16, 12))
ax4.set_xlim(0, 16)
ax4.set_ylim(0, 12)
ax4.axis('off')

# Title
ax4.text(8, 11.5, 'MODULE INTERACTIONS & DEPENDENCIES', 
         ha='center', va='center', fontsize=18, fontweight='bold', color=COLORS['main'])

# Main.tf at center
create_flowchart_box(ax4, 6.5, 5.5, 3, 1, 'main.tf\nOrchestrator', COLORS['main'])

# Modules around main.tf
create_flowchart_box(ax4, 2, 9, 3, 1.5, 'NETWORK MODULE\n• Creates VPC\n• Creates Subnet\n• Creates NAT', COLORS['module'])
create_flowchart_box(ax4, 11, 9, 3, 1.5, 'SECURITY MODULE\n• Creates Firewall\n• Uses VPC from Network\n• SSH/HTTP rules', COLORS['module'])
create_flowchart_box(ax4, 2, 2, 3, 1.5, 'IAM MODULE\n• Creates Service Account\n• Creates Workload Identity\n• Sets permissions', COLORS['module'])
create_flowchart_box(ax4, 11, 2, 3, 1.5, 'COMPUTE MODULE\n• Creates VM Instance\n• Uses Subnet from Network\n• Uses SA from IAM', COLORS['module'])

# Arrows from main to modules
create_flowchart_arrow(ax4, 7, 6.5, 4, 9, 'variables')
create_flowchart_arrow(ax4, 8.5, 6.5, 12, 9, 'variables')
create_flowchart_arrow(ax4, 7, 5.5, 4, 3.5, 'variables')
create_flowchart_arrow(ax4, 8.5, 5.5, 12, 3.5, 'variables')

# Inter-module dependencies
create_flowchart_arrow(ax4, 5, 9.75, 11, 9.75, 'vpc_name')
ax4.text(8, 10.1, 'Network → Security', ha='center', fontsize=10, fontweight='bold', color=COLORS['arrow'])

create_flowchart_arrow(ax4, 4, 2.75, 11, 2.75, 'service_account_email')
ax4.text(7.5, 3.1, 'IAM → Compute', ha='center', fontsize=10, fontweight='bold', color=COLORS['arrow'])

# Dependency explanation
dep_box = FancyBboxPatch((0.5, 0.2), 15, 1.3,
                        boxstyle="round,pad=0.1",
                        facecolor=COLORS['light_bg'],
                        edgecolor=COLORS['main'], linewidth=2)
ax4.add_patch(dep_box)

ax4.text(8, 1.2, 'EXECUTION ORDER & DEPENDENCIES', ha='center', fontsize=12, fontweight='bold', color=COLORS['main'])
ax4.text(8, 0.8, '1. Network Module runs first (creates foundation)', ha='center', fontsize=11, color=COLORS['main'])
ax4.text(8, 0.5, '2. Security & IAM modules run in parallel (use network outputs)', ha='center', fontsize=11, color=COLORS['main'])
ax4.text(8, 0.2, '3. Compute Module runs last (needs both network and IAM outputs)', ha='center', fontsize=11, color=COLORS['main'])

plt.tight_layout()
plt.savefig('4-module-interactions.png', dpi=400, bbox_inches='tight', facecolor='white')

# ============================================================================
# FLOWCHART 5: COMPLETE EXECUTION FLOW
# ============================================================================

fig5, ax5 = plt.subplots(1, 1, figsize=(12, 20))
ax5.set_xlim(0, 12)
ax5.set_ylim(0, 20)
ax5.axis('off')

# Title
ax5.text(6, 19.5, 'COMPLETE TERRAFORM EXECUTION FLOW', 
         ha='center', va='center', fontsize=16, fontweight='bold', color=COLORS['main'])

# Execution steps
steps = [
    ('START', COLORS['config'], True),
    ('terraform init\n(Download providers)', COLORS['config'], False),
    ('Load terraform.tfvars\n(project_id, region, etc.)', COLORS['config'], False),
    ('Validate variables.tf\n(Check types & rules)', COLORS['config'], False),
    ('Initialize GCP Provider\n(Authenticate & connect)', COLORS['main'], False),
    ('Execute main.tf\n(Start orchestration)', COLORS['main'], False),
    ('Call Network Module\n(Create VPC, Subnet, NAT)', COLORS['module'], False),
    ('Call Security Module\n(Create Firewall rules)', COLORS['module'], False),
    ('Call IAM Module\n(Create Service Accounts)', COLORS['module'], False),
    ('Call Compute Module\n(Create VM Instance)', COLORS['module'], False),
    ('Collect Module Outputs\n(IPs, names, etc.)', COLORS['output'], False),
    ('Generate outputs.tf\n(Final results)', COLORS['output'], False),
    ('Update terraform.state\n(Save current state)', COLORS['main'], False),
    ('DEPLOYMENT COMPLETE', COLORS['config'], True)
]

y_pos = 18.5
for i, (text, color, is_oval) in enumerate(steps):
    create_flowchart_box(ax5, 3, y_pos, 6, 0.8, text, color, is_oval)
    if i < len(steps) - 1:
        create_flowchart_arrow(ax5, 6, y_pos, 6, y_pos - 0.5)
    y_pos -= 1.3

# Timing information
timing_box = FancyBboxPatch((0.2, 1), 2, 16,
                           boxstyle="round,pad=0.1",
                           facecolor=COLORS['light_bg'],
                           edgecolor=COLORS['main'], linewidth=2)
ax5.add_patch(timing_box)

ax5.text(1.2, 16.5, 'TIMING', ha='center', fontsize=12, fontweight='bold', color=COLORS['main'])

timings = ['0s', '10s', '15s', '20s', '30s', '40s', '100s', '130s', '175s', '265s', '270s', '275s', '280s', '285s']
timing_y = 18.1
for timing in timings:
    ax5.text(1.2, timing_y, timing, ha='center', fontsize=10, color=COLORS['main'])
    timing_y -= 1.3

# Resource count
resource_box = FancyBboxPatch((9.8, 1), 2, 16,
                             boxstyle="round,pad=0.1",
                             facecolor=COLORS['light_bg'],
                             edgecolor=COLORS['main'], linewidth=2)
ax5.add_patch(resource_box)

ax5.text(10.8, 16.5, 'RESOURCES', ha='center', fontsize=12, fontweight='bold', color=COLORS['main'])

resources = ['0', '0', '0', '0', '0', '0', '4', '8', '12', '15', '15', '15', '15', '15']
resource_y = 18.1
for resource in resources:
    ax5.text(10.8, resource_y, resource, ha='center', fontsize=10, color=COLORS['main'])
    resource_y -= 1.3

plt.tight_layout()
plt.savefig('5-complete-execution-flow.png', dpi=400, bbox_inches='tight', facecolor='white')

print("✅ COMPLETE TERRAFORM UNDERSTANDING FLOWCHARTS CREATED!")
print("=" * 60)
print("📁 Files Generated:")
print("   ✅ 1-project-structure-overview.png")
print("   ✅ 2-file-relationships.png")
print("   ✅ 3-variable-flow.png")
print("   ✅ 4-module-interactions.png")
print("   ✅ 5-complete-execution-flow.png")
print("\n🎯 COMPLETE PROJECT UNDERSTANDING:")
print("   ✅ Overall project structure and flow")
print("   ✅ How files relate and depend on each other")
print("   ✅ Variable flow and data passing")
print("   ✅ Module interactions and dependencies")
print("   ✅ Complete execution timeline")
print("   ✅ Easy to understand concepts")
print("   ✅ Perfect for learning and presentations")

plt.show()