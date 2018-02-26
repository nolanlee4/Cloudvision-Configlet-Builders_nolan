excel-reader is a project that uses an excel cutsheet with device ID values in order to read an excel spreadsheet and create a CVP configlet from the information on the cutsheet


Required python libraries

pyexcel
pyexcel-xlsx

installing libraries on cvp

login as root

yum install -y epel-release
yum install -y python-pip
pip install pyexcel pyexcel-xlsx

upload the cutsheet.xlsx to the cvp server, and must give the cvp user permission to the file. chmod 777 cutsheet.xlsx

This is currently a work in progress. Right now the script works as a configlet builder with one form that accepts user input to identify the device being configured based on the systemId in the first column of the spreadsheet.

Currently, the script configures hostname, management ip, default route, but I am planning on extending to more. 
