terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "queue_name" {
  type    = string
  default = "fraud-master-bank-queue"
}

resource "aws_sqs_queue" "fraud_queue" {
  name                      = var.queue_name
  message_retention_seconds = 1209600
}

output "queue_url" {
  value = aws_sqs_queue.fraud_queue.id
}