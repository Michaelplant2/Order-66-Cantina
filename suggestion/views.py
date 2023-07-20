from django.shortcuts import redirect
from django.contrib import messages
from .models import Suggestion

def suggestion(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']

        suggestion = Suggestion(name=name, description=description)

        suggestion.save()

        messages.success(request, 'Your suggestion has been submitted, Thank you!')
        return redirect('/accounts/dashboard')