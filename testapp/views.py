from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import *
from .serial import *
from rest_framework import generics,mixins, viewsets
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.




## Method 1

# @csrf_exempt
# def emplist(request):

#     if request.method == "GET":
#         emp1 = emp.objects.all()
#         # print(emp1)
#         serial1 = empseri(emp1, many=True)
#         # return Response(serial1.data)
#         return JsonResponse(serial1.data, safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         seri = empseri(data=data)

#         if seri.is_valid():
#             seri.save()
#             return JsonResponse(seri.data, status=201)
#         return JsonResponse(seri.errors, status=400)

# @csrf_exempt
# def emp_det(request, pk):

#     try:
#         emp1 = emp.objects.get(pk=pk)

#         if request.method == "GET":
#             print("emp is :", emp1)
#             serial1 = empseri(emp1)
#             return JsonResponse(serial1.data)

#         elif request.method == 'PUT':

#             data = JSONParser().parse(request)
#             serial = empseri(emp1, data=data)

#             if serial.is_valid():
#                 serial.save()
#                 return JsonResponse(serial.data)
#             return JsonResponse(serial.errors, status=404)

#         elif request.method == 'DELETE':
#             msg=f"Deleted {emp1.fname}'s record"
#             emp1.delete()
#             return HttpResponse(msg,status=204)
#     except emp.DoesNotExist:
#         return HttpResponse("Nothing Found",status=404)


##Method 2:

# @api_view(['GET','POST'])
# def emplist(request):

#     if request.method == "GET":
#         emp1 = emp.objects.all()
#         # print(emp1)
#         serial1 = empseri(emp1, many=True)
#         # return Response(serial1.data)
#         return Response(serial1.data)

#     elif request.method == "POST":
#         seri = empseri(data=request.data)

#         if seri.is_valid():
#             seri.save()
#             return Response(seri.data, status=status.HTTP_201_CREATED)
#         return Response(seri.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def emp_det(request, pk):

#     try:
#         emp1 = emp.objects.get(pk=pk)

#     except emp.DoesNotExist:
#         return Response(f"No employee with id:{pk} exists",status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#             print("emp is :", emp1)
            # serial1 = empseri(emp1)
            # return Response(serial1.data)

#     elif request.method == 'PUT':

            # serial = empseri(emp1, data=request.data)
            # if serial.is_valid():
            #     serial.save()
            #     return Response(serial.data)
            # return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#             msg=f"Deleted {emp1.fname}'s record"
#             emp1.delete()
#             return Response(msg,status=status.HTTP_204_NO_CONTENT)


##Method 3

# class empApiView(APIView):

#     def get(self,request):
#         emp1 = emp.objects.all()
#         serial1 = empseri(emp1, many=True)
#         return Response(serial1.data)

#     def post(self,request):
#         seri = empseri(data=request.data)
#         if seri.is_valid():
#             seri.save()
#             return Response(f'Created record of {seri.data["fname"]} with id:{seri.data["id"]}', status=status.HTTP_201_CREATED)
#         return Response(seri.errors, status=status.HTTP_400_BAD_REQUEST)

# class empdet(APIView):

#     def get_object(self,id):

#         try:
#             emp1=emp.objects.get(id=id)
#             return emp1
#         except emp.DoesNotExist :
#             return Response(f"No employee with id:{id} exists",status=status.HTTP_404_NOT_FOUND)
            

#     def get(self,request,id):
#         emp1=self.get_object(id)
#         serial1 = empseri(emp1)
#         return Response(serial1.data)
    
#     def put(self,request,id):
#         emp1=self.get_object(id)
#         serial = empseri(emp1, data=request.data)
#         if serial.is_valid():
#             serial.save()
#             return Response(serial.data)
#         return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self,request,id):
#         emp1=self.get_object(id)
#         msg=f"Deleted {emp1.fname}'s record"
#         emp1.delete()
#         return Response(msg,status=status.HTTP_204_NO_CONTENT)

# ##Method:Generic :

# class GenApiView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin):
    # serializer_class=empseri
    # queryset=emp.objects.all()
#     lookup_field = 'id'
#     authentication_classes=[TokenAuthentication ,SessionAuthentication , BasicAuthentication]
#     permission_classes=[IsAuthenticated]


#     def get(self,request,id=None):
#         if id:
#             return self.retrieve(request)
#         else:
#             return self.list(request)
    
#     def post(self,request):
#         return self.create(request)
    
#     def put(self,request,id=None):
#         return self.update(request,id)
    
#     def delete(self,request,id):
#         return self.destroy(request,id)



    # using viewsets.viewset -- poora functionality likhna hoga like method 1:
    # using viewsets.Genericviewset -- like generic view and u have to pass mixins too:
# class EmpViewset(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.UpdateModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin):
#     serializer_class=empseri
#     queryset=emp.objects.all()
    # using Model viewset simpleee
class EmpViewset(viewsets.ModelViewSet):
    serializer_class=empseri
    queryset=emp.objects.all()