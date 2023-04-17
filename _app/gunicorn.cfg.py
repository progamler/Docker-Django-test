import multiprocessing

bind = ":9000"
workers = multiprocessing.cpu_count() * 2 + 1
errorlog = "gunicorn_appname.log"
