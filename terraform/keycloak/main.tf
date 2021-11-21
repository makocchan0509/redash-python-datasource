resource "keycloak_realm" "frontend" {
  realm = "sandbox"
  enabled = "true"
  attributes      = {
    frontendUrl = "https://localhost:38080/auth"
  }
}

resource "keycloak_openid_client" "root-app" {
  realm_id  = keycloak_realm.frontend.id
  client_id = "root-app"
  enabled = true
  access_type = "PUBLIC"
  valid_redirect_uris = [
    "https://root-web.masemfordev.com/*"
  ]
  standard_flow_enabled = true
  direct_access_grants_enabled  = true
  web_origins = [
    "*"
  ]
}

resource "keycloak_openid_client" "second-app" {
  realm_id  = keycloak_realm.frontend.id
  client_id = "second-app"
  enabled = true
  access_type = "PUBLIC"
  valid_redirect_uris = [
    "https://second-web.masemfordev.com/*"
  ]
  standard_flow_enabled = true
  direct_access_grants_enabled  = true
  web_origins = [
    "*"
  ]
}

resource "keycloak_openid_client" "third-app" {
  realm_id  = keycloak_realm.frontend.id
  client_id = "third-app"
  enabled = true
  access_type = "PUBLIC"
  valid_redirect_uris = [
    "https://third-web.masemfordev.com/*"
  ]
  standard_flow_enabled = true
  direct_access_grants_enabled  = true
  web_origins = [
    "*"
  ]
}

resource "keycloak_user" "demo-user" {
  realm_id   = keycloak_realm.frontend.id
  username   = "demo-user"
  enabled    = true

  first_name = "Makoto"
  last_name  = "Mase"

  initial_password {
    value     = "password"
    temporary = false
  }
}