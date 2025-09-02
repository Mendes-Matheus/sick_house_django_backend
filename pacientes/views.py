from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Paciente
from .serializers import PacienteSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    @action(detail=False, methods=['get'])
    def by_cpf(self, request):
        cpf = request.query_params.get('cpf')
        if not cpf:
            return Response({'error': 'CPF parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        paciente = get_object_or_404(Paciente, cpf=cpf)
        serializer = self.get_serializer(paciente)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_nome(self, request):
        nome = request.query_params.get('nome')
        if not nome:
            return Response({'error': 'Nome parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        pacientes = Paciente.objects.filter(nome__icontains=nome)
        serializer = self.get_serializer(pacientes, many=True)
        return Response(serializer.data)