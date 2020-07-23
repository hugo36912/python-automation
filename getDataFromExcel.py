import pandas as pd
import xlrd
import os
from pathlib import Path

class getDataFromExcel(object):
    def startGetData(sheet_name):

        
        DestPath = "Z:\\Network_Security\\Firewall_Policy_Program\\PythonFirewall\\PRDv2\\connectDatabase\\Database\\eHR_PRD_FW_lookup_V1.xlsx"
        FW_excel_lookup = DestPath
                     
        fw_db_lookup = xlrd.open_workbook(FW_excel_lookup)
        #fw_sheet_names= fw_db_lookup.sheet_names()

        #fw_zone_lookup = fw_db_lookup.sheet_by_name(fw_sheet_names[0])
        #fw_gateway_lookup = fw_db_lookup.sheet_by_name(fw_sheet_names[1])
        
        fw_lookup = fw_db_lookup.sheet_by_name(sheet_name)       
        fw_get_data = []

        num_cols = fw_lookup.ncols   # Number of columns
        for row_idx in range(0, fw_lookup.nrows):    # Iterate through rows
            #print ('-'*40)
            #print ('Row: %s' % row_idx)   # Print row number
            #fw_get_data.append(fw_lookup.row_values(row_idx))
            fw_get_data.append(fw_lookup.row_values(row_idx))

        return fw_get_data
#getDataFromExcel.startGetData()
