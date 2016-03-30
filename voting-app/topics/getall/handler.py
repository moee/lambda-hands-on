from __future__ import print_function

import json
import logging
import boto3
import os

log = logging.getLogger()
log.setLevel(logging.DEBUG)

def handler(event, context):
    log.debug("Received event {}".format(json.dumps(event)))

    c = boto3.client('dynamodb')
    response = c.scan(
        TableName='%s-%s-topics-2' % (
            os.environ['SERVERLESS_STAGE'],
            os.environ['SERVERLESS_PROJECT']
        )
    )

    result = []

    for item in response['Items']:
        result.append(
            {
                "id": item["id"]["S"],
                "topic": item["topic"]["S"],
                "speaker": item["speaker"]["S"],
                "up": item["up"]["N"],
                "down": item["down"]["N"],
                "total": item["total"]["N"]
            }
        )

    return result
