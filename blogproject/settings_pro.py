from settings import *

LOG_PATH = "/var/log/web_code_player"
if not os.path.exists(LOG_PATH):
    LOG_PATH = os.path.join(BASE_DIR, 'logs')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] [%(levelname)s]  [%(name)s::%(lineno)d] >>>>func: %(funcName)s : %(message)s'
        },
    },
    'filters':{},
    'handlers':{
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_PATH, 'web_code_player.log'),
            'maxBytes': 1024 * 1024 * 100,  # 100 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'blog': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_PATH, 'blog.log'),
            'maxBytes': 1024 * 1024 * 100,  # 100 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'comments': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_PATH, 'comments.log'),
            'maxBytes': 1024 * 1024 * 100,  # 100 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
    },
    'loggers':{
        'django': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'blog': {
            'handlers': ['blog', 'console', ],
            'level': 'DEBUG',
            'propagate': True
        },
        'comments': {
            'handlers': ['comments', 'console', ],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}