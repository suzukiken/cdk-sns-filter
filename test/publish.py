import boto3

client = boto3.client('sns')
sts = boto3.client('sts')

account = sts.get_caller_identity()['Account']

response = client.publish(
    TopicArn='arn:aws:sns:ap-northeast-1:{}:cdksnsfilter-topic'.format(account),
    Message='message',
    Subject='subject',
    MessageAttributes={
        'event': {
            'DataType': 'String',
            'StringValue': 'A',
        }
    }
)

print(response)

response = client.publish(
    TopicArn='arn:aws:sns:ap-northeast-1:{}:cdksnsfilter-topic'.format(account),
    Message='message',
    Subject='subject',
    MessageAttributes={
        'event': {
            'DataType': 'String',
            'StringValue': 'B',
        }
    }
)

print(response)