# BadJokeEmailer
Cloudformation template that deploys API Gateway endpoints, a SES Topic and lambda scripts that send a user a Chuck Norris joke daily.


The template creates and exposes 2 API endpoints, /subscribe and /unsubscribe

To subscribe a user to the SES topic, send a post request to the /subscribe endpoint in the format:
{"email":"example@gmail.com"}


