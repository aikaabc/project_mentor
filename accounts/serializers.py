from rest_framework import serializers
from .models import Student, Mentor

class StudentSerializer(serializers.ModelSerializer):
    mentors = serializers.StringRelatedField(many=True)
    class Meta:
        model = Student
        fields = ['user', 'first_name', 'last_name', 'birth_date', 'mentors']


class StudentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['user', 'first_name', 'last_name', 'birth_date']


class MentorSerializer(serializers.ModelSerializer):
    students = serializers.StringRelatedField(many=True)

    class Meta:
        model = Mentor
        fields = ['user', 'first_name', 'last_name', 'birth_date', 'students']


class MentorCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mentor
        fields = ['user', 'first_name', 'last_name', 'birth_date']

