from utilities import writing_to_file
import config
import re

class DirectConnect_cost_assessment():
    
    def __init__(self, workbook):
        self.workbook = workbook
    
    def costCalculation(self,counter,unitcost,usageAmount,port_number,port_unit,oci_port):
        try:
            total_cost = unitcost*usageAmount
            writing_to_file(self.workbook,
                    counter,
                    unitcost,
                    total_cost,
                    f"OCI fast connect",
                    f"Directconnect {port_number} - {port_unit} mapped to {oci_port}",
                    )
        
        except Exception as e:
            print(f"{e} at {counter}")
        
    def process(self):
        counter = 1
        for row in range(self.workbook.max_row+1):
            counter+=1
            cell_obj = self.workbook.cell(row=counter,column= config.line_item_usage_type_column)
            if cell_obj.value != None:
                usagetype = cell_obj.value
                usagetype_tolist = usagetype.lower().split('-') 
                # print(usagetype_tolist)
                portUsage = re.search(r"(\d+)([a-zA-Z]+)", usagetype_tolist[2])
                if portUsage:
                    port_unit = portUsage.group(2)
                    port_number = int(portUsage.group(1))
                    # print(f"{port_unit} :  = {port_number}")
                    usageAmount = self.workbook.cell(row=counter,column= config.usage_amount_column).value
                    
                    
                    if port_unit == 'm' and port_number < 1000:
                        self.costCalculation(counter,config.fastConnect_1_gbps,usageAmount,port_number,port_unit,"fastConnect 1 Gbps")
                        
                        
                    if port_unit == 'g' and port_number == 1:
                        self.costCalculation(counter,config.fastConnect_1_gbps,usageAmount,port_number,port_unit,"fastConnect 1 Gbps")
                        

                    if port_unit == 'g' and port_number > 1 and port_number <= 10:
                        self.costCalculation(counter,config.fastConnect_10_gbps,usageAmount,port_number,port_unit,"fastConnect 10 Gbps")
                    
                    if port_unit == 'g' and port_number > 10 and port_number < 100:
                        self.costCalculation(counter,config.fastConnect_100_gbps,usageAmount,port_number,port_unit,"fastConnect 100 Gbps")
                    
                    if port_unit == 'g' and port_number >= 100 and port_number < 400:
                        self.costCalculation(counter,config.fastConnect_400_gbps,usageAmount,port_number,port_unit,"fastConnect 400 Gbps")