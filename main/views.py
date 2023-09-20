
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.shortcuts import render

from main.forms import ItemForm
from main.models import Item

def show_main(request):
    items = Item.objects.all()

    context = {
        'name': 'Vinka Alrezky As', # Nama kamu
        'id': '2206820200',
        'class': 'PBP A', # Kelas PBP kamu
        'items': items
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
    

def show_xml(request: HttpRequest) -> HttpResponse:
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_xml_by_id(request: HttpRequest, id: int) -> HttpResponse:
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request: HttpRequest) -> HttpResponse:
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_json_by_id(request: HttpRequest, id: int) -> HttpResponse:
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
