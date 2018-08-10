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


class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ['name', 'location',]

admin.site.register(Book, BookAdmin)


class ElectronicsAdmin(admin.ModelAdmin):
    model = Electronics
    list_display = ['name', 'location',]

admin.site.register(Electronics, ElectronicsAdmin)


class CampingAdmin(admin.ModelAdmin):
    model = Camping
    list_display = ['name', 'location',]

admin.site.register(Camping, CampingAdmin)


class CarAdmin(admin.ModelAdmin):
    model = Car
    list_display = ['name', 'location',]

admin.site.register(Car, CarAdmin)


class KitchenwareAdmin(admin.ModelAdmin):
    model = Kitchenware
    list_display = ['name', 'location',]

admin.site.register(Kitchenware, KitchenwareAdmin)


class SportAdmin(admin.ModelAdmin):
    model = Sport
    list_display = ['name', 'location',]

admin.site.register(Sport, SportAdmin)


class MusicAdmin(admin.ModelAdmin):
    model = Music
    list_display = ['name', 'location',]

admin.site.register(Music, MusicAdmin)


class PuzzlesAndGamesAdmin(admin.ModelAdmin):
    model = PuzzlesAndGames
    list_display = ['name', 'location',]

admin.site.register(PuzzlesAndGames, PuzzlesAndGamesAdmin)


class ToolAdmin(admin.ModelAdmin):
    model = Tool
    list_display = ['name', 'location',]

admin.site.register(Tool, ToolAdmin)


class OrnamentAdmin(admin.ModelAdmin):
    model = Ornament
    list_display = ['name', 'location',]

admin.site.register(Ornament, OrnamentAdmin)


class StationaryAdmin(admin.ModelAdmin):
    model = Stationary
    list_display = ['name', 'location',]

admin.site.register(Stationary, StationaryAdmin)


class OtherAdmin(admin.ModelAdmin):
    model = Other
    list_display = ['name', 'location',]

admin.site.register(Other, OtherAdmin)