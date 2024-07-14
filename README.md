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
```bash
git clone https://github.com/thecodephilic-guy/calendar-invite-api.git
```
3. Navigate to the project directory:
```bash
cd calendar-invite-api
```
4. Create a virtual environment and activate it:
```bash
python -m venv venv
```
```bash
source venv/bin/activate
```
On Windows use 
```bash
venv\Scripts\activate
```
6. Install the required packages:
```bash
pip install -r requirements.txt
```
8. Create a `.env` file in the project root and add your email credentials:
```.env
EMAIL_HOST_USER=your-email@yourdomain.com
EMAIL_HOST_PASSWORD=your-email-password
```
10. Update `settings.py` with your email host information.
11. Run migrations:
```bash
python manage.py migrate
```
13. Start the development server:
```bash
python manage.py runserver
```

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
