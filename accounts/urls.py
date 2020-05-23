from django.urls import path, include 
from . import views 

urlpatterns = [
    path('', include('rest_auth.urls')), 
    path('registration/', include('rest_auth.registration.urls')),
    path('students/', views.StudentListView.as_view(), name='student-list'),
    path('mentors/', views.MentorListView.as_view(), name='mentor-list'),
    path('mentors/<int:pk>/', views.MentorDetailView.as_view(), name='mentor-detail'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
    path('students/create/', views.StudentCreateView.as_view(), name='student-create'),
    path('mentors/create/', views.MentorCreateView.as_view(), name='mentor-create'),
] 