from django.shortcuts import render

def portfolio(request):
    """ The view responsible for the portfolio page. """
    
    return render(request, 'in_progress.html')