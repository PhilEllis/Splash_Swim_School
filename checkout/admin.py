from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    fields = ('course', 'quantity', 'lineitem_total',)
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'order_total', 'grand_total', 'get_course_names', 'original_bag',
                       'stripe_pid')

    def get_course_names(self, obj):
        return ", ".join([line_item.course.name for line_item in obj.lineitems.all()])
    get_course_names.short_description = 'Courses'

    fields = ('order_number', 'user_profile', 'date', 'full_name', 'email', 
              'phone_number', 'country', 'postcode', 'town_or_city', 
              'street_address1', 'street_address2', 'county', 
              'order_total', 'grand_total', 'get_course_names', 
              'original_bag', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name', 
                    'order_total', 'grand_total', 'get_course_names')

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)