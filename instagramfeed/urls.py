from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('public.urls')),
    url(r'^admin/', admin.site.urls),
]
