import gevent
from gevent import socket

hosts = ['google.com', 'wwww.walterpottertaxidermy.com', 'www.antique-taxidermy.com']
jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print(job.value)