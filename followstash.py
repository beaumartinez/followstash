#!/usr/bin/env python
'''followstash

Stash all the users you follow in a private Twitter list, then unfollow those
that aren't following you.

You'll still be able to access your old timeline using the list, but your new
one will be more personal and focused. Best of both worlds.
'''

from argparse import ArgumentParser


parser = ArgumentParser(
    description="Stash all the users you follow in a private Twitter list, then unfollow those that aren't following you",
)
parser.add_argument('email', help='foauth.org email')
parser.add_argument('password', help='foauth.org password')


def followstash():
    pass
