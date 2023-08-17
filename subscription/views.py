from django.shortcuts import render

# Create your views here.
def subscriptionView(request):
    return render(request, 'subscriptions/subscriptions.html', {})