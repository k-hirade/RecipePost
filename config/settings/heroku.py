import os
import dj_database_url

from .common import *

DEBUG = False

ALLOWED_HOSTS = ["*", ]

DATABASES = {
    'default': dj_database_url.config()
}

