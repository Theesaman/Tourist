from django.urls import path
from .views import ServiceListView,TeamListView,ContactFormView,about_view,PackagesListView,HomeListView

urlpatterns = [
    path('',HomeListView.as_view(),name='home-page'),
    path('about/',about_view,name='about-page'),
    path('service/',ServiceListView.as_view(),name='service-page'),
    path('package/',PackagesListView.as_view(),name='package-page'),
    path('contact/',ContactFormView.as_view(),name='contact-page'),
    path('team/',TeamListView.as_view(),name='team-page'),
]