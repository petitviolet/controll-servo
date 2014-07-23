# -*- coding:utf-8 -*-
# Twitterからの指示を取得しsend.inoに送信

from serial import Serial
import twitter
import time

def main():
    keys = [line.strip() for line in open('keys.txt')]

    api = twitter.Api(consumer_key=keys[0],
                      consumer_secret=keys[1],
                      access_token_key=keys[2],
                      access_token_secret=keys[3],
                      cache=None)

    com = Serial('/dev/cu.usbmodem14211', 57600)
    id = 0

    while True:
        timeline = api.GetFriendsTimeline()
        for tweet in timeline:
            if tweet.user.screen_name in (u'pika_shi', u'petitviolet', u'krrrr38')\
               and u'エアコン付けて' in tweet.text and tweet.id > id:
                com.write('1')
                api.PostUpdate(status='@pika_shi 付けたで'.decode("utf-8"),
                               in_reply_to_status_id=tweet.id)
        id = timeline[0].id
        time.sleep(60)

if __name__ == '__main__':
    main()
