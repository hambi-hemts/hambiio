
import openpyxl
from numpy import arange

def writecell(workbook, worksheet, row, column, content):
    """
    workbook  = xlsx filename
    worksheet = name
    row = number of the row as in the xlsx worksheet 
    column = str or index
    """
    #wb = workbook #openpyxl.load_workbook(workbook)
    #ws = wb.get_sheet_by_name(worksheet)
    wb = workbook
    ws = worksheet
    
    if type(column) == int:
        column = openpyxl.cell.get_column_letter(column)
    
    ws[column + str(row)] = content
    #wb.save(workbook)
    
def get_column_string_by_name(workbook, worksheet, column_name, row = 1):
    
    #wb = workbook #openpyxl.load_workbook(workbook)
    #ws = wb.get_sheet_by_name(worksheet)
    wb = workbook
    ws = worksheet
    
    max_col = ws.get_highest_column() 
    max_col = openpyxl.cell.get_column_letter(max_col)
    
    search_range = 'A'+str(row)+':'+max_col+str(row)
    
    for row in ws.iter_rows(search_range):
        for mycell in row:
            if mycell.value == column_name:
                xy = openpyxl.cell.coordinate_from_string(mycell.coordinate)
                return xy[0] 
            
def get_column_index_by_name(workbook, worksheet, column_name, row = 1):
    name = get_column_string_by_name(workbook, worksheet, column_name, row)
    return openpyxl.cell.column_index_from_string(name)
            
def get_row_index_by_name(workbook, worksheet, row_name, column = 'A'):
    
    #wb = workbook #openpyxl.load_workbook(workbook)
    #ws = wb.get_sheet_by_name(worksheet)
    wb = workbook
    ws = worksheet
    
    max_row = ws.get_highest_row() 
    #max_col = openpyxl.cell.get_column_letter(max_col)
    
    search_range = column+str(1)+':'+column+str(max_row)
    
    for row in ws.iter_rows(search_range):
        for mycell in row:
            if mycell.value == row_name:
                xy = openpyxl.cell.coordinate_from_string(mycell.coordinate)
                return xy[1] 

def load2dict(worksheet, dev_id):
    """
    :param worksheet: loaded worksheet of an xlrd workbook with one column 'ID' and other columns with more properties
        :code:
            workbook = xlrd.open_workbook('xls/A3172_S3_Measurements.xlsx')
            worksheet = workbook.sheet_by_index(0)
    :param dev_id: the name of the device for which will be searched in the column 'ID'
    :return: a dictionary with the names of the properties and the value of the device with the ID provided in 'dev_id'
    """
    column = worksheet.col_values(0) # ID

    ind0 = [i for i in arange(len(column)) if column[i] == 'ID']
    ind0 = int(ind0[0])
    keys = worksheet.row_values(ind0)

    ind = [i for i in arange(len(column)) if column[i] == dev_id]
    ind = int(ind[0])
    values = worksheet.row_values(ind)

    the_dict = {keys[i] : values[i] for i in arange(len(keys))}

    return the_dict