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
    item = c.get_item(
        TableName='%s-%s-topics-2' % (
            os.environ['SERVERLESS_STAGE'],
            os.environ['SERVERLESS_PROJECT']
        ),
        Key={
            "id": { "S" : event['id'] }
        }
    )

    return {
        'id' : item['Item']['id']['S'],
        'topic' : item['Item']['topic']['S'],
        'speaker' : item['Item']['speaker']['S'],
        'up' : item['Item']['up']['N'],
        'down' : item['Item']['down']['N']
    }
