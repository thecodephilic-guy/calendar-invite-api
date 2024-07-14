# Calendar Invite API

A RESTful API built with Django that automates the creation and distribution of calendar invites.

## Features

- Create and send calendar invites via email
- Generate standardized .ics files
- Handle future-dated events
- Secure credential management

## Technologies Used

- Python
- Django
- Django Rest Framework
- iCalendar library
- SMTP (Zoho Mail)

## Setup

1. Clone the repository:
git clone https://github.com/thecodephilic-guy/calendar-invite-api.git
2. Navigate to the project directory:
cd calendar-invite-api
3. Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
4. Install the required packages:
pip install -r requirements.txt
5. Create a `.env` file in the project root and add your email credentials:
EMAIL_HOST_USER=your-email@yourdomain.com
EMAIL_HOST_PASSWORD=your-email-password
6. Update `settings.py` with your email host information.
7. Run migrations:
python manage.py migrate
8. Start the development server:
python manage.py runserver

## Usage

Send a POST request to `/api/schedule/` with the following JSON structure:

```json
{
"title": "Meeting Title",
"description": "Meeting description",
"start_time": "2024-07-15T14:00:00Z",
"end_time": "2024-07-15T15:00:00Z",
"email1": "attendee1@example.com",
"email2": "attendee2@example.com"
}
