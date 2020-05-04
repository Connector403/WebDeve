from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Import Product in BookTime'

    def handle(self, *args, **options):
        self.stdout.write("Importing Products")
