from django.urls import path

from . import views as ecr_views

urlpatterns = [
    path('', ecr_views.ecr_info.as_view(), name='ecr_info'),
    path('request/', ecr_views.ecr_request.as_view(), name='ecr_request'),
    path('status/', ecr_views.ecr_status.as_view(), name='ecr_status'),
]
