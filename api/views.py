from rest_framework import generics, viewsets,status
from social_django.utils import load_strategy
from api.models import *
from api.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render_to_response, redirect, render, get_object_or_404, redirect
import json,requests
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.context import RequestContext
# from django_oauth2.decorators import resource
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
@login_required(login_url='/')
def home(request):
    # context = RequestContext(request, {
    #     'request': request, 'user': request.user})
    # return render_to_response('/template/login.html', context_instance=context)
    return render(request, 'home.html')

def login(request):
    # context = RequestContext(request, {
    #     'request': request, 'user': request.user})
    # return render('login.html', context_instance=context)
    return render(request, 'registration/login.html')

def logout(request):
    auth_logout(request)
    return redirect('/')

# Create your views here.
# @login_required
# def Home(request):
#     return render(request, 'home.html')


# @login_required
# @transaction.atomic
# def update_profile(request):
#     if request.method == "POST":
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             return HttpResponseRedirect('/')
#         else:
#             messages.error(request, _('Please correct the error below.'))
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'home/profile.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })


# def Logout(request):
#     logout(request)
#     return HttpResponseRedirect('/')

# SUPERADMIN

class SuperadminList(generics.ListCreateAPIView):
    queryset = Superadmin.objects.all()
    serializer_class = SuperadminSerializer

class SuperadminDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Superadmin.objects.all()
    serializer_class = SuperadminSerializer

# SUBADMIN

class SubadminList(generics.ListCreateAPIView):
    queryset = Subadmin.objects.all()
    serializer_class = SubadminSerializer

class SubadminDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subadmin.objects.all()
    serializer_class = SubadminSerializer

# BORROWER

class BorrowerList(generics.ListCreateAPIView):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer


class BorrowerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer

# FACILITY

