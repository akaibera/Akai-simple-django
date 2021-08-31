from django.urls import path
from .views import pallabdef

urlpatterns = [
    path('pallab/', pallabdef),
]