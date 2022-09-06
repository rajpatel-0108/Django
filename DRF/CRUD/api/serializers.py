from dataclasses import field
from pyexpat import model
from wsgiref.validate import validator
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    address = serializers.SerializerMethodField('get_address')
    
        

    #validators
    def start_with_r(value):
        if value[0].lower() != 'r':
                raise serializers.ValidationError("Name must be start with R")
    
    name = serializers.CharField(validators = [start_with_r])
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city','address']
    
    def get_address(self,Student):
        name = Student.name
        city = Student.city
        return name + city

    #Field level Validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError("Seat Full")
        return value

    #Object level Validation
    def validate(self, data):  #data is a python dict of fields value
        nm = data.get('name')
        ct = data.get('city')

        if nm.lower() == 'jinkal' and ct.lower() != 'Baroda':
            raise serializers.ValidationError("City must be Godhara")
        return data

# #validators
# def start_with_r(value):
#     if value[0].lower() != 'r':
#         raise serializers.ValidationError("Name must be start with R")

# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100,  validators = [start_with_r])
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100) 

#     def create(self, validate_data):
#         return Student.objects.create(**validate_data)
    
#     def update(self, instance, validated_data): #instance = current value , validated_data = new value
#         # print(instance.name)
#         instance.name = validated_data.get('name', instance.name)
#         # print(instance.name)
#         instance.roll = validated_data.get('roll', instance.roll)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()
#         return instance

#     #Field level Validation
#     def validate_roll(self, value):
#         if value >= 200:
#             raise serializers.ValidationError("Seat Full")
#         return value

#     #Object level Validation
#     def validate(self, data):  #data is a python dict of fields value
#         nm = data.get('name')
#         ct = data.get('city')

#         if nm.lower() == 'jinkal' and ct.lower() != 'Baroda':
#             raise serializers.ValidationError("City must be Godhara")
#         return data

