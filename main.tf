provider "google" {
    project = var.project
    region  = var.region
    zone    = var.zone
}

resource "google_compute_instance" "vm_instance" {
    name         = "terraform-instance"
    machine_type = "f1-micro"

    boot_disk {
        initialize_params {
            image = "debian-cloud/debian-9"
        }
    }
    network_interface {
    # A default network is created for all GCP projects
    network = google_compute_network.vpc_network.self_link
    access_config {}
    }
    }

resource "google_compute_network" "vpc_network" {
    name                    = "terraform-network"
    auto_create_subnetworks = "true"
}

resource "google_spanner_instance" "projetCloud" {
  config       = "regional-europe-west1"
  display_name = "Database Insta"
  processing_units    = 100
}

resource "google_spanner_database" "database" {
  instance = google_spanner_instance.projetCloud.name
  name     = "database-insta-scrapping"  
  ddl = [
      "CREATE TABLE Media (id STRING(MAX) NOT NULL, account_id INT64 NOT NULL, tags ARRAY<STRING(MAX)> NOT NULL, id_media INT64 NOT NULL, date DATE, nb_comments INT64, nb_likes INT64, link STRING(MAX), caption STRING(MAX), type STRING(MAX)) PRIMARY KEY (id)",
      "CREATE TABLE Account (id STRING(MAX) NOT NULL, account_id INT64 NOT NULL, username STRING(MAX) NOT NULL,  nb_followers INT64, nb_following INT64, nb_medias INT64, is_verified BOOL, is_private BOOL) PRIMARY KEY (id)",
      "CREATE TABLE Comments (id STRING(MAX) NOT NULL, id_media INT64 NOT NULL, username STRING(MAX) NOT NULL, date DATE, content STRING(MAX)) PRIMARY KEY (id)",
      "CREATE TABLE Tag (id STRING(MAX) NOT NULL, tag_name STRING(MAX) NOT NULL, nb_followers INT64, nb_medias INT64) PRIMARY KEY (id)"
  ]
  deletion_protection = false
}
