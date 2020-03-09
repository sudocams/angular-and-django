from rest_framework import serializers
from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id','name', 'number', 'email', 'admin_no', 'languages', 'team', 'bio')
