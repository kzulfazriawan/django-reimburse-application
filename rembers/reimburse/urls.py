from django.urls import path
from . import views

urlpatterns = [
    path('api/save', views.api_post_new_reimburse, name='api_post_new_reimburse'),

    path('post/', views.view_create_reimburse, name='view_create_reimburse')
]
