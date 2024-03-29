from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:title>/', views.entry_detail, name='entry_detail'),
    path('search/', search_entries, name="search_entries")
]
