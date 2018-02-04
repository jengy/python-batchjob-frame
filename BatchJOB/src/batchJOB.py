# coding=gbk
'''
Created on 2018-1-23

@author: zhangshaojun
'''
from Util import *
from cfgUtil import CFGJson as c
import MonitorMail as m
import ClearDB as cl
import File2DB as f
import CleanJob as cn

def main(cfgPath):  

    workList = {
               "1-MonitorMail" : m.MonitorMail,
               "2-ClearDB"  : cl.ClearDB,
               "3-File2DB" : f.File2DB,
               "4-CleanJob" : cn.CleanJob
    }
    
    log('********** BEGIN **********', sys.stdout)
    cfgFile = cfgPath
    logPath = "log\\" + datetime.datetime.today().strftime("%Y%m%d") + "\\"
    logFile = logPath + datetime.datetime.today().strftime("%Y%m%d_%H%M%S")+".log"

    #try:
    os.chdir("..//")
    if os.access(cfgPath, os.R_OK) == False:
        log('### Config file not found.!')
        return
    if os.access(logPath, os.R_OK) == False:
        os.makedirs(logPath)
    
    log('Config file : %s' % cfgFile)
    openlog(logFile)

    cfg = c.CFGUtil(cfgFile)
    cfg.iter(workList)
    #except Exception, err:
    #    log('### ' + err.__class__.__name__ + ' -> ' + str(err))

    log('********** END **********', sys.stdout)

    return


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('gbk')
    main(sys.argv[1])