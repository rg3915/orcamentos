from daterange_filter.filter import DateRangeFilter
from django.contrib import admin
from .models import Entry, Proposal, Contract, Work, NumLastProposal


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'created', 'is_entry')
    search_fields = ('work__name_work',)


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'work', 'cliente', 'category', 'employee',
        'status', 'created', 'price')
    date_hierarchy = 'created'
    search_fields = (
        'work__name_work', 'work__customer__first_name',
        'employee__first_name')
    list_filter = (
        'status', 'category',  # 'seller',
        ('created', DateRangeFilter),
    )


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'contractor', 'created', 'is_canceled')
    date_hierarchy = 'created'
    search_fields = (
        'proposal__work__name_work', 'proposal__work__customer__first_name',
        'proposal__employee__first_name')
    list_filter = ('is_canceled', )  # 'proposal__seller')


admin.site.register(Work)
admin.site.register(NumLastProposal)
