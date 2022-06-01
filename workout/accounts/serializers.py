from rest_framework import serializers
from .models import Trainer, Customer, User
from rest_framework.validators import UniqueValidator
from django.core.validators import RegexValidator
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['is_superuser'] = user.is_superuser
        token['is_customer'] = user.is_customer
        token['is_trainer'] = user.is_trainer
        # ...
        return token


class UserRegistration(serializers.ModelSerializer):
    email = serializers.EmailField(

        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    mobile_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'.")
    password = serializers.CharField(
        write_only=True,  validators=[validate_password])
    name = serializers.CharField()
    mobile = serializers.CharField(validators=[mobile_regex])
    age = serializers.IntegerField()
    weight = serializers.IntegerField()
    height = serializers.IntegerField()

    class Meta:
        model = User

        fields = ['name', 'password', 'email', 'username',
                  'mobile', 'age', 'weight', 'height']

    def save(self):

        password = self.validated_data['password']
        # user = self.context['request'].user

        if password is None:
            raise serializers.ValidationError(
                {'error': 'password cannot be empty'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError(
                {'error': 'Email already exists!'})

        account = User(email=self.validated_data['email'], username=self.validated_data['username'],
                       is_customer=True, mobile=self.validated_data['mobile'], name=self.validated_data['name'])
        account.set_password(password)
        account.save()
        Customer.objects.create(customer=account, age=self.validated_data['age'], weight=self.validated_data['weight'],
                                height=self.validated_data['height'])

        return account


class RegisterSerializerTrainer(serializers.ModelSerializer):
    email = serializers.EmailField(

        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    mobile_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'.")
    password = serializers.CharField(
        write_only=True,  validators=[validate_password])
    name = serializers.CharField()
    mobile = serializers.CharField(validators=[mobile_regex])
    certification = serializers.CharField()
    stream = serializers.CharField()
    about = serializers.CharField()

    class Meta:
        model = User

        fields = ['name', 'password', 'email', 'username',
                  'mobile', 'certification', 'stream', 'about']

    def save(self):

        password = self.validated_data['password']

        if password is None:
            raise serializers.ValidationError(
                {'error': 'password cannot be empty'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError(
                {'error': 'Email already exists!'})

        trainer = User(email=self.validated_data['email'], username=self.validated_data['username'],
                       is_trainer=True, mobile=self.validated_data['mobile'], name=self.validated_data['name'])
        trainer.set_password(password)
        trainer.save()
        Trainer.objects.create(
            trainer=trainer, certification=self.validated_data['certification'], stream=self.validated_data['stream'], about=self.validated_data['about'])
        return trainer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'username', 'mobile']


class ProfileSerializer(serializers.ModelSerializer):
    customer = UserSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = ['customer', 'age', 'weight', 'height']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'username', 'mobile']


class TrainerProfileSerializer(serializers.ModelSerializer):
    trainer = UserSerializer(read_only=True)

    class Meta:
        model = Trainer
        fields = ['trainer', 'certification', 'stream', 'about']
