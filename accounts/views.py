from rest_framework import generics 
from .models import Student, Mentor
from .serializers import StudentSerializer, MentorSerializer, StudentCreateSerializer, MentorCreateSerializer
from allauth.account.forms import LoginForm

class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer


class MentorListView(generics.ListAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer


class MentorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer


class MentorCreateView(generics.CreateAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorCreateSerializer


