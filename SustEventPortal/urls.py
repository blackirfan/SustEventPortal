
from django.conf.urls import include, url
from django.contrib import admin



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^organization/', include('organization.urls')),
    # url(r'^organization/organization.id ', include('organization.urls')),
]
