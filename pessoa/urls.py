from django.urls import path, include
from .views import RegistreUser
from rest_framework_simplejwt import views as jwt_views
from .views import UserProfileView, RegistreMedico  # , UserLoginView
#from django.contrib.auth import views as auth_view
from django.contrib.auth import views as auth_views
from .views import PacienteView, MedicoView, ListaEspecialidade, ListaUF, ListaSangue, FiltraCpf


app_name = 'pessoa'

urlpatterns = [
    path('cadastro', RegistreUser.as_view(), name='cadastro'),
    path('perfil/', UserProfileView.as_view(), name='perfil'),
    path('cadastra_medico', RegistreMedico.as_view(), name='cadastra_medico'),
    path('pacientes', PacienteView.as_view(), name='pacientes'),
    path('medicos', MedicoView.as_view(), name='medicos'),
    path('especialidades', ListaEspecialidade.as_view(), name='especialidades'),
    path('uf', ListaUF.as_view(), name='uf'),
    path('sangue', ListaSangue.as_view(), name='sangue'),
    path('cpf/<str:pk>', FiltraCpf.as_view(), name='cpf'),

]
