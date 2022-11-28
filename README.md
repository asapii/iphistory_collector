![title](image/title.png "")

## Overview
IP_History_Collector is a tool to inspect historical IP Address each NetworkInterfaces.
In the case of IPv4 Interfaces, collect past IPv4 Private IP Address.
For IPv6 Interfaces, it collects almost all types of addresses, including Global Unicast Addresses.

## How it works
 1. Parse WMILogfile "Lwtnetlog.etl" with netsh.
 2. Exclude Global IPv4 Address Log.(Usually loged global IP Address to check NCSI)
 3. Output to csv.

## Requirement
Windows10

## Usage
 Download and execute iphistory_collector.exe with Administrator privilege.
 Automatically created output folder and csv.
 If you need more information, look at lwtnetlog.txt in output folder.
