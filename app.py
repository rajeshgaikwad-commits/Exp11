def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(2, 3))
import logging

logging.basicConfig(level=logging.INFO)

def add(a, b):
    logging.info("Addition operation performed")
    return a + b

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello from Serverless!'
    }

