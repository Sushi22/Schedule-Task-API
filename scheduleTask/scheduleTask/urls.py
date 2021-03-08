"""scheduleTask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url,include
from django.urls import path
from api.views import PingView,ScheduleView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/ping/$',PingView.as_view()), # ping endpoint
    url(r'^api/(?P<date>[0-9A-Za-z_\- :.]+)/(?P<url>https?:\/\/[^\s]+)/$',ScheduleView.as_view()) # schedule endpoint
]