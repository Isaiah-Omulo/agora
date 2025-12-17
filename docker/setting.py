import os

class BaseConfig(object):
    ENV = 'production'
    DEBUG = False
    TESTING = False

    APP_ID = os.environ.get("AGORA_APP_ID")
    APP_CERTIFICATE = os.environ.get("AGORA_APP_CERTIFICATE")
