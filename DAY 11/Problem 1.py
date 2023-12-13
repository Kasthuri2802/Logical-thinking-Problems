# Problem #1
# 1. Check whether the given string input is a valid ip address.
# Find out what are the constraints for an ip address (how many chars, what numbers are allowed, how many '.'
# etc)
# Write all constraints.
# Get an input as string. Return if it is valid or not. 
# Use string functions.


print("****************  Constraints for IP Address  *******************")
print(" The address consists of four decimal numbers separated by dots ")
print(" Each decimal number is between 0 and 255 ")
print(" 192.168.0.1 - Example of an IP Address")

def valid_IP_address(s):  

    # check number of periods  
    if s.count('.') != 3:  
        return 'Invalid IP address'

    # check for any special characters    
    specialChar = '[@_!#$%^&*()<>?/\|}{~:]'
    for i in range(len(s)):
        if s[i] in specialChar:
            return 'Invalid IP address'
    
    ip_list = s.split('.')  
   
    # check range of each number between periods  
    for element in ip_list:  
        if int(element) < 0 or int(element) > 255 or (element[0]=='0' and len(element)!=1):  
            return 'Invalid IP address'  
   
    return 'Valid IP address'  
   
ip_address = input("Enter IP address: ")
print(valid_IP_address(ip_address))  



