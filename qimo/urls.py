"""qimo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 用户管理
    path('login', views.login),
    path('register', views.register),
    path('mod', views.mod),
    path('delete', views.delete),
    path('find', views.find),
    path('finduser', views.find_userid),
    # 动漫管理
    path('upload', views.upload),
    path('addcomic', views.add_comic),
    path('deletecomic', views.delete_comic),
    path('findcomic', views.find_comic),
    path('findById', views.find_id),
    path('findIndexComic', views.find_index),
    path('findcomicByKey', views.find_key)
]
