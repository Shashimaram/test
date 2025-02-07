from utilities import writing_to_file
import config


class Sqs_cost_assesments():
    requests_cost = 0.22 # per million requests per month

    def __init__(self, workbook):
        self.workbook = workbook

    def sqs_request_calculation(self,counter):
        try:
            usage_amount = self.workbook.cell(row=counter, column = config.usage_amount_column).value
            totalcost = (usage_amount/1000000) * self.requests_cost
            writing_to_file(self.workbook,
                                counter,
                                self.requests_cost,
                                totalcost,
                                "0.22 per million requests on OCI QUEUE service",
                                "Requests")
        except Exception as e:
            print(f"error {e} at {counter}")
    

    def process(self):
         counter = 1
         for row in range(self.workbook.max_row+1):
            counter+=1
            cell_obj = self.workbook.cell(row=counter,column=config.line_item_usage_type_column)
            print(cell_obj.value)
            if cell_obj.value != None:
                usagetype = cell_obj.value
                usagetype_tolist = usagetype.lower().split('-')
            
            if 'requests' in usagetype_tolist:
                self.sqs_request_calculation(counter)