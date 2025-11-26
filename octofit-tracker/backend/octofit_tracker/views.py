import os
from rest_framework.decorators import api_view
from rest_framework.response import Response

# ...existing code...

# API root with Codespace URL support
@api_view(['GET'])
def api_root_with_codespace(request, format=None):
	codespace_name = os.environ.get('CODESPACE_NAME')
	base_url = request.build_absolute_uri('/')
	if codespace_name:
		base_url = f'https://{codespace_name}-8000.app.github.dev/'
	return Response({
		'users': base_url + 'api/users/',
		'teams': base_url + 'api/teams/',
		'activities': base_url + 'api/activities/',
		'leaderboard': base_url + 'api/leaderboard/',
		'workouts': base_url + 'api/workouts/',
	})
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import User, Team, Activity, Workout, Leaderboard
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, WorkoutSerializer, LeaderboardSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
	queryset = Activity.objects.all()
	serializer_class = ActivitySerializer

class WorkoutViewSet(viewsets.ModelViewSet):
	queryset = Workout.objects.all()
	serializer_class = WorkoutSerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
	queryset = Leaderboard.objects.all()
	serializer_class = LeaderboardSerializer

@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'users': reverse('user-list', request=request, format=format),
		'teams': reverse('team-list', request=request, format=format),
		'activities': reverse('activity-list', request=request, format=format),
		'leaderboard': reverse('leaderboard-list', request=request, format=format),
		'workouts': reverse('workout-list', request=request, format=format),
	})
