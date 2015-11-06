"""project URL Configuration

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
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from main.models import CustomUser, Thread, Post
from main import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user_detail_view/(?P<pk>.+)/$', views.UserDetailView.as_view()),
    url(r'^sign_up/$', 'main.views.signup', name='signup_view'),
    url(r'^login/$', 'main.views.login_view', name='login_view'),
    url(r'^logout/$', 'main.views.logout_view', name='logout_view'),
    url(r'^user_search/$', 'main.views.user_search', name='user_search'),
    url(r'^user_list/$', views.UserListView.as_view()),
    url(r'^user_edit/(?P<pk>\d+)/$','main.views.user_edit'),
    url(r'^invalid_user/$', 'main.views.invalid_user'),
    url(r'^thread_detail/(?P<pk>.+)/$', views.ThreadDetailView.as_view()),
    url(r'^thread_list/$', views.ThreadListView.as_view()),
    url(r'^post_detail/(?P<pk>.+)/$', views.PostDetailView.as_view()),
    url(r'^post_list/$', views.PostListView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
