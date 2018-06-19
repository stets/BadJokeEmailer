# BadJokeEmailer
Cloudformation template that deploys API Gateway endpoints, a SES Topic and lambda scripts that send a user a Chuck Norris joke daily.



# How to Use

Upload the cloudformation master template in the root of this repo via s3 or copy paste it into the Cloudformation designer and deploy it. All of the default options are fine. 

Once the stack has been deployed, it will output the name of the Invoke Url under the 'Outputs' tab under Cloudformation. 

The template creates and exposes 2 API endpoints, /subscribe and /unsubscribe

## To subscribe a user to the SNS topic 

send a post request to the /subscribe endpoint in the format:

{"email":"ChuckNorris@gmail.com"}

This will add that user to the SNS topic. The user will be emailed once a day at the same time that the stack was deployed. 

Cloudwatch triggers the lambda that grabs the joke of the day and publishes to SNS. 

## To Unsubscribe a user

send a post request to the /unsubscribe endpoint in the same format as above:

{"email":"ChuckNorris@gmail.com"}


Please do not deploy this to a production environment. The power of Chuck Norris is too great 
