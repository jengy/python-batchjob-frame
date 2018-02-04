# coding=gbk
'''
Created on 2014-2-6

@author: zhangshaojun
'''

from smtplib import SMTP as smtp
import mimetypes
import os
#from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

class SMTPUtil(object):
    '''
    classdocs
    '''


    def __init__(self, host, user, pwd):
        '''
        Constructor
        '''        
        if isinstance(host, unicode):
            self.host = host.encode('gbk')
        if isinstance(user, unicode):
            self.user = user.encode('gbk')
        if isinstance(pwd, unicode):
            self.pwd = pwd.encode('gbk')
        
        self.smtp = smtp(self.host)
        #self.smtp.helo('mail.saicfinance.com')
        self.smtp.login(self.user, self.pwd)
        self.msg = MIMEMultipart()

    def sendMail(self, subject, files, fr='rfid@saicfinance.com', to=['sj_zhang@msn.com']):
        '''
        '''
        COMMASPACE=','
        
        self.msg['From'] = fr
        self.msg['To'] = COMMASPACE.join(to)
        self.msg['Subject'] = subject
        self.msg.preamble = 'test'
        
        for f in files:
            ctype, encoding = mimetypes.guess_type(f)
            if ctype is None or encoding is not None:
                ctype='application/octet-stream'
            maintype,subtype = ctype.split('/',1)
            att=MIMEImage(open(f, 'rb').read(),subtype)
            basename=os.path.basename(f)
            att["Content-Disposition"] = 'attachmemt;filename=%s' % basename
            self.msg.attach(att)
            
        self.smtp.sendmail(fr, to, self.msg.as_string())
        
'''
s = SMTPUtil(u"10.116.1.24", u"shaojunz", u"apollo")
s.sendMail(subject=unicode('测试', 'gbk'), files=["d:\\新建文本文档.txt"])
'''