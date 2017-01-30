
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

--

### AWS Serverless Application Model

Well, not so cool :(

---

### Serverless Framework

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

### Conclusions

[Use Serverless Framework](https://serverless.com/)

[AWS Serverless Architecture Whitepaper](https://d0.awsstatic.com/whitepapers/AWS_Serverless_Multi-Tier_Architectures.pdf)

[Vogels' Blog: Reference Architectures](http://www.allthingsdistributed.com/2016/06/aws-lambda-serverless-reference-architectures.html)
