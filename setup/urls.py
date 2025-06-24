from django.contrib import admin
from django.urls import path

# Importar view
from todos.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
]
