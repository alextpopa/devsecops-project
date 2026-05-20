# DevSecOps Project - Secure CI/CD Pipeline

![Security Pipeline](https://github.com/alextpopa/devsecops-project/actions/workflows/security-pipeline.yml/badge.svg)

## Description
A comprehensive DevSecOps pipeline integrating security practices at every stage of the software development lifecycle (Shift Left Security).

## Technologies Used
- **SAST**: Bandit (static analysis for Python code)
- **SCA**: pip-audit (dependency CVE scanning)
- **Secrets Scanning**: Gitleaks (detecting hardcoded secrets)
- **Container Security**: Trivy (Docker image vulnerabilities)
- **Secrets Management**: HashiCorp Vault
- **Policy-as-Code**: OPA (Open Policy Agent)
- **CI/CD**: GitHub Actions

## Pipeline
On every Push/PR, 5 automated security jobs are executed:
1. Secrets Scanning (Gitleaks)
2. SAST (Bandit)
3. SCA (pip-audit)
4. Container Scan (Trivy)
5. Policy-as-Code (OPA)

## Local Setup

# Clone the repository
git clone https://github.com/alextpopa/devsecops-project.git

# Start Vault
docker run -d --name vault-dev --cap-add IPC_LOCK \
  -p 8200:8200 -e VAULT_DEV_ROOT_TOKEN_ID=dev-root-token hashicorp/vault:latest

# Add secrets to Vault
vault kv put secret/devsecops-app secret_key=... db_password=...

# Run the application
pip install -r app/requirements.txt
python app/app.py
