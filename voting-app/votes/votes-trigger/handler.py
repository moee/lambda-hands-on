from __future__ import print_function

import json
import logging
import boto3
import os

log = logging.getLogger()
log.setLevel(logging.DEBUG)

def process_message(message):
    log.debug("Process message {}".format(json.dumps(message)))

    c = boto3.client('dynamodb')
    item = c.get_item(
        TableName='%s-%s-topics-2' % (
            os.environ['SERVERLESS_STAGE'],
            os.environ['SERVERLESS_PROJECT']
        ),
        Key={
            "id": { "S" : message['topic_id'] }
        }
    )

    item = item['Item']

    new_total = int(item['total']['N']) + int(message['vote'])

    updates = {
        "total" : {
            "Value": { "N" : str(new_total) },
            "Action": "PUT"
        },
        "up" : {
            "Value" : { "N" : str(item['up']['N']) },
            "Action": "PUT"
        },
        "down" : {
            "Value" : { "N" : str(item['down']['N']) },
            "Action": "PUT"
        }
    }

    if new_total > 0:
        updates["up"]["Value"]["N"] = str(int(updates["up"]["Value"]["N"]) + 1)
    else:
        updates["down"]["Value"]["N"] = str(int(updates["down"]["Value"]["N"]) + 1)

    response = c.update_item(
        TableName="%s-%s-topics-2" % (
            os.environ['SERVERLESS_STAGE'],
            os.environ['SERVERLESS_PROJECT']
        ),
        Key={
            "id": { "S" : message['topic_id'] }
        },
        AttributeUpdates = updates
    )


def handler(event, context):
    log.debug("Received event {}".format(json.dumps(event)))

    for record in event["Records"]:
        process_message(json.loads(record['Sns']['Message']))

    return {}
