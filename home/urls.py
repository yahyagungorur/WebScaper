from django.conf.urls import url,include
from home.views import *

app_name = 'home'
urlpatterns = [
    url(r'^$', home_view),
    url(r'^search/$', search),
]