from utilities import writing_to_file
import config

class VPC_cost_assessment():
    def __init__(self,workbook):
        self.workbook = workbook

    def process(self):
        counter=1
        for row in range(self.workbook.max_row+1):
            counter+=1
            cell_obj = self.workbook.cell(row = counter,column=config.line_item_usage_type_column)
            if cell_obj.value != None:
                usagetype = cell_obj.value
                usagetype_tolist = usagetype.lower().split('-')

                if "vpcendpoint" in usagetype_tolist:
                    writing_to_file(workbook=self.workbook,
                                    row=counter,
                                    column_10_value=0,
                                    column_11_value=0,
                                    column_12_value="OCI private endpoints",
                                    column_13_value="OCI private endpoints VPC-Endpoint,",)

                elif "transitgateway" in usagetype_tolist:
                    writing_to_file(workbook=self.workbook,
                                    row=counter,
                                    column_10_value=0,
                                    column_11_value=0,
                                    column_12_value="Dynamic Routing Gateway (DRG)",
                                    column_13_value="OCI Dynamic Routing Gateway =  TransitGateway,")
                
                elif "publicipv4:inuseaddress" in usagetype_tolist or "publicipv4:idleaddress" in usagetype_tolist:
                    writing_to_file(workbook=self.workbook,
                                    row=counter,
                                    column_10_value=0,
                                    column_11_value=0,
                                    column_12_value="Reserved IP4",
                                    column_13_value="Public IP NO additional pricing for INUSE or IDLE")
                
                elif 'vpn' in usagetype_tolist:
                    writing_to_file(workbook=self.workbook,
                                    row=counter,
                                    column_10_value=0,
                                    column_11_value=0,
                                    column_12_value="OCI site-to-site VPN",
                                    column_13_value="AWS VPN Connection")