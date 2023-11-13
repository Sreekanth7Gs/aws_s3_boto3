import boto3
def list_s3_buckets():
    try:
        s3 = boto3.client('s3')
        response = s3.list_buckets()
        if 'Buckets' in response:
            print("Available S3 buckets:")
            for index, bucket in enumerate(response['Buckets']):
                print(f"{index + 1}. {bucket['Name']}")
        else:
            print("No S3 buckets found.")
    except Exception as e:
        print(f"Error listing S3 buckets: {e}")

def list_files_s3bucket(bucket_name):
    try :
        s3 = boto3.client('s3')
        response = s3.list_objects(Bucket=bucket_name)
        if 'Contents' in response:
            print(f"files in the {bucket_name} bucket: ")
            for obj in response['Contents']:
                print(obj['Key'])
        else:
            print(f"the {bucket_name} bucket is empty")
    except Exception as e:
        print(f"error: {e}")
if __name__ == "__main__" :
   list_s3_buckets()
   bucket_name =  input("Enter the s3 bucket name: ")   
    
list_files_s3bucket(bucket_name)                 
    