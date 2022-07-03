import { Stack, StackProps, CfnOutput, Duration } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as sns from 'aws-cdk-lib/aws-sns';
import * as sqs from 'aws-cdk-lib/aws-sqs';
import * as subscriptions from 'aws-cdk-lib/aws-sns-subscriptions';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import { SqsEventSource } from 'aws-cdk-lib/aws-lambda-event-sources';

export class CdksnsFilterStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    
    const topic = new sns.Topic(this, 'Topic', {
      // topicName: id + "Topic.fifo",
      // fifo: true
    });

    const queue_a = new sqs.Queue(this, 'QueueA', {
      // queueName: id + 'QueueA.fifo',
      retentionPeriod: Duration.days(10),
      // fifo: true
    })
    
    const queue_b = new sqs.Queue(this, 'QueueB', {
      // queueName: id + 'QueueB.fifo',
      retentionPeriod: Duration.days(10),
      // fifo: true
    })
    
    topic.addSubscription(
      new subscriptions.SqsSubscription(
        queue_a, 
        {
          filterPolicy: {
            event: sns.SubscriptionFilter.stringFilter({
              allowlist: ['A']
            })
          }
        }
      )
    )
    
    topic.addSubscription(
      new subscriptions.SqsSubscription(
        queue_b, 
        {
          filterPolicy: {
            event: sns.SubscriptionFilter.stringFilter({
              allowlist: ['B']
            })
          }
        }
      )
    )
    
    const func = new lambda.Function(this, 'Function', {
      code: lambda.Code.fromAsset('lambda'),
      runtime: lambda.Runtime.PYTHON_3_9,
      handler: 'main.lambda_handler'
    })
    
    queue_a.grantConsumeMessages(func)
    queue_b.grantConsumeMessages(func)
    
    func.addEventSource(
      new SqsEventSource(queue_a, { batchSize: 1 })
    )
    
    func.addEventSource(
      new SqsEventSource(queue_b, { batchSize: 1 })
    )
    
    new CfnOutput(this, 'SNSOutput', { value: topic.topicArn, description: "sns topic arn" })
    new CfnOutput(this, 'SQSArnOutput', { value: queue_a.queueArn, description: "sqs queue arn" })
    new CfnOutput(this, 'SQSURLOutput', { value: queue_a.queueUrl, description: "sqs queue url" })
    new CfnOutput(this, 'LambdaOut', { value: func.functionName, description: "lambda function name" })
  }
}
