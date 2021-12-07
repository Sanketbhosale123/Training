import argparse
import re
import os
import subprocess
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
    #print(type(output))
    output = output.split('\n')
    output = output[0].split('\\n')
    #print(output)
    final_dict = {}
    temp_list = []
    key_list = []
    key = ''
    i = 1
    for line in output:
        line_match =re.search(key_regex,line)
             

        if line_match:
            #print(len(line_match.group()))
            key = line_match.group()
    key_list.extend(key.split())
    print(key_list)
    final_data = []
    final_data.append(key_list)

    for line in output:
        temp_list = []
        line_match = re.search(line_regex, line)


        for i in range(1,len(key_list)+1):
            #line_match = re.search(line_regex, line)
            if line_match:
                temp_list.append( line_match.group(i))
        #print(temp_list)

        #final_dict[key_list[i-1]] = temp_list
        if len(temp_list) != 0 : 
            final_data.append(temp_list)
        #temp_list = []
        #print(final_dict)
    return final_data
main = function()
print(main)

for i in main:
    print(" ".join(i))


