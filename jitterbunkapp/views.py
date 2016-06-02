from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Bunk, UserProfile
import sys

# Main bunk feed
def index(request):
	bunk_list = Bunk.objects.order_by('-time')
	context = {'bunk_list': bunk_list}
	return render(request, 'jitterbunkapp/index.html', context)

# Specific user's personalized bunk feed
def user(request, user_id):
	user_profile = get_object_or_404(UserProfile, pk=user_id)

	# user bunked someone, add that new bunk to database
	if request.method =='POST':
		to_user_id = request.POST.get('to_user')
		to_user = get_object_or_404(UserProfile, pk=to_user_id)
		new_bunk = Bunk(from_user=user_profile, to_user=to_user, time=timezone.now())
		new_bunk.save()

	bunk_list = Bunk.objects.order_by('-time')
	context = {'bunk_list': bunk_list, 'user': user_profile}
	return render(request, 'jitterbunkapp/user.html', context)

# Form for user to bunk someone else
def bunk(request, user_id):
	user_list = UserProfile.objects.all
	user_profile = get_object_or_404(UserProfile, pk=user_id)
	context = {'user': user_profile, 'user_list': user_list}
	return render(request, 'jitterbunkapp/bunk.html', context)