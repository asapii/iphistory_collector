![title](image/title.png "")

## Overview
IP_History_Collector is a tool to inspect historical IP Address each NetworkInterfaces.  
For IPv4 Interfaces, collect past Private IPv4 Address.  
In the case of IPv6 Interfaces, collect all types of addresses, including Global Unicast Address.


## Requirement
Windows10
（Windows11 has not been verified)

## Usage
 Download contents and execute iphistory_collector.exe with Administrator privilege.  
 Then automatically create output folder and csv.  
 If you need more information, look at lwtnetlog.txt in output folder.  
 The tool analyzes wmi log file, but the log file will be refreshed when shutdown or reboot.
