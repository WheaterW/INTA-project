Configuring ARP-Ping IP
=======================

ARP-Ping IP sends ARP packets onto a LAN to check whether an IP address is being used by another device on the LAN.

#### Procedure

1. Run [**arp-ping ip**](cmdqueryname=arp-ping+ip) *ip-host* [ **interface** { *interface-name* | *interface-type* *interface-number* } [ *vlan-id* *vlanId* ] ] [ **timeout** *timeout* ]
   
   
   
   ARP-Ping IP is enabled to check whether an IP address is being used by another device.

#### Result

There are two possible results after the command is run:

* If the IP address is not being used by another device, the command output is as follows:
  
  ```
  [*HUAWEI] arp-ping ip 10.1.1.2
  ```
  ```
   ARP-Pinging 10.1.1.2:
  
  Error: Request timed out
  Error: Request timed out
  Error: Request timed out
  
   The IP address is not used by anyone!
  ```
* If the IP address is being used by another device, the command output is as follows:
  
  ```
  [*HUAWEI] arp-ping ip 10.1.1.1
  ```
  ```
   ARP-Pinging 10.1.1.1:
  
  10.1.1.1 is used by 00e0-fc7d-f202      
  ```