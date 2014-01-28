#!/usr/bin/env python

import syslog

import settings

def log_info(msg):
    syslog.openlog(settings.LOG_PROGRAM + ".info", 0, syslog.LOG_USER)
    syslog.syslog(syslog.LOG_INFO, msg)    
    print 'info: %s' % (msg,)

def log_warning(tag, msg):
    syslog.openlog(tag, 0, syslog.LOG_USER)
    syslog.syslog(syslog.LOG_WARNING, msg)
    print 'warning: %s' % (msg,)

def log_error(tag, msg):
    syslog.openlog(tag, 0, syslog.LOG_USER)
    syslog.syslog(syslog.LOG_ERR, msg)
    print 'error: %s' %(msg,)

def log_critical(tag, msg):
    syslog.openlog(tag, 0, syslog.LOG_USER)
    syslog.syslog(syslog.LOG_CRIT, msg)
    print 'critical: %s' %(msg,)
