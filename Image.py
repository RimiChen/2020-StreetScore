from os import walk
import glob
import random
import csv
import requests
import wget
#import requests
#pillow
from PIL import Image
import csv
import json
from collections import namedtuple
from random import randrange
from random import shuffle


# class ImageNode(object):
# 	def __init__(self, FolderPath, ImageName):
# 		self.ImageID = ImageName
#         self.ImagePath = FolderPath +ImageName

def openImages(FolderPath):
    print(FolderPath)


    # load all images from the folder
    index_ID_Table ={}
    folderPath = "D:\Github\ResearchCodes\StreetScore\ImagePairingScripts\\testImages_COCO_160\\"
    prefix = folderPath
    txtfiles = []

    fileCount = 0
    for file in glob.glob(prefix+"*"):
        
        fileString = file
        splitBuffer = fileString.split("\\")
        fileID = splitBuffer[-1].replace(".jpg","")
        
        txtfiles.append(fileID)
        ### Debug and test
        #print(fileID)

        # use the images file name as the name and create ImageNode, save it to hash
        # mapping indeices/ ImageID
        index_ID_Table[fileCount] = fileID
        fileCount = fileCount + 1
        # mapping ImageID/ ImageNode

    # generate image pairs and save to spreadsheet
    imagePairs = []
    numberPairs = 5

    for index in range(numberPairs):
        chosenImage_1 = index_ID_Table[random.randint(1,len(index_ID_Table))]
        chosenImage_2 = chosenImage_1 
        while chosenImage_2 == chosenImage_1:
            chosenImage_2 = index_ID_Table[random.randint(1,len(index_ID_Table))]
            break
        newSet = set([chosenImage_1, chosenImage_2])
        imagePairs.append(newSet)

        tempImage = Image.open(prefix+chosenImage_1+".jpg")
        tempImage.show()


        
    ### Debug and test
    #print(index_ID_Table)
    print(imagePairs)

def generateImages_CSV():
    #load csv
    #create a dictionary to save the images with index
    #generate random pairs (index1, index2)
    #write to output.csv with variable:  
    sampleLink = "https://drive.google.com/file/d/18HxgxoQikLznp4OoiwD9iCH-shnTtaUB/view?usp=sharing"
    sampleLink = getImageDirectLink(sampleLink)

    with open('./image.csv', newline='') as csvfile:
        data = list(csv.reader(csvfile))

    #print(data)

    imageLinks = []
    for link in data:
        imageLinks.append(getImageDirectLink(link[0]))
        #print("\n"+imageLinks[-1])

    imagePairs = []
    numberPairs = 100


    with open('output.csv', mode='w', newline='') as csv_file:
        fieldnames = ['image_url', 'image_url_2']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for index in range(numberPairs):
            chosenImage_1 = imageLinks[random.randint(0,len(imageLinks)-1)]
            chosenImage_2 = chosenImage_1 
            while chosenImage_2 == chosenImage_1:
                chosenImage_2 = imageLinks[random.randint(0,len(imageLinks)-1)]
                break
            writer.writerow({'image_url': chosenImage_1, 'image_url_2': chosenImage_2})
    #print(sampleLink)

def getImageDirectLink(oldLink):
    newLinkPrefix = "https://drive.google.com/uc?id="
    newLink = oldLink.replace("https://drive.google.com/file/d/","")
    newLink = newLink.replace("/view?usp=sharing","")
    newLink = newLinkPrefix+newLink
    #print(newLink)
  
    return newLink
def downloadFromURL(file_array):
    # load json files
    # exportedSelection_east
    # exportedSelection_west
    # exportedSelection_north
    # exportedSelection_south
    # exportedSelection_north_east
    # exportedSelection_north_west
    # exportedSelection_south_east
    # exportedSelection_south_west
    # exportedSelection_south_east_dense
    # exportedSelection_south_east_scater
    
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
    #     "exportedSelection_south_east_scater.json"       
    # ]
    
    file_prefix = "./json/"
    
    image_prefix = " http://10.76.80.20:8080/"
    
    i = 0
    
    for i in range(len(file_array)):
        print(file_array[i])
        file_name = file_prefix + file_array[i]
        print("Now file = "+file_name)
        
        image_data = {}
        
        with open(file_name) as json_file:
                json_data = json.load(json_file)
                # create a folder to save images
                
                
                for data in json_data:
                    image_address = image_prefix +data["image"].replace("..","")
                    print(image_address)
                    image_data[data["id"]] = image_address
                    image_format = data["image"].replace("..","").split("/")
                    
                    image_file = requests.get(image_address)
                    open("D:\Github\StreetScore\json\\"+file_array[i].replace(".json","")+"\\"+image_format[-1], 'wb').write(image_file.content)


                    # print(image_format[-1])
                    
                    
                    #print("D:\Github\ResearchCodes\StreetScore\ImagePairingScripts\json\\"+file_array[0].replace(".json","")+"\\"+image_format[-1])
                    #wget.download(image_address, "D:\Github\ResearchCodes\StreetScore\ImagePairingScripts\json\\"+file_array[0].replace(".json","")+"\\"+image_format[-1])
                    
                    #print(data)
                    #print(mail)
                    #data["path"] = presepective_prefic+data["hashDir"]+"/"+data["hashid"]
                    #image_data[data["objectid"]] = data
                    #print(json.dumps(image_data, indent=4, sort_keys=True))
        json_file.close()    
            
        
    
    
    
    
def onlineVerFromURL(number_pairs):
    print("from the online json file to get data")
    #http://10.152.9.249/up/media/raleigh/ps/   <hashdir> / <hashid>.jpg 
    prefix = "http://10.76.80.20/up/media/raleigh/ps/"
    #http://10.152.9.249/up/media/raleigh/ps_pers/  <hashdir> / <hashid>_0.jpg , _1.jpg , _2.jpg , _3.jpg 
    presepective_prefic = "http://10.76.80.20/up/media/raleigh/ps_pers/"
    
    json_file_online = "http://10.76.80.20/up/media/raleigh/raleigh_data.json"
    json_file_offline = "./raleigh_data.json"

    ## use offline first
    #{"sourceid": "3yxuQPKXuOIe9ZD6gRnucA", "hashid": "olejRejN", "hashDir": "jnegYbwZ", "objectid": 1}
    image_data = {}
    with open('raleigh_data.json') as json_file:
            json_data = json.load(json_file)
            for data in json_data:
                #print(mail)
                data["path"] = presepective_prefic+data["hashDir"]+"/"+data["hashid"]
                image_data[data["objectid"]] = data
                #print(json.dumps(image_data, indent=4, sort_keys=True))
    json_file.close()


    with open('output_url.csv', mode='w', newline='') as csv_file:
        fieldnames = ['image_url', 'image_url_2']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
    
        for i in range(number_pairs):
            random_two = randrange(2)
            #print(random_two)
            #print(random.choice(list(image_data)))
            index_1 = random.choice(list(image_data))
            index_2 = random.choice(list(image_data))
            while index_1 == index_2:
                index_2 = random.choice(list(image_data))
                
                
            if random_two == 0:
                postfix = "_1.jpg"
                imgae_1_path = image_data[index_1]["path"]+postfix
                imgae_2_path = image_data[index_2]["path"]+postfix
            else:
                postfix = "_3.jpg"
                imgae_1_path = image_data[index_1]["path"]+postfix
                imgae_2_path = image_data[index_2]["path"]+postfix
            
            writer.writerow({'image_url': imgae_1_path, 'image_url_2': imgae_2_path})
    
    csv_file.close()
    
    # read json file
    # combine prefix with hashdir/ hasdid  for loop
    # loop to generate number of pairing images
    print("We need "+str(number_pairs))
    
    
def offlineVerFromURL():
    print("from local file to get the key and values")

