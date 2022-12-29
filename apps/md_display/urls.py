from django.urls import path
from . import views

app_name = "apps.md_display"

urlpatterns = [
    path("research/<int:slug>", views.detail, name='detail'),
]
