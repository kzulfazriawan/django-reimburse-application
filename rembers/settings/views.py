import os
import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Settings


# Create your views here.

def api_get_settings(requests):
    return HttpResponse(json.dumps(Settings().all_as_dict()), content_type="application/json")


@csrf_exempt
def api_post_save_settings(requests):
    for k, v in json.loads(requests.body).items():
        record = Settings.objects.get(name=k)
        record.value = v
        record.save()
    return HttpResponse(json.dumps(Settings().all_as_dict()), content_type="application/json")


def view_settings(requests):
    return render(requests, os.path.join('settings', 'template.html'))
