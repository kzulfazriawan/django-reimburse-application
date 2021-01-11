from django.urls import path
from . import views

urlpatterns = [
    path('api/save', views.api_post_new_reimburse, name='api_post_new_reimburse'),
    path('api/<int:reimburse_id>', views.api_show_detail_reimburse, name='api_show_detail_reimburse'),

    path('post/', views.view_create_reimburse, name='view_create_reimburse'),
    path('all/', views.view_show_all, name='view_show_all')
]
