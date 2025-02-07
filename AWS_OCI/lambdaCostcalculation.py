from utilities import writing_to_file
import config

class Lambda_cost_assessments():

    invocationPrice = 0.0000002 # per invocation pricing
    executionPrice = 0.00001417 # execution  price per second.

    def __init__(self, workbook):
        self.workbook = workbook

    def lambdaCompute_calculation(self,counter):
        usage_amount = self.workbook.cell(row=counter, column = config.usage_amount_column).value
        totalcost = usage_amount * self.executionPrice
        writing_to_file(self.workbook,
                        counter,
                        self.executionPrice,
                        totalcost,
                        "0.00001417 execution price per second on OCI Function",
                        "Execution",
                        "B91617")

    def lambdaRequest_calculation(self,counter):
        usage_amount = self.workbook.cell(row=counter, column = config.usage_amount_column).value
        totalcost = usage_amount * self.invocationPrice
        writing_to_file(self.workbook,
                        counter,
                        self.invocationPrice,
                        totalcost,
                        "0.0000002 per Invocation price on OCI Function",
                        "Invocation",
                        "B90618")

    def process(self):
        counter = 1
        for row in range(self.workbook.max_row+1):
            counter+=1
            cell_obj = self.workbook.cell(row=counter,column= config.line_item_usage_type_column)
            # print(cell_obj.value)
            if cell_obj.value != None:
                usagetype = cell_obj.value
                usagetype_tolist = usagetype.lower().split('-')
            
            if 'gb' and 'second' in usagetype_tolist and 'storage' not in usagetype_tolist:
                # print(usagetype_tolist)
                self.lambdaCompute_calculation(counter)

            if 'request' in usagetype_tolist:
                self.lambdaRequest_calculation(counter)
            

