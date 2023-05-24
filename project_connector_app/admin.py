from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(guide)
admin.site.register(team)
admin.site.register(debugg)
admin.site.site_header = "Project Connector"
admin.site.site_title = "Project Connector"
admin.site.site_index = "Project Connector"