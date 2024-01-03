"""d04 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from ex00.views import index
from ex01.views import django_history,django_display,django_templates,django_nav
from ex02.views import Django_from
from ex03.views import color

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ex00/', index),
    path('ex01/django', django_history),
    path('ex01/display', django_display),
    path('ex01/templates', django_templates),
    path('ex01/nav', django_nav),
    path('ex02/', Django_from),
    path('ex03/', color),
]
