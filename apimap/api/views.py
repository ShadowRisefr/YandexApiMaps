from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
#from api.models import Location
from api.models import Address
# from api.serializers import LocationSerializers

import json
import requests
import sys
from api.jsonmaps import name1



def index(request):
	# Address.objects.create(raw='text',street='1',house='1',latitude='1',longitude='1')
	# Street.objects.create(raw='text',street='1',house='1',latitude='1',longitude='1')
	# Locality.objects.create(raw='text',street='1',house='1',latitude='1',longitude='1')
	# AdministrativeArea.objects.create(raw='text',street='1',house='1',latitude='1',longitude='1')
	# Country.objects.create(raw='text',street='1',house='1',latitude='1',longitude='1')
	addresses = Address.objects.all()
	print(addresses)
	#return render(request, "index.html", {"addresses": addresses})
	return render(request, "index.html")

def coord_out(request):
	array = []
	for x in name1:
		YandexMapsUrl = "https://geocode-maps.yandex.ru/1.x/?apikey=82a32a7f-84a2-4eb0-bd73-fe49223472c7&format=json&geocode={}".format(x['Name'])
		print(YandexMapsUrl)
		req = requests.get(YandexMapsUrl)
		res = req.json()
		result = res['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
		array.append(result)
	# cords = Location.objects.all()
	# serializers = LocationSerializers(cords, many=True)
	return HttpResponse({str(array)})

# def coord_in(request):
# 	#for Саня
# 	cords = Location.objects.create(name=array['name'],description=array['description'],location_l=array['location_l'],location_u=array['location_u'])
# 	return Response({"data": 'success'})

# def index(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         return render(request, 'network/home.html', {'posts': posts})
#     return HttpResponse('error')