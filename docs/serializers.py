from rest_framework import serializers

from .models import Position, Employees, User


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = "__all__"


class EmployeesSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20, write_only=True)
    password = serializers.CharField(max_length=20, write_only=True)
    password_2 = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = Employees
        fields = "__all__"
        read_only_fields = ['user', ]

    def validate(self, data):
        if data['password'] != data['password_2']:
            raise serializers.ValidationError('пароли должны совпадать')
        return data

    def create(self, validated_data):
        try:
            user = User(username=validated_data['username'])
            user.set_password(validated_data['password'])
            user.save()
        except Exception as e:
            raise serializers.ValidationError(f'Не удаётся создать пользователя. {e}')
        else:
            employee = Employees.objects.create(
                salary=validated_data['salary'],
                position=validated_data['position'],
                fullname=validated_data['fullname'],
                birthdate=validated_data['birthdate'],

                user=user,
            )
            return employee
