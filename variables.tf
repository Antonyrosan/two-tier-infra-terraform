variable "aws_region" {
  description = "The AWS region to deploy resources in"
  default     = "us-east-1"
}

variable "aws_profile" {
  description = "The AWS CLI named profile to use"
  default     = "default"
}

variable "vpc_cidr" {
  description = "CIDR block for the main VPC"
  default     = "10.0.0.0/16"
}

variable "public_subnet_cidr" {
  description = "CIDR block for the public subnet"
  default     = "10.0.1.0/24"
}

variable "private_subnet_a_cidr" {
  description = "CIDR block for private subnet A"
  default     = "10.0.2.0/24"
}

variable "private_subnet_b_cidr" {
  description = "CIDR block for private subnet B"
  default     = "10.0.3.0/24"
}

variable "key_name" {
  description = "Name of the existing EC2 Key Pair to use for SSH access"
  default     = "loginkey"
}

variable "db_username" {
  description = "Username for the RDS MySQL instance"
  default     = "admin"
}

variable "db_password" {
  description = "Password for the RDS MySQL instance"
  sensitive   = true
  default     = "Rosan0705"
}
