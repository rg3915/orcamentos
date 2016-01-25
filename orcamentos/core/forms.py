from django import forms
from .models import Person, Customer, Proposal
from .lists import gender_list, uf_list, priority_list

status_list = (
    ('', ''),
    ('c', 'cancelado'),
    ('elab', 'em elaboração'),
    ('p', 'pendente'),
    ('co', 'concluido'),
    ('a', 'aprovado')
)


class PersonForm(forms.ModelForm):
    gender = forms.ChoiceField(
        label='Sexo', choices=gender_list, initial='M', widget=forms.RadioSelect)

    class Meta:
        model = Person
        fields = '__all__'

    def clean_cpf(self):
        return self.cleaned_data['cpf'] or None


class CustomerForm(forms.ModelForm):
    gender = forms.ChoiceField(
        label='Sexo', choices=gender_list, initial='M', widget=forms.RadioSelect)

    class Meta:
        model = Customer
        fields = '__all__'

    def clean_cpf(self):
        return self.cleaned_data['cpf'] or None

    def clean_cnpj(self):
        return self.cleaned_data['cnpj'] or None


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
        choices=status_list, widget=forms.Select(attrs={'class': 'form-control'}))


class PrioritySearchForm(forms.Form):
    priority = forms.ChoiceField(
        choices=priority_list, widget=forms.Select(attrs={'class': 'form-control'}))
