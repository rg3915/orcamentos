from django.contrib import admin
from orcamentos.crm.models import Person, Customer, Employee, Seller


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'photo_img', 'email', 'customer_type', 'active')
    search_fields = ('first_name', 'last_name',)

    def photo_img(self, obj):
        return '<img width="32px" src="{}" />'.format(obj.photo)

    photo_img.allow_tags = True
    photo_img.short_description = 'foto'

admin.site.register(Person)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Employee)
admin.site.register(Seller)
