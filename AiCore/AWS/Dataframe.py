import pandas as pd
import boto3

data = pd.DataFrame([['Taj', 23], ['Radhika',24]], columns=['Name', 'Age'])

data.to_csv('Name_Age.csv', mode='a', index=False, header=False)

bucket = boto3.resource('s3').Bucket('aicore-prac')

bucket.upload_file('Name_Age.csv', 'Data/Name_Age.csv')