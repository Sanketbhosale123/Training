import argparse
import re
import os
import subprocess
import pandas as pd
my_parser = argparse.ArgumentParser(description='To parse the arguement and to fetch the output')
my_parser.add_argument('--cmd',               
                        required = True,
                       type = str,
                       help='use --cmd command argument')
line_regex = r'(\d+)\s(\S+)\s+(\S+)\s(\S+)'
key_regex = r'(\w+)\s+(\w+)\s+(\s+\s+\s+\s+\s+\s+\s+\s)\s+(\w+)\s+(\w+)'
args = my_parser.parse_args()
input_arg = args.cmd
def function ():
    temp = subprocess.Popen([input_arg],stdout = subprocess.PIPE)
    output = str (temp.communicate())
    output = output.split('\n')
    output = output[0].split('\\n')
    final_dict = {}
    temp_list = []
    key_list = []
    key = ''
    i = 1
    for line in output:
        line_match =re.search(key_regex,line)
             

        if line_match:
        
            key = line_match.group()
    key_list.extend(key.split())
    print(key_list)
    final_data = []
    final_data.append(key_list)

    for line in output:
        temp_list = []
        line_match = re.search(line_regex, line)


        for i in range(1,len(key_list)+1):

            if line_match:
                temp_list.append( line_match.group(i))
    
        if len(temp_list) != 0 : 
            final_data.append(temp_list)
    return final_data
main = function()
print(main)
df = pd.DataFrame(main[1:],columns = main[0])
print(df)
df.dropna(axis = 0,how = 'all')


