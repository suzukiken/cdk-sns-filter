Example CDK TypeScript Project

To deploy SNS and SQS with filter.

* `npm install`
* `cdk deploy`

[description](https://note.figmentresearch.com/aws/cdksns-filter)

まずデプロイ

```
cdk deploy
```

実行環境の作成

```
python -m venv test/env
source test/env/bin/activate
python -m pip install boto3
```

実行

```
source test/env/bin/activate
python utility/show_exported.py
```

```
export TOPIC_ARN=SNSトピックのARN
python test/publish.py
```