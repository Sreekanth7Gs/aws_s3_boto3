import boto3

def list_files_s3bucket(bucket_name):
    s3 = boto3.client('s3')
    try :
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
   bucket_name =  input("Enter the s3 bucket name: ")   
    
list_files_s3bucket(bucket_name)                 
    