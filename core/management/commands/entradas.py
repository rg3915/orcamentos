from django.core.management.base import BaseCommand
from optparse import make_option
from core.models import Entry


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--urgentes', default=False, action="store_true"),
    )

    def handle(self, urgentes=False, *args, **kwargs):
        entrys = Entry.objects.filter(is_entry=False).order_by('created')
        if urgentes:
            entrys = entrys.filter(priority='u')
        i = 1
        for e in entrys:
            print(" %d \t %s \t %s" %
                  (i, e.created, e.work))
            i += 1
