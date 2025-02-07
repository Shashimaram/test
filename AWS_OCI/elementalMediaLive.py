from utilities import writing_to_file
import config



class ElementalMediaLive():
    
    def __init__(self,workbook):
        self.workbook = workbook
        
    
    # Standard HD
    standard_h264_hd_below_30fps = {'hd', 'l10', '30'}
    standard_h264_hd_below_30fps_avc = {'out', 'avc', 'hd', '30'}
    standard_h264_hd_below_30fps_in = {'in', 'avc', 'hd'}
    standard_h264_hd_above_30fps_and_below_60fps = {'hd', 'l10', '60'}
    standard_h264_hd_above_30fps_and_below_60fps_avc = {'out', 'avc', 'hd', '60'}
    # standard_h264_hd_above_30fps_and_below_60fps_in = {'in', 'avc', 'hd', 'l10'}

    # Standard SD
    standard_h264_sd_below_30fps = {'sd', 'l10', '30'}
    standard_h264_sd_below_30fps_avc = {'out', 'avc', 'sd', '30'}   
    standard_h264_sd_above_30fps_and_below_60fps = {'sd', 'l10', '60'}
    standard_h264_sd_above_30fps_and_below_60fps_avc = {'out', 'avc', 'sd', '60'}
    standard_h264_sd_above_30fps_and_below_60fps_in = {'in', 'avc', 'sd', 'l10'}
    
    # Standard - H264 - 4k 
    standard_h264_4k_below_30fps = {"uhd",'30','s','avc'}
    standard_h264_4k_below_30fps_in = {'in', 'avc', 'uhd',}
    
    
    
    # Audio
    out_avc_audio = {'out', 'audio'}
    in_avc_audio = {'in', 'audio'}

    # DTS
    out_avc_dts = {'out', 'dts'}
    in_avc_dts = {'in', 'dts'}

    # Idle
    out_avc_idle = {'out', 'idle'}
    in_avc_idle = {'in', 'idle'}

    
    def process(self):
        counter = 0
        for row in range(self.workbook.max_row+1):
            counter+=1
            cell_obj = self.workbook.cell(row=counter,column=config.line_item_usage_type_column)
            if cell_obj.value != None:
                usagetype = cell_obj.value
                usagetype_tolist = usagetype.lower().split('-')
                usageAmount =   self.workbook.cell(row=counter,column=config.usage_amount_column).value
                
                if ((self.standard_h264_hd_below_30fps.issubset(usagetype_tolist) or 
                     self.standard_h264_hd_below_30fps_avc.issubset(usagetype_tolist)) and 
                    ('s' in usagetype_tolist or 'e' in usagetype_tolist)):
                    totalCost = usageAmount * config.Standard_H264_HD_Below_30fps
                    writing_to_file(self.workbook, counter, config.Standard_H264_HD_Below_30fps, totalCost, "OCI Media Flow", "Standard_H264_HD_Below_30fps")
                    
                elif (self.standard_h264_hd_above_30fps_and_below_60fps.issubset(usagetype_tolist) or self.standard_h264_hd_above_30fps_and_below_60fps_avc.issubset(usagetype_tolist) and ('s' in usagetype_tolist or 'e' in usagetype_tolist)):
                    totalCost = usageAmount * config.Standard_H264_HD_Above_30fps_and_Below_60fp
                    writing_to_file(self.workbook, counter, config.Standard_H264_HD_Above_30fps_and_Below_60fp, totalCost, "OCI Media Flow", "Standard_H264_HD_Above_30fps_and_Below_60fp")

                elif (self. standard_h264_sd_below_30fps.issubset(usagetype_tolist) or self.standard_h264_sd_below_30fps_avc.issubset(usagetype_tolist) and ('s' in usagetype_tolist or 'e' in usagetype_tolist)):
                    totalCost = usageAmount * config.Standard_H264_SD_Below_30fps
                    writing_to_file(self.workbook, counter, config.Standard_H264_SD_Below_30fps, totalCost, "OCI Media Flow", "standard_h264_sd_below_30fps")

                elif (self.standard_h264_sd_above_30fps_and_below_60fps.issubset(usagetype_tolist) or self.standard_h264_sd_above_30fps_and_below_60fps_avc.issubset(usagetype_tolist) and ('s' in usagetype_tolist or 'e' in usagetype_tolist)):
                    totalCost = usageAmount * config.Standard_H264_SD_Above_30fps_Below_60fps
                    writing_to_file(self.workbook, counter, config.Standard_H264_SD_Above_30fps_Below_60fps, totalCost, "OCI Media Flow", "standard_h264_sd_above_30fps_and_below_60fps")

                elif self.out_avc_audio.issubset(usagetype_tolist):
                    writing_to_file(self.workbook, counter, 0, 0, "OCI Media Flow", "NO Saperate pipelines for AUDIO")

                elif self.in_avc_audio.issubset(usagetype_tolist):
                    writing_to_file(self.workbook, counter, 0, 0, "OCI Media Flow", "NO Saperate pipelines for AUDIO")   

                elif self.out_avc_dts.issubset(usagetype_tolist):
                    writing_to_file(self.workbook, counter, 0, 0, "OCI Media Flow", "NO Saperate pipelines for DTS")

                elif self.in_avc_dts.issubset(usagetype_tolist):
                    writing_to_file(self.workbook, counter, 0, 0, "OCI Media Flow", "NO Saperate pipelines for DTS")
                
                elif 'dolby' in usagetype_tolist:
                    writing_to_file(self.workbook, counter, 0, 0, "OCI Media Flow", "NO Saperate pipelines for DOLBY")

                elif self.in_avc_idle.issubset(usagetype_tolist):
                     writing_to_file(self.workbook, counter, 0, 0, "OCI Media Flow", "NO Charges for IN IDLE")
                     
                elif self.out_avc_idle.issubset(usagetype_tolist):
                     writing_to_file(self.workbook, counter, 0, 0, "OCI Media Flow", "NO Charges for OUT IDLE")
#                 elif "idle" in usagetype_tolist:  # catch any other idle cases
                elif self.standard_h264_hd_below_30fps_in.issubset(usagetype_tolist):
                    totalCost = usageAmount * config.Standard_H264_HD_Below_30fps
                    writing_to_file(self.workbook, counter, config.Standard_H264_HD_Below_30fps, totalCost, "OCI Media Flow", "Standard_H264_HD_Below_30fps")

                elif self.standard_h264_4k_below_30fps.issubset(usagetype_tolist) or self.standard_h264_4k_below_30fps_in.issubset(usagetype_tolist):
                    totalCost = usageAmount * config.Standard_H264_4k_Below_30fps
                    writing_to_file(self.workbook, counter, config.Standard_H264_4k_Below_30fps, totalCost, "OCI Media Flow", "Standard_H264_4k_Below_30fps")
                else:
                    print(usagetype_tolist,counter)

# #                     # Handle AVC input usage typ