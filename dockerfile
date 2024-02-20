# Elastic APM Lambda Extension 이미지
FROM docker.elastic.co/observability/apm-lambda-extension-x86_64:latest AS lambda-extension

# Elastic APM Python 에이전트 이미지
FROM docker.elastic.co/observability/apm-agent-python:latest AS python-agent


FROM amazon/aws-lambda-python:3.8

WORKDIR /var/task

COPY requirements.txt  .

RUN pip install -r requirements.txt

# Elastic APM 익스텐션과 Python 에이전트 파일을 Lambda 함수 이미지로 복사
COPY --from=lambda-extension /opt/elastic-apm-extension /opt/extensions/elastic-apm-extension
COPY --from=python-agent /opt/python/ /opt/python/
# elasticapm-lambda에 실행 권한 부여
RUN chmod +x /opt/python/bin/elasticapm-lambda

COPY . .

CMD ["query.lambda_handler"]
