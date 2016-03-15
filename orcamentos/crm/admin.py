from django.contrib import admin
from .models import Person, Occupation, PhonePerson, Customer, Employee, PhoneEmployee
from .managers import CustomerManager
from .forms import PersonForm, EmployeeAdminForm, CustomerForm


class PhonePersonInline(admin.TabularInline):
    model = PhonePerson
    extra = 0


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [PhonePersonInline]
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    list_display = ('__str__', 'photo_img', 'email', 'customer_type', 'active')
    search_fields = ('first_name', 'last_name',)
    form = PersonForm

    def get_queryset(self, request):
        q = super(PersonAdmin, self).get_queryset(request)
        return q.filter(person_type='p')

    # def save_model(self, request, obj, form, change):
    #     obj.person_type = 'p'
    #     super(PersonAdmin, self).save_model(request, obj, form, change)

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
    form = CustomerForm

    def get_queryset(self, request):
        q = super(PersonAdmin, self).get_queryset(request)
        return q.filter(person_type='c')

    def save_model(self, request, obj, form, change):
        obj.person_type = 'c'
        super(CustomerAdmin, self).save_model(request, obj, form, change)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    inlines = [PhoneEmployeeInline]
    list_display = ('__str__', 'slug', 'date_joined',
                    'date_release', 'is_staff', 'active')
    search_fields = ('first_name', 'last_name',)
    date_hierarchy = 'date_joined'
    form = EmployeeAdminForm

admin.site.register(Occupation)
