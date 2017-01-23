
## Prerequisites

Install serverless CLI and [configure credentials](https://github.com/serverless/serverless/blob/master/docs/providers/aws/guide/credentials.md):

    npm install -g serverless

Install dependencies:

    pip install -t vendored -r requirements.txt

## Develop

Deploy the stack:

    sls deploy -v

Develop a single function:

    sls deploy function -f fetcher
    sls invoke -f fetcher -l
    sls logs -f fetcher -t

    sls deploy function -f fetcher && sls invoke -f fetcher -l
