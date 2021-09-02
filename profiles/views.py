from django.shortcuts import render


def profile(request):
    """Display's the user's profiles """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
