'''
Created on 2014-4-18

@author: zhangshaojun
'''

from netUtil import POP3Util as pop3
from Util import *

def MonitorMail(cfg, date=datetime.datetime.today()):
    
    log(cfg['name'] + ' >>>')
    print('...%s'%cfg['name'])

    try:
        host = cfg["host"]
        email = cfg["email"]
        pwd = cfg["pwd"]
        datadir = cfg["datadir"]
        sender = cfg["sender"]
        subject = cfg["subject"]
        days = cfg["days"]
        mail = pop3.POP3Util(host, email, pwd, datadir)
        mail.fetch_mail(subject, sender, days)
        log('    Fetch mail : %s SUCCESS.'%email)
    except Exception, e:
        log('    Fetch mail : %s FAIL.'%email)
    finally:
        log(cfg['name'] + ' <<<')
         
    return