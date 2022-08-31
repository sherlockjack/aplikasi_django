import os
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')


ALLOWED_HOSTS = ["*"]


MIDDLEWARE = [
    ...,
    'whitenoise.middleware.WhiteNoiseMiddleware',
]