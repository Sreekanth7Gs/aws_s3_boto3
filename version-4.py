import boto3

def get_bucket_region(bucket_name):
    try:
        s3 = boto3.client('s3')
        location = s3.get_bucket_location(Bucket=bucket_name)
        region = location.get('LocationConstraint', 'us-east-1') 
        return region
    except Exception as e:
        print(f"Error getting region for bucket {bucket_name}: {e}")
        return None

def list_s3_buckets():
    try:
      s3 = boto3.client('s3')
      response = s3.list_buckets()
      with open(output_file, 'w') as file:
        if "Buckets" in response:
            file.write("S3 Buckets and their Regions:\n")
            for index, bucket in enumerate(response['Buckets']):
                bucket_name = bucket['Name']
                region = get_bucket_region(bucket_name)
                file.write(f"{index + 1}. Bucket: {bucket_name}, Region: {region}\n")
        else:
            print("No S3 Buckets are found")
    except Exception as e:
        print(f"Error listing S3 buckets: {e}")

if __name__ == "__main__":
    output_file = "s3_buckets_output.txt"
    list_s3_buckets()
