import os

SITE_TITLE = "Historic Oregon Newspapers"
PROJECT_NAME = "Oregon Digital Newspapers Initiative"

DEBUG = False
IS_PRODUCTION = True

MARC_RETRIEVAL_URLFORMAT = "https://raw.githubusercontent.com/open-oni/marc-mirror/uo-marc/marc/%s/marc.xml"

INSTALLED_APPS = (
    'django.contrib.humanize',
    'django.contrib.staticfiles',

    # Make sure oregon theme files override plugin and core pages
    'themes.oregon',

    'onisite.plugins.title_locations',
    'onisite.plugins.featured_content',
    'onisite.plugins.map',
    'onisite.plugins.calendar',
    'core',

    # These should come last so static pages can't accidentally override theme/core pages
    'onisite.plugins.staticpages',
)

STATIC_PAGES_PATH="/opt/openoni/themes/oregon/pages"
TIME_ZONE = 'America/Los_Angeles'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}
