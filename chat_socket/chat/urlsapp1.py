from django.urls import path
from chat.views import *

app_name = 'chat'

urlpatterns = [
    path('', main, name='main'),
    path('login/', login, name='main'),
]