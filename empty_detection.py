import csv
import os

def check_empty_file(folder, out_file_name):
    empty_list = []
    image_files = os.listdir(folder)
    
    for image in image_files:
        path = folder+str(image)
        #print(path)
        statinfo = os.stat(path)
        if(statinfo.st_size == 0):
            #print(path)
            empty_list.append(image)
    #print(image_files)

    #csv_name = out_file_name
    with open(out_file_name, mode='w', newline='') as csv_file:
        fieldnames = [
            "folder",
            "file_name"
            ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

            
        for file in empty_list:
            writer.writerow({
             "folder": folder,
             "file_name": file    
            })
            
        csv_file.close()        
    
    return empty_list
    
# app starts from here
if __name__ == "__main__":

    
    sub_folder_array = [
        "exportedSelection_east",
        "exportedSelection_north",
        "exportedSelection_north_east",
        "exportedSelection_north_west",
        "exportedSelection_south",
        "exportedSelection_south_east",
        "exportedSelection_south_east_dense",
        "exportedSelection_south_east_loose",
        "exportedSelection_south_west",
        "exportedSelection_west"
    ]

    folder_path = "./json/"
    out_path = folder_path.replace("./","")
    out_path = out_path.replace("/","_")
    for folder_path in sub_folder_array:
        empty_list = check_empty_file(folder_path + folder_path+"/", out_path + folder_path+"_empty.csv")
    
    