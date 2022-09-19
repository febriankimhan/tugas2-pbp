from django.urls import path
from mywatchlist.views import show_mywatchlist, show_mywatchlist_xml, show_mywatchlist_json

app_name = 'mywatchlist'

urlpatterns = [
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', show_mywatchlist_xml, name='show_mywatchlist_xml'),
    path('json/', show_mywatchlist_json, name='show_mywatchlist_json'),
]