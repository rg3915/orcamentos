# from django.db.models import Count
from .models import *


class PersonManager(models.Manager):

    def get_person_detail_url():
        return u'/person/%i' % id
