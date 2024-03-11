from django.shortcuts import render

# TODO: Add more projects

def portfolio(request):
    """ The view responsible for the portfolio page. """
    
    return render(request, 'in_progress.html')