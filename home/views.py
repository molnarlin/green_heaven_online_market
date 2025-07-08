from django.shortcuts import render
from django.shortcuts import redirect
from .models import Subscriber
from django.contrib import messages
# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            Subscriber.objects.get_or_create(email=email)
            messages.success(
                request,
                'You’ve successfully subscribed to the newsletter!'
            )
        return redirect('subscription_success')


def subscription_success(request):
    return render(request, 'home/subscription_success.html')
