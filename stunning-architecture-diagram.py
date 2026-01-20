#!/usr/bin/env python3
"""
Enhanced Stunning Modern GCP Terraform Architecture Diagram
Creates a beautiful, modern architecture diagram with latest authentication features
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.compute import ComputeEngine
from diagrams.gcp.network import VPC
from diagrams.gcp.security import Iam
from diagrams.gcp.storage import GCS
from diagrams.gcp.devtools import SourceRepositories
from diagrams.onprem.ci import GithubActions
from diagrams.onprem.client import Users
from diagrams.onprem.iac import Terraform

# Custom styling for modern look
graph_attr = {
    "fontsize": "16",
    "fontname": "Arial Bold",
    "bgcolor": "transparent",
    "dpi": "300",
    "pad": "1.0",
    "splines": "curved",
    "concentrate": "true",
    "rankdir": "TB",
    "nodesep": "1.5",
    "ranksep": "2.0"
}

node_attr = {
    "fontsize": "12",
    "fontname": "Arial",
    "style": "filled,rounded",
    "fillcolor": "white",
    "color": "#2196F3",
    "penwidth": "2"
}

edge_attr = {
    "fontsize": "10",
    "fontname": "Arial",
    "color": "#1976D2",
    "penwidth": "2",
    "arrowsize": "1.2"
}

with Diagram(
    "🚀 Enterprise GCP Terraform Infrastructure - Enhanced Authentication",
    filename="stunning-architecture",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr
):
    
    # Developer and CI/CD Layer
    with Cluster("👨‍💻 Development & CI/CD", graph_attr={"bgcolor": "#E3F2FD", "style": "rounded,filled"}):
        developer = Users("Developer\n(rksuraj@learningmyway.space)")
        github = SourceRepositories("GitHub Repository\n(surajkmr39-lang/GCP-Terraform)")
        github_actions = GithubActions("GitHub Actions\n(WIF Authentication)")
        terraform_cli = Terraform("Terraform CLI\n(Multi-Auth Strategy)")
    
    # Enhanced Authentication Layer
    with Cluster("🔐 Enhanced Authentication Infrastructure", graph_attr={"bgcolor": "#F3E5F5", "style": "rounded,filled"}):
        # WIF Components
        wif_pool = Iam("Workload Identity Pool\n(github-actions-pool)")
        wif_provider = Iam("WIF Provider\n(github-actions)")
        github_sa = Iam("GitHub Actions SA\n(github-actions-sa)")
        
        # Production Service Account (NEW)
        prod_sa = Iam("Production SA\n(terraform-prod-sa)\n🆕 NEW")
        
        # State Storage
        gcs_state = GCS("Terraform State\n(Remote Backend)\nGCS Bucket")
    
    # Multi-Environment Infrastructure with Authentication Methods
    environments = []
    env_configs = [
        ("Development", "#E8F5E8", "10.10.0.0/16", "34.59.39.203", "ADC Auth", "✅ DEPLOYED"),
        ("Staging", "#FFF3E0", "10.20.0.0/16", "Ready", "Standard Auth", "🔄 READY"),
        ("Production", "#FFEBEE", "10.30.0.0/16", "Ready", "Impersonation", "🔐 ENHANCED")
    ]
    
    for env_name, bg_color, cidr, status, auth_method, deploy_status in env_configs:
        with Cluster(f"🌐 {env_name} Environment", graph_attr={"bgcolor": bg_color, "style": "rounded,filled"}):
            vpc = VPC(f"{env_name.lower()}-vpc\n({cidr})")
            vm = ComputeEngine(f"{env_name.lower()}-vm\n({status})\n{deploy_status}")
            auth_label = Iam(f"Auth: {auth_method}")
            
            vpc >> Edge(label="hosts", style="dashed") >> vm
            auth_label >> Edge(label="secures", color="#9C27B0") >> vm
            environments.append((vpc, vm, auth_label))
    
    # SSL/TLS Documentation Layer (NEW)
    with Cluster("🌐 SSL/TLS Security Suite", graph_attr={"bgcolor": "#E8F5E8", "style": "rounded,filled"}):
        ssl_docs = SourceRepositories("SSL/TLS Documentation\nlearningmyway.space")
        ssl_viewer = SourceRepositories("Interactive SSL Guide\n(Web Interface)")
        ssl_flowcharts = SourceRepositories("Visual Flowcharts\n(Process Diagrams)")
    
    # Enhanced connections with beautiful styling
    developer >> Edge(label="💻 commits", color="#FF9800", style="bold") >> github
    github >> Edge(label="🔄 triggers", color="#2196F3", style="bold") >> github_actions
    
    # WIF Authentication Flow
    github_actions >> Edge(label="🔑 authenticates", color="#9C27B0", style="bold") >> wif_pool
    wif_pool >> Edge(label="🎭 provides identity", color="#9C27B0") >> wif_provider
    wif_provider >> Edge(label="🔐 impersonates", color="#9C27B0") >> github_sa
    
    # Production Impersonation (NEW)
    developer >> Edge(label="🏭 impersonates", color="#E91E63", style="bold") >> prod_sa
    prod_sa >> Edge(label="🔐 secures prod", color="#E91E63") >> environments[2][2]  # Production auth
    
    # Terraform and State Management
    terraform_cli >> Edge(label="📊 stores state", color="#FF5722", style="bold") >> gcs_state
    github_actions >> Edge(label="🚀 deploys", color="#4CAF50", style="bold") >> terraform_cli
    developer >> Edge(label="🖥️ local dev", color="#2196F3") >> terraform_cli
    
    # Connect to environments with different authentication methods
    for i, (vpc, vm, auth) in enumerate(environments):
        if i == 0:  # Development - ADC
            terraform_cli >> Edge(label="🏗️ ADC auth", color="#4CAF50") >> vpc
        elif i == 1:  # Staging - Standard
            terraform_cli >> Edge(label="🔄 standard", color="#FF9800", style="dashed") >> vpc
        else:  # Production - Impersonation
            prod_sa >> Edge(label="🔐 impersonation", color="#E91E63", style="bold") >> vpc
    
    # SSL/TLS Documentation connections (NEW)
    ssl_docs >> Edge(label="📚 guides", color="#4CAF50") >> ssl_viewer
    ssl_viewer >> Edge(label="🎨 visualizes", color="#4CAF50") >> ssl_flowcharts

print("✨ Enhanced stunning architecture diagram generated successfully!")
print("📁 Files created:")
print("   • stunning-architecture.png (High-resolution image with latest features)")
print("   • stunning-architecture.pdf (Presentation ready)")
print("   • stunning-architecture.svg (Scalable vector)")
print("")
print("🆕 New features included:")
print("   • Multi-environment authentication strategy")
print("   • Production service account impersonation")
print("   • SSL/TLS documentation suite")
print("   • Current deployment status")
print("   • Enhanced security patterns")