import boto3
import pandas as pd
from io import StringIO
from config import S3_BUCKET, S3_PREFIX, AWS_REGION

def extract_from_s3():
    """Extract CSV files from an S3 bucket and combine them into one DataFrame."""
    s3 = boto3.client('s3', region_name=AWS_REGION)
    objs = s3.list_objects_v2(Bucket=S3_BUCKET, Prefix=S3_PREFIX)
    all_data = []
    for obj in objs.get("Contents", []):
        key = obj["Key"]
        if key.endswith(".csv"):
            print(f"📥 Reading {key} from S3...")
            file = s3.get_object(Bucket=S3_BUCKET, Key=key)
            df = pd.read_csv(file["Body"])
            all_data.append(df)
    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)
        print(f"✅ Extracted {len(combined_df)} rows from S3.")
        return combined_df
    print("⚠️ No CSV files found in S3.")
    return pd.DataFrame()
