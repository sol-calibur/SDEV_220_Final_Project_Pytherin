from django.core.management.base import BaseCommand
from scheduling.models import Shift

class Command(BaseCommand):
    help = 'Clear all assigned shifts'

    def handle(self, *args, **kwargs):
        Shift.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully cleared all assigned shifts'))