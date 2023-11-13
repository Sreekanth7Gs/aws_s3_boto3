import boto3

def find_buckets_with_file(filename):
    s3 = boto3.client('s3')

    try:
        response = s3.list_buckets()
        buckets = [bucket['Name'] for bucket in response['Buckets']]
        print(f"All Buckets: {buckets}")  
        buckets_with_file = []
        for bucket in buckets:
            try:
                s3.head_object(Bucket=bucket, Key=filename)
                buckets_with_file.append(bucket)
            except s3.exceptions.ClientError as e:
               
                if e.response['Error']['Code'] != '404':
                    raise
                
        if buckets_with_file:
            print(f"The file '{filename}' is present in the following buckets:")
            for bucket in buckets_with_file:
                print(bucket)
        else:
            print(f"The file '{filename}' is not found in any S3 bucket.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    filename = input("Enter the filename to search: ")
    find_buckets_with_file(filename)
