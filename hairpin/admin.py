from django.contrib import admin
from hairpin.models import Category, Product, Cami, Order, PayRecord, CAMI_TYPE_MAP


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    分类管理
    """
    list_display = ['id', 'title', 'desc']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    产品管理
    """
    list_display = ['id', 'category_name', 'title', 'cami_type_name', 'price', 'desc', 'status']

    def category_name(self, obj):
        return obj.category.title

    def cami_type_name(self, obj):
        return CAMI_TYPE_MAP[obj.cami_type]

    cami_type_name.short_description = '卡密类型'
    category_name.short_description = '产品分类'


@admin.register(Cami)
class CamiAdmin(admin.ModelAdmin):
    """
    卡密管理
    """
    pass


@admin.register(PayRecord)
class PayRecordAdmin(admin.ModelAdmin):
    """
    支付记录管理
    """
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    订单管理
    """
    pass
