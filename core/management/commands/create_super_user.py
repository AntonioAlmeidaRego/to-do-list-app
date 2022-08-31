from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='inform username for user')
        parser.add_argument('email', type=str, help='inform email for user')
        parser.add_argument('password', type=str, help='inform password for user')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        email = kwargs['email']
        password = kwargs['password']

        def get_user(username):
            try:
                return User.objects.get(username=username)
            except Exception as e:
                print('error > ', e)
            return None

        if not get_user(username=username):
            User.objects.create_superuser(email=email, username=username, password=password)
