from django.contrib import admin

# Register your models here.
from .models import WasteCollectionRequest, Collector

# Register WasteCollectionRequest model
admin.site.register(WasteCollectionRequest)

# Register Collector model
admin.site.register(Collector)
