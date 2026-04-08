from django.core.management.base import BaseCommand
from django.core.management import call_command
from core.models import Profile


class Command(BaseCommand):
    help = 'Load initial portfolio data if not already present'

    def handle(self, *args, **kwargs):
        if Profile.objects.exists():
            self.stdout.write(self.style.WARNING('Data already exists — skipping seed.'))
            return

        self.stdout.write('Loading portfolio fixture data...')
        call_command('loaddata', 'core/fixtures/initial_data.json')
        self.stdout.write(self.style.SUCCESS('Portfolio data loaded successfully!'))
