from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_mywatchlist = MyWatchList.objects.all()
    counteryes = 0
    counterno = 0
    for movie in data_mywatchlist:
        if (movie.watched == "Yes"):
            counteryes += 1
        elif (movie.watched == "No"):
            counterno += 1
    if (counteryes > counterno):
        message = "Selamat, kamu sudah banyak menonton!"
    else:
        message = "Wah, kamu masih sedikit menonton!"
        
    context = {
        'list_movie': data_mywatchlist,
        'nama': 'Andresha Pradana', 
        'NPM' : '2106651591',
        'Pesan' : message
    }
        
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")