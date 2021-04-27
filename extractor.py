#-------------------------------------------------------------------------------
"""
Pulls rasters from annoying folders
"""
#-------------------------------------------------------------------------------
import os
import arcpy

# set the workspaces
p_folder = r'I:\GGRD30\Lidar'
arcpy.env.workspace = r'I:\GGRD30\Lidar'
condit = '50'
################################################################################

def extractor(parent_folder, output_folder):
    # get all folders in the parent folder
    folders = os.listdir(parent_folder)
    # get the total number of folders
    total = len(folders)

    arcpy.SetProgressor("#", "finding the files ...")
    # initate the naming count
    count = 0


    # scan through each of the folders and list their rasters
    for folder in folders:
        arcpy.AddMessage(folder)
        arcpy.env.workspace = p_folder + '' + str(folder)
        raw_rast = arcpy.ListDatasets()
        rasters = []
        arcpy.AddMessage(raw_rast)

        
        #filter out all non-named rasters starting with be
        for rast in raw_rast:
            f2 = str(rast)[:1]
            if f2 == condit:
                rasters.append(rast)
            else:
                pass
        
        # set the progresor on how many rasters to process
        total = len(rasters)
        arcpy.SetProgressor('step', "Copying LAS Files: " + str(count), count, total, 1)

        # copy each of the rasters from the filtered list
        for raster in rasters:
            arcpy.CopyFeatures_management(raster, os.path.join(output_folder, str(count) + ".las"))
            count = count + 1
            arcpy.SetProgressorPosition(count)
            arcpy.SetProgressorLabel("Copying Las File: " + str(count))
            
################################################################################


def main(parent_folder, output_folder):
    arcpy.AddMessage("Starting")

    extractor(parent_folder, output_folder)

    arcpy.AddMessage("this shit actually worked")
################################################################################
if __name__ == '__main__':
    parent_folder = arcpy.GetParameterAsText(0)
    output_folder = arcpy.GetParameterAsText(1)

    if 0 == 1:
        arcpy.AddMessage("Do you like endless loops or something? Use different folders!")
        pass
    else:
        main(parent_folder, output_folder)
