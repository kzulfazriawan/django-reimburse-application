import os
import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Reimburse
from .forms import ReimburseUploadForm


# Create your views here.

@csrf_exempt
def api_post_new_reimburse(requests):
    form = ReimburseUploadForm(requests.POST, requests.FILES)
    if form.is_valid():
        form.save()
        return JsonResponse({'error': False, 'message': 'Upload successfully'})
    else:
        return JsonResponse({'error': True, 'errors': form.errors})


def view_create_reimburse(requests):
    return render(requests, os.path.join('reimburse', 'form.html'))
