import boto3
from dist.list_buckets_response import ListBucketsResponse


service = "s3"
client = boto3.client(service, region_name="us-east-2")
buckets = client.list_buckets()
buckets_object = ListBucketsResponse(**buckets)
for buck in buckets_object.Buckets:
    print(buck.Name)
