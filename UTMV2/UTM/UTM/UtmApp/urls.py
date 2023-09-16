from django.urls import path
 
# importing views from views..py
from .views import *
 
urlpatterns = [
    path('', shorten_link, name='shorten_link'),
    path('result',decode,name='decode')
]