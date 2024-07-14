from django.urls import path
from .views import ScheduleEventView

urlpatterns = [
    path('schedule/', ScheduleEventView.as_view(), name='schedule_event'),
]