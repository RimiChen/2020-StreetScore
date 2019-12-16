
from Image import *
import math
from random import shuffle

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

    
    # file_array = [
    #     "exportedSelection_east.json",
    #     "exportedSelection_west.json",
    #     "exportedSelection_north.json",
    #     "exportedSelection_south.json",
    #     "exportedSelection_north_east.json",
    #     "exportedSelection_north_west.json",
    #     "exportedSelection_south_east.json",
    #     "exportedSelection_south_west.json",
    #     "exportedSelection_south_east_dense.json",
    #     "exportedSelection_south_east_loose.json"       
    # ]
    
    file_array = [
        "exportedSelection_north_east.json",
        "exportedSelection_south_east.json",
        "exportedSelection_north_west.json",
        "exportedSelection_south_west.json"      
                
    ]

    
    regions = {}
    
    duplicate_rate = 0.1
    filp_rate = 0.1
    total = 6000
    
    generated_total = math.floor((1-(duplicate_rate+filp_rate))*total)
    print("need total = "+str(total))
    print("generated total = "+str(generated_total))
    
    # x samples from a set, file_array length = k.  C(kx,2) = (1- (duplicate_rate + filp_rate))* total image pairs   
    
    k = len(file_array)
    #x = math.floor((-1+math.sqrt(1+4*2*generated_total/k/(k-1)))/2)
    x =1
    print("sample number = "+str(x))
    
    
    

    while (k)*(k-1)/2*(x+1)*x/2 < generated_total:
        x = x+1
    #x = x -1


    real_generated_total = (k)*(k-1)/2*(x+1)*x/2
    
    print("sample number = "+str(x))
    duplicate_total =  math.floor(duplicate_rate *  total)
    filp_total =   math.floor(filp_rate * total)
    
    while not (real_generated_total + filp_total + duplicate_total ==  total):
        if(real_generated_total + filp_total + duplicate_total> total):
            if filp_total >0:
                filp_total = filp_total - 1
            else:
                duplicate_total = duplicate_total -1
        elif(real_generated_total + filp_total + duplicate_total< total):
                    filp_total = filp_total + 1
            
    print("final generated total = "+str(real_generated_total))
    print("final duplicate total = "+str(duplicate_total))
    print("final filp total = "+str(filp_total))
    
    sample_count = 0
    for layer_i in file_array:
        #print(file_array)
        #print(layer_i)
        regions[layer_i] = getSampledImages("./json/", layer_i, x)
        sample_count = sample_count +1
            
    
    

    #print(json.dumps(regions, indent=4, sort_keys=True))
    
    image_result = []
    for layer_i in range(k):
        for layer_j in range(k):
            if(layer_i < layer_j):
                # print(str(layer_i)+", "+str(layer_j))
                result_pairs = getImagePairs_Iter(regions[file_array[layer_i]], regions[file_array[layer_j]])
                image_result.extend(result_pairs)
                #print(len(result_pairs))
                #print(json.dumps(result_pairs, indent=4, sort_keys=True))
                
                
    
    #print(len(image_result)) 
    
    final_pairs = finalizePairs(image_result, duplicate_total, filp_total)        
    #print(json.dumps(final_pairs, indent=4, sort_keys=True))                 
    
    #print(len(final_pairs))
    
    randomizePairs(final_pairs)
    shuffle(final_pairs)
    
    #print(json.dumps(final_pairs, indent=4, sort_keys=True))                 
    # for region in range(len(file_array)):
        # sample 
    
    # for index_1 in range(len(file_array)):
    #     for index_2 in range(len(file_array)):
    #         if not (index_1 == index_2) and index_1 < index_2:
    #             selectImages("./json/", file_array[index_1], file_array[index_2], 200)
    

    record_file = []
    file_count = 0
    for file in file_array:
        record_file.append(file_array[file_count].replace(".json", ".csv"))
        
        csv_name = record_file[file_count]
        with open(csv_name, mode='w', newline='') as csv_file:
            fieldnames = ['image_url']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()

            for image in range(len(regions[file_array[file_count]])):
                writer.writerow({'image_url': regions[file_array[file_count]][image]})
                
        file_count = file_count + 1
    
    
    
    csv_name = "out.csv"
    with open(csv_name, mode='w', newline='') as csv_file:
        print("Creating file " + csv_name)
        fieldnames = ['image_url', 'image_url_2']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()

        for image in range(len(final_pairs)):
            writer.writerow({'image_url': final_pairs[image]["img1"], 'image_url_2': final_pairs[image]["img2"]})        