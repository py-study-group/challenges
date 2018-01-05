#!/usr/local/bin/python3
'''
This script will:
1. Get the local IP address and subnet mask
2. Calculate the address range in the local network segment
3. Scan all addresses and display those that are "alive"
4. Store results in CSV
'''
import argparse
import ipaddress
import netifaces
import os
import sys

CSV_FILE = 'hosts_export.csv' # file to save exports


def main(args):
    hosts = []
    print("Scanning network. This may take a while...")
    for ip, netmask in get_ipaddresses():
        hosts.extend(get_alive_hosts(ip, netmask, args))
    print_results(hosts)
    if args.export:
        export_results(hosts)


def print_results(hosts):
    '''Print the results'''
    [print(host) for host in hosts]


def export_results(hosts, filename=CSV_FILE):
    '''Export the results'''
    with open(filename, 'w') as f:
        f.write("\n".join(hosts))


def get_ipaddresses():
    '''Get local IP Addresses'''
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        if interface == 'lo':
            continue
        results = netifaces.ifaddresses(interface).get(netifaces.AF_INET)
        if results:
            for ip_address in results:
                yield ip_address['addr'], ip_address['netmask']


def get_alive_hosts(ip, netmask, args):
    '''Returns list of alive hosts'''
    results = ipaddress.IPv4Network((ip, netmask), strict=False)
    alive_hosts = []
    for host in results.hosts():
        if is_alive(host):
            if args.verbose:
                print('{} is alive'.format(host))
            alive_hosts.append(host)
        else:
            if args.verbose:
                print('{} is not alive'.format(host))
    return [str(host) for host in alive_hosts]


def is_alive(host):
    '''Returns bool if host is pingable'''
    result = os.system("ping -c 1 -t 1 -n " + str(host) + " 2>&1 >/dev/null")
    if result == 0:
        return True
    return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get 'alive' hosts on local network")
    parser.add_argument("-e", "--export", action="store_true", help="export to a file")
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose mode")
    args = parser.parse_args()
    main(args)
