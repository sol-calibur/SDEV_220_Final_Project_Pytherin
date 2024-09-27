from django.core.management.base import BaseCommand
from scheduling.scheduler import assign_shifts

# Custom management command to assign shifts to employees
class Command(BaseCommand):
    # Help text for the command
    help = 'Assign shifts to employees'

    # Handle method to execute the command
    def handle(self, *args, **kwargs):
        # Call the assign_shifts function to assign shifts
        assign_shifts()
        # Output a success message to the console
        self.stdout.write(self.style.SUCCESS('Successfully assigned shifts'))