from django import forms
from orcamentos.proposal.models import Proposal

STATUS = (
    ('', ''),
    ('c', 'cancelado'),
    ('elab', 'em elaboração'),
    ('p', 'pendente'),
    ('co', 'concluido'),
    ('a', 'aprovado')
)


class ProposalForm(forms.ModelForm):
    num_prop = forms.IntegerField(
        widget=forms.NumberInput(attrs={'readonly': 'readonly'}))
    num_type_prop = forms.IntegerField(
        widget=forms.NumberInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Proposal
        fields = '__all__'


class StatusSearchForm(forms.Form):
    status = forms.ChoiceField(
        choices=STATUS, widget=forms.Select(attrs={'class': 'form-control'}))


class PrioritySearchForm(forms.Form):
    priority = forms.ChoiceField(
        choices=PRIORITY, widget=forms.Select(attrs={'class': 'form-control'}))
