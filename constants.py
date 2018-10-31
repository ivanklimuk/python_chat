import os

LOG_LEVEL = os.getenv('LOG_LEVEL', 20)
LOG_FORMAT = os.getenv('LOG_FORMAT', '[%(levelname)s]-[%(asctime)s]-[%(message)s]')

MAX_CONNECTIONS = int(os.getenv('MAX_CONNECTIONS', 10))

HOST = os.getenv('HOST', 'localhost')
PORT = os.getenv('PORT', 9201)
BUFSIZ = os.getenv('BUFFSIZE', 1024)

CLIENTS = {}
ADDRESSES = {}
