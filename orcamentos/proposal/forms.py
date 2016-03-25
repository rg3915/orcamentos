from django import forms
from .models import Contract, Entry, Proposal, Work
from orcamentos.utils.lists import PRIORITY, NORMAL


STATUS = (
    ('', ''),
    ('c', 'cancelado'),
    ('elab', 'em elaboração'),
    ('p', 'pendente'),
    ('co', 'concluido'),
    ('a', 'aprovado')
)


class EntryForm(forms.ModelForm):
    priority = forms.ChoiceField(
        label='Prioridade',
        choices=PRIORITY,
        initial=NORMAL,
        widget=forms.RadioSelect)

    class Meta:
        model = Entry
        exclude = ('status',)


class ContractForm(forms.ModelForm):

    class Meta:
        model = Contract
        fields = ('contractor', 'is_canceled')


class ProposalForm(forms.ModelForm):
    num_prop = forms.IntegerField(
        widget=forms.NumberInput(attrs={'readonly': 'readonly'}))
    num_prop_type = forms.IntegerField(
        widget=forms.NumberInput(attrs={'readonly': 'readonly'}))
    price = forms.DecimalField(localize=True)

    class Meta:
        model = Proposal
        fields = '__all__'


class WorkForm(forms.ModelForm):

    class Meta:
        model = Work
        fields = '__all__'


class StatusSearchForm(forms.Form):
    status = forms.ChoiceField(
        choices=STATUS, widget=forms.Select(attrs={'class': 'form-control'}))


class PrioritySearchForm(forms.Form):
    priority = forms.ChoiceField(
        choices=PRIORITY, widget=forms.Select(attrs={'class': 'form-control'}))
