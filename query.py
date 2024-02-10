
from search_utils import search_with_embedding
import json

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

    # search_with_embedding 함수 호출
    result = search_with_embedding(model_text)

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


