import json



def lambda_handler(event, context):
    body = {
        "message": "Hello - Test"

    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response

