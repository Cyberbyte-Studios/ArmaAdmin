import humanize

from django.core.management.base import BaseCommand

from armaadmin.downloads.helper import start


class Command(BaseCommand):
    help = 'Generates hashes for all files'

    def handle(self, *args, **options):
        job = start()
        if job.finished:
            self.stdout.write(self.style.SUCCESS(
                'Job {id}: {started} Finished: {finished} Elapsed: {elapsed}. Total: {total} Created: {created} Updated: {updated} Deleted: {deleted}. New file size {size}'.format(
                    id=job.id,
                    started=job.started,
                    finished=job.finished,
                    elapsed=job.finished-job.started,
                    total=job.total,
                    created=job.created,
                    updated=job.updated,
                    deleted=job.deleted,
                    size=humanize.naturalsize(job.size)
                )
            ))
        else:
            self.stdout.write(self.style.ERROR('Job {id} failed to finish'.format(id=job.id)))
