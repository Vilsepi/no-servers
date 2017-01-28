
Previously:

- Creating and managing Lambda functions is hard
- Deploying (new versions) is hard
- Managing APIs is hard

- Lambda_Proxy: oh yeah! API gateway dumps all request data to Lambda as JSON, expects a specific JSON as response. No more template mapping!



---


What about the frontend assets?

**[serverless-single-page-app-plugin](https://github.com/serverless/examples/tree/master/aws-node-single-page-app-via-cloudfront)**

- Requires a lot of (CloudFront) configuration

**[serverless-client-s3](https://github.com/serverless/serverless-client-s3)**

- Requires a fork to support latest Serverless
- Does not delete bucket if renamed
- Does not create Route53 DNS Record or CloudFront distribution

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
