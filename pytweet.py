#!/usr/bin/env python
#-*- coding: utf-8 -*-

import tweepy
import sys

consumer_key = Your consumer_key
consumer_secret = your consumer_secret
access_token = Your access_token
access_secret = Your access_secret

msg = sys.stdin.readline() 

api = tweepy.OAuthHandler(consumer_key,consumer_secret)
api.set_access_token(access_token,access_secret)
tweet = tweepy.API(api)

tweet.update_status(msg)
