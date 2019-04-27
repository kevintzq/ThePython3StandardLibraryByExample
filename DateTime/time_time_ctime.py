#!/usr/bin/python3

import time

print('Time is: ', time.time())
print('Time is: ', time.ctime())
later=time.time()+15
print('15 secs from now: ', time.ctime(later))