from django import forms
from orcamentos.utils.lists import GENDER, CUSTOMER_TYPE, PERSON_TYPE
from orcamentos.crm.models import Person, Employee, Customer


class SelectDateWidget(forms.SelectDateWidget):

    def create_select(self, *args, **kwargs):
        old_state = self.is_required
        self.is_required = False
        result = super().create_select(*args, **kwargs)
        self.is_required = old_state
        return result


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
        fields = (
            # 'active',
            'address',
            # 'blocked',
            # 'birthday',
            'cep',
            'city',
            'cnpj',
            'company',
            'complement',
            'cpf',
            'customer_type',
            'department',
            'district',
            'email',
            'first_name',
            'gender',
            'ie',
            'last_name',
            # 'occupation',
            'person_type',
            'photo',
            'rg',
            'slug',
            'treatment',
            'uf',
        )
        # widgets = {
        #     'birthday': SelectDateWidget
        # }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     current_year = now().year
    #     self.fields['birthday'].widget.years = [
    #         current_year - x for x in range(50)][::-1]

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
        fields = (
            'gender', 'treatment', 'first_name', 'last_name', 'slug',
            'photo', 'occupation', 'company', 'department',
            'email', 'cpf', 'rg', 'cnpj', 'ie', 'person_type',
            'customer_type', 'address', 'complement', 'district',
            'city', 'uf', 'cep', 'active', 'blocked'
        )

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

    def clean_cnpj(self):
        return self.cleaned_data['cnpj'] or None


class EmployeeAdminForm(forms.ModelForm):
    gender = forms.ChoiceField(
        label='Sexo', choices=GENDER, initial='M', widget=forms.RadioSelect)

    class Meta:
        model = Employee
        fields = (
            'username', 'slug', 'gender', 'first_name', 'last_name',
            'is_staff', 'email', 'photo', 'department',
            'cpf', 'rg', 'occupation', 'address', 'complement',
            'district', 'city', 'uf', 'cep', 'date_joined',
            'date_release', 'active', 'blocked'
        )

    def clean_cpf(self):
        return self.cleaned_data['cpf'] or None

    def clean_cnpj(self):
        return self.cleaned_data['cnpj'] or None
