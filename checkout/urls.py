from django.conf.urls import url
from .views import checkout

"""Url for the checkout app"""

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
]