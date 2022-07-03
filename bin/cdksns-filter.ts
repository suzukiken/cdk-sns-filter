#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { CdksnsFilterStack } from '../lib/cdksns-filter-stack';

const app = new cdk.App();
new CdksnsFilterStack(app, 'CdksnsFilterStack', {
  env: { account: process.env.CDK_DEFAULT_ACCOUNT, region: process.env.CDK_DEFAULT_REGION },
});