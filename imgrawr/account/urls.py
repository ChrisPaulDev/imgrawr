from django.conf.urls import include, url

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^account/login/$', auth_views.login, name='account_login'),
    url(r'^account/logout/$', auth_views.logout, name='account_logout'),
    url(r'^account/', include('registration.backends.simple.urls')),
]