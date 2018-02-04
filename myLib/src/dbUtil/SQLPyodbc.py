# coding=gbk
'''
Created on 2014-1-7

@author: zhangshaojun
'''

import pyodbc
import MyExcept as err
 
i=0
def prt_record(fields, resList):
    global i       
    for fields in resList:
        i = i + 1
        print i, ')', fields

class MSSQLHelper:
    """
    """
    def __init__(self,dsn):
        #if not self.db:
        #    raise(NameError,"No db connection")
        try:
#            self.conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=' + self.host + ';DATABASE=' + self.db + ';UID=' + self.user + ';PWD=' + self.pwd)
            self.dsn = dsn
            self.conn = pyodbc.connect(self.dsn)
        except Exception:
            raise err.DBError, '__init__() DSN:%s' + self.dsn

    def close(self):
        self.conn.close()
         
    def __GetConnect(self):
        """ 
        """
        try:
            cur = self.conn.cursor()
        except Exception:
            raise err.DBError, '__GetConnect() call fail.'
        
        return cur

    def ExecQuery(self,sql):
        """ 
        """
        cur = self.__GetConnect()
        try:
            cur.execute(sql.encode("utf8"))
            resList =  cur.fetchall()
        except Exception:
            raise err.DBError, 'ExecQuery() : sql = .' + sql
            
        return resList

    def ExecQueryFun(self,sql, fields, fun=prt_record):
        """
        """
        cur = self.__GetConnect()
        try:
            cur.execute(sql.encode("utf8"))  
            count = 0
            while (1) :
                resList = cur.fetchmany(1000)
                if resList == None or len(resList) == 0:
                    break
                else:
                    fun(fields, resList)
                    count = count + len(resList)
        except Exception:
            raise err.DBError, 'ExecQueryFun() : sql = .' + sql

        return count

    def ExecProc(self,sql, params=None):
        """
        """
        try:
            cur = self.__GetConnect()
            if params is None:
                cur.execute(sql.encode("utf8"))
            else:
                cur.execute(sql.encode("utf8"), params)
            self.conn.commit()
        except Exception:
            raise err.DBError, 'ExecQueryFun() : sql = .' + sql

    def ExecMany(self,sql, params):
        """
        """
        try:
            cur = self.__GetConnect()
            cur.executemany(sql.encode("utf8"), params)
            cur.commit()
            cur.close()
        except Exception:
            raise err.DBError, 'ExecMany() : sql = .' + sql

    def ExecQueryFunWithParm(self,sql, fields, params, fun=prt_record):
        """
        """
        cur = self.__GetConnect()
        cur.execute(sql.encode("utf8"), params)  
        #try:
        count = 0
        while (1) :
            resList = cur.fetchmany(1000)
            if resList == None or len(resList) == 0:
                break
            else:
                fun(fields, resList)
                count = count + len(resList)
        #except Exception:
            #raise err.DBError, 'ExecQueryFun() : sql = ' + sql + ' Params : ' + params

        return count


'''
dsn="DRIVER={SQL Server Native Client 11.0};SERVER=,1433;DATABASE=moni;UID=sa;PWD=sa"
ms = MSSQLHelper(dsn)
fields = ('tagid', 'tagstatus')
ms.ExecProc('sp_clear_imp_tables')
#ms.ExecQueryFun("select tagid, tagstatus from mon_tag_stat where statustime > dateadd(hh, -2, getdate())", fields, prt_record)
#ms.ExecMany("insert into imp_onway_maxus (Dealer, City, Province, VCode, ArriveDate, RefFile) values (?, ?, ?, ?, ?, ?)",[['dealer1','shanghai','shanghai','LSV002','2018-1-4 0:0:0','second.xls']])
ms.close()
'''