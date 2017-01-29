
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

### Serverless AWS

(architecture pic)

--

### AWS Lambda

![AWS Lambda](assets/images/lambda.png)

--

### AWS API Gateway

![AWS Lambda](assets/images/apigateway.png)

---

## Previously life was hard

- Creating and managing Lambda functions is hard
- Deploying (new versions) is hard
- Managing APIs is hard

--

## Behold!

- AWS Serverless Application Model
- Environment Variables
- LAMBDA_PROXY: oh yeah! API gateway dumps all request data to Lambda as JSON, expects a specific JSON as response. No more template mapping!

--

## AWS Serverless Application Model

--

Well, not so cool :(

--

## Serverless Framework

---

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

## Conclusion

Don't use Lambda without Serverless Framework.
