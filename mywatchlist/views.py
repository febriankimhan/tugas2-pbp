from django.shortcuts import render
from mywatchlist.models import MyWatchList

from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data = MyWatchList.objects.all()
    watched_movies = MyWatchList.objects.filter(watched=True)
    if len(watched_movies) >= len(data) // 2:
        teks = "Selamat, kamu sudah banyak menonton!"
    else:
        teks = "Wah, kamu masih sedikit menonton!"
    context = {
        'list_mywatchlist': data,
        'conclusion': teks
    }
    return render(request, "mywatchlist.html", context)

def show_mywatchlist_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_mywatchlist_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")