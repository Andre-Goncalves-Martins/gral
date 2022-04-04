from django.urls import path
from .views import CriaExameView,  CadastroProcedimentoView, CriarConsultaView, CriarProntuariosView
from .views import ExameView, ConsultaView, BancoSanguineoView, GuiaMedicoView, ProcedimentoView, MeusMedicoView, MeusPacientesView
from .views import TipoExame, EstadoExame, ListaProcedimento, ListaHora, ListasData
from .views import AttExameView, FiltraExame

app_name = 'funcionalidade'

urlpatterns = [
    # create urls
    path('marcar_consulta', CriarConsultaView.as_view(), name='marcar_consulta'),
    path('marcar_exame', CriaExameView.as_view(), name='marcar_exame'),
    path('marcar_procedimento', CadastroProcedimentoView.as_view(),
         name='marcar_procedimento'),
    path('criar_prontuario', CriarProntuariosView.as_view(), name='marcar_exame'),

    # list urls
    path('guia_medico', GuiaMedicoView.as_view(), name='guiamedico'),
    path('procedimento', ProcedimentoView.as_view(), name='procedimento'),
    path('consulta', ConsultaView.as_view(), name='consulta'),
    path('exame', ExameView.as_view(), name='exame'),
    path('meus_medicos', MeusMedicoView.as_view(), name='meus_medicos'),
    path('meus_pacientes', MeusPacientesView.as_view(), name='meus_pacientes'),

    # generics urls
    path('banco_sanguineo', BancoSanguineoView.as_view(), name='bancosanguineo'),
    path('tipo_exame', TipoExame.as_view(), name='tipo_exame'),
    path('estado_exame', EstadoExame.as_view(), name='estado_exame'),
    path('lista_procedimento', ListaProcedimento.as_view(),
         name='lista_procedimento'),
    path('lista_hora', ListaHora.as_view(), name='lista_hora'),
    path('lista_data', ListasData.as_view(), name='lista_data'),

    # update urls
    path('att_exame/<int:pk>', AttExameView.as_view(), name='att_exame'),

    # retrieve urls
    path('filtra_exame/<int:pk>', FiltraExame.as_view(), name='f_exame'),


]
