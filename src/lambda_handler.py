from generate import generate_toplist_csv, make_s3_key
from utils import get_env
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client('s3')

def handler(event, context):
    bucket = get_env("OUTPUT_BUCKET", required=True)
    prefix = get_env("OUTPUT_PREFIX", default="results/")

    csv_text = generate_toplist_csv()
    key = make_s3_key(prefix)

    s3.put_object(Bucket=bucket, Key=key, Body=csv_text.encode("utf-8"))
    logger.info("Wrote %d bytes to s3://%s/%s", len(csv_text), bucket, key)

    return {"status": "ok", "bucket": bucket, "key": key, "bytes": len(csv_text)}
