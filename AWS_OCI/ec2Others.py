from utilities import writing_to_file
import config

class ec2_Others_cost_assessments():
    def __init__(self,workbook):
        self.workbook = workbook
    
    volume_Extensions = {"EBS:VolumeP-Throughput.gp3",
                         "EBS:directAPI.snapshot.List",
                         "EBS:VolumeP-IOPS.piops",
                         "EBS:VolumeIOUsage"}
        
    def process(self):
        counter = 1
        for row in range(self.workbook.max_row+1):
            counter+=1
            cell_obj = self.workbook.cell(row=counter,column= config.line_item_usage_type_column)
            desc = self.workbook.cell(row=counter, column=config.line_item_Description_column).value
            usageUnit = self.workbook.cell(row=counter, column=config.usage_unit_column).value
            usageAmount = self.workbook.cell(row=counter, column=config.usage_amount_column).value
            if cell_obj.value != None:
                usagetype = cell_obj.value
                usagetype_tolist = usagetype.lower().split('-')
                
                if "gp3" in desc.lower() and "gb-mo" in usageUnit.lower():
                    ociUnitPrice = "0.0255,0.0017"
                    ociPrice = (usageAmount*0.0255)+(usageAmount*10*0.0017)
                    comments = "gp3 storage is mapped to balanced in OCI"
                    writing_to_file(self.workbook,
                                    counter,
                                    ociUnitPrice,
                                    ociPrice,
                                    comments,
                                    "OCI Block Volume",
                                    "B91961,B91962")
                elif "gp2" in desc.lower() and "gb-mo" in usageUnit.lower():
                    ociUnitPrice = "0.0255,0.0017"
                    ociPrice = (usageAmount*0.0255)+(usageAmount*10*0.0017)
                    comments = "gp2 storage is mapped to balanced in OCI"
                    writing_to_file(self.workbook,
                                    counter,
                                    ociUnitPrice,
                                    ociPrice,
                                    comments,
                                    "OCI Block Volume",
                                    "B91961,B91962")
                elif "magnetic provisioned storage" in desc.lower() and "gb-mo" in usageUnit.lower():
                    ociUnitPrice = "0.0255"
                    ociPrice = (usageAmount*0.0255)
                    comments = "magnetic provisioned storage is mapped to lower cost in OCI"
                    writing_to_file(self.workbook,
                                    counter,
                                    ociUnitPrice,
                                    ociPrice,
                                    comments,
                                    "OCI Block Volume",
                                    "B91961")
                elif "io1" in desc.lower() and "gb-mo" in usageUnit.lower():
                    ociUnitPrice = "0.0255"
                    ociPrice = (usageAmount*0.0255)+(usageAmount*30*0.0017)
                    comments = "io1 storage storage is mapped to Ultra High Performance in OCI"
                    writing_to_file(self.workbook,
                                    counter,
                                    ociUnitPrice,
                                    ociPrice,
                                    comments,
                                    "OCI Block Volume",
                                    "B91961,B91962")
                elif "io2" in desc.lower() and "gb-mo" in usageUnit.lower():
                    ociUnitPrice = "0.0255"
                    ociPrice = (usageAmount*0.0255)+(usageAmount*30*0.0017)
                    comments = "io2 storage storage is mapped to Ultra High Performance in OCI"
                    writing_to_file(self.workbook,
                                    counter,
                                    ociUnitPrice,
                                    ociPrice,
                                    comments,
                                    "OCI Block Volume",
                                    "B91961,B91962")
                elif "st1" in desc.lower() and "gb-mo" in usageUnit.lower():
                    ociUnitPrice = "0.0255"
                    ociPrice = (usageAmount*0.0255)
                    comments = "st1 storage is mapped to lower cost in OCI"
                    writing_to_file(self.workbook,
                                    counter,
                                    ociUnitPrice,
                                    ociPrice,
                                    comments,
                                    "OCI Block Volume",
                                    "B91961")
                elif "sc1" in desc.lower() and "gb-mo" in usageUnit.lower():
                    ociUnitPrice = "0.0255"
                    ociPrice = (usageAmount*0.0255)
                    comments = "sc1 storage is mapped to lower cost in OCI"
                    writing_to_file(self.workbook,
                                    counter,
                                    ociUnitPrice,
                                    ociPrice,
                                    comments,
                                    "OCI Block Volume",
                                    "B91961")
                elif self.volume_Extensions.issubset(usagetype_tolist):
                    comments = "Included with Volumes TestAdded"
                    writing_to_file(self.workbook,
                                    counter,
                                    0,
                                    0,
                                    comments,
                                    "OCI Block Volume")
                elif "ebs:snapshotusage" in usagetype_tolist:
                    ociUnitPrice = "0.0255"
                    ociPrice = (usageAmount*0.0255)
                    comments = "OCI Backups"
                    writing_to_file(self.workbook,
                                    counter,
                                    ociUnitPrice,
                                    ociPrice,
                                    comments,
                                    "OCI Backup",
                                    "B91961")
                
                elif "natgateway" in usagetype_tolist:
                    if "bytes" in usagetype_tolist:
                        comments = "NatGateway No Pricing for Bytes Processed"
                    elif "hours" in usagetype_tolist:
                        comments = "NatGateway No Pricing for Hours of Operation"
                    writing_to_file(self.workbook,
                                    counter,
                                    0,
                                    0,
                                    comments,
                                    "OCI Nategateway",)
                    
            
                



