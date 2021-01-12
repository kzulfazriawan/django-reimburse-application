from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from .models import Reimburse


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class APIReimburse(View):
    def get(self, requests):
        if requests.user.is_authenticated:
            return JsonResponse(Reimburse.all_as_dict(requests.user.id), status=200, safe=False)
        else:
            return JsonResponse({'message': 'unauthenticated'}, status=401)

    def post(self, requests):
        if requests.user.is_authenticated:
            try:
                extension = str(requests.FILES['document_attach']).split('.')[-1].lower()

                if extension == 'jpg' or extension == 'jpeg':
                    extension = 'JPG'
                elif extension == 'png':
                    extension = 'PNG'
                elif extension == 'pdf':
                    extension = 'PDF'

                data = Reimburse(
                    date=requests.POST.get('date'),
                    document_attach=requests.FILES.get('document_attach'),
                    document_type=extension,
                    category=requests.POST.get('category'),
                    status='submitted',
                    amount=requests.POST.get('amount'),
                    description=requests.POST.get('description'),
                    user_id=requests.user.id
                )
                data.save()

            except Exception as err:
                raise err.with_traceback(err.__traceback__)
            else:
                return JsonResponse({'message': 'data saved'}, status=200)
        else:
            return JsonResponse({'message': 'unauthenticated'}, status=401)


class ViewCreateReimburse(TemplateView):
    template_name = 'reimburse/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ViewShowReimburse(TemplateView):
    template_name = 'reimburse/all.html'

    def get(self, requests, *args, **kwargs):
        if requests.user.is_authenticated:
            context = self.get_context_data()
            data = Reimburse.objects.filter(user_id=requests.user.id).order_by('id')

            paginator = Paginator(data, 10)

            try:
                data = paginator.page(requests.GET.get('page', 1))
            except PageNotAnInteger:
                data = paginator.page(1)
            except EmptyPage:
                data = paginator.page(paginator.num_pages)
            context['data'] = data
            return super().render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ViewDetailReimburse(TemplateView):
    template_name = 'reimburse/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def api_show_detail_reimburse(requests, reimburse_id):
    if requests.user.is_authenticated:
        return JsonResponse(Reimburse.get_one(id=reimburse_id, user_id=requests.user.id), status=200)
    else:
        return JsonResponse({'message': 'unauthenticated'}, status=401)
