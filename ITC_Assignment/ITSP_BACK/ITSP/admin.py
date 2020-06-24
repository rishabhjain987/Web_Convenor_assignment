from django.contrib import admin

# Register your models here.
from .models import itsp_team
admin.site.site_header = "ITSP Admin"
admin.site.site_title = "ITSP Admin Area"
admin.site.index_title = "Welcome to ITSP Admin Area"

admin.site.register(itsp_team)
