# BadJokeEmailer
This project is a Cloudformation template that deploys AWS Resources to create a Chuck Norris joke emailer.

The template contains an API Gateway and endpoints, 2 lambdas written in python and necesarry IAM roles to ensure everything has access.
One lambda handles requests from API Gateway and adds or removes users from the SNS topic, while the other is configured to GET a Chuck Norris joke from ChuckNorris.io and send it to the subscribed users.

![Architecture Diagram](assets/cloudcraft.png)

# How to Use

Upload the cloudformation master template in the root of this repo via s3 or copy paste it into the Cloudformation designer and deploy it. All of the default options will deploy fine.

Once the stack has been deployed, it will output the name of the subscribe and unsubscribe API endpoints under the 'Outputs' tab on the main Cloudformation page. 

![API Invocation URLs outputted for easy access](assets/APIurls.png)

## To Subscribe a User

Send a post request to the /subscribe endpoint in the format:

{"email": "ChuckNorris@gmail.com"}

![Subscribing a user with Postman](assets/post_sub.png)

This will add that user to the SNS topic. The user will be emailed once a day at 11:30 EST.
The time can be changed on the cron line under the cloudwatch rule resource. 


## To Unsubscribe a User

Send a post request to the /unsubscribe endpoint in the format:

{"email": "ChuckNorris@gmail.com"}

![Unsubscribing a user with Postman](assets/post_unsub.png)

Please do not deploy this to a production environment. The power of Chuck Norris is too great  (also, there are insecure roles and probably other bugs)
