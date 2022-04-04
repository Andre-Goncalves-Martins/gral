from rest_framework import serializers
from pessoa.models import Medico, User
from .models import Exame, Consulta, BancoSanguineo, Procedimento, Prontuario
from pessoa.serializers import PacienteSerializer, MedicoSerializer


class ExameSerializer(serializers.ModelSerializer):
    pacient = PacienteSerializer()

    class Meta:
        model = Exame
        fields = ('id', 'pacient', 'exam_type', 'state')


class CriarExameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exame
        fields = ('exam_date', 'exam_hour', 'pacient',
                  'exam_type')

    def create(self, validated_data):
        validated_data['pacient'] = self.context.get('request').user
        exame = Exame.objects.create(**validated_data)
        exame.save()
        return exame


class AttExameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exame
        fields = ('id', 'state')

    def update(self, instance, validated_data):
        instance.state = validated_data.get('state', instance.state)
        return super().update(instance, validated_data)


class CriarConsultaSerializer(serializers.ModelSerializer):
    doctor = serializers.CharField()

    class Meta:
        model = Consulta
        fields = ('consult_date', 'pacient', 'consult_hour', 'doctor')

    def create(self, validated_data):
        validated_data['pacient'] = self.context.get('request').user
        nomedico = validated_data['doctor']
        medico = User.objects.filter(first_name=nomedico)
        doctor = Medico.objects.filter(user_id=medico.values('id')[0]['id'])
        validated_data['doctor'] = doctor[0]
        consulta = Consulta.objects.create(**validated_data)
        consulta.save()
        return consulta


class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ('id', 'doctor', 'pacient',)


class ProcedimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedimento
        fields = ('id', 'type', 'date', 'pacient', 'doctor')


class CadastroProcedimentoSerializer(serializers.ModelSerializer):
    doctor = serializers.CharField()

    class Meta:
        model = Procedimento
        fields = ('type', 'date', 'pacient', 'doctor')

    def create(self, validated_data):
        validated_data['pacient'] = self.context.get('request').user
        nomedico = validated_data['doctor']
        medico = User.objects.filter(first_name=nomedico)
        doctor = Medico.objects.filter(user_id=medico.values('id')[0]['id'])
        validated_data['doctor'] = doctor[0]
        proced = Procedimento.objects.create(**validated_data)
        proced.save()
        return proced

    # def create(self, validated_data):
    #     validated_data['pacient'] = self.context.get('request').user
    #     procede = Procedimento.objects.create(**validated_data)
    #     procede.save()
    #     return procede


class ProntuarioSerializer(serializers.ModelSerializer):
    doctor = MedicoSerializer()
    pacient = PacienteSerializer()

    class Meta:
        model = Prontuario
        fields = ('date', 'pacient', 'doctor')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', )


class GuiaMedicoSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Medico
        fields = ('crm', 'uf',
                  'specialty', 'user')
