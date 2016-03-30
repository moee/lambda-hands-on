FROM node:4

RUN npm install serverless -g
RUN apt-get update -qq
RUN apt-get install -y python-pip vim
RUN pip install awscli boto3

ADD credentials /root/.aws/credentials
