'''
Created on 2014-4-18

@author: zhangshaojun
'''
import shutil
from Util import *


def CleanJob(cfg, date=datetime.datetime.today()):

    log(cfg['name'] + ' >>>')
    print('...%s'%cfg['name'])

    cleandaynum = -90
    cleandate = datetime.date.today() + datetime.timedelta(days=cleandaynum)
    cleanpath = "bak\\" + cleandate.strftime("%Y%m%d")
    log('    Clean :' + cleanpath, sys.stdout)
    try:
        shutil.rmtree(cleanpath)
    except Exception:
        pass
    finally:
        log('    Cleaned !', sys.stdout)
        
    cleanpath = "log\\" + cleandate.strftime("%Y%m%d")
    log('    Clean :' + cleanpath, sys.stdout)
    try:
        shutil.rmtree(cleanpath)
    except Exception:
        pass
    finally:
        log('    Cleaned !', sys.stdout)       
         
    
    log(cfg['name'] + ' <<<')
         
    return
