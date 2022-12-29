from django.urls import path
from . import views
from apps.md_display import views as md_views
app_name = "apps.main"

urlpatterns = [
    path("", views.index, name="index"),
    path("researches/", md_views.researches, name="researches"),
    path("<str:slug>/", views.general, name="general"),
]
