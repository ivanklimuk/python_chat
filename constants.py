import os

LOG_LEVEL = os.getenv('LOG_LEVEL', 20)
LOG_FORMAT = os.getenv('LOG_FORMAT', '[%(levelname)s]-[%(asctime)s]-[%(message)s]')

MAX_CONNECTIONS = int(os.getenv('MAX_CONNECTIONS', 10))

HOST = 'localhost'
PORT = 9201
BUFSIZ = 1024
