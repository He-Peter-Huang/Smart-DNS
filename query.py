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
f=open('nameservers.txt') # open 'nameservers.txt' file
lines=f.readlines()		# convert file into list
domain=input("Domain:") # get domain input from user
command_mkdir="mkdir "+domain # create directory command
os.system(command_mkdir) #create directory
y = sum(1 for line in open('nameservers.txt')) # get file line number
x=0 # setting up loop
for x in range(0,y): #loop
	nameservers=lines[x] # get line from list
	dns = ''.join([line.strip() for line in nameservers]) # take a way \n
	command_query="dig @"+dns+" "+domain+" +short +tries=1 +time=3 >> "+domain+"/"+domain+".rawlist" # query domain --> ip command
	os.system(command_query) # query domain --> ip
	percentage= round(x/y*100,2) # calculate finished percentage
	percentage=str(percentage)+"%" # convert progress to string
	os.system("echo "+percentage+" > progress/"+domain+".progress") # write percentage to file
	x=x+1 # loop +1
command_uniq="sort "+domain+"/"+domain+".rawlist | uniq >> "+domain+"/"+domain+".uniqlist" # Take out duplicate ip command
os.system(command_uniq) # Take out duplicate ip
command_ipv4="grep  '^[\.[:digit:]]*$' <"+domain+"/"+domain+".uniqlist >>"+domain+"/"+domain+".ipv4" # Take out non ip text command
os.system(command_ipv4) # Take out non ip text
command_no_private_address="awk '!/^10./' "+domain+"/"+domain+".ipv4 | awk '!/^192.168/' | awk '!/^172.16/' | awk '!/^172.17/' | awk '!/^172.18/' | awk '!/^172.19/' | awk '!/^172.30/' | awk '!/^172.31/' | awk '!/^1.1.1.1/'| awk '!/^2.2.2.2/'| awk '!/^3.3.3.3/'| awk '!/^127.0.0/' >> domains/"+domain # Take out private address command
os.system(command_no_private_address) # Take out private address
command_no_private_address2="awk '!/^10./' "+domain+"/"+domain+".ipv4 | awk '!/^192.168/' | awk '!/^172.16/' | awk '!/^172.17/' | awk '!/^172.18/' | awk '!/^172.19/' | awk '!/^172.30/' | awk '!/^172.31/' | awk '!/^1.1.1.1/'| awk '!/^2.2.2.2/'| awk '!/^3.3.3.3/'| awk '!/^127.0.0/' >> domains/"+domain+"/"+domain # Take out private address command
os.system(command_no_private_address2) # Take out private address


# He (Peter) Huang