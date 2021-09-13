from .base import *


env_list = dict()
local_env = open(os.path.join(BASE_DIR, '.env')) #운영체제 경로에서 base_dir과 .env join 한 경로

while True:
    line = local_env.readline()
    if not line:
        break
    line = line.replace('\n', '')
    start = line.find('=') #=을 find해서 start에
    key = line[:start]
    value = line[start+1:] #=부분은 필요없으니까 +1
    env_list[key] = value

SECRET_KEY = env_list['SECRET_KEY'] #.env에서 해당 value 받아오기

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'password',
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}

