# coding=gbk
'''
Created on 2014-1-17

@author: zhangshaojun
'''
import json
from MyExcept import *

def prt(item):
    print(item["name"])

class CFGUtil(object):
    '''
    classdocs
    '''
    def __init__(self, filename):
        '''
        Constructor
        '''
        try:
            fp = open(filename, 'r')
        except IOError:
            raise FileError, filename
        
        self.jObject = json.load(fp)
        
        return
        
    def iterate(self, group, name='*', fun=prt):
        '''
        '''
        for item in self.jObject[group]:
            if item['enabled'] == 1:
                if name == '*' or item['name'] == name:
                    fun(item)
    
    def iter(self, grpdict, flist=None):
        '''
        '''
        i = 0
        keys = grpdict.keys()
        keys.sort()
        for group in keys:
            for item in self.jObject[group]:
                if item['enabled'] == 1:
                    grpdict[group](item)

'''
Unit test
ju = CFGUtil("d:\\temp\\FCSInterface.json")
ju.iterate("FCS2SaicFC", prt)
ju.iterate("SaicFC2FCS", prt)
'''
