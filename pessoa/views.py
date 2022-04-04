from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import CadastraUSerializer, CadastraMSerializer, PacienteSerializer, MedicoSerializer, UserSerializer
from .models import User, Medico, UF, LISTA_ESPECIALIDADES, TIPO_SANGUE
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


# Create your views here.
class ListaSangue(generics.GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        try:
            status_code = status.HTTP_200_OK
            response = {
                'data': sorted([c[0] for c in TIPO_SANGUE]),
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


class ListaUF(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            status_code = status.HTTP_200_OK
            response = {
                'data': sorted([c[0] for c in UF]),
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


class ListaEspecialidade(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            status_code = status.HTTP_200_OK
            response = {
                'data': sorted([c[0] for c in LISTA_ESPECIALIDADES]),
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


class FiltraCpf(generics.ListAPIView):
    serializer_class = PacienteSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None

    def get_queryset(self):
        item = self.kwargs['pk']
        return User.objects.filter(cpf=item)


class MedicoView(generics.ListAPIView):
    queryset = User.objects.filter(user_type='Médico')
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None


class PacienteView(generics.ListAPIView):
    queryset = User.objects.filter(user_type='Paciente')
    serializer_class = PacienteSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None


class RegistreMedico(generics.CreateAPIView):  # Cadastra Usuário
    queryset = Medico.objects.all()
    serializer_class = CadastraMSerializer
    permission_classes = (IsAdminUser,)


class RegistreUser(generics.CreateAPIView):  # Cadastra Usuário
    queryset = User.objects.all()
    serializer_class = CadastraUSerializer
    permission_classes = (AllowAny,)


class UserProfileView(generics.GenericAPIView):  # Perfil do Usuário
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_class = JWTAuthentication

    def get(self, request):
        try:
            user_profile = User.objects.get(id=request.user.pk)
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status_code': status_code,
                'message': 'User profile fetched successfully',
                'user': [{
                    'id': user_profile.id,
                    'first_name': user_profile.first_name,
                    'email': user_profile.email,
                    'cpf': user_profile.cpf,
                    'phone': user_profile.phone,
                    'user_type': user_profile.user_type,
                    'blood_type': user_profile.blood_type,
                }]
            }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'User does not exists',
                'error': str(e)
            }
        return Response(response, status=status_code)
