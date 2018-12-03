from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from orcamentos.crm.models import Employee


class Command(BaseCommand):
    help = ''' Cria um usuário admin. '''

    def handle(self, *args, **kwargs):
        '''
        Cria um Employee.
        Precisamos de Employee para fazer todas as transações no sistema.
        '''
        username = 'admin'
        first_name = 'Admin'
        last_name = 'Admin'
        email = 'admin@email.com'
        user = Employee.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            gender='I'
        )
        user.set_password('admin')
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        print('Usuário criado com sucesso.')
