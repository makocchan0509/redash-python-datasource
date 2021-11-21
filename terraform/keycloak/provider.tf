terraform {
  required_providers {
    keycloak = {
      source  = "mrparkers/keycloak"
      version = "3.5.1"
    }
  }
}

provider "keycloak" {
  client_id     = "admin-cli"
  username      = var.keycloak-username
  password      = var.keycloak-password
  url           = var.keycloak-url
}