import boto3
import os
import json

sns = boto3.client("sns")

TOPIC_ARN = os.environ.get("TOPIC_ARN")

message = {"type": "number", "id": "13132323"}
response = sns.publish(
    TopicArn=TOPIC_ARN,
    Subject="subject",
    Message=json.dumps(message),
    MessageAttributes={"event": {"DataType": "String", "StringValue": "A"}},
)

print(response)
