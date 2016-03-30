from __future__ import print_function

import json
import logging
import boto3
import string
import random
import os

log = logging.getLogger()
log.setLevel(logging.DEBUG)

def get_random_id():
    lst = [random.choice(string.ascii_letters + string.digits) for n in xrange(10)]
    return "".join(lst)

def handler(event, context):
    c = boto3.client('dynamodb')
    id = get_random_id()

    c.put_item(
        TableName='%s-%s-topics-2' % (
            os.environ['SERVERLESS_STAGE'],
            os.environ['SERVERLESS_PROJECT']
        ),
        Item={
            'id': { "S" : id },
            'topic' : { "S" : event['topic'] },
            'speaker' : { "S" : event['speaker'] },
            'up' : { "N" : "0" },
            'down' : { "N" : "0" },
            'total' : { "N" : "0" },
        }
    )
    log.debug("Received event {}".format(json.dumps(event)))
    return { "id" : id }
