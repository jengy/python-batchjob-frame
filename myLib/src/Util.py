'''
Created on 2014-1-20

@author: zhangshaojun
'''
import datetime
import os
import sys

logf = sys.stdout

def openlog(logfile):
    global logf
    logf = open(logfile, 'w')
    
def log(msg, f=None):
    if f is None and logf is not None:
        f = logf
    else:
        f = sys.stdout       
    print >> f, str(datetime.datetime.now()) + ' ' + msg
    f.flush()

def bakFile(bakpath, filenames):
    '''
    '''
    log('\t BEGIN backup file.')

    if os.access(bakpath, os.R_OK) == False:
        os.makedirs(bakpath)
    
    for filename in filenames:
        bakname = os.path.split(filename)
        try:
            os.remove(bakpath+'\\'+bakname[1])
        except WindowsError:
            pass
        finally: # rename actually 
            try:
                os.rename(filename, bakpath+'\\'+bakname[1])
            except WindowsError, e:
                log('\t\t ' + filename + ' =X ' + bakpath+'\\'+bakname[1])
            else:
                log('\t\t ' + filename + ' => ' + bakpath+'\\'+bakname[1])

    log('\t END backup file.')

    return
