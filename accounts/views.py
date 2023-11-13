# accounts/views.py
# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Friend_Request
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import TrackerUserCreationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Friend_Request
from .models import TrackerUser
from .forms import FriendRequestForm
class SignUpView(generic.CreateView):
    form_class = TrackerUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

@login_required
def send_friend_request(request, userID):
    from_user = request.user
    to_user = TrackerUser.objects.get(id=userID)
    friend_request, created = Friend_Request.objects.get_or_create(
        from_user=from_user, to_user=to_user)
    if created:
        return HttpResponse('friend request sent')
    else:
        return HttpResponse('friend request was already sent')
    
@login_required
def accept_friend_request(request, requestID):
    friend_request = Friend_Request.objects.get(id=requestID)
    if friend_request.to_user == request.user:
        friend_request.to_user.friends.add(friend_request.from_user)
        friend_request.from_user.friends.add(friend_request.to_user)
        friend_request.delete()
        return HttpResponse('friend request accepted')
    else:
        return HttpResponse('friend request not accepted')

@login_required
def send_friend_request(request, user_id):
    to_user = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        form = FriendRequestForm(request.POST)
        if form.is_valid():
            friend_request = form.save(commit=False)
            friend_request.from_user = request.user
            friend_request.to_user = to_user
            friend_request.save()
            return redirect('friend_requests')  # Redirect to friend requests page or wherever you want
    else:
        form = FriendRequestForm()

    return render(request, 'send_friend_request.html', {'form': form, 'to_user': to_user})