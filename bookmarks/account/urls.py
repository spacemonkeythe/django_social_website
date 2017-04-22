from django.conf.urls import url
from django.contrib.auth.views import login as django_login, logout as django_logout
#from django.contrib.auth.views import logout-then-login
from . import views

urlpatterns = [
    #url(r'^login/$', views.user_login, name='login'),

    url(r'^login/$', django_login, name='login'),
    url(r'^logout/$', django_logout, name='logout'),
    # url(r'^logout-then-login/$',
    #     logout-then-login,
    #     name='logout-then-login'),
    url(r'^$', views.dashboard, name='dashboard')
]
