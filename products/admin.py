from django.contrib import admin
from .models import Product, Category, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'category', 'price', 'stock_quantity', 'featured', 'tag')
    list_filter = ('category', 'featured', 'farm_source', 'tag')
    search_fields = ('name', 'sku', 'description')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('sku',)
    inlines = [ProductImageInline]
    fieldsets = (
        (None, {
            'fields': ('name', 'sku', 'category', 'description', 'slug')
        }),
        ('Pricing', {
            'fields': ('price', 'offer_price')
        }),
        ('Details', {
            'fields': ('weight', 'stock_quantity', 'farm_source', 'best_before')
        }),
        ('Display', {
            'fields': ('featured', 'tag', 'label', 'rating', 'image')
        }),
        ('Options', {
            'fields': ('has_sizes', 'related_products')
        }),
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name')
    search_fields = ('name', 'slug')

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'alt_text')
    search_fields = ('product__name', 'alt_text')
