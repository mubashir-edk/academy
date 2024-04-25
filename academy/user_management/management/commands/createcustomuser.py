from django.core.management.base import BaseCommand
from user_management.models import CustomUser

class Command(BaseCommand):
    help = 'Create custom users: teacher, student, office staff and admin'

    def add_arguments(self, parser):
        parser.add_argument('--email', type=str, help='Email address')
        parser.add_argument('--username', type=str, help='Username')
        parser.add_argument('--password', type=str, help='Password')
        parser.add_argument('--user_type', type=str, help='User type: teacher, student, office_staff')

    def handle(self, *args, **kwargs):
        email = kwargs['email']
        username = kwargs['username']
        password = kwargs['password']
        user_type = kwargs['user_type']

        if email and username and password:
            user = CustomUser.objects.create_user(email=email, username=username, password=password)
            if user_type == 'teacher':
                user.is_teacher = True
            elif user_type == 'student':
                user.is_student = True
            elif user_type == 'office_staff':
                user.is_office_staff = True
            elif user_type == 'admin':
                user.is_staff = True
                user.is_superuser = True
            user.save()
            user_type_str = user_type if user_type else "Superuser"
            self.stdout.write(self.style.SUCCESS(f'{user_type_str.capitalize()} {username} created successfully!'))
        else:
            self.stdout.write(self.style.ERROR('Please provide email, username, and password'))
