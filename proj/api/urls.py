from django.urls import path
from .api import *


urlpatterns = [
    path('get_emotitoken', GetEmotitokenView.as_view(), name='create_emotitoken'),
]