provider "helm" {
  kubernetes {
    config_path = "~/.kube/config"
    config_context = "gke_avid-math-376819_asia-south1-a_altair"
  }
}

resource "helm_release" "freya" {

  name       = "freya"

  chart      = "./freya"

}