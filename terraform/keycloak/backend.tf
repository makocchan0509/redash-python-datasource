terraform {
  backend "gcs" {
    bucket = "terraform-masem"
    prefix = "redash-keycloak-state"
  }
}
