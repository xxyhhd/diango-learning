from django.conf.urls import url, include
from app.views import *


urlpatterns = [
    # 添加首页的路由
    url(r'^$', main.index),
    url(r'^test', main.test),

]
