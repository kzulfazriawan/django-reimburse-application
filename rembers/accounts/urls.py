from django.urls import path
from . import views

urlpatterns = [
    path('api', views.APIAccounts.as_view(), name='account_resources_api'),
    path('api/auth', views.APIAuth.as_view(), name='auth_resources_api'),

    path('update-profile', views.ViewAccounts.as_view(), name='view_account_template'),
#    path('profile', ),
    path('auth', views.ViewLogin.as_view(), name='view_auth_template'),
]
