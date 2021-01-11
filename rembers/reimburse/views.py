import os
import json

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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


def api_show_detail_reimburse(request, reimburse_id):
    data = Reimburse.get_one(id=reimburse_id)
    return HttpResponse(json.dumps(data), content_type="application/json")


def view_show_all(request):
    data_list = Reimburse.objects.all()
    paginator = Paginator(data_list, 10)

    try:
        data = paginator.page(request.GET.get('page', 1))
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    return render(request, 'reimburse/all.html', {"data": data})


def view_create_reimburse(requests):
    return render(requests, os.path.join('reimburse', 'form.html'))
