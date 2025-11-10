# Gunicorn configuration
workers = 4
worker_class = 'gunicorn.workers.gthread.ThreadWorker'
threads = 2
bind = '0.0.0.0:10000'
accesslog = '-'
