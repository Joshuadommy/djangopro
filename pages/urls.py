from django.urls import path
from django.urls.resolvers import URLPattern
from .views import home_page_view

urlpatterns = [
    path('', home_page_view, name='home')
]