"""
Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2.
Но в данном случае результат должен быть итоговым по всем ip-адресам, представленным в табличном формате
(использовать модуль tabulate). Таблица должна состоять из двух колонок
"""
import tabulate
import ipaddress
from netaddr import iter_iprange

subnet1 = ipaddress.ip_network('188.18.254.0/28')
subnet_lst = list(subnet1.hosts())
available_ip = []
unavailable_ip = []


def host_ping(ip_add):
    try:
        ipaddress.ip_network(ip_add)
        print(f'{ip_add} - Узел доступен')
        available_ip.append(ip_add)
    except ValueError:
        print(f'{ip_add} - Узел недоступен')
        unavailable_ip.append(ip_add)


def host_range_ping(ip_list):
    ip_list = list(iter_iprange('188.18.254.3', '188.18.254.10'))
    for ip_addr in ip_list:
        if ip_addr in ip_list:
            host_ping(ip_addr)


def host_range_ping_tab():
    columns = ['Доступные IP', 'Недоступные IP']
    ip_lst = [available_ip, unavailable_ip]
    print(tabulate(ip_lst, headers=columns))


host_range_ping(subnet_lst)
host_range_ping_tab()
