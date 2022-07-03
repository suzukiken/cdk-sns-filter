import logging
import json

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def lambda_handler(event, context):

    logger.debug(event)

    for record in event["Records"]:
        decoded_body = json.loads(record["body"])
        logger.debug(decoded_body)
        decoded_message = json.loads(decoded_body["Message"])
        logger.debug(decoded_message)


"""
event
{'Records': [{'messageId': '979f5ab5-539b-4c59-8bdf-5251dbbec9c4', 'receiptHandle': 'AQEBuz9CyhqNsqJy2zPHvEfmw/bYck2N52nPwtMYv9bxD5uQf+X82tAzdQrMYTwiV1ILW4WXOhDPLiTFW2am48yiXvqq2DcDqbl+VaTOzGdNPk5Dq47JYZvbHwtehYZ7np1ImtIzu8hS7u6tKeZVE5ZV7XRPbXlp5TD3AmkbZz0W6NXcsZlgJNwEC98rpSspEz42CrksRDq4OwGsfsGUSs63b6o/rKIl1u0Z7WZOsddqOx88Ypz6vx/3VC8Xx0RdN3MmjLLb9CqDeuSnzuaC+gbhScuwHXFklJKuPtfj7gYKw86jLYjYwLnhIjdHxaFchlU4SF3rg1v0Fg9ollNeWPT/GLRVh5xq0Ts/wAFyIasVSM2ksX/XNTrm1fSVdyHibDgxzB+hW5GTA6zlhchF5rRSkOeoP3inp5oqUURlyUxaD7MDu1PUqs58DtL65oM5psT+', 'body': '{\n  "Type" : "Notification",\n  "MessageId" : "63bac73c-b60d-543f-9c9d-9c07a9e391e5",\n  "TopicArn" : "arn:aws:sns:ap-northeast-1:656169322665:CdksnsFilterStack-TopicBFC7AF6E-438LNOXCZZXC",\n  "Subject" : "subject",\n  "Message" : "{\\"type\\": \\"number\\", \\"id\\": \\"13132323\\"}",\n  "Timestamp" : "2022-07-03T04:40:14.764Z",\n  "SignatureVersion" : "1",\n  "Signature" : "OTcwnKLI7FRCbac7eDB6qHidMRmXDx89FUUQJoQTx4p6PWM4qylr0Dvu68/ZjeHXGWib9vxm2oxXcEdJBnrZIRREEIMIIplZ+CT4hpIcd3CnnsQIb1wxDKnBfoj5t4T51iAZqu7qjhwmntC1A8/r03k+rkpqhDEluYWAKVIuRnEbF3+MqaAsnmkgo/o1sxhuG5jPT2cWRUPeCQhRwK6awKmW8SpxttIblTN8KKCLIF+UYHvrHT3+Fh5so8pT6e6srRKltLLftPUnjebjuKgEPbKqrOlXj05Z29ExF0w97hR2qu4ko3CL239w2e/axP70ommlDFH1xPc9dpVLKaeTcQ==",\n  "SigningCertURL" : "https://sns.ap-northeast-1.amazonaws.com/SimpleNotificationService-7ff5318490ec183fbaddaa2a969abfda.pem",\n  "UnsubscribeURL" : "https://sns.ap-northeast-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:ap-northeast-1:656169322665:CdksnsFilterStack-TopicBFC7AF6E-438LNOXCZZXC:527c7e76-db2e-46ff-979e-3cacc6e9fb44",\n  "MessageAttributes" : {\n    "event" : {"Type":"String","Value":"A"}\n  }\n}', 'attributes': {'ApproximateReceiveCount': '1', 'SentTimestamp': '1656823214801', 'SenderId': 'AIDAIERWYNSNBY7YRB6SY', 'ApproximateFirstReceiveTimestamp': '1656823214802'}, 'messageAttributes': {}, 'md5OfBody': '0425e6dff5ce1a4b9704b423c2ef455e', 'eventSource': 'aws:sqs', 'eventSourceARN': 'arn:aws:sqs:ap-northeast-1:656169322665:CdksnsFilterStack-QueueAC49CDDBE-6Yq6Tm3FGVoT', 'awsRegion': 'ap-northeast-1'}]}


"""
"""
decoded_body
{'Type': 'Notification', 'MessageId': '63bac73c-b60d-543f-9c9d-9c07a9e391e5', 'TopicArn': 'arn:aws:sns:ap-northeast-1:656169322665:CdksnsFilterStack-TopicBFC7AF6E-438LNOXCZZXC', 'Subject': 'subject', 'Message': '{"type": "number", "id": "13132323"}', 'Timestamp': '2022-07-03T04:40:14.764Z', 'SignatureVersion': '1', 'Signature': 'OTcwnKLI7FRCbac7eDB6qHidMRmXDx89FUUQJoQTx4p6PWM4qylr0Dvu68/ZjeHXGWib9vxm2oxXcEdJBnrZIRREEIMIIplZ+CT4hpIcd3CnnsQIb1wxDKnBfoj5t4T51iAZqu7qjhwmntC1A8/r03k+rkpqhDEluYWAKVIuRnEbF3+MqaAsnmkgo/o1sxhuG5jPT2cWRUPeCQhRwK6awKmW8SpxttIblTN8KKCLIF+UYHvrHT3+Fh5so8pT6e6srRKltLLftPUnjebjuKgEPbKqrOlXj05Z29ExF0w97hR2qu4ko3CL239w2e/axP70ommlDFH1xPc9dpVLKaeTcQ==', 'SigningCertURL': 'https://sns.ap-northeast-1.amazonaws.com/SimpleNotificationService-7ff5318490ec183fbaddaa2a969abfda.pem', 'UnsubscribeURL': 'https://sns.ap-northeast-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:ap-northeast-1:656169322665:CdksnsFilterStack-TopicBFC7AF6E-438LNOXCZZXC:527c7e76-db2e-46ff-979e-3cacc6e9fb44', 'MessageAttributes': {'event': {'Type': 'String', 'Value': 'A'}}}

"""
"""
decoded_message
{'type': 'number', 'id': '13132323'}
"""
