from django.contrib import admin
from .models import Occupation, Person, Customer
from .models import Employee, Seller, Entry
from .models import Category, Work, Proposal, Contract, NumLastProposal


class EntryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created', 'is_entry')


class ProposalAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'work', 'cliente', 'category', 'employee', 'seller', 'status',
        'created', 'price')
    date_hierarchy = 'created'
    search_fields = (
        'work__name_work', 'work__customer__first_name', 'employee__user__first_name')
    list_filter = ('status', 'category', 'seller')


class ContractAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'contractor', 'created', 'is_canceled')
    date_hierarchy = 'created'
    search_fields = (
        'proposal__work__name_work', 'proposal__work__customer__first_name',
        'proposal__employee__user__first_name')
    list_filter = ('is_canceled', 'proposal__seller')


admin.site.register(Entry, EntryAdmin)
admin.site.register(Proposal, ProposalAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Customer)
admin.site.register(Work)
admin.site.register(Person)
admin.site.register(Employee)
admin.site.register(Seller)
admin.site.register(Occupation)
admin.site.register(Category)
admin.site.register(NumLastProposal)
