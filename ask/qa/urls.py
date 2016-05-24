from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^question/(?P<pk_question>\d+)/$', views.question, name='question'),
    url(r'^ask/.*$', views.ask),
    url(r'^popular/.*$', views.popular),
    url(r'^new/.*$', views.index)
]

admin.autodiscover()