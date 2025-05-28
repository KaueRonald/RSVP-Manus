import os
from pathlib import Path
from dotenv import load_dotenv

# ─── Diretório base do projeto ───────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent

# ─── Carrega .env ─────────────────────────────────────────────────────────────
load_dotenv(BASE_DIR / '.env')

# ─── Chave e Debug ────────────────────────────────────────────────────────────
SECRET_KEY     = os.getenv('SECRET_KEY')
DEBUG          = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS  = []

# ─── Apps instaladas ──────────────────────────────────────────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # seus apps
    'apps.users',
    'apps.events',
    # …
]

# ─── Middleware ───────────────────────────────────────────────────────────────
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ─── URLconf raiz ─────────────────────────────────────────────────────────────
ROOT_URLCONF = 'config.urls'

# ─── Templates ────────────────────────────────────────────────────────────────
TEMPLATES = [
    {
        'BACKEND' : 'django.template.backends.django.DjangoTemplates',
        'DIRS'    : [ os.path.join (BASE_DIR / 'templates')],
        'APP_DIRS': True,
        'OPTIONS' : {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ─── WSGI ─────────────────────────────────────────────────────────────────────
WSGI_APPLICATION = 'config.wsgi.application'

# ─── Banco de dados ───────────────────────────────────────────────────────────
DATABASES = {
    'default': {
        'ENGINE':   os.getenv('DB_ENGINE'),
        'NAME':     os.getenv('DB_NAME'),
        'USER':     os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST':     os.getenv('DB_HOST'),
        'PORT':     os.getenv('DB_PORT'),
    }
}

# ─── Senhas ───────────────────────────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ─── Internacionalização ─────────────────────────────────────────────────────
LANGUAGE_CODE = 'pt-br'
TIME_ZONE     = 'UTC'
USE_I18N      = True
USE_L10N      = True
USE_TZ        = True

# ─── Arquivos estáticos ───────────────────────────────────────────────────────
STATIC_URL        = '/static/'
STATICFILES_DIRS  = [os.path.join(BASE_DIR, 'static') ]

# ─── Configurações de Login ───────────────────────────────────────────────────
LOGIN_URL          = '/users/login/'
LOGIN_REDIRECT_URL = '/events/list'
LOGOUT_REDIRECT_URL= '/users/login/'
