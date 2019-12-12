
from Image import *

# app starts from here
if __name__ == "__main__":
    ###run a script to pair the images and created spreadsheets

    ###give images a random ID
    #assignRandomID()
    
    ###save images info to hash map. because image pool will be huge, retrieve the images only when requested
    #mappingImageNodes()

    ### generated spreadsheet with the chosen pairing ways, and restore the generated sheets to disk
    #generateSpreadSheet(PAIRING_METHOD)
    #openImages("Test String")
    #generateImages_CSV()
    #onlineVerFromURL(100)
    
    ## use this to get all image files
    #downloadFromURL()

    file_array = [
        "exportedSelection_east.json",
        "exportedSelection_west.json",
        "exportedSelection_north.json",
        "exportedSelection_south.json",
        "exportedSelection_north_east.json",
        "exportedSelection_north_west.json",
        "exportedSelection_south_east.json",
        "exportedSelection_south_west.json",
        "exportedSelection_south_east_dense.json",
        "exportedSelection_south_east_loose.json"       
    ]

    
    for index_1 in range(len(file_array)):
        for index_2 in range(len(file_array)):
            if not (index_1 == index_2):
                selectImages("./json/", file_array[index_1], file_array[index_2], 200)
    


