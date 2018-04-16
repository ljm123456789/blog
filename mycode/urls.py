from django.conf.urls import url
from . import views

app_name = 'mycode'

urlpatterns = [

    url('^datain/$', views.datain, name='datain'),
    url('^dataout/$', views.dataout, name='dataout'),
    url('^checkqr/$', views.checkqr, name='checkqr'),
    url('^query/$', views.query, name='query'),
    url('^test/', views.test),
    url('^login/',views.verify_user),
    url('^builddir/$', views.builddir, name='builddir'),
    # url('^basic/$', views.basci, name='basic'),

]


