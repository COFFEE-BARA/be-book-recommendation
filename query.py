
from search_utils import search_with_embedding
import json
from open_ai import keyword_search
# from elasticapm.contrib.serverless.aws import capture_serverless
# import elasticapm
import os

# SERVICE_NAME = os.getenv('SERVICE_NAME')
# SECRET_TOKEN = os.getenv('ELASTIC_APM_SECRET_TOKEN')
# SERVER_URL = os.getenv('ELASTIC_APM_LAMBDA_APM_SERVER')
# ENVIRONMENT = os.getenv('ENVIRONMENT')


# # Elastic APM 구성
# client = elasticapm.Client({
#     'SERVICE_NAME': SERVICE_NAME,
#     'SECRET_TOKEN': SECRET_TOKEN,
#     'SERVER_URL': SERVER_URL,
#     'ENVIRONMENT' : ENVIRONMENT
# })



# @capture_serverless()
def lambda_handler(event, context):

    try:
        body = json.loads(event['body'])
        model_text = body.get('query', '')
        
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': '*'
            },
            'body': json.dumps({'message': 'Invalid JSON in request body'})
        }
    
    # try:
    #     # Elastic APM 트랜잭션 시작
    #     client.begin_transaction("processing")
        
    #     match_queries = keyword_search(model_text)
    #     result = search_with_embedding(model_text, match_queries)

    #     # Elastic APM 트랜잭션 종료
    #     client.end_transaction('process_event', 'success')
    
    # except Exception as e:
    #     client.capture_exception()  # 예외 상황을 Elastic APM으로 보고
    #     return {
    #         'statusCode': 500,
    #         'body': json.dumps({'message': 'Error processing request'}),
    #         'headers': {{
    #             'Content-Type': 'application/json',
    #             'Access-Control-Allow-Origin': '*',
    #             'Access-Control-Allow-Headers': 'Content-Type',
    #             'Access-Control-Allow-Methods': '*'
    #         }}
    #     }


    match_queries = keyword_search(model_text)
    result = search_with_embedding(model_text, match_queries)


    return {
        'statusCode': result['code'],
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',  
            'Access-Control-Allow-Headers': 'Content-Type', 
            'Access-Control-Allow-Methods': '*'  
        },
        'body': json.dumps({
            'message': result['message'],
            'data': result['data']
        })
    }


# # 테스트를 위한 event 객체 정의
# event = {
#     'body': json.dumps({
#         'query': '서버리스 환경으로 배포를 하고 싶은데 관련한 책을 추천해줘'
#     })
# }

# print(lambda_handler(event , None))

