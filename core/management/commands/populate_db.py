from django.core.management.base import BaseCommand
from core.models import TestData


class Command(BaseCommand):
    help = "My shiny new management command."

    def add_arguments(self, parser):
        parser.add_argument('database', nargs='+')

    def handle(self, *args, **options):
        database = str(options['database'][0])
        print("delete previous records....")
        TestData.objects.using(database).all().delete()
        # making the dummy records
        for r in range(0,10):
            TestData.objects.using(database).create(desc='test description of model number {} in {}'.format(str(r),database))
            print('creating model {} in {}'.format(str(r),database))
