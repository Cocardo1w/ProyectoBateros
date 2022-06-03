from django.contrib import admin
from appbateros.models import Blog

from appbateros.views import post
from appbateros.models import Blog

# Register your models here.
admin.site.register(Blog)