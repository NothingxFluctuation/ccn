from django.http import HttpResponse
from .models import Message
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.

@login_required
def send_message(request):
    from_user = request.user
    to_user = User.objects.all().exclude(username=from_user.username)[0]
    Message.objects.create(from_user=from_user,
                            to_user=to_user,
                            text=request.GET['text'])
    return HttpResponse('OK')
    

@login_required
def receive_message(request):
    messages = Message.objects.filter(to_user=request.user,is_read=False)
    for msg in messages:
        msg.is_read=True
        msg.save()
    return HttpResponse(messages)
    

def user_login(request):
    name = request.GET['username']
    password = request.GET['password']
    user = authenticate(username=name, password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            return HttpResponse('authenticated')
        else:
            return HttpResponse('account disabled')
    else:
        return HttpResponse('not a user')
    
