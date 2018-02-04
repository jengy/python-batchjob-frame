'''
Created on 2018.1.22

@author: zhangshaojun
'''

from xlrd import *


class xlsRdUtil(object):
    '''
    classdocs
    '''
    def __init__(self, fileName, sheet_no=None):
        '''
        Constructor
        '''
        self.workbook = open_workbook(fileName)
        if sheet_no is not None and len(sheet_no) > 0:
            self.cursheet = self.workbook.sheets()[sheet_no]
        else:
            self.cursheet = self.workbook.sheets()[0]
            
        return
    
    def read_row(self, row_no, col_list=None):
        '''
        '''
        if col_list is None or len(col_list)==0:
            return self.cursheet.row_values(row_no)
        else:
            row_value = []
            for col_no in col_list:
                value = self.cursheet.cell_value(row_no, col_no)
                if value is not None:
                    # date datatype convert to string
                    if self.cursheet.cell_type(row_no, col_no) == XL_CELL_DATE:
                        value = "%s-%s-%s %s:%s:%s"%xldate_as_tuple(value, 0)
                    if self.cursheet.cell_type(row_no, col_no) == XL_CELL_NUMBER:
                        value = "%d"%value
                    row_value.append(value)
                else:
                    row_value.append('')
                
                
            if len(row_value) > 0:
                return row_value
            else:
                return None
    
    def read_cell(self, row_no, col_no):
        return self.cursheet.Cell(row_no, col_no).value


'''
xls = xlsRdUtil("d:\\11915.xlsx")
for row_no in range(xls.cursheet.nrows):
    row = xls.read_row(row_no)
    print row
'''    
    