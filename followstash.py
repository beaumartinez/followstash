#!/usr/bin/env python
'''followstash

Stash all the users you follow in a private Twitter list, then unfollow those
that aren't following you.

You'll still be able to access your old timeline using the list, but your new
one will be more personal and focused. Best of both worlds.
'''

from argparse import ArgumentParser

from requests import Session
from requests_foauth import Foauth


parser = ArgumentParser(
    description="Stash all the users you follow in a private Twitter list, then unfollow those that aren't following you",
)
parser.add_argument('email', help='foauth.org email')
parser.add_argument('password', help='foauth.org password')


class Followstash(object):

    def __init__(self):
        args = parser.parse_args()

        foauth = Foauth(args.email, args.password)

        self.session = Session()
        self.session.mount('https://', foauth)

    def followstash(self):
        following = self._get_all_following()
        list_ = self._get_list()

        self._add_to_list(following, list_)
        self._unfollow(following)

    def _get_all_following(self):
        pass

    def _get_list(self):
        pass

    def _add_to_list(self, following, list_):
        pass

    def _unfollow(self, following):
        pass


if __name__ == '__main__':
    followstash = Followstash()
    followstash.followstash()
