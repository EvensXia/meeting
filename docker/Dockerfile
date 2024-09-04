FROM ubuntu:24.04

ENV TZ=Asia/Shanghai \
    DEBIAN_FRONTEND=noninteractive \
    VIRTUAL_ENV=/opt/venv \
    PATH="$VIRTUAL_ENV/bin:$PATH"

RUN apt update && apt upgrade -y && apt install -y \
    python3-venv python-is-python3 python3-setuptools python3-pip \
    python3-dev default-libmysqlclient-dev build-essential pkg-config  \
    && ln -fs /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && dpkg-reconfigure --frontend noninteractive tzdata \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m venv $VIRTUAL_ENV
RUN ln -sf $VIRTUAL_ENV/bin/python /usr/bin/python

# build input ARG
ARG WECHAT_APPID
ARG WECHAT_APPSECRET
ENV WECHAT_APPID=${WECHAT_APPID}
ENV WECHAT_APPSECRET=${WECHAT_APPSECRET}

COPY server/requirements.txt /tmp/requirements.txt
# 安装Python库到虚拟环境
RUN python3 -m pip install --upgrade pip \
    && pip install -r /tmp/requirements.txt

WORKDIR /app/mettings
COPY . .
WORKDIR /app/mettings/server
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
