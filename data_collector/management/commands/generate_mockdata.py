from django.core.management.base import BaseCommand
from faker import Faker
import random
from data_collector.models import AdData
from django.utils import timezone
import datetime

class Command(BaseCommand):
    help = 'Generates mock ad data'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Indicates the number of mock ad data to be created')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        fake = Faker()

        for _ in range(count):
            AdData.objects.create(
                source=fake.company(),
                impressions=random.randint(100, 10000),
                clicks=random.randint(10, 1000),
                cost=fake.pydecimal(left_digits=4, right_digits=2, positive=True),
                date=timezone.now() - datetime.timedelta(days=random.randint(0, 365))
            )
        
        self.stdout.write(self.style.SUCCESS(f'Successfully generated {count} mock ad data entries'))