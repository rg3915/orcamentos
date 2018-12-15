import string
import names
import pandas as pd
import timeit
from datetime import datetime
from random import choice, randint, random, sample
from django.contrib.auth.models import User, Group, Permission
from django.utils import timezone
from django.utils.text import slugify
from orcamentos.crm.models import Occupation, Employee, Customer, Contact
from orcamentos.proposal.models import Work, Proposal, Contract, NumLastProposal


class Utils:
    ''' Métodos genéricos. '''
    @staticmethod
    def gen_string(max_length):
        '''
        Gera uma string randomica.
        '''
        pass

    @staticmethod
    def gen_date(min_year=2000, max_year=datetime.now().year):
        '''
        Gera um date no formato yyyy-mm-dd.
        '''
        pass

    def gen_digits(max_length):
        '''
        Gera dígitos numéricos
        '''
        pass

    def gen_name():
        '''
        Gera nomes
        '''
        pass

    def gen_text():
        '''
        Gera texto do tipo lorem
        '''
        pass


class UserClass:
    '''
    Métodos pra criar User.
    '''
    @staticmethod
    def create_mysuperuser():
        '''
        Cria admin
        '''
        User.objects.create_user(
            username='admin',
            first_name='Admin',
            last_name='Admin',
            email='admin@email.com',
        )

    @staticmethod
    def update_pass_of_users():
        '''
        Atualiza a senha de todos os usuários
        '''
        users = User.objects.all()
        for user in users:
            user.is_staff = False
            user.is_superuser = False
            user.set_password('d')
            user.save()


class CrmClass:

    @staticmethod
    def create_occupation():
        '''
        Cria Cargos
        '''
        pass

    @staticmethod
    def create_employee():
        '''
        Cria Funcionários
        '''
        pass

    @staticmethod
    def create_customer():
        '''
        Cria Clientes
        '''
        pass

    @staticmethod
    def create_work():
        '''
        Cria Obras
        '''
        pass


tic = timeit.default_timer()

CrmClass.create_occupation()
CrmClass.create_employee()
CrmClass.create_seller()
CrmClass.create_customer()
CrmClass.create_work()

UserClass.create_mysuperuser()
UserClass.update_pass_of_users()

toc = timeit.default_timer()
print('time', toc - tic)
