from django.urls import path

from . import views as ecr_views

urlpatterns = [
    path(
        'find/',
        ecr_views.mentor_find.as_view(),
        name='mentor_find'),
    path(
        'find/<int:cid>/',
        ecr_views.mentor_display.as_view(),
        name='mentor_display'),
    path(
        'request/<int:cid>/',
        ecr_views.mentor_display.as_view(),
        name='mentor_request'),
    path(
        'update/<int:cid>/',
        ecr_views.mentor_profile_edit.as_view(),
        name='mentor_profile_edit'),
]
