#!/usr/bin/env python3

import socket as s
import time as t

host_names = ['drive.google.com', 'mail.google.com', 'google.com.']
hosts = {}
error = False

while not error:
    for host in host_names:
        ip = s.gethostbyname(host)
        print(host, ip)

        # set current ip dict
        if not hosts.get(host):
            hosts.update({host: ip})
        else:
            if hosts.get(host) != ip:
                print('Ошибка: ', host, ' IP не сходится: ', hosts.get(host), ' ', ip, '.')
                error = True
    t.sleep(2)
