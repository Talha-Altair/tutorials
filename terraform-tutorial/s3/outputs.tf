
output "hosted_zone_id" {
  value = aws_s3_bucket.altair.hosted_zone_id
}

output "ip" {
  value = aws_instance.ezio.public_ip
}