from django.shortcuts import render
from .models import Tarea
from .serializers import TareaSerialazer
from rest_framework import viewsets, permissions

# View para controlar las peticiones get, put, post y delete
class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TareaSerialazer
    

    
    
