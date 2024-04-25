from django.shortcuts import get_object_or_404
from .serializers import *
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from .models import *

class OfficeStaffAPI(APIView):
    
    parser_classes = [MultiPartParser]
    
    def get_all_officestaff(self, request):
        office_staff = OfficeStaff.objects.all()
        serializer = OfficeStaffSerializer(office_staff, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_each_officestaff(self, request, id):
        office_staff = get_object_or_404(OfficeStaff, pk=id)
        serializer = OfficeStaffSerializer(office_staff)
        return Response(serializer.data , status=status.HTTP_200_OK)

    def get(self, request, id=None):
        if id:
            return self.get_each_officestaff(request, id)
        else:
            return self.get_all_officestaff(request)
        
    def post(self, request):
        serializer = OfficeStaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, id):
        office_staff = get_object_or_404(OfficeStaff, pk=id)
        serializer = OfficeStaffSerializer(office_staff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        office_staff = get_object_or_404(OfficeStaff, pk=id)
        office_staff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    