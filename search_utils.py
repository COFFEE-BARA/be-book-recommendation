
from elasticsearch import Elasticsearch, ConnectionError
import os


ELASTIC_CLOUD_ID = os.getenv('ELASTIC_CLOUD_ID')
ELASTIC_API_KEY = os.getenv('ELASTIC_API_KEY')
ELASTIC_INDEX = os.getenv('ELASTIC_INDEX')
ELASTIC_MODEL = os.getenv('ELASTIC_MODEL')



es = Elasticsearch(
  cloud_id=ELASTIC_CLOUD_ID,
  api_key=ELASTIC_API_KEY,
  request_timeout=600
)



def search_with_embedding(model_text, match_queries, index=ELASTIC_INDEX, model_id=ELASTIC_MODEL, k=10, num_candidates=100):
    

    if not match_queries:
        return {
            "code": 400,
            "message": "match_query가 없습니다.",
            "data": None
        }

    if not model_text:
        return {
            "code": 400,
            "message": "query가 없습니다.",
            "data": None
        }

    query = {
    "query": {
        "bool": {
            "should": match_queries,
            "minimum_should_match": 1 
            }
        },
      "knn": {
        "field": "Vector",
        "query_vector_builder": {
          "text_embedding": {
            "model_id": model_id,
            "model_text": model_text
          }
        },
        "k": k,
        "num_candidates": num_candidates
      },
      "_source": ["Search", "ISBN", "Price", "Title", "Author", "ImageURL"]
    }

    try:
        response = es.search(index=index, body=query)
        if response['hits']['hits']:
            # 쿼리 결과가 있는 경우
            data = {
                "recommendedBookList": [
                    {
                        "isbn": hit["_source"]["ISBN"],
                        "title": hit["_source"]["Title"],
                        "author": hit["_source"]["Author"],
                        "image": hit["_source"]["ImageURL"],
                        "price": hit["_source"]["Price"]
                    } for hit in response['hits']['hits']
                ]
            }
            return {
                "code": 200,
                "message": "책을 성공적으로 추천했습니다.",
                "data": data
            }
        else:
            # 검색 결과가 없는 경우
            return {
                "code": 400,
                "message": "적합한 책을 찾을 수 없습니다.",
                "data": None
            }
    except ConnectionError:
        # ES 연결 에러
        return {
            "code": 500,
            "message": "서버 에러",
            "data": None
        }
