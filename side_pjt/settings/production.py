# config/settings/development.py

from .base import *

DEBUG = True

ALLOWED_HOSTS = [
 # EC2 퍼블릭 주소
 '13.125.225.154',
 'ddoongddangs.com',
]