#import pyexcel to read excel sheets
import pyexcel

#build dictionary of excel sheet
#my_array = pyexcel.get_array(file_name="testcsv.xlsx")
my_dict = pyexcel.get_dict(file_name="testcsv.xlsx")

# print '%s' % (my_array)

print my_dict
#define variables from keys of dictionary
systemId = my_dict['systemId']
ip_address = my_dict['ipAddress']
hostname = my_dict['hostname']
netmask = my_dict['Netmask']
gateway = my_dict['defaultGateway']
print
# print systemId[0]

#get user input from form, to be added
user_input = "test2"

device_index = systemId.index(user_input)

#print systemId[device_index]
print 'hostname %s' % (hostname[device_index])
print "!"
print "interface management 1"
print " ip address %s/%s" % (ip_address[device_index], netmask[device_index])
print "!"
print "ip route 0.0.0.0/0 %s" % gateway[device_index]