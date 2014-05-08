# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from ideas.views import *

urlpatterns = patterns('',
    url(r'^$', IdeasListView.as_view(), name='index'),
    url(r'vote/', vote, name='vote'),
    url(r'create/', CreateIdeaView.as_view(), name='create'),
    url(r'details/(?P<slug>[\w-]+)', IdeasDetailView.as_view(), name='details'),
    url(r'delete/(?P<slug>[\w-]+)', DeleteIdeaView.as_view(), name='delete'),
    url(r'update/(?P<slug>[\w-]+)', UpdateIdeaView.as_view(), name='update'),
)
