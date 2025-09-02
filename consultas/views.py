from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import Consulta
from .serializers import ConsultaSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.filter(ativo=True)
    serializer_class = ConsultaSerializer

    def perform_destroy(self, instance):
        # Soft delete
        instance.ativo = False
        instance.save()

    @action(detail=False, methods=['get'])
    def by_paciente(self, request):
        paciente_id = request.query_params.get('paciente_id')
        if not paciente_id:
            return Response({'error': 'paciente_id parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        consultas = Consulta.objects.filter(paciente_id=paciente_id, ativo=True)
        serializer = self.get_serializer(consultas, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_status(self, request):
        status_consulta = request.query_params.get('status')
        if not status_consulta:
            return Response({'error': 'status parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        consultas = Consulta.objects.filter(status=status_consulta, ativo=True)
        serializer = self.get_serializer(consultas, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def search(self, request):
        termo = request.query_params.get('termo')
        if not termo:
            return Response({'error': 'termo parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        consultas = Consulta.objects.filter(
            Q(paciente__nome__icontains=termo) |
            Q(tipo_consulta__icontains=termo) |
            Q(status__icontains=termo),
            ativo=True
        )
        serializer = self.get_serializer(consultas, many=True)
        return Response(serializer.data)