
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bkk',         # e.g. 'cims_db'
        'USER': 'bkk',            # e.g. 'root'
        'PASSWORD': 'bkk',    # e.g. 'password123'
        'HOST': 'localhost',                  # or your DB host/IP
        'PORT': '3306',                       # default MySQL port
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}

EMAIL_USE_TLS   = True
EMAIL_HOST      = 'smtp.gmail.com'
EMAIL_HOST_USER = 'tech@hamwe.org'
EMAIL_HOST_PASSWORD = 'priv mxdb ujkh cprr'
DEFAULT_FROM_EMAIL  = 'tech@hamwe.org'
SERVER_EMAIL = 'tech@hamwe.org'
EMAIL_PORT      = 587
