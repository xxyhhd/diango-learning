# diango-learning
diango学习记录

1. django 安装
    Pip install django==1.11.4
	检查版本：
	>>> import django
	>>> django.get_version()
    '1.11.4'

2. django 命令
    建立虚拟环境
    pip install virtualenv
    python -m venv ‘name’ (先进入目标文件夹，然后此命令创建名为name的文件夹)
    激活虚拟环境
    建立虚拟环境后，进入新建文件夹中的Scripts文件夹中打开命令行输入：activate

    创建超级管理员
    python manage.py createsuperuser
    修改管理员密码
    python manage.py changepassword username

    进入name目录
    pip install django==
    django-admin startproject name: 创建名为name的django项目
    Django-admin starpapp name 创建应用
    python manage.py runserver 启动服务
    python manage.py runserver 0.0.0.0:8000 启动服务

    pip install mysqlclient  安装数据库
    python manage.py migrate  同步数据库
    python manage.py makemigrations 根据model模块创建数据库，（仅创建未同步）
    python manage.py startapp app_name  新建app

3. settings文件
```python
        import os
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'w#k4o9avped7h-$v@cz6--!x+f%b1nwddsz4z*c_=3yc$^mdeb'


    # Debug 功能
    DEBUG = True


    # 允许哪些主机允许访问，*是所有人
    ALLOWED_HOSTS = ['*']

    # 添加自己的应用
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    ]


    MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    ROOT_URLCONF = 'day1.urls'


    # 配置模板目录
    TEMPLATES = [
    {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    # 'DIRS': [],
    'DIRS': [os.path.join(BASE_DIR,'templates')],
    'APP_DIRS': True,
    'OPTIONS': {
    'context_processors': [
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    ],
    },
    },
    ]
    WSGI_APPLICATION = 'day1.wsgi.application'



    # Database
    # https://docs.djangoproject.com/en/1.11/ref/settings/#databases
    # 配置数据库，默认是sqlite
    # DATABASES = {
    # 'default': {
    # 'ENGINE': 'django.db.backends.sqlite3',
    # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    # }
    # 更改成MySQL
    DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'django', # 数据库名
    'USER': 'root',
    'PASSWORD': '123456789',
    'HOST': '127.0.0.1',
    'PORT': 3306,
    }
    }
    # 注意，更改为MySQL之后须在init文件添加如下代码
    # import pymysql
    # pymysql.install_as_MySQLdb()
    # Password validation



    # https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
    AUTH_PASSWORD_VALIDATORS = [
    {
    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    ]

    # 设置时区和中文
    # Internationalization
    # https://docs.djangoproject.com/en/1.11/topics/i18n/
    LANGUAGE_CODE = 'zh-hans'
    TIME_ZONE = 'Asia/Shangshai'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True



    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.11/howto/static-files/
    STATIC_URL = '/static/'
```

4. 配置视图文件
```python
    # App/users/main.py
    from django.shortcuts import render, HttpResponse 
    # render：渲染模板，HttpReponse：响应
    # Create your views here.

    def index(req):
    return HttpResponse('Hello, 你好')

    def test(req):
    return HttpResponse('测试')


    # App/users/__init__.py
    from .import main # 在init文件导入视图函数
```
5. 配置路由
```python
    # 应用里的urls.py, 需要单独创建
    from django.conf.urls import url, include
    from app.views import *
    urlpatterns = [
    # 添加首页的路由
    url(r'^$', main.index),
    url(r'^test', main.test),
    ]

    # 项目的urls.py
    from django.conf.urls import url, include
    from django.contrib import admin
    urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 添加来自应用的的路由
    url(r'^', include('app.urls')),
    ]
```