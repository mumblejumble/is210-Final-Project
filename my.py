#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Final Project: Make an Appointment"""


QUESTION = (raw_input('Would you like to schedule a homevisit? ')).upper()[:1]
ERROR_M = 'Sorry, the day or time you selected is not available.'

if QUESTION == 'Y':
    NAME = (raw_input('Can I have your name please? ')).upper()
    WEEKDAY = (raw_input('What day would you like? ')).lower()[:3]
    A_DAYS = ['mon', 'tue', 'wed', 'thu', 'fri']
    if WEEKDAY in A_DAYS:
        TIME = int(raw_input('What time? '))
        A_TIME = [12, 13, 14, 15, 16, 17]
        if TIME in A_TIME:
            MESSAGE = ('Thank you {}, your homevisit is schedule'
                       'on {} at {}.'.format(NAME, WEEKDAY, TIME))
            print MESSAGE
        else:
            print ERROR_M
    else:
        print ERROR_M
else:
    print 'Have a good day, bye.'
