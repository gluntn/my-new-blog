#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "newblog.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
>>>>>>> 00d492edd3d17150c0b3ab2ca47205f7d62278c3

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
