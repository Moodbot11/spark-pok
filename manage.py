#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import sys

# Raise Python's max‐digits limit so our huge harmony integers can be JSON-ified
sys.set_int_max_str_digits(100000)

import os

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'primeapi.settings')
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

