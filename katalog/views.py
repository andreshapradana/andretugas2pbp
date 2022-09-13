from django.shortcuts import render
from katalog.models import CatalogItem

def show_catalog(request):
    data_catalog = CatalogItem.objects.all()
    context = {
        'list_barang': data_catalog,
        'nama': 'Andresha Pradana', 
        'NPM' : '2106651591'
    }
    return render(request, "katalog.html", context)
