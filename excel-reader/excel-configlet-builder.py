#!/usr/bin/env python
#
# Copyright (c) 2017, Arista Networks, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#   Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
#
#   Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
#
#   Neither the name of Arista Networks nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL ARISTA NETWORKS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
# IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#import pyexcel to read excel sheets
import pyexcel
from cvplibrary import Form
from cvplibrary import CVPGlobalVariables,GlobalVariableNames

#build dictionary of excel sheet
my_dict = pyexcel.get_dict(file_name="/opt/CVPfiles/cutsheet.xlsx")

#define variables from keys of dictionary
systemId = my_dict['systemId']
ip_address = my_dict['ipAddress']
hostname = my_dict['hostname']
netmask = my_dict['Netmask']
gateway = my_dict['defaultGateway']
print

#get user input from form
user_input = Form.getFieldById('systemId').getValue()

device_index = systemId.index(user_input)

#print systemId[device_index]
print 'hostname %s' % (hostname[device_index])
print "!"
print "interface management 1"
print " ip address %s/%s" % (ip_address[device_index], netmask[device_index])
print "!"
print "ip route 0.0.0.0/0 %s" % gateway[device_index]
