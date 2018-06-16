import boto3

# simple script to receive API POST requests and add users to SES subscribers within AWS
# setup the SNS connection
client = boto3.client('sns')
topic_arn = ''

def lambda_handler(event, context):
    # grab email and API resource path
    email = event['body-json']['email']
    resourcePath = event['context']['resource-path']


    # check resource and subscribe/unsubscribe the user based on it
    if resourcePath == "/subscribe":
        # add the email to the SNS topic specified by ARN
        client.subscribe(TopicArn=topic_arn, Protocol="email", Endpoint=email)
        return "Hey there, your email " + email + " is now subscribed to bad jokes!"
    elif resourcePath == "/unsubscribe":
        
        a = client.list_subscriptions()
        print a 
        for each in a['Subscriptions']:
            print each['Endpoint']
            if email == each['Endpoint']:
                client.unsubscribe(SubscriptionArn=each['SubscriptionArn'])
                print "Hey, I found you! You're " + each['Endpoint'] + ", right?"
        
        
        
        
        # remove the email to the SNS topic specified by ARN
        #client.unsubscribe(TopicArn=topic_arn)
        return "Sorry to hear that you didn't like our awesome jokes, we are now unsubscribing: " + email, a

