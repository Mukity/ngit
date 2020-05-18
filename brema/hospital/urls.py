from django.urls import path

from . import views

urlpatterns = [
    path('used', views.used),
    path('donated', views.donated),
    path('showUsed', views.showUsed),
    path('showDonated', views.showDonated),
    path('manageRequests', views.manageRequests),
    path('request_added', views.addRequest),
]
