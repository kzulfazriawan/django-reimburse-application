import os
import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator

from .models import Settings
from .forms import PostSaveSettings


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class APISettings(View):
    def get(self, requests):
        return JsonResponse(Settings.all_as_dict(), status=200, safe=False)

    def post(self, requests):
        for k, v in json.loads(requests.body).items():
            data = Settings.objects.get(name=k)
            form = PostSaveSettings({'value': v}, instance=data)
            if form.is_valid():
                form.save()
        return JsonResponse({'message': 'settings updated'}, status=200)


class ViewSettings(TemplateView):
    template_name = 'settings/template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def api_get_name_settings(requests):
    try:
        return JsonResponse(Settings.get_one(name=requests.GET.get("name", "category")), status=200)
    except AttributeError:
        return JsonResponse({'message': 'settings not found'}, status=404)
