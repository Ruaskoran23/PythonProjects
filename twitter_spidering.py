#this is a twitter spidering program that looks for links and store them in a database
import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl
import sqlite3

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#json of the twitter url
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('twitter_spider.sqlite')
conn_handle = conn.cursor()

conn_handle.execute('''CREATE TABLE IF NOT EXISTS 
                    Twitter (Name TEXT, Retrieved INTEGER, Friends INTEGER)''')

while True:
    account = input('Enter a user account name:')
    if (len(account) < 1):
        conn_handle.execute('SELECT Name FROM Twitter WHERE Retrieved = 0 LIMIT 1')
        try:
            account = conn_handle.fetchone[0]
        except:
            print('No such Twitter account found') 
            continue
    url = twurl.augment(TWITTER_URL, {'screen_name' = account, 'count' = 20})
    print('Retreiving:', url)
    url_handle = urllib.request.urlopen(url, context = ctx)
    data = url_handle.read().decode()
    headers = dict(url_handle.getheaders())

    print('Remaining:', headers['x-rate-limit-remaining'])
    js = json.loads(data)

    conn_handle.execute('UPDATE Twitter SET Retrieved = 1 WHERE Name =?', (account,))

    countold = 0
    countnew = 0

    for user in js['users']:
        friend = user['screen_name']
        print(friend)
        conn_handle.execute('SELECT Friends FROM Twitter WHERE Name = ? LIMIT 1', (friend,))
        try:
            count = conn_handle.fetchone()[0]
            conn_handle.execute('UPDATE Twitter SET friends = ? WHERE name = ?',
            (count+1, friend))
            countold = countold + 1
        except:
            conn_handle.execute('''INSERT INTO Twitter (name, retrieved, friends)
            VALUES (?, 0, 1)''', (friend, ))
            countnew = countnew + 1
    print('New accounts=', countnew, 'revisited=' countold)
    conn.commit()
conn_handle.close()

    