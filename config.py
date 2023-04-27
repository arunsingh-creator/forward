#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("5509916510:AAHroyKDRf7HaKq4Z79X3AhzoYXMefk6BpA")
    # The Telegram API things
    API_ID = int(os.environ.get("10577960"))
    API_HASH = os.environ.get("80fd047285f4e94ca80311928b6bb5da")
    AUTH_USERS = os.environ.get("1937257991")

