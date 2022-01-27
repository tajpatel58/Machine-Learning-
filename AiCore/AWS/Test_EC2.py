import boto3 

ai_core_bucket = boto3.resource('s3').Bucket('aicore-prac')

ai_core_bucket.download_file('Data/Name_Age.csv', 'Name_Age_2.csv')