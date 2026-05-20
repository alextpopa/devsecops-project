package dockerfile.security

import rego.v1

deny contains msg if {
    input.runs_as_root == true
    msg := "Container must not run as root user"
}

deny contains msg if {
    input.debug_mode == true
    msg := "Flask debug mode must be disabled in production"
}

deny contains msg if {
    input.hardcoded_secrets == true
    msg := "Hardcoded secrets detected in source code"
}

deny contains msg if {
    input.base_image == "python:latest"
    msg := "Must use specific image version, not 'latest'"
}
