from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^profile$', views.index, name='index'),
    url(r'^submit/(?P<user_id>\w{0,10})-(?P<level>\w{0,10})/$', views.submit, name='show'),
    url(r'^show/(?P<submit_id>\w{0,10})/$', views.show, name='show'),
    url(r'^rates', views.rates, name='rates'),
]
