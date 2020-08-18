import logging
import random

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info(event)

    message_array = [
        "hello world",
        "retry"
    ]
    message = random.choice(message_array)
    logger.info(message)

    return {
        "statusCode": 200,
        "body": {
            "message": message,
        }
    }
