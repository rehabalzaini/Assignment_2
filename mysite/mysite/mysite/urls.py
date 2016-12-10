"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from todo.views import show_todo,get_todo
from users.views import signup
from blog.views import show_entries,get_entry
from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
url(r'^todo/$', show_todo),
url(r'^blog/entries/$', show_entries),
    url(r'^todo/(?P<todo_id>[0-9]+)', get_todo),
    url(r'^blog/entries/(?P<entry_id>[0-9]+)', get_entry),
    url(r'^users/register/$', signup),
    url(r'^users/', include("django.contrib.auth.urls")),
    url(r'^blog/entries/', include("django.contrib.auth.urls"))

]
