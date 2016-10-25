from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from crm.models import Customer, SalesPerson, Todo, Deal, Product, DealProducts, DealStatus

# Customize admin panel
admin.AdminSite.index_title = u'simpleCRM, simple administration.'
admin.AdminSite.site_title  = u'simpleCRM administration.'
admin.AdminSite.site_header = u'simpleCRM administration.'


class DealInline(admin.TabularInline):
    model = Deal
    extra = 1

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'company', 'position', 'phone_number', 'sales_person')
    search_fields = ['first_name']

class TodoAdmin(admin.ModelAdmin):
    list_display  = ('action', 'action_description', 'data_time', 'sales_person')
    list_filter   = ['data_time']

# Define an inline admin descriptor for SalePerson model which acts a bit like a singleton
class SalePersonInline(admin.StackedInline):
    model = SalesPerson
    can_delete = False
    verbose_name_plural = 'SalesPersons'

class SalesPersonAdmin(admin.ModelAdmin):
    model = SalesPerson

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (SalePersonInline, )

class DealAdmin(admin.ModelAdmin):
    list_display    = ('description', 'sales_person')
    list_filter     = ['sales_person']

class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'description', 'price')

class DealProductsAdmin(admin.ModelAdmin):
    list_display = ('product', 'qty')

class DealStatusAdmin(admin.ModelAdmin):
    list_display = ('status',)

admin.site.register(Customer, ContactAdmin)
admin.site.register(DealProducts, DealProductsAdmin)
admin.site.register(DealStatus, DealStatusAdmin)
admin.site.register(Todo, TodoAdmin)
admin.site.register(Deal, DealAdmin )
admin.site.register(Product, ProductAdmin )
admin.site.register(SalesPerson, SalesPersonAdmin )
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)





