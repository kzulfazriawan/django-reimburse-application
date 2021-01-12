from django.urls import path
from . import views

urlpatterns = [
    path('api', views.APISettings.as_view(), name='settings_resources_api'),
    path('api/first', views.api_get_name_settings, name='api_get_name_settings'),

    path('', views.ViewSettings.as_view(), name='view_settings_template')
]
