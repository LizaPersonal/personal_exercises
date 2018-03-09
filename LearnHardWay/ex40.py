class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


chorus = "Happy birthday to you"
name = "Happy birthday dear Liza"

happy_bday = Song([chorus,
                   chorus,
                   name,
                   chorus])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()