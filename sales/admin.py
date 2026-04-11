from django.contrib import admin
from django.db import models
from .models import Supplier, Category, Item, Order, OrderItem


# -------------------------
# Supplier Admin
# -------------------------
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)


# -------------------------
# Category Admin
# -------------------------
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)


# -------------------------
# Item Admin
# -------------------------
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "supplier", "price", "unit", "created_at")
    list_filter = ("category", "supplier", "unit")
    search_fields = ("name",)


# -------------------------
# OrderItem Inline
# -------------------------
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    fields = ("item", "quantity", "unit_price", "price")
    readonly_fields = ("price",)


# -------------------------
# Order Admin
# -------------------------
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "order_reference",
        "farmer",
        "cooperative",
        "order_price",
        "status",
        "order_date",
        "accept_date",
        "reject_date",
        "ship_date",
        "collect_date",
    )
    list_filter = ("status", "order_date", "cooperative")
    search_fields = ("order_reference", "farmer__surname", "farmer__first_name")
    exclude = ("accept_date", "reject_date", "collect_date", "reject_reason",
               "ship_date", "delivery_accept_date", "delivery_reject_date",
               "delivery_reject_reason", "collect_reason", "ship_reason", "order_reference", "status")
    inlines = [OrderItemInline]

    readonly_fields = ("order_reference", "order_price")

    def save_model(self, request, obj, form, change):
        # Calculate total price if OrderItems exist
        super().save_model(request, obj, form, change)
        total = obj.get_orders().aggregate(
            total_price=models.Sum('price')
        )['total_price'] or 0
        if obj.order_price != total:
            obj.order_price = total
            obj.save()