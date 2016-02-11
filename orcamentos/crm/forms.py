from django import forms
from orcamentos.core.lists import GENDER
from orcamentos.crm.models import Customer, Person


class CustomerForm(forms.ModelForm):
    gender = forms.ChoiceField(
        label='Sexo', choices=GENDER, initial='M', widget=forms.RadioSelect)

    class Meta:
        model = Customer
        fields = '__all__'

    def clean_cpf(self):
        return self.cleaned_data['cpf'] or None

    def clean_cnpj(self):
        return self.cleaned_data['cnpj'] or None


class PersonForm(forms.ModelForm):
    gender = forms.ChoiceField(
        label='Sexo', choices=GENDER, initial='M', widget=forms.RadioSelect)

    class Meta:
        model = Person
        fields = '__all__'

    def clean_cpf(self):
        return self.cleaned_data['cpf'] or None
