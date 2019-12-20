import csv
import os
import json
import requests

def redownload(csv_file, image_prefix, save_path):
    #print("re-download bad files")
    #print(csv_file)
    
    # create name array
    download_list = []
    with open(csv_file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        the_first = 0
        for row in readCSV:
            if the_first == 0:
                # ignore this line
                print(row)
            else:
                new_node = {
                    "folder": row[0],
                    "file_name": row[1],
                }
                download_list.append(new_node)
                #name_array[row[2]] = new_node
            the_first = the_first + 1
            #print(row[0])
        csvfile.close()
        
    for image in download_list:
        #print(image)
        #print(image["file_name"])
        download_path = image_prefix + image["file_name"]
        image_file = requests.get(download_path)
        print("D:\Github\StreetScore\json\\"+save_path+"\\"+ image["file_name"])
        open("D:\Github\StreetScore\json\\"+save_path+"\\"+ image["file_name"], 'wb').write(image_file.content)
        
            
    
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
    
    record_empty = {}
    
    for file_path in sub_folder_array:
        empty_list = check_empty_file(folder_path + file_path+"/", out_path + file_path+"_empty.csv")
        record_empty[file_path]  = out_path + file_path+"_empty.csv"
    
    
    print(json.dumps(record_empty, indent=4, sort_keys=True))
    #http://10.76.80.20:8080//data/100x100/buildings_thumbs_256/YerYP2dO.jpg
    image_prefix = "http://10.76.80.20:8080//data/100x100/buildings_thumbs_256/"
    
    for bak_folder in record_empty:
        save_path = bak_folder+"_bak"
        redownload("./"+record_empty[bak_folder], image_prefix, save_path)