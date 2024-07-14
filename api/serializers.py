from rest_framework import serializers
from .models import CalendarEvent
from django.utils.timezone import is_aware, make_aware

class CalendarEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarEvent
        fields = ['title', 'description', 'start_time', 'end_time', 'email1', 'email2']

    def validate_start_time(self, value):
        if not is_aware(value):
            return make_aware(value)
        return value

    def validate_end_time(self, value):
        if not is_aware(value):
            return make_aware(value)
        return value