from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('logins/',views.logins,name='logins'),
    path('logouts/',views.logouts,name='logouts'),
    path('home2/',views.home2,name='home2'),
    path('Tours/',views.tours,name='tours'),
    path('edu/',views.edu,name='edu'),
    path('m_tours/',views.m_tours,name='m_tours'),
    path('vendor/',views.vendor,name='vendor'),
    path('payup/',views.payup,name='payup')
]
