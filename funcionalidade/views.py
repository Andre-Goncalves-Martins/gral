from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from pessoa.models import Medico, TIPO_SANGUE, User
from .models import Exame, Consulta, BancoSanguineo, Procedimento, Prontuario, TIPO_EXAME, ESTADOS_EXAMES, LISTA_PROCEDIMENTOS
from .models import LISTA_DATAS, LISTA_HORARIOS
from .serializers import ExameSerializer, ConsultaSerializer,  ProntuarioSerializer, AttExameSerializer, CriarExameSerializer
from .serializers import CriarConsultaSerializer, GuiaMedicoSerializer, ProcedimentoSerializer, CadastroProcedimentoSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.


class ConsultaView(generics.ListAPIView):  # Mostrar consultas
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None


# Cadastrar procedimento
class CadastroProcedimentoView(generics.CreateAPIView):
    queryset = Procedimento.objects.all()
    serializer_class = CadastroProcedimentoSerializer
    permission_classes = (IsAuthenticated,)


class ProcedimentoView(generics.ListAPIView):  # Consultar procedimentos
    queryset = Procedimento.objects.all()
    serializer_class = ProcedimentoSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None


class CriarProntuariosView(generics.CreateAPIView):  # Criar Prontuario
    queryset = Procedimento.objects.all()
    serializer_class = ProntuarioSerializer
    permission_classes = (IsAuthenticated,)


class ProntuariosView(generics.ListAPIView):  # Mostrar Prontuarios
    queryset = Prontuario.objects.all()
    serializer_class = ProntuarioSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None


class ListaHora(generics.GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        try:
            status_code = status.HTTP_200_OK
            response = {
                'data': [c[0] for c in LISTA_HORARIOS],
            }
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'List does not exists',
                'error': str(e)
            }

        return Response(response, status_code)


class ListasData(generics.GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        try:
            status_code = status.HTTP_200_OK
            response = {
                'data': [c[0] for c in LISTA_DATAS],
            }
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'List does not exists',
                'error': str(e)
            }

        return Response(response, status_code)


class CriarConsultaView(generics.CreateAPIView):  # Criar consulta
    queryset = Consulta.objects.all()
    serializer_class = CriarConsultaSerializer
    permission_classes = (IsAuthenticated,)


class ExameView(generics.ListAPIView):  # Mostrar exames
    queryset = Exame.objects.all()
    serializer_class = ExameSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None


class GuiaMedicoView(generics.ListAPIView):  # Mostra Guia Médico
    queryset = Medico.objects.all()
    serializer_class = GuiaMedicoSerializer
    permission_classes = (AllowAny,)
    # Está Paginada


class CriaExameView(generics.CreateAPIView):  # Cria exames
    queryset = Exame.objects.all()
    serializer_class = CriarExameSerializer
    permission_classes = (IsAuthenticated,)


class MeusPacientesView(generics.ListAPIView):
    serializer_class = ProntuarioSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None

    def get(self, request, *args, **kwargs):
        self.queryset = Prontuario.objects.filter(doctor_id=request.user.pk)
        return super().get(request, *args, **kwargs)


class MeusMedicoView(generics.ListAPIView):
    serializer_class = ProntuarioSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None

    def get(self, request, *args, **kwargs):
        self.queryset = Prontuario.objects.filter(pacient_id=request.user.pk)
        return super().get(request, *args, **kwargs)


class FiltraExame(generics.ListAPIView):
    #queryset = Exame.objects.all()
    serializer_class = ExameSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None

    # def get_object(self):
    #     item = self.kwargs.get('pk')
    #     return get_object_or_404(Exame, pacient=item)

    def get_queryset(self):
        item = self.kwargs['pk']
        return Exame.objects.filter(pacient=item)

    # def get(self, request):
    #     data = self.get_queryset()
    #     try:
    #         status_code = status.HTTP_200_OK
    #         response = {
    #             'id': data['id'],
    #             'pacient': data['pacient'],
    #             'exam': data['exam_type'],
    #         }
    #     except Exception as e:
    #         status_code = status.HTTP_400_BAD_REQUEST
    #         response = {
    #             'success': 'false',
    #             'status code': status.HTTP_400_BAD_REQUEST,
    #             'message': 'List does not exists',
    #             'error': str(e)
    #         }
    #     return Response(response, status_code)


class AttExameView(generics.UpdateAPIView):
    queryset = Exame.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = AttExameSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return serializer


class BancoSanguineoView(generics.GenericAPIView):  # Consulta ao banco sanguíneo
    queryset = BancoSanguineo.objects.all()
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        resp = self.get_queryset()

        def volumeSangue(objetos, tipo):
            banco = objetos.filter(blood_type=tipo)
            soma = 0
            for volume in banco.values():
                soma += volume['volum']/1000
            return soma

        try:
            status_code = status.HTTP_200_OK
            response = [{
                'volume': volumeSangue(objetos=resp, tipo=tip[0]),
                'tipo': tip[0]
            }for tip in TIPO_SANGUE],

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'List does not exists',
                'error': str(e)
            }
        return Response(response, status_code)


class ListaProcedimento(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            status_code = status.HTTP_200_OK
            response = {
                'data': sorted([c[0] for c in LISTA_PROCEDIMENTOS]),
            }
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'List does not exists',
                'error': str(e)
            }
        return Response(response, status_code)


class TipoExame(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            status_code = status.HTTP_200_OK
            response = {
                'data': sorted([c[0] for c in TIPO_EXAME]),
            }
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'List does not exists',
                'error': str(e)
            }
        return Response(response, status_code)


class EstadoExame(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            status_code = status.HTTP_200_OK
            response = {
                'data': sorted([c[0] for c in ESTADOS_EXAMES]),
            }
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'List does not exists',
                'error': str(e)
            }
        return Response(response, status_code)
