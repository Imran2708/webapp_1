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

        #store the access token in a file
        output_file_path = os.path.join(os.environ["TMP"], "access_token.txt")
        with open(output_file_path, "W") as output_file:
            output_file.write(access_token)
            
        return func.HttpResponse(
             access_token,
             status_code=200
        )
    else:
        #store the access token in a file
        output_file_path = os.path.join(os.environ["TMP"], "error_token_code.txt")
        with open(output_file_path, "W") as output_file:
            output_file.write(str(response.status_code))
        return func.HttpResponse(str(response.status_code))
