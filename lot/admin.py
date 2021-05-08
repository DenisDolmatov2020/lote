from django.contrib import admin
from lot.models import Lot, Image


class LotImageInline(admin.TabularInline):
    fk_name = 'lot'
    model = Image


@admin.register(Lot)
class LotAdmin(admin.ModelAdmin):
    inlines = [LotImageInline]
