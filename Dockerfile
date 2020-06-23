FROM node:14.4.0-stretch-slim as Node_Builder

WORKDIR /app
COPY cheers-fornt .

RUN set -ex ;\
    npm install --registry=https://registry.npm.taobao.org ;\
    npm run build

FROM python:3.7.7-slim-stretch

WORKDIR /app
COPY requirements.txt ./requirements.txt
COPY sources.list /etc/apt/sources.list


RUN set -ex ;\
    apt update ;\
    apt install -y default-libmysqlclient-dev gcc ;\
#    rm -rf /var/lib/apt/lists/* ;\
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --no-cache-dir

COPY . .
COPY --from=Node_Builder /templates ./templates

EXPOSE 80