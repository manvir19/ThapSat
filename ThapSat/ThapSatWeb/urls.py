from django.urls import path
from . import views
urlpatterns = [
    path( '' , views.home , name="home" ),
    path( 'updates' , views.updates , name="updates" ),
    path( 'departments' , views.departments , name="departments" ),
    path( 'subsystems' , views.subsystems , name="subsystems" ),
    path( 'social' , views.social , name="social" ),



]