import os
import sys
import json
import csv

file= sys.argv[1]
single_file_name=os.path.basename(file)
json_file_name="../json/"+single_file_name+".json"

print(single_file_name)
with open(file,'r') as f:
    reader=csv.DictReader(f)
    list=[row for row in reader]

print ("reader")
with open(json_file_name,'w') as f:
    json.dump(list,f)

