"""应用程序users定义URL模式"""
from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    #登录页面
    url(r'^login/$',login,{'template_name':'users/login.html'},name='login'),
    #我们没有编写自己的视图login,所有后面的{。。。}里的字典内容就是视图信息，告诉去哪里找模板

    #注销
    url(r'^logout/$',views.logout_view,name='logout'),
    #注册
    url(r'^register/$',views.register,name='register'),

]