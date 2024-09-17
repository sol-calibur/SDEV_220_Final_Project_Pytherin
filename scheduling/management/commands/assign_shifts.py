from django.core.management.base import BaseCommand
from scheduling.scheduler import assign_shifts

class Command(BaseCommand):
    help = 'Assign shifts to employees'

    def handle(self, *args, **kwargs):
        assign_shifts()
        self.stdout.write(self.style.SUCCESS('Successfully assigned shifts'))