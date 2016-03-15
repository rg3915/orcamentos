from django import forms
# from orcamentos.crm.validate import validate_documents
from orcamentos.utils.lists import GENDER, CUSTOMER_TYPE, PERSON_TYPE
from orcamentos.crm.models import Person, Employee, Customer


class CustomerForm(forms.ModelForm):
    gender = forms.ChoiceField(
        label='Sexo', choices=GENDER, initial='M', widget=forms.RadioSelect)
    person_type = forms.ChoiceField(
        label='Cliente ou contato', choices=PERSON_TYPE, initial='c',
        widget=forms.RadioSelect)
    customer_type = forms.ChoiceField(
        label='Tipo', choices=CUSTOMER_TYPE, initial='p',
        widget=forms.RadioSelect)

    class Meta:
        model = Customer
        fields = ['gender', 'treatment', 'first_name', 'last_name', 'email',
                  'slug', 'photo', 'birthday', 'occupation', 'company',
                  'department', 'cpf', 'rg', 'cnpj', 'ie',
                  'address', 'complement', 'district', 'city', 'uf', 'cep',
                  'active', 'blocked', 'person_type', 'customer_type']

    def clean_cpf(self):
        return self.cleaned_data['cpf'] or None

    def clean_cnpj(self):
        return self.cleaned_data['cnpj'] or None


class PersonForm(forms.ModelForm):
    gender = forms.ChoiceField(
        label='Sexo', choices=GENDER, initial='M', widget=forms.RadioSelect)
    person_type = forms.ChoiceField(
        label='Cliente ou contato', choices=PERSON_TYPE, initial='p',
        widget=forms.RadioSelect)

    class Meta:
        model = Person
        fields = ['gender', 'treatment', 'first_name', 'last_name', 'slug',
                  'photo', 'birthday', 'company', 'department', 'email',
                  'cpf', 'rg', 'cnpj', 'ie', 'person_type', 'customer_type',
                  'address', 'complement', 'district', 'city', 'uf', 'cep',
                  'active', 'blocked']

    def clean_cpf(self):
        return self.cleaned_data['cpf'] or None

    def clean_cnpj(self):
        return self.cleaned_data['cnpj'] or None


class EmployeeForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    class Meta:
        model = Employee
        fields = ['username', 'email', 'password']

    def clean_cpf(self):
        return self.cleaned_data['cpf'] or None


class EmployeeAdminForm(forms.ModelForm):
    gender = forms.ChoiceField(
        label='Sexo', choices=GENDER, initial='M', widget=forms.RadioSelect)

    class Meta:
        model = Employee
        fields = ['username', 'slug', 'gender', 'first_name', 'last_name',
                  'is_staff', 'email', 'photo', 'birthday', 'department',
                  'cpf', 'rg', 'occupation', 'address', 'complement', 'district',
                  'city', 'uf', 'cep', 'date_joined', 'date_release',
                  'active', 'blocked']

    def clean_cpf(self):
        return self.cleaned_data['cpf'] or None
