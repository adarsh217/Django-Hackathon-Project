# hackathon/models.py

from django.db import models

class Hackathon(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    background_image = models.URLField()
    hackathon_image = models.URLField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    reward_prize = models.CharField(max_length=255)

class Enrollment(models.Model):
    name = models.CharField(max_length=255)
    hackathon = models.ForeignKey(Hackathon, related_name='enrollments', on_delete=models.CASCADE)

class Entry(models.Model):
    name = models.CharField(max_length=255)
    summary = models.TextField()
    submission = models.TextField()
    hackathon = models.ForeignKey(Hackathon, related_name='entries', on_delete=models.CASCADE)
