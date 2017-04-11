from django.core.management.base import BaseCommand, CommandError

from shortener.models import ShortenedURL

class Command(BaseCommand):
    help = 'Refreshes all shortcodes'

    def handle(self, *args, **options):
        return ShortenedURL.objects.refresh_shortcodes()        