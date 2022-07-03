import boto3
import os

client = boto3.client("sns")
sts = boto3.client("sts")

TOPIC_ARN = os.environ.get("TOPIC_ARN")

response = client.publish(
    TopicArn=TOPIC_ARN,
    Message="Hello",
    Subject="subject",
    # MessageGroupId="1",
    # MessageDeduplicationId="1",
    MessageAttributes={
        "event": {
            "DataType": "String",
            "StringValue": "A",
        }
    },
)

print(response)
"""
response = client.publish(
    TopicArn=TOPIC_ARN,
    Message="Hello",
    Subject="subject",
    # MessageGroupId="1",
    # MessageDeduplicationId="1",
    MessageAttributes={
        "event": {
            "DataType": "String",
            "StringValue": "B",
        }
    },
)

print(response)
"""
