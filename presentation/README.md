
# Serverless

More dev, less ops?

---

## Term confusion

- [Serverless Computing:](https://en.wikipedia.org/wiki/Serverless_computing) Functions-as-a-service, run applications with less infrastructure management
- [Serverless Framework:](https://github.com/serverless/serverless) 3rd-party tools for easier serverless development across several cloud providers
- [AWS Serverless Application Model:](https://github.com/awslabs/serverless-application-model) specification and tools to develop serverless apps more easily in AWS

---

![Serverless stack](assets/images/serverless_stack.png)

---

[![Serverless Architecture](assets/images/aws_serverless_architecture.png)](https://github.com/awslabs/lambda-refarch-webapp)
<!-- .slide: data-background="#fff" -->

--

### AWS Lambda

![AWS Lambda](assets/images/lambda_flow.png)

--

### Lambda features in 1 slide

- stuff

--

### AWS API Gateway

![AWS Lambda](assets/images/apigateway.png)

--

### API Gateway features in 1 slide

- Proxying, schemas, transformations
- Authorization (API keys)
- Stages (dev, prod...)
- Caching

---

## Previously life was hard

- Creating and managing Lambda functions is hard
- Deploying (new versions) is hard
- Managing APIs is hard. There was [aws-apigateway-importer](https://github.com/awslabs/aws-apigateway-importer) but 

--

## Life-improvements

- [AWS Serverless Application Model:](https://github.com/awslabs/serverless-application-model) Define and deploy functions and interfaces as YAML.
- [Environment Variables:](https://aws.amazon.com/blogs/aws/new-for-aws-lambda-environment-variables-and-serverless-application-model/) variate function without changing and redeploying code.
- [API Gateway Lambda Proxy:](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-set-up-simple-proxy.html) Much simpler integration without template mapping.

--

### Proxy instead of Mapping Templates

![Lambda Proxy](assets/images/lambda_proxy.png)

--

## AWS Serverless Application Model

Well, not so cool :(

---

## Serverless Framework

--

### What about the frontend assets?

- **[serverless-single-page-app-plugin](https://github.com/serverless/examples/tree/master/aws-node-single-page-app-via-cloudfront)**
  - Requires a lot of (CloudFront) configuration
- **[serverless-client-s3](https://github.com/serverless/serverless-client-s3)**
  - Requires a fork to support latest Serverless
  - Does not delete bucket if renamed
  - Does not create Route53 DNS Record or CloudFront distribution

--

```
    plugins:
      - serverless-client-s3
    custom:
      client:
        bucketName: serverless.heap.fi

    # package.json
    {
      "name": "no-servers-frontend",
      "version": "0.0.1",
      "devDependencies": {
        "serverless-client-s3": "git://github.com/kevzettler/serverless-client-s3.git#serverless_1.0_beta_compatibility"
      }
    }
```

---

## Conclusions

[Use Serverless Framework](https://serverless.com/)

[AWS Serverless Architecture Whitepaper](https://d0.awsstatic.com/whitepapers/AWS_Serverless_Multi-Tier_Architectures.pdf)

[Vogels' Blog: Reference Architectures](http://www.allthingsdistributed.com/2016/06/aws-lambda-serverless-reference-architectures.html)
