from django.urls import path
from . import views

urlpatterns = [
    path('api', views.APIReimburse.as_view(), name='reimburse_resource_api'),
    path('api/<int:reimburse_id>', views.api_show_detail_reimburse, name='api_show_detail_reimburse'),

    path('create/', views.ViewCreateReimburse.as_view(), name='view_create_reimburse_template'),
    path('detail/', views.ViewDetailReimburse.as_view(), name='view_detail_reimburse_template'),
    path('', views.ViewShowReimburse.as_view(), name='view_show_reimburse_template')
]
