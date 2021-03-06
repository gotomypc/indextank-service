# Django settings for RTS project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
DATABASE_NAME = 'indextank'             # Or path to database file if using sqlite3.
DATABASE_USER = '****'             # Not used with sqlite3.
DATABASE_PASSWORD = '****'         # Not used with sqlite3.
DATABASE_HOST = 'database'             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Etc/GMT+0'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',                      
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'backoffice.urls'

TEMPLATE_DIRS = (
    'templates'
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.humanize',
    'backoffice',
)

AUTH_PROFILE_MODULE = 'backoffice.PFUser'
STATIC_URLS = [ '/_static' ]
ALLOWED_INCLUDE_ROOTS = ('static')
LOGIN_URL = '/login'

#PROCS_DIR = '../indexengine/'

USER_COOKIE_NAME = "pf_user"
COMMON_DOMAIN = 'localhost'
#SESSION_COOKIE_DOMAIN = COMMON_DOMAIN
FORCE_SCRIPT_NAME = ''
USE_MULTITHREADED_SERVER = True
LOGGER_CONFIG_FILE='logging.conf'

# 0.001 MB per doc
INDEX_SIZE_RATIO = 0.002

EMAIL_HOST='localhost'
EMAIL_PORT=25
EMAIL_HOST_USER='user%localhost'
EMAIL_HOST_PASSWORD='****'
