from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Flight, Booking


class FlightSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flight
		fields = ['destination', 'time', 'price', 'id']


class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'id']


class BookingDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'passengers', 'id']


class UpdateBookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['date', 'passengers']

class RegisterSerializer(serializers.ModelSerializer):

	class Meta :
		model = User
		fields = ['username', 'password', 'first_name', 'last_name']

	def create(self, validated_data):
		username_from_user = validated_data.get('username')
		password_from_user = validated_data.get('password')
		first_name_from_user = validated_data.get('first_name')
		last_name_from_user = validated_data.get('last_name')

		new_user = User(username = username_from_user )

		new_user.set_password(password_from_user)
		new_user.first_name = first_name_from_user
		new_user.last_name = last_name_from_user

		new_user.save()

		return validated_data





