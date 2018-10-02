from django.core.management.base import BaseCommand

from izi_accounts import facade


class Command(BaseCommand):
    help = 'Close all inactive card-accounts'

    def handle(self, *args, **options):
        facade.close_expired_accounts()