def getImagePairs_Iter(file_1, file_2):
    image_pairs = []
    x_1 = len(file_1)
    x_2 = len(file_2)
    
    #x_1 = 3
    #x_2 = 3
    for i in range(x_1):
        for j in range(x_2):
            if(i <= j):
                new_pair = {"img1":file_1[i], "img2":file_2[j]}
                #new_pair = {"img1":i, "img2":j}
                image_pairs.append(new_pair)
                
    return image_pairs
                

def getSampledImages(prefix, fileName, number):
    webprefix = "https://rimichen.github.io/StreetScore/"
    dict_1 = []
    image_samples = []
    new_file_name =  prefix + fileName
    new_prefix = prefix.replace("./","")+ fileName.replace(".json", "")+"/"  
 
    with open(new_file_name) as json_file:
            json_data = json.load(json_file)
            # create a folder to save images
            
            for data in json_data:
                image_format = data["image"].replace("..","").split("/")
                image_address = fileName +image_format[-1]
                #print(image_address)
                web_image = webprefix+new_prefix+image_format[-1]
                dict_1.append(web_image)
                #print(web_image)
    json_file.close() 
    
    
    for index in range(number):
        image_samples.append(random.choice(list(dict_1)))
    
    
    return image_samples      
    
def finalizePairs(final, duplicate_number, filp_number):
    #print(len(final))
    #print(duplicate_number)
    #print(filp_number)
    new_pairs = []
    
    for i in range(duplicate_number):
        target_pair = random.choice(final)
        new_pair = target_pair
        new_pairs.append(new_pair)
        
    #print(len(new_pairs))    
    for j in range(filp_number):
        target_pair = random.choice(final)
        new_pair = {"img1": target_pair["img2"], "img2": target_pair["img1"]}
        new_pairs.append(new_pair)
        
    
    #print(len(new_pairs))
    new_pairs.extend(final)
    
    return new_pairs
    
    
def randomizePairs(final):
    new_final = shuffle(final)
    
    return new_final
    

def selectImages(prefix, cate_1, cate_2, number):
    print("Sampling and generate ") 
    
    webprefix = "https://rimichen.github.io/StreetScore/"

    
    dict_1 = []
    dict_2 = []
    
    json_file_path_1 = prefix + cate_1
    json_file_path_2 = prefix + cate_2
    image_folder_path_1 = prefix + cate_1.replace(".json", "")+"/"
    image_folder_path_2 = prefix + cate_2.replace(".json", "")+"/"
    
    print(json_file_path_1)
    print(json_file_path_2)
    print(image_folder_path_1)
    print(image_folder_path_2)
    
    new_prefix = prefix.replace("./","")+cate_1.replace(".json", "")+"/"    
    with open(json_file_path_1) as json_file:
            json_data = json.load(json_file)
            # create a folder to save images
            
            
            for data in json_data:
                image_format = data["image"].replace("..","").split("/")
                image_address = image_folder_path_1 +image_format[-1]
                #print(image_address)
                web_image = webprefix+new_prefix+image_format[-1]
                dict_1.append(web_image)
                #print(web_image)
    json_file.close()        

    new_prefix = prefix.replace("./","")+cate_2.replace(".json", "")+"/"
    with open(json_file_path_2) as json_file:
            json_data = json.load(json_file)
            # create a folder to save images
            
            
            for data in json_data:
                image_format = data["image"].replace("..","").split("/")
                image_address = image_folder_path_2 +image_format[-1]
                #print(image_address)
                web_image = webprefix+new_prefix+image_format[-1]
                dict_2.append(web_image)
                #print(web_image)
    json_file.close()        
    
      
    csv_name = cate_1.replace(".csv", "")+"_"+cate_2.replace(".csv", "")+".csv"
    with open(csv_name, mode='w', newline='') as csv_file:
        print("Creating file " + csv_name)
        fieldnames = ['image_url', 'image_url_2']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for index in range(number):
            chosenImage_1 = dict_1[random.randint(0,len(dict_1)-1)]
            chosenImage_2 = dict_2[random.randint(0,len(dict_2)-1)]
            writer.writerow({'image_url': chosenImage_1, 'image_url_2': chosenImage_2})
    