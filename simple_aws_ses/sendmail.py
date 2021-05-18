#configure SES on AWS by verifying the identities, also send mail from your domain by verifying the identity of the domain
import boto3
ses = boto3.client('ses')
FROM_EMAIL_ADDRESS=input("Enter sender email: \n")
TO_EMAIL_ADDRESS=input("Enter reciever email: \n")
SUBJECT=input("Enter subject: \n")
TEXT=input("Enter email: \n")

ses.send_email(Source=FROM_EMAIL_ADDRESS,Destination={ 'ToAddresses':(TO_EMAIL_ADDRESS,)},Message={'Subject':{'Data': SUBJECT},'Body': {'Text': {'Data': TEXT }}})
