from django.urls import path
from home import views
from django.contrib import admin

admin.site.site_header="Login to Anzar Portal"
admin.site.site_title="Welcome to Anzar's Dashboard"
admin.site.index_title="Welcome to Anzar Portal"

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('projects/',views.projects, name='projects'),
    path('contact/',views.contact, name='contact'),
]
