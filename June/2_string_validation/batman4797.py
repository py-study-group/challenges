#!/usr/bin/env python3

import re, sys, os, time

def mail_valid():

    print("\nEntered e-mail-ID is {}\n".format(sys.argv[1]))
    print("The e-mail-ID should contain letters|numbers|period|underscore|hypen as \nmost of e-mail -service providers have this RULE\n")
    print("Checking wait...")
    time.sleep(1)

    email  = re.compile(r"^[a-zA-Z0-9][\w\-\.]+@\w+\.\w{2,5}$")
    if email.match(sys.argv[1]):
        print("\nYes, Its Valid e-mail-ID\n")
    else:
        print("\n Sorry, Its not valid e-mail-ID\n")


if __name__ == "__main__":
    os.system("clear||cls")
    mail_valid()
