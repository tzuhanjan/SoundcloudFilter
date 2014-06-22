import soundcloud, sys

CLIENT_ID = ''
CLIENT_SECRET = ''

def getKeys():
    global CLIENT_ID, CLIENT_SECRET
    f = open('CLIENT_ID')
    CLIENT_ID = f.readline().strip()
    f.close()
    f = open('CLIENT_SECRET')
    CLIENT_SECRET = f.readline().strip()
    f.close()
getKeys()

client = soundcloud.Client(client_id=CLIENT_ID)

def shareCallback(user, error):
    if (error):
        print("Error:" + error.message)
    else:
        print("it worked")

def numShares(track):
    return len(client.get('/e1/users/%d/track_reposts' % track.user_id))

def displayInfo(track, verbose=True):
    #shares = numShares(track)
    a,b,c = 0,0,0
    try:
        if verbose:
            print('Title:', track.title)
            print('\t# of Plays:', track.playback_count)
            print('\t# of Likes:', track.favoritings_count)
            print('\t# of Comments:', track.comment_count)
            #print('\t# of Shares:', shares)
            print('\tLike/Play Ratio:', track.favoritings_count/track.playback_count)
            #print('\tShares/Play Ratio:', shares/track.playback_count)
            #print('\tShares/Likes Ratio:', shares/track.favoritings_count
        c = track.favoritings_count/track.playback_count
        #b = shares/track.playback_count
        #a = shares/track.favoritings_count
    except:
        print("error getting info for " + track.title)
        #return [a,b,c,track]
        return [c, track]
    #if track.playback_count == 0:
    #    return (sys.float_info.max, track)
    #return [a, b, c, track]
    return [c, track]

def collectInfo():
    query = input("What would you like to search for?\n")
    tracks = client.get('/tracks/', q=query, limit=20)
    trackInfo = list(map(lambda x: displayInfo(x, False), tracks))
    upperLim = 2
    if len(trackInfo) < 5:
        upperLim = len(trackInfo)
    x = list(reversed(sorted(trackInfo, \
            key = lambda x: tuple(x[:-1]))))
    for a in x[:upperLim]:
        displayInfo(a[-1])
        print(a[0], a[-1].title, a[-1].permalink_url)
#    print('\n\n')
#    x = list(reversed(sorted(trackInfo, \
#            key = lambda x: (x[1],x[2]))))
#    for a in x[:upperLim]:
#        displayInfo(a[-1])
#        print(a[0], a[1], a[-1].title, a[-1].permalink_url)
#    print('\n\n')
#    x = list(reversed(sorted(trackInfo, \
#            key = lambda x: x[2])))
#    for a in x[:upperLim]:
#        displayInfo(a[-1])
#        print(a[0], a[1], a[-1].title, a[-1].permalink_url)


collectInfo()

