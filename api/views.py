from django.core.mail import EmailMessage
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CalendarEventSerializer
from icalendar import Calendar, Event

class ScheduleEventView(APIView):
    def post(self, request):
        serializer = CalendarEventSerializer(data=request.data)
        if serializer.is_valid():
            start_time = serializer.validated_data['start_time']
            end_time = serializer.validated_data['end_time']
            
            # Create iCalendar file
            cal = Calendar()
            event = Event()
            event.add('summary', serializer.validated_data['title'])
            event.add('description', serializer.validated_data['description'])
            event.add('dtstart', start_time)
            event.add('dtend', end_time)
            cal.add_component(event)

            # Send email with attachment
            email = EmailMessage(
                'Calendar Invite',
                'Please find the calendar invite attached.',
                settings.EMAIL_HOST_USER,
                [serializer.validated_data['email1'], serializer.validated_data['email2']]
            )
            email.attach('invite.ics', cal.to_ical(), 'text/calendar')
            
            try:
                email.send(fail_silently=False)
                return Response({'message': 'Invite sent successfully'}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)