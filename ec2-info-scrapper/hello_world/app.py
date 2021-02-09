import json

import requests

from bs4 import BeautifulSoup


import boto3


def lambda_handler(event = NULL, context = NULL):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
        
    #     base = "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html"

    #     result = requests.get(base)

    #     soup = BeautifulSoup(result.content,'html.parser')

    #     links = soup.find_all('h1')
    #     # print(links)
    #     for link in links:
    #         content = link.find_next('p')
    #         #print(content.text)

    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    # return {
    #     "statusCode": 200,
    #     "body": json.dumps({
    #         "message": "EC2 info scrapped from AWS Documentation page",
    #         "location": ip.text.replace("\n", ""),
    #         "content" : " ".join(content.text.split())
    #     }),
    # }

     
#     #TXQ2XHODZE

    
    client = boto3.client('lexv2-models')

    response = client.create_bot(
    botName='TestBot',
    description='abcd',
    roleArn='arn:aws:iam::185627371157:role/aws-service-role/lex.amazonaws.com/AWSServiceRoleForLexBots',
    dataPrivacy={
        'childDirected': True
    },
    idleSessionTTLInSeconds=123
 )
     
    json_object= json.dumps(response, indent = 4)   

    return json_object

#     response = client.create_intent(
#     intentName='test-intent',
#     description='this is a test intent',
#     sampleUtterances=[
#         {
#             'utterance': 'what is aws'
#         },
#     ],
#     dialogCodeHook={
#         'enabled': False
#     },
#     fulfillmentCodeHook={
#         'enabled': False
#     },    
#     botId='TXQ2XHODZE',
#     botVersion='DRAFT',
#     localeId='English'
# )

#     response = client.list_bots(
#     sortBy={
#         'attribute': 'BotName',
#         'order': 'Ascending'
#     },
#     filters=[
#         {
#             'name': 'BotName',
#             'values': [
#                 'bot',
#             ],
#             'operator': 'CO'
#         },
#     ],
#     maxResults=123
# )
    #print(response['botId'])

    # return {
    #     "statusCode": 200,
    #     "body": json.dumps({
    #         "message": "Successfully returned value",
    #         "content" : response['botId']
    #     }),
    # }
   