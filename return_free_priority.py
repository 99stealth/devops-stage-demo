#/usr/bin/python

import boto3
import cfnresponse


def get_response_from_listener(client, listener_arn):
    return client.describe_rules(ListenerArn=listener_arn)


def count_to_infinity():
    index = 1
    while True:
        yield index
        index += 1


def search_available_priority(response):
    priorities = []
    for rule in response['Rules']:
         if rule['Priority'] != 'default':
             priorities.append(int(rule['Priority']))
    for priority in count_to_infinity():
        if priority not in priorities:
            return priority


def lambda_handler(event, context):
    if event['RequestType'] == 'Delete':
        cfnresponse.send(event, context, cfnresponse.SUCCESS, {'Value': '0'})
        return
    elif event['RequestType'] == 'Update':
        pass
    elif event['RequestType'] == 'Create':
        client = boto3.client('elbv2')
        response_from_listener = get_response(client, event['ResourceProperties']['listener_arn'])
        available_priority = search_available_priority(response_from_listener)
        rule_id = str(available_priority)
        cfnresponse.send(event, context, cfnresponse.SUCCESS, {'Value': rule_id})
        return rule_id
