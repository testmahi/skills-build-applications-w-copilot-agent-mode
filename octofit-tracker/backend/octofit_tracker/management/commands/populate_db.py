from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', total_score=0)
        dc = Team.objects.create(name='DC', total_score=0)

        # Create users
        ironman = User.objects.create(username='ironman', email='ironman@marvel.com', team=marvel, leaderboard_score=100)
        captain = User.objects.create(username='captainamerica', email='cap@marvel.com', team=marvel, leaderboard_score=90)
        batman = User.objects.create(username='batman', email='batman@dc.com', team=dc, leaderboard_score=95)
        superman = User.objects.create(username='superman', email='superman@dc.com', team=dc, leaderboard_score=98)

        # Create activities
        Activity.objects.create(user=ironman, type='run', duration=30, calories=300, date='2026-02-12')
        Activity.objects.create(user=batman, type='cycle', duration=45, calories=400, date='2026-02-12')

        # Create workouts
        Workout.objects.create(user=ironman, description='Pushups', date='2026-02-12')
        Workout.objects.create(user=superman, description='Squats', date='2026-02-12')

        # Create leaderboard
        Leaderboard.objects.create(user=ironman, score=100)
        Leaderboard.objects.create(user=batman, score=95)
        Leaderboard.objects.create(user=superman, score=98)
        Leaderboard.objects.create(user=captain, score=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
