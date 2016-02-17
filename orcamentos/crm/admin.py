from django.contrib import admin
from orcamentos.crm.models import Person, Occupation, Customer, Phone, Employee, Seller
from orcamentos.crm.forms import CustomerForm, EmployeeAdminForm


class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 1


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [PhoneInline]


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
    list_display = ('__str__', 'slug', 'date_joined',
                    'date_release', 'is_staff', 'active')
    search_fields = ('first_name', 'last_name',)
    date_hierarchy = 'date_joined'
    form = EmployeeAdminForm

admin.site.register(Occupation)
admin.site.register(Seller)
