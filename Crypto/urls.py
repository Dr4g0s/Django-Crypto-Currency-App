from django.urls import path
from .views import crypto, prices

app_name = "Crypto"

urlpatterns = [
    path('', crypto, name='crypto'),
    path('prices/', prices, name='prices'),
]
