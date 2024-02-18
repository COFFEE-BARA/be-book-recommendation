import os
import openai

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


openai.api_key = OPENAI_API_KEY

def keyword_search(query):
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "업무: 문맥 이해 및 키워드 추출. 맥락: 사용자의 문장을 분석하여 가장 중요한 기술적 키워드 2개를 식별하고, 이를 '컴마 형식'으로 반환하는 것이 목표입니다. 예시: '키워드1, 키워드2'"},
            {"role": "user", "content": f"이 문장을 분석하고, 도서 검색에 필요한 가장 중요한 키워드 2개만을 '컴마 형식'으로 나열해주세요. 예시 응답: 'aws, 클라우드'. 문장: '{query}'"}
        ]
    )

    response = res.choices[0].message['content']
    keyword_list = [kw.strip() for kw in response.split(',')]
    match_queries = [{"match": {"Search": kw}} for kw in keyword_list]

    return match_queries