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
7. `sls resources deploy` - This deploys the cloudformation template to aws
8. `sls dash deploy` - Deploy functions and/or endpoints
    1. You might want to start with the greeter to verify everything is working
9. If you deploy the votes app, manually subscribe the lambda function `aws-meetup-vienna-votes-trigger`
    1. As Version select the appropriate application stage (e.g. `demo`)
    2. There is a SNS plugin that is supposed to do that, but it doesn't work right now with sls 0.5.1
10. Adjust `this.url` in `client/dist/index.js`
11. Run `sls static deploy` to deploy the static content

### Bonus: Running lambdash

[Lambdash](https://alestic.com/2015/06/aws-lambda-shell-2/) let's you execute arbitrary shell commands in lambda to explore the environment. 

1. Clone [lambdash](https://github.com/alestic/lambdash) somewhere inside the demo shell
2. cd into it
3. run `bash ./lambdash-install`
4. Execute commands with `./lambdash COMMAND`
5. When you're done delete the lambda function with `./lambdash-uninstall`

## Cleaning up

After you're done don't forget to remove all resources from AWS (`sls project remove`), otherwise they will incur costs! The S3 bucket cannot be removed automatically, so you have to do that manually.

## Acknowledgements

* Thanks to [@karlhorky](https://github.com/karlhorky) and [@sanjabonic](https://github.com/sanjabonic) for [building the client] (https://github.com/karlhorky/voting-app-aws-demo)
