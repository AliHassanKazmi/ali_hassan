"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from myapp.views import mechanical
from myapp.views import all_equipment
from myapp.views import dashboard_view
from myapp.views import chart_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mechanical/<str:equipment>/', mechanical, name='mechanical'),
    path('allequipment/', all_equipment, name='all_equipment'),
    path('', dashboard_view, name='dashboard'),
    path('chart/', chart_view, name='chart'),




]
