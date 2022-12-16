# ---------------------------------------------------------------------#
# Title: heroku.py
# Desc: Replaces settings.py only if running the web app in Heroku
# Change Log: (Who, When, What)
# <Example Dev, 2030-Jan-01, Created File>
# ---------------------------------------------------------------------#

import os
import dj_database_url

# .file_name means the file_name is in the same folder directory
from .settings import *

DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3")
    )
}

DEBUG = False
TEMPLATE_DEBUG = False
STATIC_ROOT = os.path.join(BASE_DIR, "static")
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = ["*"]  # who can connect to your website

MIDDLEWARE = (  # Allows you to enable whitenoise
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Serves static files in Heroku
    *MIDDLEWARE,
)
