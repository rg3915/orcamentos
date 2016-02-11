from django import forms
from orcamentos.proposal.models import Contract, Entry, Proposal, Work
from orcamentos.core.lists import PRIORITY

STATUS = (
    ('', ''),
    ('c', 'cancelado'),
    ('elab', 'em elaboração'),
    ('p', 'pendente'),
    ('co', 'concluido'),
    ('a', 'aprovado')
)


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = '__all__'


class ContractForm(forms.ModelForm):

    class Meta:
        model = Contract
        fields = ('contractor', 'is_canceled')


class ProposalForm(forms.ModelForm):
    num_prop = forms.IntegerField(
        widget=forms.NumberInput(attrs={'readonly': 'readonly'}))
    num_prop_type = forms.IntegerField(
        widget=forms.NumberInput(attrs={'readonly': 'readonly'}))

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
