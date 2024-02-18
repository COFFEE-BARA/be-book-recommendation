
from search_utils import search_with_embedding
import json
from open_ai import keyword_search
from elasticapm.contrib.serverless.aws import capture_serverless
import elasticapm
import os

SERVICE_NAME = os.getenv('SERVICE_NAME')
SECRET_TOKEN = os.getenv('SECRET_TOKEN')
SERVER_URL = os.getenv('SERVER_URL')


# Elastic APM 구성
client = elasticapm.Client({
    'SERVICE_NAME': SERVICE_NAME,
    'SECRET_TOKEN': SECRET_TOKEN,
    'SERVER_URL': SERVER_URL,
})



@capture_serverless()
def lambda_handler(event, context):
    # POST 요청의 바디에서 model_text 추출
    try:
        body = json.loads(event['body'])
        model_text = body.get('query', '')
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid JSON in request body'})
        }
    
    match_queries = keyword_search(model_text)
    result = search_with_embedding(model_text, match_queries)

    # API Gateway 호환 응답 형식으로 변환
    return {
        'statusCode': result['code'],
        'headers': {
            'Content-Type': 'application/json'
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