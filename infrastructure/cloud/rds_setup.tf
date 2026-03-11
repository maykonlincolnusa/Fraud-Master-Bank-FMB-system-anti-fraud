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

variable "db_name" {
  type    = string
  default = "fraudmaster"
}

variable "db_username" {
  type    = string
  default = "fraudmaster"
}

variable "db_password" {
  type      = string
  sensitive = true
}

variable "db_subnet_group" {
  type        = string
  description = "Existing DB subnet group name"
}

variable "db_security_groups" {
  type        = list(string)
  description = "List of security group IDs"
}

resource "aws_db_instance" "fraud_db" {
  identifier              = "fraud-master-bank-db"
  allocated_storage       = 20
  engine                  = "postgres"
  engine_version          = "15"
  instance_class          = "db.t3.micro"
  db_name                 = var.db_name
  username                = var.db_username
  password                = var.db_password
  skip_final_snapshot     = true
  db_subnet_group_name    = var.db_subnet_group
  vpc_security_group_ids  = var.db_security_groups
}

output "db_endpoint" {
  value = aws_db_instance.fraud_db.address
}