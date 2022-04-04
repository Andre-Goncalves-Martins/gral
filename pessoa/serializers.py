from rest_framework import serializers
from .models import Medico, User
from rest_framework.validators import UniqueValidator
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from email.message import EmailMessage
import smtplib
import ssl


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'cpf', 'first_name')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name')


class MedicoSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Medico
        fields = ('user',)


class CadastraMedicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medico
        fields = ('crm', 'uf', 'specialty')


class CadastraMSerializer(serializers.ModelSerializer):
    medico = CadastraMedicoSerializer()

    class Meta:
        model = User
        fields = ('first_name', 'email', 'password',
                  'medico')

    def create(self, validated_data):
        validated_data['username'] = validated_data['email']
        validated_data['user_type'] = 'Médico'
        password = validated_data.pop('password', None)
        medico_data = validated_data.pop('medico')

        usuario = User.objects.create(**validated_data)
        Medico.objects.create(user=usuario, **medico_data)
        if password is not None:
            usuario.set_password(password)
        usuario.save()
        return usuario


class CadastraUSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ('first_name', 'cpf', 'phone',
                  'email', 'password', 'blood_type')
        extra_kwargs = {
            'first_name': {'required': True},
            'cpf': {'required': True},
            'phone': {'required': True},
            'email': {'required': True},
            'password': {'required': True},
        }

    def create(self, validated_data):
        validated_data['username'] = validated_data['email']
        my_email = validated_data['email']
        name = validated_data['first_name']
        validated_data['user_type'] = 'Paciente'
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()

        msg = EmailMessage()
        msg.set_content(
            f"Olá {name}!!!, Obrigado por Escolher o Gral, Cadastro Realizado Com Sucesso!!!!")
        msg["Subject"] = "Cadastro Gral"
        msg["From"] = "gral.suport@gmail.com"
        msg["To"] = f"{my_email}"

        context = ssl.create_default_context()

        with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
            smtp.starttls(context=context)
            smtp.login(msg["From"], "gral123456")
            smtp.send_message(msg)

        return instance
