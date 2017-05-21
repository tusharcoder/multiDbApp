from django.conf.urls import url
from .views import *


urlpatterns = [
    #api urls
    url(r'^test/$',getTestData),
]
