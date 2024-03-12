import os
DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': '139.99.209.131',
            'DB_NAME': 'retail_db',
            'DB_USER': os.environ.get('DB_USER_SOURCE'),
            'DB_PASS': os.environ.get('DB_PASS_SOURCE')
        },
        'TARGET_DB': {
            'DB_TYPE': 'postgres',
            'DB_HOST': '139.99.209.131',
            'DB_NAME': 'retail_db',
            'DB_USER': os.environ.get('DB_USER_TARGET'),
            'DB_PASS': os.environ.get('DB_PASS_TARGET')
        }
    }
}