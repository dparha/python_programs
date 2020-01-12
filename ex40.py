#!/usr/bin/env python3

# python the hard way exercise 40


class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy birthday to you"])
bulls_on_parade = Song(["They rally around tha family"])
party_like_1999 = Song(["Tonight we're gonna party like it's 1999."])


happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
party_like_1999.sing_me_a_song()
