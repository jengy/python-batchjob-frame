'''
Created on 2014-4-18

@author: zhangshaojun
'''
from excelUtil import xlrdRd as xls
from dbUtil import SQLPyodbc as sql
from Util import *

def File2DB(cfg, date=datetime.datetime.today()):

    log(cfg['name'] + ' >>>')
    print('...%s'%cfg['name'])
    
    fileParm = cfg["file"]
    dbParm = cfg["db"]

    fileName = "%s\\%s"%(fileParm["datpath"], fileParm["fname"])
    fileName2 = "%s\\%s-%s"%(fileParm["datpath"], datetime.datetime.today().strftime("%Y%m%d%H%M%S"), fileParm["fname"])
    firstRow = fileParm["row"]
    col_list = fileParm["col"]
    if os.access(fileName, os.R_OK) == False:
        log('    File : %s not exists.'%fileName)
        log(cfg['name'] + ' <<<')
        return
    
    try:
        dsn = dbParm["dsn"]
        sqlStr = dbParm["sqlstr"]
        ms = sql.MSSQLHelper(dsn)
    
        insValues = []
        xlsFile = xls.xlsRdUtil(fileName)
        for row_no in range(xlsFile.cursheet.nrows):
            if row_no < firstRow:
                continue
            row = xlsFile.read_row(row_no, col_list)
            if row is None:
                break
            
            #print row
            row.append(fileName)
            insValues.append(row)
            if len(insValues) == 1000:
                ms.ExecMany(sqlStr,insValues)
                del insValues[0:len(insValues)]
            
        if len(insValues) > 0:
            ms.ExecMany(sqlStr,insValues)
        fileName2 = fileName2 + '.ok'
        log('    File : %s uploaded SUCCESS.'%fileName)
    except Exception, e:
        fileName2 = fileName2 + '.fail'
        log('    File : %s uploaded FAIL.'%fileName)
    finally:
        os.rename(fileName, fileName2)
        log(cfg['name'] + ' <<<')
         
    return
