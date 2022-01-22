from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from hackapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('hackapp.urls')),
]
