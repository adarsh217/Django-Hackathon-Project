# hackathon/serializers.py

from rest_framework import serializers
from .models import Hackathon, Enrollment, Entry

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'name']

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['id', 'name', 'summary', 'submission']

class HackathonSerializer(serializers.ModelSerializer):
    enrollments = EnrollmentSerializer(many=True, read_only=True)
    entries = EntrySerializer(many=True, read_only=True)

    class Meta:
        model = Hackathon
        fields = ['id', 'title', 'description', 'background_image', 'hackathon_image',
                  'start_datetime', 'end_datetime', 'reward_prize', 'enrollments', 'entries']

class CreateHackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = '__all__'
