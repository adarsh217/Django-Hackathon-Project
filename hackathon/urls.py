from django.urls import path
from . import views
from .views import CreateHackathonView, HackathonListView, HackathonEnrollmentView, HackathonEntryView

urlpatterns = [
    path('hackathons/', HackathonListView.as_view(), name='hackathon-list'),
    path('hackathons/create/', CreateHackathonView.as_view(), name='create-hackathon'),
    path('hackathons/<int:pk>/enrollments/', HackathonEnrollmentView.as_view(), name='hackathon-enrollment'),
    path('hackathons/<int:pk>/entries/', HackathonEntryView.as_view(), name='hackathon-entry'),
    path('', views.index, name='index'),
    path('hackathons/', views.HackathonList.as_view(), name='hackathon-list'),
]
