# hackathon/views.py

from rest_framework import generics, status
from rest_framework.response import Response
from .models import Hackathon, Enrollment, Entry
from .serializers import HackathonSerializer, EnrollmentSerializer, EntrySerializer, CreateHackathonSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hackathon, Enrollment, Entry
from .serializers import HackathonSerializer, EnrollmentSerializer, EntrySerializer
from django.shortcuts import render


class CreateHackathonView(generics.CreateAPIView):
    serializer_class = HackathonSerializer

class HackathonListView(generics.ListAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer

class HackathonEnrollmentView(APIView):
    def post(self, request, pk):
        data = request.data
        data['hackathon'] = pk
        serializer = EnrollmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HackathonEntryView(APIView):
    def post(self, request, pk):
        data = request.data
        data['hackathon'] = pk
        serializer = EntrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    return render(request, 'index.html')


class HackathonList(generics.ListCreateAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer

class HackathonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer

class EnrollmentList(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

    def create(self, request, *args, **kwargs):
        hackathon = Hackathon.objects.get(pk=kwargs['hackathon_pk'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(hackathon=hackathon)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class EntryList(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

    def create(self, request, *args, **kwargs):
        hackathon = Hackathon.objects.get(pk=kwargs['hackathon_pk'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(hackathon=hackathon)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class CreateHackathon(generics.CreateAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = CreateHackathonSerializer
