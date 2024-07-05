import boto3
from list_buckets_output import ListBucketsResponse

service = "s3"
bucket_name = "jira-tickets-dba"
client = boto3.client(service, region_name="us-east-2")
# response = client.list_bucket_analytics_configurations(Bucket=bucket_name)
# buckets_model = IsTruncated(**response)
buckets = client.list_buckets()
buckets_model = ListBucketsResponse(**buckets)
print(buckets_model.Buckets[0].Name)
print(buckets_model)
# buckets_model.Buckets[1].CreationDate