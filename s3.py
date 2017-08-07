import boto3

import os
import sys

def get_s3_resource(aws_access_key_id, aws_secret_access_key):

	session = boto3.session.Session(region_name='eu-central-1')
	return session.resource('s3',
		config= boto3.session.Config(signature_version='s3v4'),
		aws_access_key_id=aws_access_key_id,
		aws_secret_access_key=aws_secret_access_key					
	)

if __name__ == "__main__":

	bucket_name = sys.argv[1]
	file_to_upload = sys.argv[2]

	aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
	aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")

	res = get_s3_resource(aws_access_key_id, aws_secret_access_key)
	bucket = res.Bucket(bucket_name)

	with open(file_to_upload, 'rb') as f:
		bucket.put_object(Key=file_to_upload, Body=f, ACL="public-read", ContentType='text/html')
