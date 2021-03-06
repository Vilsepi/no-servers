#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import boto3

table_name = os.environ.get("TABLE_NAME")
table = boto3.resource("dynamodb").Table(table_name)

def _log_dynamo(response):
    print "HTTPStatusCode:{}, RetryAttempts:{}, ScannedCount:{}, Count:{}".format(
        response.get("ResponseMetadata").get("HTTPStatusCode"),
        response.get("ResponseMetadata").get("RetryAttempts"),
        response.get("ScannedCount"),
        response.get("Count")
    )

def get_items(event, context):
    response = table.scan(Limit=10)
    _log_dynamo(response)
    return {
        "statusCode": 200,
        "body": json.dumps(response["Items"], indent=1),
        "headers": {"Access-Control-Allow-Origin": "*"}
    }

def get_item(event, context):
    response = table.get_item(Key={"id": event.get("pathParameters").get("id")})
    _log_dynamo(response)
    return {
        "statusCode": 200,
        "body": json.dumps(response["Item"], indent=1)
    }

def echo(event, context):
    print event
    return {
        "statusCode": 200,
        "body": json.dumps({
            "lambdaRequestEvent": event,
            "lambdaContext": {
                "function_name": context.function_name,
                "function_version": context.function_version,
                "memory_limit_in_mb": context.memory_limit_in_mb,
                "remaining_time_in_millis": context.get_remaining_time_in_millis()
            }
        }, indent=1),
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "MyCustomHeader": "Hello Header"
        }
    }
