from rest_framework import serializers
from .models import Leave


class LeaveSerializer(serializers.ModelSerializer):

    def validate(self, data):
        employee = data['employee']
        start_date = data['start_date']
        end_date = data['end_date']

        if start_date > end_date:
            raise serializers.ValidationError(
                "End date must be greater than or equal to start date"
            )

        duration = (end_date - start_date).days + 1

        if duration > employee.leave_balance:
            raise serializers.ValidationError(
                "Insufficient leave balance"
            )

        return data

    class Meta:
        model = Leave
        fields = '__all__'