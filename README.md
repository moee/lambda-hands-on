# lambda-hands-on

## Prerequisites

I built a Docker image that contains an encapsulated environment that includes everything needed to run this demo. Optionally, if you don't want to install docker, you can also install serverless directly on your machine.

## Hands on!

1. Clone this repo
2. Copy `credentials.templates` to `credentials` and fill in your AWS Credentials
3. Run `./serverless-demo-shell` to start the serverless bash shell
4. cd into `/usr/src/app/voting-app`
5. `sls project init -c true`
    1. Enter a new stage name (e.g. `demo`)
    2. In the next step, select Existing Profile and pick `default`
6. `sls variables set`
    1. Name: accountId, Value: *YOUR AWS ACCOUNT ID*, e.g. 1234567890
7. `sls resources deploy`
    1. You might want to start with the greeter to verify everything is working
8. If you deploy the votes app, manually subscribe the lambda function `aws-meetup-vienna-votes-trigger`
    1. As Version select the appropriate application stage (e.g. `demo`)
    2. There is a SNS plugin that is supposed to do that, but it doesn't work right now with sls 0.5.1
9. Adjust `this.url` in `client/dist/index.js`
10. Run `sls static deploy` to deploy the static content

## Cleaning up

After you're done don't forget to remove all resources from AWS (`sls project remove`), otherwise they will incur costs!

## Acknowledgements

* Thanks to @karlhorky and @sanjabonic for building the client (https://github.com/karlhorky/voting-app-aws-demo)
