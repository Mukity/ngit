from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.HomePageView),
    path('login', views.LoginView),
    path('Login', views.Logout),

    path('signup', views.SignupView),
    path('Signup', views.Success),

    path('Feedback_successful', views.Feedback),

    path('donor', views.Donor),

    path('hospital', views.Hospital),
    path('hospital/', include('hospital.urls')),

    path('requests', views.Requests),
]
