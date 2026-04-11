
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
