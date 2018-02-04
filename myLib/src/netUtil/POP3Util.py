'''
Created on 2018.1.22
@author: zhangshaojun
'''
import poplib
from datetime import datetime
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

def decode_str(s):
#    print("s:%s"%s)
    value, charset = decode_header(s)[0]
#    print("value:%s"%value)
    if charset:
#        print("before : %s"%value)
        value = value.decode(charset)
#        print(u"after : %s"%value)
#    print("after:%s"%value)
    return value

def print_info(msg, indent=0):
    print('###################################')
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))
            
class POP3Util(object):
    '''
    classdocs
    '''

    def __init__(self, host='',
                       email='',
                       password='',
                       datadir='d:\\temp'):
        '''
        Constructor
        '''
        self.email = email
        self.password = password
        self.host = host
        self.datadir = datadir
        
        self.server = poplib.POP3(host)
        #print(self.server.getwelcome())
        self.server.user(email)
        self.server.pass_(password)
    
    
    def fetch_mail(self, subjects, senders, days=None):
        
        curTime = datetime.now()
        resp, mails, octets = self.server.list()
        for idx in range(len(mails)):
            idx = len(mails) - idx
            resp, lines, octets = self.server.retr(idx)
            msg = Parser().parsestr('\r\n'.join(lines))

            mailSender  = decode_str(msg.get('From'))
            mailSubject = decode_str(msg.get('Subject'))
            
            if days is not None:
                mailDate = msg.get('Date')
                if mailDate[0] in ['0','1','2','3']:
                    mailDate = datetime.strptime(mailDate[0:20],'%d %b %Y %H:%M:%S')
                else:
                    mailDate = datetime.strptime(mailDate[5:25],'%d %b %Y %H:%M:%S')
                delta = curTime - mailDate
                if delta.days > days:
                    break
#            print(mailDate)
#           # choose mail subject and mail sender
            thisMail = 0
            if senders is not None and len(senders) > 0:
                for sender in senders:
                    if mailSender.find(sender) >= 0 :
                        thisMail = 1
                        break
                    else:
                        continue
            if subjects is not None and len(subjects) > 0:
                for subject in subjects:
                    if mailSubject.find(subject) >= 0:
                        thisMail = 1
                        break
                    else:
                        continue
            # filter configured
            if senders is not None and len(senders) > 0 or \
               subjects is not None and len(subjects) > 0:
                if not thisMail:
                    continue
            else:
                pass
            
            #print( 'mailSubject : ' + mailSubject)            
            #print( 'mailSender : ' + mailSender)            
            for part in msg.walk():  
                fileName = part.get_filename()  
                contentType = part.get_content_type()  
                mycode=part.get_content_charset();  
                
                if fileName :  
                    if fileName.upper().find('UTF-8') > 0 or \
                       fileName.upper().find('GB2312') > 0:
                        fileName = decode_str(fileName)  

#                    print('Attachment >>> ' + fileName)
                    data = part.get_payload(decode=True)  
                    fEx = open("%s\\%s"%(self.datadir, fileName), 'wb')  
                    fEx.write(data)  
                    fEx.close()  
                        
                elif contentType == 'text/html':  
                    data = part.get_payload(decode=True)  
                    content=str(data);  
            
        return

'''   
s='=?UTF-8?B?44CQ5Zui5aeU5LyY5oOg56Wo56aP5Yip44CRMjAxOOW5tDHmnIgyOOaXpeeIseS5kOaxh+KAouKAnA==?='
decode_str(s)
pop3 = POP3Util()
pop3.fetch_mail(['FR'], ['moni@saicfinance.cn'])
'''