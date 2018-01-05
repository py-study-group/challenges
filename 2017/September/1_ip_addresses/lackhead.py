#!/usr/local/bin/python3
#
# Monthly programming challenges for the study.py group
#
# Get the local IP address and subnet mask and calculate the address
# range in you network segment. Scan all the addresses and display
# those that are alive.
# Bonus points: Extract the IPs on a CSV file
#
# Author: Chad Lake (https://github.com/lackhead)
#


###############################################
# Dependencies                                #
###############################################
import netifaces
import argparse
import sys
import ipaddress
import subprocess
import os


###############################################
# Functions                                   #
###############################################
def ping_host(host):
    # ping a host and return True/False if it responds
    try:
        return not subprocess.call(["ping", "-c 1", "-t 1", "-n", str(host)], stdout=subprocess.DEVNULL)
    except KeyboardInterrupt:
        sys.exit()


###############################################
# Main program body                           #
###############################################


#
# Deal with command line arguments
#
Parser = argparse.ArgumentParser(description="Check for IP addreses that respond on the network")
Parser.add_argument("-i", "--interface", help="local network interface to check")
Parser.add_argument("-f", "--file", help="output addresses to a CSV file")
Parser.add_argument("-l", "--list", action='store_true', help="list available interfaces")
Parser.add_argument("-q", "--quiet", action='store_true', help="do not display addresses that are being scanned")
Args = Parser.parse_args()
# print out list of interfaces if that's what they want
if Args.list:
    print(", ".join(netifaces.interfaces()))
    sys.exit()
# determine the interface to use
if Args.interface:
    Interface = Args.interface
    # validate that it's a real Interface
    try:
        testval = netifaces.interfaces().index(Interface)
    except:
        print("{} is not a valid Interface".format(Interface))
        sys.exit(1)
else:
    # pick the first default gateway we can find
    Gateway = netifaces.gateways()
    try:
        Interface = Gateway['default'][netifaces.AF_INET][1]
    except KeyError:
        print("No default interface found; please specify interface with the --interface option.")


#
# From the interface, determine the network we're looking at
#
try:
    InterfaceAddresses = netifaces.ifaddresses(Interface)[netifaces.AF_INET]
except KeyError:
    print("No IP address found for interface {}".format(Interface))
    sys.exit(2)
# It is possible that there is more than one IP addr bound to this interface; default
# to the first one in the list
MyAddress = InterfaceAddresses[0]['addr']
MyNetmask = InterfaceAddresses[0]['netmask']
MyNetwork = ipaddress.IPv4Network((MyAddress, MyNetmask), strict=False)


#
# Before we get started, see if we can open up any necessary files
#
if Args.file:
    try:
        FOUT = open(Args.file, 'w')
    except OSError:
        print("Unable to open {} for writing!".format(Args.file))
        sys.exit(3)


#
# Walk thorugh the subnet and see who is alive
#
AliveIPs = []
for NetIp in MyNetwork.hosts():
    if ping_host(NetIp):
        AliveIPs.append(str(NetIp))
        if not Args.quiet:
            print("{} is alive".format(NetIp))
    else:
        if not Args.quiet:
            print("{} did not respond".format(NetIp))


#
# If they want the output written to a CSV file, dup STDOUT
#
if FOUT:
    print(",".join(AliveIPs), file=FOUT)
else:
    print("IPs in your network that are alive:")
    print("\n".join(AliveIPs))


###############################################
# We're done                                  #
###############################################
sys.exit()
