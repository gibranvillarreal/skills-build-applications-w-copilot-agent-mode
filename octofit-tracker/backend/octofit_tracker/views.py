from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'users': reverse('user-list', request=request, format=format),
		'teams': reverse('team-list', request=request, format=format),
		'activities': reverse('activity-list', request=request, format=format),
		'leaderboard': reverse('leaderboard-list', request=request, format=format),
		'workouts': reverse('workout-list', request=request, format=format),
	})
