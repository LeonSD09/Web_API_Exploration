import praw

reddit = praw.Reddit(client_id='A-D0XwYD4I_VVQ',
                     client_secret=None,
                     redirect_uri='http://localhost:8080',
                     user_agent='Playing with Snakes by /u/lsdangio')



for submission in reddit.subreddit('listentothis').top(time_filter='week',limit=25):
    print(submission.title)
"""
Heather Hammers -- I Still Love You [Acoustic] (2018)
Mariya Takeuchi -- An unforgettable feeling [City Pop/Soul] (1984)
Mom Jeans -- Girl Scout Cookies [Emo] (2016)
CHELSEA JADE - LAUGH IT OFF [Pop]
O’Brother - Your Move [Post-Rock/Alternative Rock] (2016)
Leila Adu - Asylums for the Feeling [Acoustic] (2018)
Death Bells - Echoes [Dream Pop/Brit Pop/Post Punk] (2018)
Sudan Archives - Nont for Sale [folk/soul/electronic] (2018)
The Hot Sardines - I Wanna Be Like You [French/Jazz] (2016)
Stay Outside -- All The Way Down [Indie Rock] (2018)
Kresnt - D.Y.D [Hip Hop] (2018)
Junko Ohashi - Dancin' (1983) [Japanese Funk/Boogie]
Arkana -- Malkuth [Atmospheric/Electronic] (2018)
Mighty River -- Railroad Earth [Bluegrass Rock] (2002)
Hot 8 Brass Band - Get Up [rap/brass funk] (2018)
Texxcoco - Velvet Love [Indie Rock] (2018)
Stig Trip - Loop 2 [Instrumental rock/guitar] (2017)
Justin Abisror - X Marks the Spot [Pop] (2018)
B9 (비나인) -- RESET [Korean/Indie/Rock](2016)
Ha the Unclear -- Secret Lives of Furniture [alt-pop/indie] (2016)
Gazpacho - Demon [Progressive Rock] (2014)
Fatlip - What's Up Fatlip? [Rap/hip hop] (2005)
Luna Aura - Sucker Punch [pop] (2018)
Simba - Super SKRT | Lil Yachty Type Beat [Rap/HipHop] (2018)
Asheru & Blue Black - This Is Me [Hip Hop] (2001)
"""


ltt_top25_wk = reddit.subreddit('listentothis').top(time_filter='week',limit=25)
for x in ltt_top25_wk:
    print(x)
"""
8pq2z2
8qrqz7
8qbrgn
8q2175
8r16ix
8qqsqu
8q76bs
8pnfga
8q9h5s
8pp3yp
8r3c4y
8poflq
8q8uom
8qiknz
8pne2v
8quvx4
8q0d2j
8qeyhb
8q928l
8qhdl4
8r0hzz
8qw0yt
8qbh9h
8pw77b
8r0bsx
"""

for x in ltt_top25_wk:
    print(x.title)