class FacilityList(generics.ListCreateAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer


class FacilityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

#FACILITY

#ADD NEW AND SHOW ALL FACILITIES
@api_view(['GET', 'POST'])
def FacilityList(request):
    #dumping request.data in an array
    jsonList = [] 
    jsonList.append(request.data)
    
    #SHOW ALL FACILITIES 1 AND 0 STATUS
    if request.method == 'GET':
        queryset = Facility.objects.all()
        serializer_class = FacilitySerializer(queryset, many=True)
        return Response(serializer_class.data)
    
    #ADD NEW FACILITIES 
    elif request.method == 'POST':
        c = jsonList[0]['name']
        search = Facility.objects.filter(name__iexact = c)  #checking if enetered name is already in db
        if search:
            return Response("Facility alredy exist")
        else:
            queryset = FacilitySerializer(data=request.data)
            if queryset.is_valid():
                queryset.save()
                return Response(queryset.data, status=status.HTTP_201_CREATED)
            return Response(queryset.errors, status=status.HTTP_400_BAD_REQUEST)

#GET ALL AVAILABLE FACILITIES
@api_view(['GET'])
def Facilityavailable(request):
    queryset = Facility.objects.filter(status = 1).all()
    serializer_class = FacilitySerializer(queryset, many=True)
    return Response(serializer_class.data)

#GET ALL UNAVAILABLE FACILITIES
@api_view(['GET'])
def FacilityUnavailable(request):
    queryset = Facility.objects.filter(status = 0).all()
    serializer_class = FacilitySerializer(queryset, many=True)
    return Response(serializer_class.data)

#EDIT particular facilitiy
@api_view(['POST'])
def FacilityEdit(request):
    jsonlist = []
    jsonlist.append(request.data)
    print(request.data)
    print(jsonlist)
    queryset = Facility.objects.filter(name__iexact = jsonlist[0]['name'])
    print(queryset)
    if queryset:
        if jsonlist[0]['name'] == '':
            queryset[0].name = queryset[0].name
            queryset[0].save()
        else:
            queryset[0].name = jsonlist[0]['name']
            queryset[0].save()

        if jsonlist[0]['status'] == '':
            pass
            # queryset[0].status = queryset[0].status
            # queryset[0].save()

        else:
            queryset[0].status = jsonlist[0]['status']
            queryset[0].save()

        if jsonlist[0]['quantity'] == '':
            queryset[0].quantity = queryset[0].quantity
            queryset[0].save()

        else:
            queryset[0].quantity = jsonlist[0]['quantity']
            queryset[0].save()

        return Response("Updated")
    else:
        return Response("Facility doesn't exist")

#CHANGE STATUS OF FACILITIES TO UNVAILABLE
@api_view(['POST'])
def Facilitystatus0(request):
    jsonList = []
    jsonList.append(request.data)
    name = jsonList[0]['name']
    queryset = Facility.objects.filter(status = 1 ).filter(name__iexact = name)
    if queryset:
        queryset[0].status = 0
        queryset[0].save()
        return Response('Status changed!')
    else:
        return Response('Not found!')

#CHANGE STATUS OF FACILITIES TO AVAILABLE
@api_view(['POST'])
def Facilitystatus1(request):
    jsonList = []
    jsonList.append(request.data)
    name = jsonList[0]['name']
    queryset = Facility.objects.filter(status = 0 ).filter(name__iexact = name)
    if queryset:
        queryset[0].status = 1
        queryset[0].save()
        return Response('Status changed!')
    else:
        return Response('Not found!')

#ADD QUANTITY IN FACILITIES
@api_view(['POST'])
def Facilityquantity(request):
    jsonList = []
    jsonList.append(request.data)
    newquantity = jsonList[0]['quantity']
    name = jsonList[0]['name']
    if isinstance(newquantity, str) == True: #check if the entered quantity is in int or str
        return Response('please enter valid number of quantity')
    else:
        queryset = Facility.objects.filter(status = 1 ).filter(name__iexact = name)
        if queryset:
            queryset[0].quantity = queryset[0].quantity + newquantity 
            queryset[0].save()
            return Response('New Facility/s added!')
        else:
            return Response('Not found!')


# EQUIPMENT

@api_view(['GET', 'POST'])
def EquipmentList(request):
    jsonList = []
    jsonList.append(request.data)
    
    #SHOW ALL EQUIPMENTS 1 AND 0 STATUS
    if request.method == 'GET':
        queryset = Equipment.objects.all()
        serializer_class = EquipmentSerializer(queryset, many=True)
        return Response(serializer_class.data)
    
    #ADD NEW EQUIPMENT 
    elif request.method == 'POST':
        c = jsonList[0]['name']
        search = Equipment.objects.filter(name__iexact = c)
        if search:
            return Response("Equipment alredy exist")
        else:
            queryset = EquipmentSerializer(data=request.data)
            if queryset.is_valid():
                queryset.save()
                return Response(queryset.data, status=status.HTTP_201_CREATED)
            return Response(queryset.errors, status=status.HTTP_400_BAD_REQUEST)

#GET ALL AVAILABLE EQUIPMENTS
@api_view(['GET'])
def Equipmentavailable(request):
    queryset = Equipment.objects.filter(status = 1).all()
    serializer_class = EquipmentSerializer(queryset, many=True)
    return Response(serializer_class.data)

#GET ALL UNAVAILABLE EQUIPMENTS
@api_view(['GET'])
def EquipmentUnavailable(request):
    queryset = Equipment.objects.filter(status = 0).all()
    serializer_class = EquipmentSerializer(queryset, many=True)
    return Response(serializer_class.data)

#EDIT particular facilitiy
@api_view(['POST'])
def EquipmentEdit(request):
    jsonlist = []
    jsonlist.append(request.data)

    queryset = Equipment.objects.filter(name__iexact = jsonlist[0]['name'])
    print(queryset)
    if queryset:
        if jsonlist[0]['name'] == '':
            queryset[0].name = queryset[0].name
        else:
            queryset[0].name = jsonlist[0]['name']

        if jsonlist[0]['status'] == '':
            queryset[0].status = queryset[0].status
        else:
            queryset[0].status = jsonlist[0]['status']

        if jsonlist[0]['quantity'] == '':
            queryset[0].quantity = queryset[0].quantity
        else:
            queryset[0].quantity = jsonlist[0]['quantity']
        return Response("Updated")
    else:
        return Response("Equipment doesn't exist")

#CHANGE STATUS OF EQUIPMNT TO UNVAILABLE
@api_view(['POST'])
def Equipmentstatus0(request):
    jsonList = []
    jsonList.append(request.data)
    name = jsonList[0]['name']
    print(name)
    queryset = Equipment.objects.filter(status = 1 ).filter(name__iexact = name)
    # print(queryset[0].status)
    if queryset:
        queryset[0].status = 0
        queryset[0].save()
    # serializer_class = EquipmentSerializer(queryset, many=True)
        return Response('Status changed!')
    else:
        return Response('Not found!')

#CHANGE STATUS OF EQUIPMNT TO AVAILABLE
@api_view(['POST'])
def Equipmentstatus1(request):
    jsonList = []
    jsonList.append(request.data)
    name = jsonList[0]['name']
    print(name)
    queryset = Equipment.objects.filter(status = 0 ).filter(name__iexact = name)
    # print(queryset[0].status)
    if queryset:
        queryset[0].status = 1
        queryset[0].save()
    # serializer_class = EquipmentSerializer(queryset, many=True)
        return Response('Status changed!')
    else:
        return Response('Not found!')

#ADD QUANTITY IN EQUIPMENTS
@api_view(['POST'])
def Equipmentquantity(request):
    jsonList = []
    jsonList.append(request.data)
    newquantity = jsonList[0]['quantity']
    name = jsonList[0]['name']
    print(name)
    print(newquantity)
    queryset = Equipment.objects.filter(status = 1 ).filter(name__iexact = name)
    # print(queryset[0].status)
    if queryset:
        queryset[0].quantity = queryset[0].quantity + newquantity 
        queryset[0].save()
    # serializer_class = EquipmentSerializer(queryset, many=True)
        return Response('New equipment/s added!')
    else:
        return Response('Not found!')

