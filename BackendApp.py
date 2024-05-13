# Using Django code Framework

from django.http import JsonResponse
from django.urls import path
from django.core.management import execute_from_command_line
from django.core.wsgi import get_wsgi_application
from django.conf import settings

settings.configure(DEBUG=True, ROOT_URLCONF=__name__)

# Data for demonstration
users = [
    {'name': 'John Doe', 'address': '123 Main St'},
    {'name': 'Jane Smith', 'address': '456 Elm Ave'}
]

def get_users(request):
    return JsonResponse(users, status=200)

urlpatterns = [
    path('get_users', get_users),
]

if __name__ == '__main__':
    application = get_wsgi_application()
    execute_from_command_line(["manage.py", "runserver"])
