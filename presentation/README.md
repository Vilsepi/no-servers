
# Serverless

more dev, less ops?

---

### Which serverless?

- [Serverless Computing:](https://en.wikipedia.org/wiki/Serverless_computing) Functions-as-a-service, run applications with less infrastructure management
- [Serverless Framework:](https://github.com/serverless/serverless) 3rd-party tools for easier serverless development across several cloud providers
- [Serverless Application Model:](https://github.com/awslabs/serverless-application-model) AWS specification and tools to develop serverless apps more easily

--

![Serverless stack](assets/images/serverless_stack.png)

--

[![Serverless Architecture](assets/images/aws_serverless_architecture.png)](https://github.com/awslabs/lambda-refarch-webapp)
<!-- .slide: data-background="#fff" -->

---

### AWS Lambda

![AWS Lambda](assets/images/lambda_flow.png)

--

### Code execution as a service

- No servers, SSH keys, networks, IP addresses
- Python 2.7, Node 4.3, Java 8, C#
- Automatic scaling, each request is handled individually
- Charged by code execution time for each 100ms
- Metrics, logging, versioning

--

### AWS API Gateway

![AWS Lambda](assets/images/apigateway.png)

--

### HTTPS Proxy as a service

- Proxying, schemas, transformations
- Authorization (API keys), throttling, quota
- Stages (dev, prod...) & versioning
- Caching
- SDK generation

---

### Previously life was hard

- Creating and managing Lambda functions is hard
- Deploying (new versions) is hard
- Managing APIs is hard. There was [aws-apigateway-importer](https://github.com/awslabs/aws-apigateway-importer) but 

--

### Life-improvements

- [AWS Serverless Application Model:](https://github.com/awslabs/serverless-application-model) Define and deploy functions and interfaces as YAML.
- [Environment Variables:](https://aws.amazon.com/blogs/aws/new-for-aws-lambda-environment-variables-and-serverless-application-model/) variate function without changing and redeploying code.
- [API Gateway Lambda Proxy:](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-set-up-simple-proxy.html) Much simpler integration without template mapping.

--

### Proxy instead of Mapping Templates

![Lambda Proxy](assets/images/lambda_proxy.png)

---

### AWS Serverless Application Model

- Herokuish tools to deploy functions and interfaces

--

<pre><code data-trim="" class="yaml">
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Resources:
  GetFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: index.get
      Runtime: nodejs4.3
      Policies: AmazonDynamoDBReadOnlyAccess
      Environment:
        Variables:
          TABLE_NAME: !Ref Table
      Events:
        GetResource:
          Type: Api
          Properties:
            Path: /resource/{resourceId}
            Method: get
  Table:
    Type: AWS::Serverless::SimpleTable
</code></pre>

--

### Deploying is easy, right?

First we preprocess the cloudformation template

    aws cloudformation package
      --template-file original.yml
      --output-template-file compiled.yml
      --s3-bucket mahbucket

Then we deploy the cloudformation stack

    aws cloudformation deploy
      --template-file compiled.yml
      --stack-name mahstack
      --capabilities CAPABILITY_IAM

--

```
#!/bin/bash
set -euo pipefail
IFS=$'\n\t'
function deps {
  rm -rf ../build
  mkdir -p ../build
  pip install -r requirements.txt -t ../build/
}
function package {
  cp -rf {tweet,healthcheck} ../build/
  cp -f {*.py,sam.yml} ../build/
  cd ../build
  aws cloudformation package --template-file killMeNow.yml
}
```

So I'll just wrap the awscli with a little bit of extra tooling, no biggie... Uhh, how did I get here?

--

- No way to exclude files in deployment
- Function deployment is slow via CloudFormation change sets
- No local invocation of functions
- No easy way to view logs

--

*"Conclusion: Creating, deploying and managing a serverless app **has never been easier**."*

---

### Serverless Framework

- Easy deployment! Fast function updates! Automatically create artifact bucket!
- Invoke from your terminal! Logs in your terminal! Run functions locally!
- Supports AWS Lambda, Google CloudFunctions and Azure Functions
- Not enough? Plugins!

--

<pre><code data-trim="" class="python">
sudo npm install -g serverless
sls create --template aws-nodejs

sls deploy -v
sls deploy function -f fetcher

sls invoke -f fetcher -l
sls logs -f fetcher -t

sls remove
</code></pre>

--

<pre><code data-trim="" class="yaml">
service: acme-service
custom:
  acmeVariable: acme-variable
provider:
  name: aws
functions:
  acmeApiFunction:
    handler: api.get_item
    events:
      - http: GET items/{id}
package:
  exclude:
    - "do_not_upload_me.txt"
resources:
  Resources:
    AcmeDynamoTable:
      Type: AWS::DynamoDB::Table
</code></pre>

--

### Demo

--

### What about the frontend assets?

- **[serverless-single-page-app-plugin](https://github.com/serverless/examples/tree/master/aws-node-single-page-app-via-cloudfront)**
  - Requires a lot of (CloudFront) configuration
- **[serverless-client-s3](https://github.com/serverless/serverless-client-s3)**
  - Requires a fork to support latest Serverless
  - Does not delete bucket if renamed
  - Does not create Route53 DNS Record or CloudFront distribution

---

### Conclusions

[Use Serverless Framework](https://serverless.com/)

[AWS Serverless Architecture Whitepaper](https://d0.awsstatic.com/whitepapers/AWS_Serverless_Multi-Tier_Architectures.pdf)

[Vogels' Blog: Reference Architectures](http://www.allthingsdistributed.com/2016/06/aws-lambda-serverless-reference-architectures.html)
