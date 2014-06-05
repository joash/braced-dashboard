from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

def home(request):

	return render(request, 'home.html', {'home_tab': 'active'} )

def contact(request):

  return render(request, 'contact.html')

def faq(request):

	return render(request, 'faq.html')

def documentation(request):

	return render(request, 'documentation.html')
