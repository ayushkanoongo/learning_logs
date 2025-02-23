# from django.urls import path, url
from django.conf.urls import url

from . import views

app_name = 'learning_logs'
urlpatterns = [
    #home page
    url(r'^$', views.index, name='index'),

    #Show all topics
    url(r'^topics/$', views.topics, name='topics'),

    #Detail Page for a single topic
    url(r'^topics/(?P<topic_id>\d+)$', views.topic,name='topic'),

    #Page for adding a new Topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    #Page for adding a new entry,
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    #Page for edit entries
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry')
]