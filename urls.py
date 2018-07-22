"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from web.app1 import views
from web.app2 import views as v2

from django.conf.urls import url
from web.app3 import views as v3

from app4 import views as v4

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index, name='index'),
    # path('index2', v2.index, name='index'),
    # path('table/', views.table, name='table'),
    # path('table1/', views.table1, name='table1'),
    # path('add/', views.add, name='add'),
    # url(r'^add2/(\d+)/(\d+)/$', views.add2, name='add'),
    # url(r'^value/(\d+)/$', views.value, name='value'),
    # path('home_list/', views.home_list, name='home'),
    # path('home1/', views.index1, name='home1'),
    # app2
    # url(r'^articles/(\d+)/$', v2.year_archive),
    # url(r'^articles/([0-9]{4})/([0-9]{2})/$',app2.views.)
    # app3
    url(r'^book/$', v3.latest_books),
    path('',v3.index, name = 'index'),
    url(r'^add/(\d+)/(\d+)/$', v3.add, name = 'add'),
    path('index/',v4.index, name = 'index'),

]
