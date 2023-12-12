# Problem #1
# 1. Check whether the given string input is a valid ip address.
# Find out what are the constraints for an ip address (how many chars, what numbers are allowed, how many '.'
# etc)
# Write all constraints.
# Get an input as string. Return if it is valid or not. 
# Use string functions.

s = '[@_!#$%^&*()<>?/\|}{~:]'
c=0
print("****************  Constraints for IP Address  *******************")
print(" The address consists of four decimal numbers separated by dots ")
print(" Each decimal number is between 0 and 255 ")
print(" 192.168.0.1 - Example of an IP Address")
ip_address = input("Enter IP address: ")
for i in range(len(ip_address)):
    if ip_address[i] in s:
        c+=1
if c:
    print("Invalid IP Address")   
else:   
    result = ip_address.split('.')
    print(result)
    if(len(result)<4):
        print("Invalid IP Address")
    for i in result:
        if(int(i)>0 and int(i)<255):
            continue
        else:
            print("Invalid IP Address")





