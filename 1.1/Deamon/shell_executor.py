# !/usr/bin/env python

import threading
import time
import commands

import utils
import settings

class KickStarter:
    ''' Initiate Shell executers assigning them shell files '''
    def __init__(self):
        self.GENERIC_ERROR = settings.GENERIC_ERROR_CODE
        self.IO_GENERIC_ERROR = settings.IO_GENERIC_ERROR_CODE
        self.LOG_PROGRAM = settings.LOG_PROGRAM

    def start(self):
        while 1:
            for shell in settings.shells:
                shell_executer = ShellExecuter(shell)
                shell_executer.start()
            time.sleep(settings.interval)

class ShellExecuter(threading.Thread):
    ''' Execute a given shell file '''
    def __init__(self, shell_file):
        threading.Thread.__init__(self)
        self.shell_file = shell_file
        self.GENERIC_ERROR = settings.GENERIC_ERROR_CODE
        self.IO_GENERIC_ERROR = settings.IO_GENERIC_ERROR_CODE
        self.LOG_PROGRAM = settings.LOG_PROGRAM

    def run(self):
        self.execute()

    def execute(self):
        res = commands.getstatusoutput('./%s' % (self.shell_file,))
        if res[0] != 0:
            utils.log_error(self.LOG_PROGRAM + "." +  self.GENERIC_ERROR, 'Error executing shell %s' % (self.shell_file))

def start():
    KickStarter().start()
