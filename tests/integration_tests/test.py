import boto3

from response.list_buckets_response import ListBucketsResponse


service = "s3"
client = boto3.client(service, region_name="us-east-2")
buckets = client.list_buckets()
buckets_object = ListBucketsResponse(**buckets)


for buck in buckets_object.Buckets:
    print(buck.Name)
    print(type(buck.CreationDate))

print(buckets_object.model_dump_json(indent=3))
