from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = []
        users.append(User.objects.create(email='tony@stark.com', username='Iron Man', team=marvel, is_superhero=True))
        users.append(User.objects.create(email='steve@rogers.com', username='Captain America', team=marvel, is_superhero=True))
        users.append(User.objects.create(email='bruce@wayne.com', username='Batman', team=dc, is_superhero=True))
        users.append(User.objects.create(email='clark@kent.com', username='Superman', team=dc, is_superhero=True))

        # Create activities
        Activity.objects.create(user=users[0], activity_type='Running', duration_minutes=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], activity_type='Cycling', duration_minutes=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], activity_type='Swimming', duration_minutes=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], activity_type='Yoga', duration_minutes=40, date=timezone.now().date())

        # Create workouts
        workout1 = Workout.objects.create(name='Super Strength', description='Strength training for superheroes')
        workout2 = Workout.objects.create(name='Flight Training', description='Aerobic workout for flying heroes')
        workout1.suggested_for.set([users[0], users[1], users[2]])
        workout2.suggested_for.set([users[3]])

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
