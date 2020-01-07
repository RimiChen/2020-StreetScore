import csv
import json


def summary_json(file_name, data):
    summary = {}
    
    for record in data:
        if record[file_name] not in summary:
            summary[record[file_name]] = 1
        else:
            summary[record[file_name]] = summary[record[file_name]] + 1
    
    json_file = open(str(file_name)+".json", "w")
    # magic happens here to make it pretty-printed
    json_file.write(json.dumps(summary, indent=4, sort_keys=True))
    json_file.close()    

def getAnswer(img_1, img_2, ans_1, ans_2):
    ans = ""
    
    #print(type(ans_1))
    #print(ans_2)
    if ans_1 == ("true" or "TRUE"):
        ans = img_1
    elif ans_2 == ("true" or "TRUE"):
        ans = img_2
        
    
    return ans
    
# app starts from here
if __name__ == "__main__":
    file_array = [
        "Batch_3871724_batch_results.csv"
    ]
    records = {}
    path_prefix = "./"
    
    pair_set = 5
    
    
    # create name array
    ans_list = []
    
    for name in file_array:
        with open(path_prefix + name) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            the_first = 0
            for row in readCSV:
                if the_first == 0:
                    # ignore this line
                    print(row)
                else:
                    #print(row[0])
                    #count = 0
                    #for cl in row:
                        #print("count "+str(count)+" :")
                        #print(cl)
                        
                        
                    #    count = count + 1
                    # if row[16] == "Rejected":
                    #     print("ignore this line")
                    if row[16] == "Approved":
                        
                        for pair in range(pair_set):
                            pair_img_1 = row[27+2*pair+0]
                            pair_img_2 = row[27+2*pair+1]
                            img_region_1 = ""
                            img_region_2 = ""
                            
                            q1_tag = "complete"
                            q1_1 = row[37+pair]
                            q1_2 = row[67+pair]
                            
                            q2_tag = "maintained"
                            q2_1 = row[42+pair]
                            q2_2 = row[72+pair]
                            
                            q3_tag = "newer"
                            q3_1 = row[47+pair]
                            q3_2 = row[77+pair]
                            
                            q4_tag = "occupied"
                            q4_1 = row[52+pair]
                            q4_2 = row[82+pair]
                            
                            q5_tag = "safer"
                            q5_1 = row[57+pair]
                            q5_2 = row[87+pair]
                            
                            q6_tag = "wealthier"
                            q6_1 = row[62+pair]
                            q6_2 = row[92+pair]
                            
                            new_answer = {}
                            new_answer["img_1"] = pair_img_1
                            new_answer["img_2"] = pair_img_2
                            new_answer["region_1"] = img_region_1
                            new_answer["region_2"] = img_region_2
                            
                            new_answer[q1_tag] = getAnswer(pair_img_1, pair_img_2, q1_1, q1_2)
                            new_answer[q2_tag] = getAnswer(pair_img_1, pair_img_2, q2_1, q2_2)
                            new_answer[q3_tag] = getAnswer(pair_img_1, pair_img_2, q3_1, q3_2)
                            new_answer[q4_tag] = getAnswer(pair_img_1, pair_img_2, q4_1, q4_2)
                            new_answer[q5_tag] = getAnswer(pair_img_1, pair_img_2, q5_1, q5_2)
                            new_answer[q6_tag] = getAnswer(pair_img_1, pair_img_2, q6_1, q6_2)
                            
                            ans_list.append(new_answer)
                            
                            
                the_first = the_first + 1
            csvfile.close()
        
        print(json.dumps(ans_list[0], indent=4, sort_keys=True))
        #print(json.dumps(name_array, indent=4, sort_keys=True))   
    
    # write out a json file for result
    # now write output to a file
    json_file = open("result.json", "w")
    # magic happens here to make it pretty-printed
    json_file.write(json.dumps(ans_list, indent=4, sort_keys=True))
    json_file.close()
    
    # get summary for result
    summary = {}
    
    name_arry = [
        q1_tag,
        q2_tag,
        q3_tag,
        q4_tag,
        q5_tag,
        q6_tag
    ]
    
    for name in name_arry:
        summary_json(name, ans_list)
    
    
    
    # csv_name = "out.csv"
    # with open(csv_name, mode='w', newline='') as csv_file:
    #     fieldnames = [
    #         "First name",
    #         "Last name",
    #         "Email address"
    #         ]
        
    #     for file in file_array:
    #         fieldnames.append(file)

    #     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
   
    #     writer.writeheader()

    #     for record in name_array:
    #         now_row = {}
    #         now_row["First name"] = name_array[record]["first_name"]
    #         now_row["Last name"] = name_array[record]["last_name"]
    #         now_row["Email address"] = record
            
    #         count = 0
    #         for file in file_array:
    #             now_row[file] = name_array[record]["attendance"][count]
    #             count = count + 1

    #         writer.writerow(now_row)        