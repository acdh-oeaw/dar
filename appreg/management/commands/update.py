from django.core.management.base import BaseCommand, CommandError
from appreg.models import WebApp 


class Command(BaseCommand):
    help = 'Runs through all WebApps and updates them.'
    
    def handle(self, *args, **options):
        for w in WebApp.objects.all():
            self.stdout.write("Updating {}".format(w.title))
            w.save()

