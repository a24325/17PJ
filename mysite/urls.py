"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from home.views import Small_covers
from home.views import Small_covers2
from home.views import Small_covers3
urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    url(r'^$', Small_covers.as_view(),name='home'),
    url(r'^result/$',Small_covers2.as_view(),name='result'),
    url(r'^result2/$',Small_covers3.as_view(),name='result2'),
]
