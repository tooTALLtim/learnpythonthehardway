class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy Birthday to you",
                   "Happy Birthday to yooou",
                   "Happy Birthday to meeeee",
                   "Happy Birthday to me"])

bulls_on_parade = Song(["They rally round the family",
                       "With a pocket full of shells",
                       "Weapons not food not homes not shoes",
                       "No need, just feed the war cannibal animal"])

all_you_need = Song(["There's nothing you can do that can't be done",
                     "Nothin\' you can sing that can't be sung",
                     "Nothing you can say but you can learn how to play the game"])

this_is_just_a_test = ("Like a thick-ass book that's filled with dope rhymes",
                       "Like a broken clock that can't tell time",
                       "One two one two this is just...a...test")

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
all_you_need.sing_me_a_song()

# two ways to pass this_is_just_a_test to the Song() class
# way number one
Song(this_is_just_a_test).sing_me_a_song()
# way number two
beastie_boys = Song(this_is_just_a_test)
beastie_boys.sing_me_a_song()