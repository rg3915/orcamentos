from django.contrib import admin
from .models import Person, Occupation, PhonePerson, Employee, PhoneEmployee
from .forms import PersonForm, EmployeeAdminForm


class PhonePersonInline(admin.TabularInline):
    model = PhonePerson
    extra = 0


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [PhonePersonInline]
    # @admin.register(Customer)
    # class CustomerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'photo_img', 'email', 'customer_type', 'active')
    search_fields = ('first_name', 'last_name',)
    form = PersonForm

    def photo_img(self, obj):
        return '<img width="32px" src="{}" />'.format(obj.photo)

    photo_img.allow_tags = True
    photo_img.short_description = 'foto'


class PhoneEmployeeInline(admin.TabularInline):
    model = PhoneEmployee
    extra = 0


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    inlines = [PhoneEmployeeInline]
    list_display = ('__str__', 'slug', 'date_joined',
                    'date_release', 'is_staff', 'active')
    search_fields = ('first_name', 'last_name',)
    date_hierarchy = 'date_joined'
    form = EmployeeAdminForm

admin.site.register(Occupation)
