import json

from django.http import JsonResponse
from django.shortcuts import render


def index_view(request):
    return render(request, "visualize/index.html", {})


def get_view(request):
    with open("dump/messages.json", encoding='utf-8') as json_file:
        data = json.load(json_file)

    return JsonResponse(data, safe=False)

