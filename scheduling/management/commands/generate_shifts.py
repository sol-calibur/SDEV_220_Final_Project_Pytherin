from django.core.management.base import BaseCommand
from scheduling.models import Shift, Department
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Generate shifts based on predefined rules'

    def handle(self, *args, **kwargs):
        departments = Department.objects.all()
        start_date = datetime.now().date()
        end_date = start_date + timedelta(days=7)

        for department in departments:
            for single_date in (start_date + timedelta(n) for n in range((end_date - start_date).days)):
                Shift.objects.create(
                    shift_type='day',
                    date=single_date,
                    start_time='09:00:00',
                    end_time='17:00:00',
                    department=department
                )
                Shift.objects.create(
                    shift_type='night',
                    date=single_date,
                    start_time='17:00:00',
                    end_time='01:00:00',
                    department=department
                )

        self.stdout.write(self.style.SUCCESS('Successfully generated shifts'))