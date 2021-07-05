+++
title = "SNSのメッセージフィルタリング"
date = "2021-04-27"
tags = ["SNS"]
+++

1つのSNSトピックを用意して様々な用途に使おうと考えた場合に、MessageAttributesでメッセージの配信先を選択することができる。

[AWSのドキュメント](https://docs.aws.amazon.com/sns/latest/dg/sns-message-filtering.html)

以下のリポジトリの内容はそのSNSフィルタを試してみるためにMessageAttributesにeventという名前の文字列の値を設定することにしてSNSのフィルタポリシーでそのeventの値に応じてメッセージを配信する先のSQSを切り替えるということをしてみている。

[Githubのリポジトリ](https://github.com/suzukiken/cdksns-filter)
