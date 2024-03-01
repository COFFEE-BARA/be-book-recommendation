# 📚 Checkbara
![checkbara1](https://github.com/COFFEE-BARA/be-library-stock/assets/72396865/5a3da8b6-009d-40f5-a3f8-a1561df83631)
![checkbara2](https://github.com/COFFEE-BARA/be-library-stock/assets/72396865/eeef4f87-fb54-471b-bbba-2f9fac767823)
![checkbara3](https://github.com/COFFEE-BARA/be-library-stock/assets/72396865/3a8da5c0-19ee-4251-9161-96a835ce0b3f)
<img width="875" alt="checkbara4" src="https://github.com/COFFEE-BARA/be-library-stock/assets/72396865/fe97f585-7be6-4810-bc0a-f3c331ce9c39">

<br/>

| <img width="165" alt="suwha" src="https://github.com/COFFEE-BARA/be-bookstore-stock/assets/72396865/19e01fac-5384-4ec7-98f1-9e1e613429b4"> | <img width="165" alt="yoonju" src="https://github.com/COFFEE-BARA/be-bookstore-stock/assets/72396865/fb0a14c6-2d02-4105-962e-4565663817cc"> | <img width="165" alt="yugyeong" src="https://github.com/COFFEE-BARA/be-bookstore-stock/assets/72396865/90b7268d-92e5-43d1-9da8-ae48afd9e8c1"> | <img width="165" alt="dayeon" src="https://github.com/COFFEE-BARA/be-bookstore-stock/assets/72396865/f19e65e6-0856-4b6a-a355-993ce83ddcb7"> |
| --- | --- | --- | --- |
| 🐼[유수화](https://github.com/YuSuhwa-ve)🐼 | 🐱[송윤주](https://github.com/raminicano)🐱 | 🐶[현유경](https://github.com/yugyeongh)🐶 | 🐤[양다연](https://github.com/dayeon1201)🐤 |
| Server / Data / BE | AI / Data / BE | Infra / BE / FE | BE / FE |

<br/>
<br>
<br>

# be-book-recommendation
## 📹 시연 영상
![챗봇](https://github.com/COFFEE-BARA/crawler-kyobo-isbn/assets/65851554/a28f0cca-ae1f-46b9-a087-6ea18216bd9d)


## 📝 Elastic index
<details><summary> Mappings </summary>

```
{
  "mappings": {
    "properties": {
      "Author": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "text",
            "analyzer": "author_analyzer"
          },
          "partial": {
            "type": "text",
            "analyzer": "edge_ngram_analyzer"
          }
        }
      },
      "DetailCategory": {
        "type": "keyword"
      },
      "ISBN": {
        "type": "keyword"
      },
      "ImageURL": {
        "type": "keyword"
      },
      "IndexContent": {
        "type": "text"
      },
      "Introduction": {
        "type": "text"
      },
      "MiddleCategory": {
        "type": "keyword"
      },
      "Price": {
        "type": "integer"
      },
      "PubDate": {
        "type": "date",
        "format": "yyyy-MM-dd"
      },
      "Publisher": {
        "type": "keyword"
      },
      "PublisherReview": {
        "type": "text"
      },
      "PurchaseURL": {
        "type": "keyword"
      },
      "Search": {
        "type": "text"
      },
      "Title": {
        "type": "text",
        "analyzer": "title_analyzer"
      },
      "Vector": {
        "type": "dense_vector",
        "dims": 768,
        "index": true,
        "similarity": "cosine"
      },
      "document": {
        "type": "object"
      },
      "id": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 256
          }
        }
      },
      "index": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 256
          }
        }
      },
      "pipeline": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 256
          }
        }
      }
    }
  }
}
```
</details>


<br>
<br>


## 🌎 API 명세


<details><summary> 1️⃣ [POST] BASE_URL/api/book/recommendation
</summary>
    
: 유저가 원하는 내용을 입력하면 입력한 내용에 맞게 ai가 책을 추천해준다.
    
<img width="518" alt="11" src="https://github.com/COFFEE-BARA/be-book-recommendation/assets/97875918/fbccca9e-32af-4e9c-aa14-fbe1b2ba16da">

</details>
    
<details><summary> 2️⃣ Request </summary>
 
- **☝🏻Request Header**

    ```
    Content-Type: application/json
    ```
    
- **✌🏻Request Body**
  
     | Name | Type | Description | Required |
     | --- | --- | --- | --- |
     | query | String | 최대 1365자(한글기준) | Required |
    
     ```
    {
    		"query" : "aws와 유사한 클라우드 서비스를 공부하고 싶은데 관련 책 추천해줘"
    }
    ```
</details>
    
<details><summary> 3️⃣ Response </summary>
 
- **☝🏻성공**
  | Name | Type | Description |
  | --- | --- | --- |
  | code | Integer | 상태 코드 |
  | message | String | 상태 메시지 |
  | data | List | 상태 코드 |
  | - recommendedBookList | List | ai가 추천하는 책, list는 추천순으로 정렬됨. |
  | -- isbn | Long | 책의 13자리 isbn |
  | -- title | String | 책이름 |
  | -- author | String | 책 저자(들) |
  | -- image | String | 책 표지 이미지 url |
  | -- price | Long | 책의 가격(재고검색을 위해 필요) |



    ```
    {
        "message": "책을 성공적으로 추천했습니다.",
        "data": {
            "recommendedBookList": [
                {
                    "isbn": "9791158391317",
                    "title": "서비스 운영이 쉬워지는 AWS 인프라 구축 가이드 (서버 구축부터 배포, 모니터링, 관리 자동화, 데브옵스까지)",
                    "author": "김담형",
                    "image": "https://shopping-phinf.pstatic.net/main_3243626/32436267587.20221227210159.jpg",
                    "price": 24300
                },
                {
                    "isbn": "9791158393977",
                    "title": "AWS 구조와 서비스 (AWS의 전체 구조와 기술이 한눈에 들어오는 아마존 웹 서비스 핵심 가이드)",
                    "author": "우에노 후미아키^코바야시 쿄헤이^오자와 코스케^다카나시 토모유키",
                    "image": "https://shopping-phinf.pstatic.net/main_3773568/37735685622.20230313183543.jpg",
                    "price": 17100
                },
                {
                    "isbn": "9791198189295",
                    "title": "클라우드 서비스 개발자를 위한 AWS로 구현하는 CI/CD 배포 입문 (신입 개발자부터 실제 서비스 구축 경험이 없는 모든 개발자를 위한 실무 밀착형 입문서)",
                    "author": "최주호^정재원^정동진",
                    "image": "https://shopping-phinf.pstatic.net/main_3817483/38174830618.20230926084650.jpg",
                    "price": 18000
                },
                {
                    "isbn": "9791161757087",
                    "title": "AWS 쿡북 (개념과 예제를 다루는 실용 안내서)",
                    "author": "존 컬킨^마이크 자존",
                    "image": "https://shopping-phinf.pstatic.net/main_3636192/36361929618.20230711113104.jpg",
                    "price": 31500
                },
                {
                    "isbn": "9791161756080",
                    "title": "Amazon VPC 네트워킹 원리와 보안 (AWS 토폴로지로 이해하는, 2022년 세종도서 학술부문 선정도서)",
                    "author": "차정도",
                    "image": "https://shopping-phinf.pstatic.net/main_3245798/32457980676.20230919123526.jpg",
                    "price": 28800
                },
                {
                    "isbn": "9791158391201",
                    "title": "AWS 시스템 설계와 마이그레이션 (아마존웹서비스 업무시스템설계와 마이그레이션을위한 베스트프랙티스)",
                    "author": "사사키 타쿠로^하야시 신이치로^세토지마 토시히로^미야카와 료^카나자와 케이",
                    "image": "https://shopping-phinf.pstatic.net/main_3248956/32489567071.20220527042551.jpg",
                    "price": 26600
                },
                {
                    "isbn": "9791190014595",
                    "title": "타입스크립트, AWS 서버리스로 들어올리다 (오직 개발에만 집중할 수 있게 도와주는 실무 가이드)",
                    "author": "신규하",
                    "image": "https://shopping-phinf.pstatic.net/main_3248371/32483718302.20221229074737.jpg",
                    "price": 34200
                },
                {
                    "isbn": "9791190014304",
                    "title": "당신이 지금 알아야 할 AWS (한 번 읽으면 제대로 남는 AWS 클라우드 입문서)",
                    "author": "이영호",
                    "image": "https://shopping-phinf.pstatic.net/main_3248653/32486532057.20230214162810.jpg",
                    "price": 25200
                },
                {
                    "isbn": "9791158394608",
                    "title": "진짜 챗GPT API 활용법 (ChatGPT API 기반의 음성 비서부터 카카오톡/텔레그램 챗봇 제작, 랭체인 활용, 파인튜닝까지)",
                    "author": "김준성^유원준^안상준",
                    "image": "https://shopping-phinf.pstatic.net/main_4187308/41873081621.20230906071215.jpg",
                    "price": 23940
                },
                {
                    "isbn": "9788931457070",
                    "title": "Amazon Web Services로 시작하는 클라우드 입문 (서버구축경험이적어도!프로그램개발자도쉽게!기초부터알수있는클라우드입문)",
                    "author": "WINGS 프로젝트 아사 시호",
                    "image": "https://shopping-phinf.pstatic.net/main_3250463/32504635060.20220527044714.jpg",
                    "price": 24300
                }
            ]
        }
    }
    ```
    
- **✌🏻실패**
  - 필요한 값이 없는 경우
    
    ```
    {
        "code": 400,
        "message": "query가 없습니다.",
        "data": null
    }
    ```
    
  - 서버에러
    
    ```
    {
        "code": 500,
        "message": "서버 에러",
        "data": null
    }
    ```

</details>

<br>
<br>


## 🛠️ 사용 기술 스택

### Programming Language & Library
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 	![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white) ![ElasticSearch](https://img.shields.io/badge/-ElasticSearch-005571?style=for-the-badge&logo=elasticsearch)

### DB
<img src="https://img.shields.io/badge/elastic-005571?style=for-the-badge&logo=elastic&logoColor=white">

### CI/CD & Deploy
<img src="https://img.shields.io/badge/codebuild-68A51C?style=for-the-badge&logo=codebuild&logoColor=white"/> <img src="https://img.shields.io/badge/codepipeline-527FFF?style=for-the-badge&logo=codepipeline&logoColor=white"/> <img src="https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"> <img src="https://img.shields.io/badge/awslambda-FF9900?style=for-the-badge&logo=awslambda&logoColor=white"/> <img src="https://img.shields.io/badge/amazonapigateway-FF4F8B?style=for-the-badge&logo=amazonapigateway&logoColor=white"/> <img src="https://img.shields.io/badge/ecr-FC4C02?style=for-the-badge&logo=ecr&logoColor=white"/>


### Develop Tool
 <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"> <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"> <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"> 


### Communication Tool
<img src="https://img.shields.io/badge/slack-4A154B?style=for-the-badge&logo=slack&logoColor=white"> <img src="https://img.shields.io/badge/notion-000000?style=for-the-badge&logo=notion&logoColor=white">

<br>
<br>

## 💫 동작 흐름

### 🌘 모델 선정

<img width="563" alt="12" src="https://github.com/COFFEE-BARA/be-book-recommendation/assets/97875918/494c0480-5f72-4707-8822-db3aa703b0d8">


- **모델 설명**:
    - 본 모델은 Sentence-transformers를 기반으로 하며 KLUE의 STS(Sentence Textual Similarity) 데이터셋을 통해 훈련을 진행한 모델입니다.
    - 한국어 문장간 결속성 측정 도구인 K-TAACO(가제)의 지표 중 하나인 문장 간 의미적 결속성을 측정하기 위해 본 모델을 제작하였습니다.
- **문장 간 의미적 유사도 측정**:
    - Sentence Transformers: 이 라이브러리는 문장 간의 사용된 LLM 모델은 문장 유사도 비교를 위해 특별히 설계되었음 의미적 유사도를 계산하기 위해 최적화되어 있습니다.
    - 한국어로 튜닝된 Sentence Transformers 모델을 사용하면, 벡터 공간에서 문장의 의미를 정확하게 캡처하고, 이를 바탕으로 유사도를 효율적으로 계산할 수 있습니다.
    - 사용자 쿼리와 도서 목차 간의 유사도를 계산하는 용도로 매우 적합합니다.

<br>

### 🌗 기능 컴포넌트

- **`API Gateway`**: 사용자로부터 책 추천 요청을 받아 Lambda 함수로 전달합니다.
- **`Lambda 함수`**: 사용자의 요청을 처리하고, ES Cloud의 LLM 모델을 사용하여 적절한 책 데이터를 검색합니다.
- **`ES Cloud`**:
    - **LLM 모델**: 사용자 쿼리를 바탕으로 관련성 높은 도서 정보를 분석합니다.
    - **book-index**: 책의 메타데이터를 저장하고 검색합니다.
    - **KNN 검색**: LLM 모델의 결과를 활용하여 도서 데이터에서 가장 유사한 항목을 찾아냅니다.
- **`Open AI`**: 본 시스템은 Open AI의 기능을 활용하여 사용자 쿼리에 최적화된 결과를 제공합니다.

<br>

### 🌖 기능 작동방식

<img width="526" alt="13" src="https://github.com/COFFEE-BARA/be-book-recommendation/assets/97875918/4c2975d1-6476-4a24-aa29-6bf9b98cbca2">


1. 사용자는 웹 인터페이스를 통해 책 추천을 위한 쿼리를 API Gateway에 전송합니다.
2. API Gateway는 이 요청을 Lambda 함수에 전달합니다.
3. Lambda 함수는 LLM 모델을 활용하여 ES Cloud 내의 `book-index`에서 쿼리와 관련된 도서 정보를 검색합니다.
4. 검색 결과는 KNN 알고리즘을 통해 더욱 정제되어, 가장 관련성 높은 도서 목록이 추출됩니다.
5. 최종 추천 도서 목록은 사용자에게 응답으로 반환됩니다.

<br>

### 🌕 기능 구현 및 배포

1. **키워드 선정**: 사용자의 쿼리에서 중요한 키워드 2개를 OpenAI 프롬프트를 활용하여 선정합니다.
    
    <img width="562" alt="14" src="https://github.com/COFFEE-BARA/be-book-recommendation/assets/97875918/c71fd486-fb52-48b0-91d8-d196be950296">

    
2. **Elasticsearch 검색**: 선정된 키워드를 이용해 Elasticsearch에서 `bool` `match` 쿼리 조건을 추가하고, 인덱스 내의 데이터와 사용자 쿼리의 벡터 유사도를 검색합니다.
    
    <img width="591" alt="15" src="https://github.com/COFFEE-BARA/be-book-recommendation/assets/97875918/49065d0e-4106-475c-a45a-248d98869caa">

    
3. **Docker 이미지 빌드 및 ECR 푸시**: 해당 기능을 구현한 코드를 Docker 이미지로 빌드하고, 생성된 이미지를 Amazon ECR로 푸시합니다.
4. **AWS Lambda 연결**: Amazon ECR에 푸시된 이미지를 기반으로 AWS Lambda 함수를 생성하여 서버리스 백엔드를 구현합니다.
5. **AWS API Gateway 연결:** 생성된 AWS Lambda 함수를 AWS API Gateway에 메소드를 생성하여 연결합니다.
