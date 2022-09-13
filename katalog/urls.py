from django.urls import path
from katalog.views import show_catalog

app_name = 'catalog'

urlpatterns = [
    path('', show_catalog, name='show_catalog'),
]