from django.contrib import admin


from .models import REG,PLACE
from django.contrib import admin
from rest_framework_api_key.admin import APIKeyModelAdmin
from .models import OrganizationAPIKey

@admin.register(OrganizationAPIKey)
class OrganizationAPIKeyModelAdmin(APIKeyModelAdmin):
    pass
admin.site.register(REG)
admin.site.register(PLACE)