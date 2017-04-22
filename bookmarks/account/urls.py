from django.conf.urls import url
from django.contrib.auth import views as auth_views
#from django.contrib.auth.views import logout-then-login
from . import views

urlpatterns = [
    #url(r'^login/$', views.user_login, name='login'),

    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    # url(r'^logout-then-login/$',
    #     logout-then-login,
    #     name='logout-then-login'),
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^password-change$', auth_views.password_change, name='password_change'),
    url(r'^password-change-done$', auth_views.password_change_done, name='password_change_done')
]
