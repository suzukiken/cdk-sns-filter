import * as cdk from '@aws-cdk/core';
import * as sqs from '@aws-cdk/aws-sqs';
import * as sns from '@aws-cdk/aws-sns';
import * as subscriptions from '@aws-cdk/aws-sns-subscriptions';

export class CdksnsFilterStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    
    const PREFIX_NAME = id.toLowerCase().replace("stack", "")

    const topic = new sns.Topic(this, 'topic', {
      topicName: PREFIX_NAME + '-topic'
    })
    
    const queue_a = new sqs.Queue(this, 'queue_a', {
      queueName: PREFIX_NAME + '-queue_a',
      retentionPeriod: cdk.Duration.days(10),
    })
    
    const queue_b = new sqs.Queue(this, 'queue_b', {
      queueName: PREFIX_NAME + '-queue_b',
      retentionPeriod: cdk.Duration.days(10),
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
    
    new cdk.CfnOutput(this, 'output', { value: topic.topicArn })
  }
}
