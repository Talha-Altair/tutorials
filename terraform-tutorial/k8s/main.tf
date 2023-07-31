provider "kubernetes" {
  config_path    = "~/.kube/config"
  config_context = "gke_avid-math-376819_asia-south1-a_altair"
}

resource "kubernetes_namespace" "altair" {
  metadata {
    name = "altair"
  }
}

resource "kubernetes_deployment" "loki" {
  metadata {
    name = "loki"
    labels = {
      test = "loki"
    }
    namespace = "altair"
  }

  spec {
    replicas = 3

    selector {
      match_labels = {
        test = "loki"
      }
    }

    template {
      metadata {
        labels = {
          test = "loki"
        }
      }

      spec {
        container {
          image = "nginx:1.21.6"
          name  = "loki"

        }
      }
    }
  }
}

resource "kubernetes_service" "loki" {
  metadata {
    name      = "loki"
    namespace = "altair"
  }

  spec {
    selector = {
      test = "loki"
    }
    port {
      protocol    = "TCP"
      port        = 80
      target_port = 80
    }
    type = "LoadBalancer"
  }
}
