import os
from website.settings import BASE_DIR

SECRET_KEY = 'lkhfosiw(*^%^#kjvcg%#@%&(*l;k,bhfxgfxtdst8764#'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
