from django.contrib import admin

# Register your models here.
from .models import Furniture, Appliance, Disc, Technology, Other

class FurnitureAdmin(admin.ModelAdmin):
    model = Furniture
    list_display = ['name', 'location',]

admin.site.register(Furniture, FurnitureAdmin)

class ApplianceAdmin(admin.ModelAdmin):
    model = Appliance
    list_display = ['name', 'location',]

admin.site.register(Appliance, ApplianceAdmin)

class DiscAdmin(admin.ModelAdmin):
    model = Disc
    list_display = ['name', 'location',]

admin.site.register(Disc, DiscAdmin)

class TechnologyAdmin(admin.ModelAdmin):
    model = Technology
    list_display = ['name', 'location',]

admin.site.register(Technology, TechnologyAdmin)

class OtherAdmin(admin.ModelAdmin):
    model = Other
    list_display = ['name', 'location',]

admin.site.register(Other, OtherAdmin)