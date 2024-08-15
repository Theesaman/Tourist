from django.shortcuts import render
from .bot import send_message
from .forms import ContactForm
from .models import Team,Service,Contact,Packages
from django.views.generic.list import ListView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import FormView

class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
      your_name = form.cleaned_data.get('name')
      your_email = form.cleaned_data.get('email')
      content = form.cleaned_data.get('content')
      text = f"Your Name: {your_name}\nYour Email: {your_email}\ntext: {content}"
      send_message(text)
      return super().form_valid(form)



def home_view(request):
    return render(request,'index.html')

def about_view(request):
    return render(request,'about.html')

# def service_view(request):
#     return render(request,'service.html')

class PackagesListView(ListView):
    model = Packages
    template_name = 'package.html'
    context_object_name = 'package'

class HomeListView(ListView):
    model = Packages
    template_name = 'index.html'
    context_object_name = 'package'


# def package_view(request):
#     return render(request,'package.html')

class ContactFormView(FormView):
    form_class = ContactForm
    success_url = '/'
    template_name = "contact.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs): 
        name = request.POST.get('first_name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('description', '')
        contact = Contact(first_name=name,email=email,description=message)
        contact.save()
        
        send_message(f"Ism : {name}\nEmail : {email}\nText : {message}")

        return HttpResponseRedirect(reverse('home-page')) 
    

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        content = form.cleaned_data.get('content')
        text = f"Name: {name}\nEmail: {email}\nContent : {content}"
        send_message(text)
        
        # form.save() o'rniga ma'lumotlarni saqlashni qo'shing agar kerak bo'lsa
        # example: 
        # form.instance.save()

        return super().form_valid(form)

class TeamListView(ListView):
    model = Team
    template_name = 'team.html'
    context_object_name = 'team'
    

class ServiceListView(ListView):
    model = Service
    template_name = 'service.html'
    context_object_name = 'service'