from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.index,name ='index'),
    url(r'^(?P<organization_id>\d+)/$', views.detail, name='detail'),


#in here ? symbol P <organization_id> is resent the table id name.
]