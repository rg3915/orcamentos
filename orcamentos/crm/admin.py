from django.contrib import admin
from .models import Person, Occupation, PhonePerson, Customer, Employee, \
    PhoneEmployee, Seller
from .managers import CustomerManager, SellerManager
from .forms import PersonForm, EmployeeAdminForm, CustomerForm


class PhonePersonInline(admin.TabularInline):
    model = PhonePerson
    extra = 0


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [PhonePersonInline]
    objects = CustomerManager()
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    list_display = ('__str__', 'photo_img', 'email', 'active')
    search_fields = ('first_name', 'last_name',)
    form = PersonForm

    def photo_img(self, obj):
        return '<img width="32px" src="{}" />'.format(obj.photo)

    photo_img.allow_tags = True
    photo_img.short_description = 'foto'


class PhoneEmployeeInline(admin.TabularInline):
    model = PhoneEmployee
    extra = 0


@admin.register(Customer)
class CustomerAdmin(PersonAdmin):
    objects = CustomerManager()
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    list_display = ('__str__', 'photo_img', 'email', 'customer_type', 'active')
    form = CustomerForm

    def save_model(self, request, obj, form, change):
        obj.person_type = 'c'
        super(CustomerAdmin, self).save_model(request, obj, form, change)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    inlines = [PhoneEmployeeInline]
    list_display = ('__str__', 'slug', 'occupation', 'date_joined',
                    'date_release', 'is_staff', 'active')
    search_fields = ('first_name', 'last_name',)
    date_hierarchy = 'date_joined'
    form = EmployeeAdminForm


@admin.register(Seller)
class SellerAdmin(PersonAdmin):
    objects = SellerManager()
    inlines = [PhoneEmployeeInline]
    list_display = ('__str__', 'email', 'occupation',
                    'internal', 'commissioned', 'active')
    search_fields = ('first_name', 'last_name',)
    date_hierarchy = 'date_joined'
    form = EmployeeAdminForm

    def save_model(self, request, obj, form, change):
        obj.occupation = 'Vendedor'
        super(SellerAdmin, self).save_model(request, obj, form, change)

admin.site.register(Occupation)
