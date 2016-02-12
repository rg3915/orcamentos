from django.contrib import admin
from orcamentos.crm.models import Person, Occupation, Customer, Employee, Seller
from orcamentos.crm.forms import CustomerForm


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'photo_img', 'email', 'customer_type', 'active')
    search_fields = ('first_name', 'last_name',)
    form = CustomerForm
    # fieldsets = (
    #     (None, {
    #         'fields': ('gender', 'treatment', 'first_name', 'last_name', 'slug',
    #                    'photo', 'birthday', 'company', 'department', 'email',
    #                    'cpf', 'rg', 'cnpj', 'ie', 'customer_type', 'address',
    #                    'complement', 'district', 'city', 'uf', 'cep', 'active')
    #     }),
    # )

    def photo_img(self, obj):
        return '<img width="32px" src="{}" />'.format(obj.photo)

    photo_img.allow_tags = True
    photo_img.short_description = 'foto'


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'slug', 'active')
    search_fields = ('first_name', 'last_name',)

admin.site.register(Person)
admin.site.register(Occupation)
admin.site.register(Seller)
