"""Defines URL patterns for learning_logs."""
from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    #showing all topics.
    path('topics/', views.topics, name='topics'),
    #opening a topic page specific based on id:
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #so we are building an url in regarding the user want to enter the data:
    path('new_topic/',views.new_topic, name='new_topic'),
    #above we defined for to enter a new topic now for that topic writing entry below url is:
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #now modifying the entries:
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]