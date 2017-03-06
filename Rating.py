###############################
###############################
### Author: He(Peter) Huang ###
###############################
######### First Edit: #########
######## March 5, 2017 ########
###############################
######### Last Edit: ##########
######## March 6, 2017 ########
###############################
###############################

import os # import os module
import re # import re module
file_name='www.baidu.com' # set file name
domain=file_name # set domain name
f=open(file_name) # open file
lines=f.readlines() # read file
y = sum(1 for line in open(file_name)) # read file line number
non_decimal = re.compile(r'[^\d.]+') # set up strip non_decimal

x=0 # set up loop
for x in range(0,y): # for loop
	ip_address=lines[x] # set ip address to line number
	ip_address = ''.join([line.strip() for line in ip_address]) # strip ip address
	command_wget_load_time="curl -o /dev/null -s -w %{time_total}\\n --connect-timeout 2 -H 'Host:"+domain+"' http://"+ip_address # Wget time command
	wget_load_time=os.popen(command_wget_load_time).read() # Wget time
	wget_load_time=float(non_decimal.sub('', wget_load_time)) # Strip + Float Wget Time
	command_ping_latency_time="ping -c 2 -W 0 "+ip_address+" | tail -1| awk '{print $4}' | cut -d '/' -f 2" # Ping delay command
	ping_latency_time=os.popen(command_ping_latency_time).read() # Ping delay
	ping_latency_time=float(non_decimal.sub('', ping_latency_time)) # Strip + Float Ping delay
	if (ping_latency_time==0): # If time out
		ping_latency_time=9999 # Add 9999 to delay to be significant
	rating=round((wget_load_time*100+ping_latency_time)/2,3) # Rating 
	os.system('echo '+str(rating)+'\t'+ip_address+' >> '+domain+'.raw.rating') # Write Rating and IP address to file
	percentage= round(x/y*100,2) # Calculate Percentage finished
	percentage=str(percentage)+"%" # Converting to string and add %
	os.system("echo "+percentage+" > progress/"+domain+".progress") # Write Percentage Finished
	x=x+1 # Loop +1
command_sort="sort -g "+domain+".raw.rating >> "+domain+".sorted.rating" # Sort servers Best --> Worst command
os.system(command_sort) # Sort servers Best --> Worst
command_no_time="grep -oE '((1?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.){3}(1?[0-9][0-9]?|2[0-4][0-9]|25[0-5])' "+domain+".sorted.rating >> "+domain+".rating" # Take out rating and leave ip command
os.system(command_no_time) # Take out rating and leave ip command

## He (Peter) Huang