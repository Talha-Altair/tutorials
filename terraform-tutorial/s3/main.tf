terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region     = "ap-south-1"
  access_key = var.access_key
  secret_key = var.secret_key
}

resource "aws_s3_bucket" "altair" {
  bucket = "talha-altair-27"
  tags = {
    "num" = var.num_var
  }
}

resource "aws_instance" "ezio" {
  ami           = "ami-0f8ca728008ff5af4"
  instance_type = "t2.micro"
  tags = {
    "num" = var.num_var
  }
  key_name = "course-altair"
}
