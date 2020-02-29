# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 22:41:48 2020

@author: xiaofei Wang
"""


import os
import json

#select from only one file
def select_temp(input_path,output_path):
    with open(input_path,"r") as f:
        for line in f:
            try:
                data = json.loads(line)
            except:
                data = {}
            if "payload" in data.keys():
                temp1 = json.loads(data["payload"])
                if "received" in temp1:
                    if temp1["received"] >= "2019-01-01T00:00:00" and temp1["received"] <= "2019-01-02T24:00:00":
                        with open(output_path,"a") as o_file:    #output to output_path
                            o_file.write(line)

#select from all the files in the root_path folder
def select(root_path,output_path):    
    for file in os.listdir(root_path):
        temp_file = "./cdlog.txt_2019_01_23_061607/" + file
        select_temp(temp_file,output_path)

root_path = "cdlog.txt_2019_01_23_061607"     
output_path_1 = "output.txt"
select(root_path,output_path_1)



















