from django.core.management.base import BaseCommand

from izi_accounts.setup import create_default_accounts


class Command(BaseCommand):
    help = "Initialize izi accounts default structure"

    def handle(self, *args, **options):
        create_default_accounts()
