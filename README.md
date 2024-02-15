# be-book-recommendation

## OpenAI & Elasticsearch 기반 서버리스 백엔드 구현

이 프로젝트는 OpenAI의 프롬프트를 사용하여 사용자 쿼리에서 중요한 키워드를 선정하고, 선정된 키워드로 Elasticsearch의 Search API를 활용해 벡터 유사도 검색을 수행하는 서버리스 백엔드 구현을 목표로 합니다. 구현된 코드는 Docker 이미지로 빌드되어 Amazon ECR(Elastic Container Registry)로 푸시되며, AWS Lambda를 통해 서버리스 아키텍처를 구성합니다.

## 프로젝트 흐름

1. **키워드 선정**: 사용자의 쿼리에서 중요한 키워드 2개를 OpenAI 프롬프트를 활용하여 선정합니다.
2. **Elasticsearch 검색**: 선정된 키워드를 이용해 Elasticsearch에서 `bool` `match` 쿼리 조건을 추가하고, 인덱스 내의 데이터와 사용자 쿼리의 벡터 유사도를 검색합니다.
3. **Docker 이미지 빌드 및 ECR 푸시**: 해당 기능을 구현한 코드를 Docker 이미지로 빌드하고, 생성된 이미지를 Amazon ECR로 푸시합니다.
4. **AWS Lambda 연결**: Amazon ECR에 푸시된 이미지를 기반으로 AWS Lambda 함수를 생성하여 서버리스 백엔드를 구현합니다.

## 시작하기 전에

이 프로젝트를 시작하기 전에 다음 요구 사항을 충족해야 합니다:

- AWS 계정 및 AWS CLI 설치 및 구성
- Docker 설치
- OpenAI API 키
- Elasticsearch 서버 또는 Elasticsearch Service 계정

## 설정 단계

### 1. OpenAI API 키 설정

OpenAI API를 사용하기 위해, `.env` 파일 또는 환경 변수에 OpenAI API 키를 설정합니다.

```bash
export OPENAI_API_KEY='your_openai_api_key_here'
```

### 2. Elasticsearch 연결 정보 설정

Elasticsearch 연결 정보(예: 호스트, 포트, 사용자 이름, 비밀번호 등)를 환경 변수에 설정합니다.

### 3. Docker 이미지 빌드 및 ECR 푸시

Dockerfile을 사용하여 Docker 이미지를 빌드하고, 생성된 이미지를 AWS ECR로 푸시합니다.

```bash
# Docker 이미지 빌드
docker build -t your-image-name .

# ECR 로그인
aws ecr get-login-password --region your-region | docker login --username AWS --password-stdin your-aws-account-id.dkr.ecr.your-region.amazonaws.com

# Docker 이미지 태그 지정
docker tag your-image-name:latest your-aws-account-id.dkr.ecr.your-region.amazonaws.com/your-image-name:latest

# Docker 이미지 ECR로 푸시
docker push your-aws-account-id.dkr.ecr.your-region.amazonaws.com/your-image-name:latest
```

### 4. AWS Lambda 함수 생성

AWS Lambda 콘솔 또는 AWS CLI를 사용하여 ECR에 푸시된 Docker 이미지를 기반으로 Lambda 함수를 생성합니다.

## 사용 예시

사용자가 "서버리스 환경으로 배포를 하고 싶은데 관련한 책을 추천해줘"와 같은 쿼리를 제출할 경우, 시스템은 다음과 같은 프로세스를 거쳐 응답을 제공합니다:

1. OpenAI 프롬프트를 통해 "서버리스", "배포"와 같은 키워드를 추출합니다.
2. 추출된 키워드를 사용하여 Elasticsearch에서 관련 도서 정보를 검색합니다.
3. 검색 결과를 사용자에게 반환합니다.

## 기여하기

프로젝트에 기여하고 싶으신 분은, pull request를 통해

 기여할 수 있습니다. 모든 기여자는 프로젝트의 발전에 소중한 역할을 합니다.

