"""
URL configuration for d05 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ex00.views import ex00
from ex02.views import Movies02,populate,display
from ex03.views import populate,display
from ex04.views import init,populate,display,remove

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ex00/init/', ex00),
    path('ex02/init/', Movies02),
    path('ex02/populate/', populate),
    path('ex02/display/', display),
    path('ex03/populate/', populate),
    path('ex03/display/', display),
    path('ex04/init/', init),
    path('ex04/populate/', populate),
    path('ex04/display/', display),
    path('ex04/remove/', remove),
]
