#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# import os
# import sys


# def main():
"""Run administrative tasks."""
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newproject.settings')
    # try:
        # from django.core.management import execute_from_command_line
    # except ImportError as exc:
        # raise ImportError(
"Couldn't import Django. Are you sure it's installed and "
"available on your PYTHONPATH environment variable? Did you "
"forget to activate a virtual environment?"
        # ) from exc
    # execute_from_command_line(sys.argv)


# if __name__ == '__main__':
#  main()


# if __name__ == "__main__":
    # default_port = 8000

    # Define the port number for the specific app
    # first_app_port = 9000

    # from django.core.management import execute_from_command_line

    # Check if the specific app port number is provided as a command-line argument
    # if len(sys.argv) > 1 and sys.argv[1] == "firstapp":
        # execute_from_command_line(['manage.py', 'runserver', f'0.0.0.0:{first_app_port}'])
    # else:
        # execute_from_command_line(['manage.py', 'runserver', f'0.0.0.0:{default_port}'])

# if __name__ == "__main__":
#  import sys
#  main()

# Define the port number for the specific app
    # first_app_port = 9000
    # from django.core.management import execute_from_command_line

    # Check if the specific app port number is provided as a command-line argument
    # if len(sys.argv) > 1 and sys.argv[1] == "firstapp":
        # execute_from_command_line(['manage.py', 'runserver', f'0.0.0.0:{first_app_port}'])
    # else:
        # execute_from_command_line(['manage.py', 'runserver', f'0.0.0.0:{default_port}'])
        
import os

import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()