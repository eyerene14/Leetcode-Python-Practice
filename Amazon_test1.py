#return [2 songDurations]
# The function is expected to return an INTEGER_ARRAY
# The function accepts following parameters:
#   1. INTEGER rideDuration
#   2. INTEGER_ARRAY songDurations

from operator import index

from collections import Counter
rideDuration = 90
songDurations = [1,3,15,25,35,60]
songDurations = [1,3,15,20,35,25,40,60]

def findSongs(rideDuration, songDurations):

    maxSongDuration = rideDuration - 30
    pairs = {}
    for v in songDurations:
        #secondSongDurationNeeded = ssdn
        ssdn = maxSongDuration - v
        if ssdn in songDurations:
            songDurations.index(v)
            twoSongs.append(songDurations.index(ssdn))
    return twoSongs

r = findSongs(rideDuration, songDurations)
print(r)
print(r.pop(1))
print(min(r))
print(sum(r)) 