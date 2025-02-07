import config


def writing_to_file(workbook,row,column_10_value,column_11_value,column_12_value,column_13_value,skuid = None):
    workbook.cell(row=row,column=config.OCI_unit_price_column,value=column_10_value)
    workbook.cell(row=row,column=config.OCI_sum_cost_column,value=column_11_value)
    workbook.cell(row=row,column=config.OCI_Service_column,value=column_12_value)
    workbook.cell(row=row,column=config.category_column,value=column_13_value)
    
    if skuid is not None:
        workbook.cell(row=row,column=config.OCI_sku_column,value=skuid)



