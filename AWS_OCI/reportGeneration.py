import json
# import pandas as pd

class ReportGenerating:
    def __init__(self, workbook,reportsheet):
        self.workbook = workbook
        self.jsonReport = {}
        self.reportsheet = reportsheet

    # jsonReport = {}
    columnValueTracker = []

    def calculatingTotals(self):
        try:
            rowNumber = 1
            for i in range(1, self.workbook.max_row + 1):
                rowNumber += 1
                columnValue = self.workbook.cell(row=rowNumber, column=13).value

                if columnValue is not None:
                    awsCost = self.workbook.cell(row=rowNumber, column=9).value
                    usageAmount = self.workbook.cell(row=rowNumber, column=8).value
                    usageAmountUnit = self.workbook.cell(row=rowNumber, column=7).value
                    ociCost = self.workbook.cell(row=rowNumber, column=11).value
                    ociUnitCost = self.workbook.cell(row=rowNumber, column=10).value

                    if columnValue in self.columnValueTracker:
                        self.jsonReport[columnValue]["awsCost"] += awsCost
                        self.jsonReport[columnValue]["ociCost"] += ociCost
                        if usageAmountUnit in self.jsonReport[columnValue]["usageAmount"]:
                            self.jsonReport[columnValue]["usageAmount"][usageAmountUnit] += usageAmount
                        else:
                            self.jsonReport[columnValue]["usageAmount"][usageAmountUnit] = usageAmount
                    else:
                        self.jsonReport[columnValue] = {
                            "awsCost": awsCost,
                            "usageAmount": {usageAmountUnit: usageAmount},
                            "ociCost": ociCost,
                            "ociUnitCost": ociUnitCost,
                        }
                        self.columnValueTracker.append(columnValue)

        except Exception as e:
            print(f"counter : {rowNumber}")
        
        print(self.jsonReport)
        rowNumber = 1
        for key, value in self.jsonReport.items():
            # print(f" {key}   :   {value}")
            self.reportsheet.cell(row=1, column=2).value = "awsCost"
            self.reportsheet.cell(row=1, column=3).value = "ociCost"
            self.reportsheet.cell(row=1, column=4).value = "ociUnitCost"
            rowNumber +=1
            self.reportsheet.cell(row=rowNumber, column=1).value = key

            if isinstance(value,dict):
                for i_key,i_value in value.items():
                    # print(f" {i_key}   :   {i_value}")
                    if i_key == "awsCost":
                        self.reportsheet.cell(row=rowNumber, column=2).value = i_value
                    elif i_key == "ociCost":
                        self.reportsheet.cell(row=rowNumber, column=3).value = i_value
                    elif i_key == "ociUnitCost":
                        self.reportsheet.cell(row=rowNumber, column=4).value = i_value
                    elif i_key == "usageAmount":
                        print(i_value)
                        columnNumber = 5
                        for usageUnit, usageAmount in i_value.items():
                            # print(f" {usageUnit}   :   {usageAmount}")
                            self.reportsheet.cell(row=rowNumber, column=columnNumber).value = f"{usageUnit} : {usageAmount}"
                            columnNumber += 1



                            








            # print(key)
            # self.reportsheet.cell(row=rowNumber, column=["awsCost"]).value = value[awsCost]
            # self.reportsheet.cell(row=rowNumber, column=["ociCost"]).value = value[ociCost]
            # self.reportsheet.cell(row=rowNumber, column=["ociUnitCost"]).value = value[ociUnitCost]
            # print(value)

            






            # column_number = 2
            # for key, value in self.jsonReport.items():
            #     if isinstance(value, dict):
            #         for usage_type, usage_value in value.items():
            #             self.reportsheet.cell(row=rowNumber, column=column_number).value = usage_type
            #             column_number += 1
            #             self.reportsheet.cell(row=rowNumber, column=column_number).value = usage_value
            #             column_number += 1
            #     else:
            #         self.reportsheet.cell(row=rowNumber, column=column_number).value = value
            #         column_number += 1
        
        # print(self.reportsheet.cell(row = 1,column = 1).value)