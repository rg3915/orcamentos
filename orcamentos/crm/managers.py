from django.db import models


class CustomerManager(models.Manager):

    def get_queryset(self):
        return super(CustomerManager, self).get_queryset().filter(person_type='c')

# Person (contato)
# Employee
# Seller
