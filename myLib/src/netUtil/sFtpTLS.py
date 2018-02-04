'''
Created on 2014-1-6

@author: zhangshaojun
'''
from ftplib import FTP_TLS 
import sys
#import psyco

#psyco.full()

class sFtpUtil(object):
    '''
    classdocs
    '''
    
    def __init__(self,sftp_address, sftp_port, sftp_user, sftp_pass):
        '''
        Constructor
        '''
        try:
            self.sftp_Client = FTP_TLS(sftp_address)
            self.sftp_Client.login(sftp_user, sftp_pass)
            self.sftp_Client.prot_p()
        except Exception:
            sys.stderr.write('\n\nparamiko.Transport.connect FAILED.\n')
            sys.exit(1)

    def put(self, rmt_file, lcl_file):
        '''
        put file
        '''
        try:
            self.sftp_Client.put(lcl_file, rmt_file)
        except Exception:
            print('Exception')

    def get(self, lcl_file, rmt_file):
        '''
        get file
        '''
        try:
            self.sftp_Client.get(rmt_file, lcl_file)
        except Exception:
            print('Exception')

    def close(self):
        '''
        close connection
        '''
        try:
            self.sftp_Client.close()
        except Exception:
            print('Exception')

'''      
conn=sFtpUtil('10.116.15.31', 9022, 'rfid', 'rfid')
assert(conn != None)
#conn.put('first.txt', 'd:\\temp\\a.txt')
conn.get('d:\\temp\\b.txt', 'first.txt')
conn.close()
'''