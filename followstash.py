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
        # This returns all following (at least when tested with 1797)
        following_response = self.session.get('https://api.twitter.com/1.1/friends/ids.json')
        following_response.raise_for_status()

        following = following_response.json()
        following = following['ids']
        following = reversed(following)

        return following

    def _get_list(self):
        lists_response = self.session.get('https://api.twitter.com/1.1/lists/list.json')
        lists_response.raise_for_status()

        lists = lists_response.json()

        for list_ in lists:
            if list_['slug'] == 'followstash':
                return list_['id']

        # We couldn't find the list. Create it
        list_create_response = self.session.post('https://api.twitter.com/1.1/lists/create.json?name=Followstash&mode=private')
        list_create_response.raise_for_status()

        list_ = list_create_response.json()

        return list_['id']

    def _add_to_list(self, following, list_name):
        following = tuple(following)
        groups = _groups(following)

        for group in groups:
            formatted_group = ','.join(map(str, group))

            list_add_response = self.session.post('https://api.twitter.com/1.1/lists/members/create_all.json?list_id={}&user_id={}'.format(list_name, formatted_group))

            try:
                list_add_response.raise_for_status()
            except:
                print list_add_response.text
                print list_add_response.headers
                raise

    def _unfollow(self, following):
        pass


def _groups(list_, group_size=100):
    for i in xrange(0, len(list_), group_size):
        yield list_[i:i + group_size]


if __name__ == '__main__':
    followstash = Followstash()
    followstash.followstash()
