import json

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from .forms import PatchUserProfileForm
from .models import UserProfileInfo


# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class APIAccounts(View):

    def get(self, requests):
        if requests.user.is_authenticated:
            try:
                return JsonResponse(UserProfileInfo.get_accounts(requests.user.id), status=200)
            except AttributeError:
                return JsonResponse({"message": "Access denied"}, status=403)
        else:
            return JsonResponse({"message": "Unauthenticated"}, status=401)

    def post(self, requests):
        if requests.user.is_authenticated:
            try:
                try:
                    data = UserProfileInfo.objects.get(user_id=requests.user.id)
                    form = PatchUserProfileForm(requests.POST, requests.FILES, instance=data)
                    if form.is_valid():
                        form.save()

                except ObjectDoesNotExist:
                    # problem user_id
                    data = UserProfileInfo(
                        name=requests.POST.get('name'),
                        phone_number=requests.POST.get('phone_number'),
                        profile_picture=requests.FILES.get('profile_picture'),
                        bank_name=requests.POST.get('bank_name'),
                        bank_account=requests.POST.get('bank_account'),
                        description=requests.POST.get('description', ''),
                        user_id=requests.user.id
                    )
                    data.save()

            except Exception as e:
                raise e.with_traceback(e.__traceback__)
            else:
                return JsonResponse({'message': 'Update successfully'}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class APIAuth(View):
    def post(self, requests):
        authentication = authenticate(
            **json.loads(requests.body)
        )

        if authentication:
            if authentication.is_active:
                login(requests, authentication)
                return JsonResponse({"message": "Authentication lifted"}, status=200)
            else:
                return JsonResponse({"message": "Authentication denied"}, status=401)
        else:
            return JsonResponse({"message": "Invalid credentials"}, status=404)

    @login_required
    def delete(self, requests):
        try:
            logout(requests)
            return JsonResponse({"message": "Authentication revoked"}, status=200)
        except Exception:
            return JsonResponse({"message": "revoke failed"}, status=422)


class ViewAccounts(TemplateView):
    template_name = 'accounts/edit-profile.html'

    def get(self, requests, *args, **kwargs):
        context = self.get_context_data()
        context['data'] = UserProfileInfo.get_accounts(requests.user.id)
        return super().render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ViewLogin(TemplateView):
    template_name = 'accounts/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
