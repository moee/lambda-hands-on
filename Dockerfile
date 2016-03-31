FROM node:4

ADD credentials /root/.aws/credentials

RUN npm install serverless -g
RUN apt-get update -qq
RUN apt-get install -y python-pip vim
RUN pip install awscli boto3

RUN npm install --save serverless-cors-plugin

