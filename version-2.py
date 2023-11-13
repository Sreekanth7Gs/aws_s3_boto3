import boto3
import sys

def list_files_in_bucket(bucket_name):
    s3 = boto3.client('s3')
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)

        if "Contents" in response:
            print(f"Files in the '{bucket_name}' bucket:")
            for obj in response['Contents']:
                print(obj['Key'])
        else:
            print(f"The bucket '{bucket_name}' is empty.")
    except s3.exceptions.NoSuchBucket as e:
        print(f"Error: The bucket '{bucket_name}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <bucket_name>")
    else:
        bucket_name = sys.argv[1]
        list_files_in_bucket(bucket_name)
