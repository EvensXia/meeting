# encoding: utf-8
from __future__ import absolute_import, unicode_literals
import os
from loguru import logger
SECRET_KEY = 'input your secret key'

REDIS_HOST = '127.0.0.1'
REDIS_PASSWORD = ''
REDIS_PORT = '6379'
REDIS_CACHE_DB = 5
REDIS_SESSION_DB = 6
REDIS_CELERY_DB = 7
REDIS_CONSTANCE_DB = 8
REDIS_CHANNEL_DB = 9

# CREATE SCHEMA `meeting` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci ;

# MYSQL_HOST = '127.0.0.1'
# MYSQL_PORT = '3306'
# MYSQL_DBNAME = 'meeting'
# MYSQL_USERNAME = 'root'
# MYSQL_PASSWORD = ''

WECHAT_APPID = os.environ.get("WECHAT_APPID")
WECHAT_APPSECRET = os.environ.get("WECHAT_APPSECRET")
logger.info(f"WECHAT_APPID = {WECHAT_APPID}")
logger.info(f"WECHAT_APPSECRET = {WECHAT_APPSECRET}")
# 配置以下信息管理员会收到异常邮件，不需要可直接删除
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
SERVER_EMAIL = ''
DEFAULT_FROM_EMAIL = ''

ADMINS = (('管理员姓名', '管理员邮箱'),)
