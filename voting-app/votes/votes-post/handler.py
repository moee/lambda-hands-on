from __future__ import print_function

import json
import logging
import boto3
import os
import random
import string
import json

log = logging.getLogger()
log.setLevel(logging.DEBUG)

def get_random_id():
    lst = [random.choice(string.ascii_letters + string.digits) for n in xrange(10)]
    return "".join(lst)

def handler(event, context):
    log.debug("Received event {}".format(json.dumps(event)))

    c = boto3.client('dynamodb')
    id = get_random_id()

    c.put_item(
        TableName='%s-%s-votes-2' % (
            os.environ['SERVERLESS_STAGE'],
            os.environ['SERVERLESS_PROJECT']
        ),
        Item={
            'topic_id': { "S" : event["topic_id"] },
            "vote" : { "N" : event["vote"] }
        }
    )

    s = boto3.client('sns')
    s.publish(
        TopicArn=os.environ['SERVERLESS_SNS_TOPIC'],
        Message=json.dumps(
            {
                "topic_id": event["topic_id"],
                "vote": event["vote"],
            }
        )
    )

    return {}
