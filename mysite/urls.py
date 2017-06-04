"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
    
    url(r'^join/$', views.signup, name='join'),
    url(r'^login/$', auth_views.login, name='login', kwargs={'template_name': 'mia/login.html'}),
    url(r'^logout/$', auth_views.logout, name='logout', kwargs={'template_name': 'mia/logout.html'}),
"""
from django.conf.urls import url,include
from django.contrib import admin
from mia import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from mia.views import UserCreateView,UserCreateDone

urlpatterns = [
    url(r'^',include('mia.urls',namespace='mia')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^signup/$',UserCreateView.as_view(), name='signup'),
    url(r'^signup_ok/$',UserCreateDone.as_view(), name='signup_ok'),
]