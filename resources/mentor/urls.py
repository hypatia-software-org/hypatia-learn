from django.urls import path

from . import views as ecr_views

urlpatterns = [
    path('find/', ecr_views.mentor_find.as_view(), name='mentor_find'),
]
