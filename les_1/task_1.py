"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping
будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел
должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять
их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес
сетевого узла должен создаваться с помощью функции ip_address().
"""
import ipaddress

subnet1 = ipaddress.ip_network('188.18.254.0/28')
subnet_lst = list(subnet1.hosts())
subnet_lst.append('188.18.254.124')
#print(subnet_lst)


def host_ping(ip_lst):
    for ip_add in ip_lst:
        try:
            ipaddress.ip_network(ip_add)
            print(f'{ip_add} - Узел доступен')
        except ValueError:
            print(f'{ip_add} - Узел недоступен')


host_ping(subnet_lst)