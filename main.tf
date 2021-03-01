# Terraform block
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 2.70"
    }
  }
}

# Providers
provider "aws" {
  profile = "default"
  region  = "eu-central-1"
}

# Resources
# AWS Lightsail instance
resource "aws_lightsail_instance" "bf_lightsail" {
  name              = "blockchain_frontier_bot"
  availability_zone = "eu-central-1"
  blueprint_id      = "ubuntu_20_04"
  bundle_id         = "micro_2_0"
  key_pair_name     = "blockchain-frontier-bot"
}