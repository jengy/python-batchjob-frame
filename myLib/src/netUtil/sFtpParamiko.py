'''
Created on 2014-1-6

@author: zhangshaojun
'''
import paramiko 
import sys
import os
import MyExcept as err

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
            self.sftp_Trans = paramiko.Transport((sftp_address, sftp_port))
            self.sftp_Trans.connect(username=sftp_user, password=sftp_pass) # should put variable here or will block in pydev
            self.sftp_Client = paramiko.SFTP.from_transport(self.sftp_Trans)
        except paramiko.SSHException:
            try:
                self.sftp_Trans.close()
            except AttributeError:
                pass
            raise err.FtpError, '__init__() ' + sftp_address + ':' + str(sftp_port) + ';user=' + sftp_user

    def put(self, lcl_file, rmt_file):
        '''
        put file
        '''
        try:
            self.sftp_Client.put(lcl_file, rmt_file)
        except Exception:
            raise err.FtpError, 'put() ' + lcl_file + ':' + rmt_file
        
        return lcl_file, rmt_file

    def get(self, rmt_file, lcl_file):
        '''
        get file
        '''
        try:
            self.sftp_Client.get(rmt_file, lcl_file)
        except Exception:
            raise err.FtpError, 'get() ' + rmt_file + ':' + lcl_file
        
        return rmt_file, lcl_file

    def mget(self, rmt_pattern, lcl_path="./"):
        '''
        get file
        '''
        try:
            pathsplit = os.path.split(rmt_pattern)
            rmt_path = pathsplit[0]
            pattern = pathsplit[1].split('.')
            filelist = self.sftp_Client.listdir(rmt_path)
            retlist = []
            for filename in filelist:
                if filename.startswith(pattern[0]) and filename.endswith(pattern[1]):
                    self.get(filename, lcl_path+filename)
                    retlist.append(filename)
        except Exception:
            raise err.FtpError, 'mget() ' + rmt_pattern + ':' + lcl_path
        
        return retlist

    def close(self):
        '''
        close connection
        '''
        try:
            self.sftp_Client.close()
        except Exception:
            raise err.FtpError, 'Ftp close() fail.'

'''      
conn=sFtpUtil('10.116.15.31', 9022, 'rfid', 'rfid')
assert(conn != None)
retlist = conn.mget('./FCS12.CTL', 'd:\\temp\\')
for item in retlist:
    print(item)
#conn.get('d:\\temp\\b.txt', 'first.txt')
conn.close()
'''