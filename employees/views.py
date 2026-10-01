from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Employee
from .serializers import EmployeeSerializer

# from leaves.models import Leave
from leaves.serializers import LeaveSerializer

from django.shortcuts import get_object_or_404

class EmployeeListCreateView(APIView):

    def get(self, request):
        employees = Employee.objects.all()

        serializer = EmployeeSerializer(employees, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class EmployeeDetailView(APIView):

    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)

        serializer = EmployeeSerializer(employee)

        return Response(serializer.data)

    def put(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)

        serializer = EmployeeSerializer(
            employee,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)

        employee.delete()

        return Response(
            {"message": "Employee deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )

class EmployeeLeaveHistoryView(APIView):

    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)

        leaves = employee.leaves.all()

        serializer = LeaveSerializer(leaves, many=True)

        return Response(serializer.data)