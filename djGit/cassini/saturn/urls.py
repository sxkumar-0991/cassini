from .views import ListSongsView
from django.conf.urls import url

app_name = 'saturn'

urlpatterns = [
    url(r'songs/',ListSongsView.as_view(), name='all-songs'),
]