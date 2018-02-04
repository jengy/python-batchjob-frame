# coding=gbk
'''
Created on 2014-4-24

@author: zhangshaojun
'''
#from tempfile import TemporaryFile
#from datetime import datetime
from xlwt import *

class xlsWtUtil:
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.workbook = Workbook()
        
        return
    
    def new_sheet(self, sheetname):
        '''
        '''
        self.sheet = self.workbook.add_sheet(sheetname)
        self.row = 0
        return
        
    def append_rows(self, taglist, vlist):
        '''
        '''
        if self.row == 0:
            row = self.sheet.row(self.row)
            for i in range(0, len(taglist)):
                row.write(i, taglist[i])
            self.row = self.row + 1
            
        for i in range(0, len(vlist)):
            row = self.sheet.row(self.row)
            for j in range(0, len(taglist)):
                if vlist[i][j] == None:
                    value = ''
                else:
                    value = vlist[i][j]
                row.write(j, unicode(value))
            self.row = self.row + 1
        
        return self.row

    def save_file(self, filename):
        '''
        '''
        self.filename = filename
        self.workbook.save(self.filename)
        
        return


'''
e = excelUtil()
e.new_sheet('sheet-x-1')
e.append_rows(['col1'],[['value11']])

e.save_file('d:\\20140429.xls')
e.new_sheet("sheet-x-2")
e.append_rows(['col2'],[['value2']])
e.save_file('d:\\20140429.xls')   

book = Workbook()
sheet1 = book.add_sheet('test 1')
book.add_sheet('test 2')

sheet1.write(0, 0, 'A1')
sheet1.write(0, 1, 'B1')
row1 = sheet1.row(1)
row1.write(0, 'A2')
row1.write(1, 'B2')

book.save('d:\\temp\\test.xls')
'''