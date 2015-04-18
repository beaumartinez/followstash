# Followstash

Stash all the users your following into a private list.

## Why?

Because. Come at me brah.

Being serious now, I follow a lot of accounts but sometimes I like to [purge](https://github.com/beaumartinez/unfollow).
It's nice to have a permanent list of Beau Certified™ users.

## OK how do I use this?

Ain't nobody got time for OAuth, consumer tokens, and all that so I use [foauth.org](https://foauth.org/). You'll need
to authorize the Twitter service (simple read-only access) will do, and you should be set.

Fire the script up with—

    $ ./followstash.py <foauth.org email> <foauth.org password>

And it'll do it's thing. Any errors and it'll tell you. Once it's done, check your lists on Twitter and you should have
one with all the users you're following (the list will be called Followstash).

I was too lazy to PyPI this or anything like that so you'll have to clone the repo for now.
