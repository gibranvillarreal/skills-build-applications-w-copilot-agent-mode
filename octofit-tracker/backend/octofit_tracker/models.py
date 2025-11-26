from djongo import models
from bson import ObjectId

class Team(models.Model):
	id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
	name = models.CharField(max_length=100, unique=True)
	description = models.TextField(blank=True)
	class Meta:
		verbose_name = 'Team'
		verbose_name_plural = 'Teams'
	def __str__(self):
		return self.name

class User(models.Model):
	id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
	email = models.EmailField(unique=True)
	username = models.CharField(max_length=100)
	team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='members')
	is_active = models.BooleanField(default=True)
	class Meta:
		verbose_name = 'User'
		verbose_name_plural = 'Users'
	def __str__(self):
		return self.username

class Activity(models.Model):
	id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
	type = models.CharField(max_length=100)
	duration = models.PositiveIntegerField(help_text='Duration in minutes')
	date = models.DateField()
	class Meta:
		verbose_name = 'Activity'
		verbose_name_plural = 'Activities'
	def __str__(self):
		return f"{self.user.username} - {self.type} on {self.date}"

class Workout(models.Model):
	id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	suggested_for = models.ManyToManyField(User, blank=True, related_name='suggested_workouts')
	class Meta:
		verbose_name = 'Workout'
		verbose_name_plural = 'Workouts'
	def __str__(self):
		return self.name

class Leaderboard(models.Model):
	id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries')
	score = models.IntegerField(default=0)
	class Meta:
		verbose_name = 'Leaderboard'
		verbose_name_plural = 'Leaderboard'
	def __str__(self):
		return f"{self.user.username} - {self.score}"
