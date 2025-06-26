from django.contrib import admin
from .models import CowinData
from .models import *

class CowinDataAdmin(admin.ModelAdmin):
    list_display = [
        "center_id","name","state","pincode","fee_type","fee",
    ]



admin.site.register(CowinData, CowinDataAdmin)