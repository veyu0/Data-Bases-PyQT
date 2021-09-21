"""
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
Меняться должен только последний октет каждого адреса.
По результатам проверки должно выводиться соответствующее сообщение.
"""
import ipaddress
from netaddr import iter_iprange

subnet1 = ipaddress.ip_network('188.18.254.0/28')
subnet_lst = list(subnet1.hosts())
print(subnet_lst)


def host_ping(ip_add):
    try:
        ipaddress.ip_network(ip_add)
        print(f'{ip_add} - Узел доступен')
    except ValueError:
        print(f'{ip_add} - Узел недоступен')


def host_range_ping(ip_list):
    ip_list = list(iter_iprange('188.18.254.3', '188.18.254.10'))
    for ip_addr in ip_list:
        if ip_addr in ip_list:
            host_ping(ip_addr)


host_range_ping(subnet_lst)
