'''
Created on 2014-4-18

@author: zhangshaojun
'''
from dbUtil import SQLPyodbc as sql
from Util import *


def ClearDB(cfg, date=datetime.datetime.today()):

    log(cfg['name'] + ' >>>')
    print('...%s'%cfg['name'])

    dbParm = cfg["db"]

    try:
        dsn = dbParm["dsn"]
        prcStr = dbParm["prcstr"]
        ms = sql.MSSQLHelper(dsn)
        ms.ExecProc(prcStr)
        ms.close()
        log('    Procedure : %s call SUCCESS.'%prcStr)
    except Exception, e:
        log('    Procedure : %s call FAIL.'%prcStr)
    finally:
        log(cfg['name'] + ' <<<')
         
    return
