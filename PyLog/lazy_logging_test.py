#!/usr/bin/env python
# coding=utf-8

import logging

class lazyEval:
    def __init__(self, f, *args):
        self.func = f
        self.args = args
    def __str__(self):
        return str(self.func(*self.args))

logger = logging.getLogger('LazyLogging')
logger.setLevel(logging.DEBUG)
hander = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name) - %(levelname)s - %(message)s')
hander.setFormatter(formatter)
logger.addHandler(hander)

def getUserCount():
    logger.info('getUserCount is called')
    return 1

# logger.debug("There are" + str(getUserCount()) + "users logged in now")
# logger.debug("There are %s users logged in now.", getUserCount())
logger.debug("There are %s users logged in now.", lazyEval(getUserCount))
