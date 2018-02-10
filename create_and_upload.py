""" create_and_upload.py

Usage:
    create_and_upload [--ip=<ip_address>] [--user=<username>] [--passowrd=<password>] [--bucket=<bucket_name>] [--filename=<filename>]

"""

import os
import docopt
import tempfile

from builder import build_html
from s3 import upload_html, AWSCredentials

if __name__ == "__main__":

    args = docopt.docopt(__doc__)

    credentials = AWSCredentials(os.getenv("AWS_ACCESS_KEY_ID"), os.getenv("AWS_SECRET_ACCESS_KEY"))

    ip_address = args.get("<ip_address>", os.environ["MEDIA_CENTRE_IP"])

    username = args.get("<username>", os.environ["MEDIA_CENTRE_USER"])
    password = args.get("<password>", os.environ["MEDIA_CENTRE_PASSWORD"])
    bucket_name = args.get("<bucket_name>", os.environ["S3_BUCKET_NAME"])
    filename = args.get("<filename>", os.environ["FILENAME"])

    print("Building HTML...")
    html = build_html(ip_address, username, password)
    
    with open(filename, 'w') as f:
        f.write(html)
    
    print("Uploading to {}...".format(bucket_name))
    upload_html(bucket_name, filename, credentials)
