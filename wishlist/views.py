import http
from django.http import HttpResponse
from django.core import serializers

from django.shortcuts import render
from wishlist.models import BarangWishlist

# Create your views here.
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Jeremy Alva Prathama'
    }

    return render(request, "wishlist.html", context)

def retrieve_xml(request):
    data = BarangWishlist.objects.all()

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def retrieve_json(request):
    data = BarangWishlist.objects.all()

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def retrieve_xml_by_id(request, id):
    data = BarangWishlist.objects.filter(pk=id)

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def retrieve_json_by_id(request, id):
    data = BarangWishlist.objects.filter(pk=id)

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


