from django.contrib import admin
from shop.models import GroupShop, Shop, ShopCondition


class ShopConditionInline(admin.TabularInline):
    fk_name = 'shop'
    model = ShopCondition


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    inlines = [ShopConditionInline]


admin.site.register(GroupShop)
