from django.db import models

# Represents a user with a name and photo
class UserProfile(models.Model):
	username = models.CharField(max_length=200, default="username")
	photo_url = models.CharField(max_length=200, default="photourl")

# Represents a bunk event, with a from user, to user, and time
class Bunk(models.Model):
	from_user = models.ForeignKey(UserProfile, related_name="sent")
	to_user = models.ForeignKey(UserProfile, related_name="received")
	time = models.DateTimeField('time')