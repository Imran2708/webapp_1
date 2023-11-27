import logging
import requests
import os

import azure.functions as func

# Define subscription key and region
subscription_key = os.getenv("AZURE_SPEECH_API_KEY")
region = os.getenv("AZURE_SPEECH_REGION")

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Define token endpoint
    token_endpoint = f"https://{region}.api.cognitive.microsoft.com/sts/v1.0/issueToken"

    # Make HTTP request with subscription key as header
    response = requests.post(token_endpoint, headers={"Ocp-Apim-Subscription-Key": subscription_key})

    if response.status_code == 200:
        access_token = response.text

        #store the token explicitly
        output = access_token
        logging.info(f"Output: {output}")
        return func.HttpResponse(
             output,
             status_code=200
        )
    else:
        output = str(reponse.status_code)
        logging.error(f"Error: {output}")
        return func.HttpResponse(output))
