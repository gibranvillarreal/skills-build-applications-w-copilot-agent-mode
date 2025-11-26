from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data using raw MongoDB deletion to avoid Djongo PK issues
        for model in [Leaderboard, Activity, Workout, User, Team]:
            try:
                model.objects.collection.delete_many({})
            except Exception:
                pass

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = [
            User.objects.create(email='tony@stark.com', username='IronMan', team=marvel),
            User.objects.create(email='steve@rogers.com', username='CaptainAmerica', team=marvel),
            User.objects.create(email='bruce@wayne.com', username='Batman', team=dc),
            User.objects.create(email='clark@kent.com', username='Superman', team=dc),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Yoga', duration=20, date=timezone.now().date())

        # Create workouts
        workout1 = Workout.objects.create(name='Full Body Blast', description='A full body workout')
        workout2 = Workout.objects.create(name='Cardio Burn', description='High intensity cardio')
        workout1.suggested_for.set([users[0], users[2]])
        workout2.suggested_for.set([users[1], users[3]])

        # Create leaderboard
        Leaderboard.objects.create(user=users[0], score=100)
        Leaderboard.objects.create(user=users[1], score=90)
        Leaderboard.objects.create(user=users[2], score=80)
        Leaderboard.objects.create(user=users[3], score=70)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
