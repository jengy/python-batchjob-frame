'''
Created on 2014-3-5

@author: zhangshaojun
'''

import errno
import os

class MyError(IOError):
    def __init__(self, args=None):
        self.args = args
    
    def __str__(self):
        self.errmsg = ''
        for msg in self.args:
            self.errmsg = self.errmsg + msg
        
        return self.errmsg

class FtpError(MyError):
    pass

class DBError(MyError):
    pass

class FileError(MyError):
    pass

def updArgs(args, newarg=None):
    
    if isinstance(args, IOError):
        myargs = []
        myargs.extend([arg for arg in args])
    else:
        myargs = list(args)
    
    if newarg:
        myargs.append(newarg)
    
    return tuple(myargs)

def fileArgs(file, mode, args):
    
    if args[0] == errno.EACCES and 'access' in dir(os):
        perms = ''
        permd = {
                 'r': os.R_OK,
                 'w': os.W_OK,
                 'X': os.X_OK
                 }
        pkeys = permd.keys()
        pkeys.sort()
        pkeys.reverse()
        
        for eachPerm in 'rwx':
            if os.access(file, permd[eachPerm]):
                perms =+ eachPerm
            else:
                perms += '-'
        
        if isinstance(args, IOError):
            myargs = []
            myargs.extend([args for arg in args])
        else:
            myargs = list(args)
        myargs[1] = "'%s' %s (perms: '%s')" % (mode, myargs[1], perms)
        myargs.append(args.filename)
    else:
        myargs = args
    
    return tuple(myargs)