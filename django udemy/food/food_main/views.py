from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Item
from django.core import serializers

def index(request):
    return JsonResponse({"message": "Hello from food_main"})


def items1(request):
    items_list = Item.objects.all()
    items_json = []

    for item in items_list:
        items_json.append({
            "item_name": item.item_name,
            "item_desc": item.item_desc,
            "item_price": item.item_price,
            "to_string": item.__str__()
        })
    
    return JsonResponse(items_json, safe=False)

def items2(request):
    options = {}
    items_list = Item.objects.all()
    items_json = serializers.serialize('json', items_list,)
    return HttpResponse(items_json, content_type="application/json")

