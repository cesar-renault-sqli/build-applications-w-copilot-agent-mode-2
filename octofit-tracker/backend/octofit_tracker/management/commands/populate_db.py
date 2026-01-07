from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)

        # Workouts
        w1 = Workout.objects.create(name='Super Strength', description='Heavy lifting', difficulty='Hard')
        w2 = Workout.objects.create(name='Flight Training', description='Aerial maneuvers', difficulty='Medium')

        # Activities
        Activity.objects.create(user=tony, type='Run', duration=30, date=timezone.now())
        Activity.objects.create(user=steve, type='Swim', duration=45, date=timezone.now())
        Activity.objects.create(user=bruce, type='Cycle', duration=60, date=timezone.now())
        Activity.objects.create(user=clark, type='Fly', duration=120, date=timezone.now())

        # Leaderboard
        Leaderboard.objects.create(user=tony, score=100)
        Leaderboard.objects.create(user=steve, score=90)
        Leaderboard.objects.create(user=bruce, score=95)
        Leaderboard.objects.create(user=clark, score=110)

        # Créer un index unique sur le champ email de la collection users
        from django.conf import settings
        from pymongo import MongoClient
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
        db = client[settings.DATABASES['default']['NAME']]
        db.users.create_index([('email', 1)], unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db has been populated with test data.'))
