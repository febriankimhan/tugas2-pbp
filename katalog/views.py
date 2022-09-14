from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    data_katalog = CatalogItem.objects.all()
    context = {
        'list_barang': data_katalog,
        'nama': 'Febrian Dwi Kimhan',
        'npm': '2106706691'
    }
    return render(request, "katalog.html", context)