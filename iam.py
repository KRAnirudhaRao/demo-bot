import boto3

client = boto3.client('iam')

response=client.list_users()
users=response['Users']
for user in response:
    print(user['UserName'])
    

