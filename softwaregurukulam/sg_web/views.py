from django.http import HttpResponse
from sg_web.models import Category, Course 
from django.shortcuts import render, render_to_response
from django.template.context_processors import request, csrf
from sg_web.forms import MyRegistrationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http.response import HttpResponseRedirect
from django.contrib.gis.shortcuts import render_to_kmz

def __init__(self, *args, **kwargs): 
    super().__init__(*args, **kwargs) 
    self.fields['password'].widget.attrs['class'] = 'form-control'

def SignUp(request):
    
    if request.method =='POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_success/')
    
    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    
    return render_to_response('registration/signup.html', args)

def Register_Success(request):
    return render_to_response('registration/register_success.html')    

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    category_list = Category.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list}
    
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'sg_web/index.html', context_dict)

def seleniumbasic(request):
    return render(request, 'selenium/seleniumbasic.html')

def seleniumxpath(request):
    return render(request, 'selenium/xpath.html')

def testng(request):
    return render(request, 'selenium/testng.html')

def djangobasic(request):
    return render(request, 'django/djangobasic.html')

def category(request, category_name_slug):
    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        course = Course.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['course'] = course
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'sg_web/category.html', context_dict)
        
def about(request):
    return render(request, 'sg_web/about.html')

def contactus(request):
    return render(request, 'sg_web/contactus.html')
