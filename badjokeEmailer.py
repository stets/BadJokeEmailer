from botocore.vendored import requests
import boto3
import json


# Lambda functiont to request Chuck Norris jokes and then publish them to an SES feed

# set up sns client
client = boto3.client('sns')

def lambda_handler(event, context):
    # fire a request off at the Chuck Norris API and format it
    joke = requests.get('https://api.chucknorris.io/jokes/random', headers={'Content-Type': 'application/json'}).json()['value']
    data = json.dumps(joke)
    # put the topic ARN in a variable
    topic_arn = ''
    # publish the joke to the topic
    client.publish(Message=joke, TopicArn=topic_arn)
    # return the joke for debug purposes
    return joke
