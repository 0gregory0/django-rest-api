from rest_framework import serializers
from db_app.models import Address, Company, Geo, Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ("id", "name", "username", "email", "address", "phone", "website", "company")
        depth = 2

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("name", "catchPhrase", "bs")

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ("street", "suite", "city", "zipcode", "geo")

class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geo
        fields = ("lat", "lng")