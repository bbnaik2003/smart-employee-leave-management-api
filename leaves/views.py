from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Leave
from .serializers import LeaveSerializer

from django.shortcuts import get_object_or_404
from django.db import transaction


class LeaveListCreateView(APIView):

    def get(self, request):
        leaves = Leave.objects.all()

        serializer = LeaveSerializer(leaves, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = LeaveSerializer(data=request.data)

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


class LeaveDetailView(APIView):

    def patch(self, request, pk):
        leave = get_object_or_404(Leave, pk=pk)

        new_status = request.data.get("status")

        if leave.status != "Pending":
            return Response(
                {"error": "Only pending leaves can be processed"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if new_status == "Approved":

            duration = leave.calculate_duration()
            employee = leave.employee

            if employee.leave_balance < duration:
                return Response(
                    {"error": "Insufficient leave balance"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            with transaction.atomic():
                employee.leave_balance -= duration
                employee.save()

                leave.status = "Approved"
                leave.save()

        elif new_status == "Rejected":

            leave.status = "Rejected"
            leave.save()

        else:
            return Response(
                {"error": "Invalid status"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = LeaveSerializer(leave)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )