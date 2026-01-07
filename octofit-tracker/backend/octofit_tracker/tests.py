from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        t = Team.objects.create(name='TestTeam')
        self.assertEqual(str(t), 'TestTeam')
    def test_user_create(self):
        team = Team.objects.create(name='T')
        u = User.objects.create(name='U', email='u@t.com', team=team)
        self.assertEqual(str(u), 'u@t.com')
    def test_workout_create(self):
        w = Workout.objects.create(name='W', description='desc', difficulty='Easy')
        self.assertEqual(str(w), 'W')
    def test_activity_create(self):
        team = Team.objects.create(name='T2')
        u = User.objects.create(name='U2', email='u2@t.com', team=team)
        a = Activity.objects.create(user=u, type='Run', duration=10, date='2024-01-01')
        self.assertEqual(a.type, 'Run')
    def test_leaderboard_create(self):
        team = Team.objects.create(name='T3')
        u = User.objects.create(name='U3', email='u3@t.com', team=team)
        l = Leaderboard.objects.create(user=u, score=42)
        self.assertEqual(l.score, 42)
