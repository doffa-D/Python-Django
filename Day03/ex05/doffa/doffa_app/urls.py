from django.urls import path,include
from .views import doffa


urlpatterns = [
    path('', doffa),
]
