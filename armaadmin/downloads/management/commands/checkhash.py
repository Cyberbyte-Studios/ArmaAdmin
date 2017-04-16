import time
import humanize

from django.core.management.base import BaseCommand
from django.db.models import Sum

from armaadmin.downloads.helper import do_magic
from armaadmin.downloads.models import File


class Command(BaseCommand):
    help = 'Generates hashes for all files'

    def handle(self, *args, **options):
        start = time.time()
        do_magic()
        end = time.time()
        total_size = File.objects.aggregate(Sum('size'))['size__sum'] or 0
        self.stdout.write(self.style.SUCCESS(
            '{files} files added in {time}. Total file size {size}'.format(
                size=humanize.naturalsize(total_size),
                files=File.objects.all().count(),
                time=end - start
            )
        ))