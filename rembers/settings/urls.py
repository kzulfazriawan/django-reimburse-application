from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.api_get_settings, name='api_get_settings'),
    path('api/name/', views.api_get_name_settings, name='api_get_name_settings'),
    path('api/save', views.api_post_save_settings, name='api_save_settings'),

    path('', views.view_settings, name='view_settings')
]
