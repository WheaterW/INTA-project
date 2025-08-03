display ipv6 nd anti-attack rate-limit configuration
====================================================

display ipv6 nd anti-attack rate-limit configuration

Function
--------



The **display ipv6 nd anti-attack rate-limit configuration** command displays the configuration values of nd anti-attack rate limits.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 nd anti-attack rate-limit configuration**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to check the configuration of the rate at which ND messages are sent. You can adjust the rate to a proper range as required.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configuration values of ND anti-attack rate limit.
```
<HUAWEI> display ipv6 nd anti-attack rate-limit configuration
ND rate-limit for VS Global configuration:
----------------------------------------------------------------------------------
Packet-Type    rate(pps)                                          
----------------------------------------------------------------------------------
NS             550     
NA             550     
RS             550     
RA             550     
NDMISS         550     
----------------------------------------------------------------------------------

ND rate-limit for LS Global configuration:
----------------------------------------------------------------------------------
Packet-Type    rate(pps)                                          
----------------------------------------------------------------------------------
NS             5000    
NA             5000    
RS             5000    
RA             5000    
NDMISS         5000    
----------------------------------------------------------------------------------

ND rate-limit for exact source mac configuration:
----------------------------------------------------------------------------------
Packet-Type    MAC-address         rate(pps)                                      
----------------------------------------------------------------------------------
NA             00e0-fc12-3456      550     
----------------------------------------------------------------------------------
Total: 1       

ND rate-limit for every source mac configuration:
----------------------------------------------------------------------------------
Packet-Type    rate(pps)                                          
----------------------------------------------------------------------------------
RS             550     
RA             550     
NS             550     
NA             550     
----------------------------------------------------------------------------------

ND rate-limit for exact source ip configuration:
----------------------------------------------------------------------------------
Packet-Type    IPv6-address                                    rate(pps)          
----------------------------------------------------------------------------------
RS             2001:DB8:1::1                                   550     
----------------------------------------------------------------------------------
Total: 1       

ND rate-limit for every source ip configuration:
----------------------------------------------------------------------------------
Packet-Type    rate(pps)                                          
----------------------------------------------------------------------------------
RS             550     
RA             550     
NS             550     
NA             550     
NDMISS         550       
----------------------------------------------------------------------------------

ND rate-limit for interface exact source ip configuration:
----------------------------------------------------------------------------------
Interface                   Packet-Type  IPv6-address                 rate(pps)   
----------------------------------------------------------------------------------
100GE1/0/1                  NS           2001:DB8:1::1                550     
----------------------------------------------------------------------------------
Total: 1       

ND rate-limit for interface configuration:
----------------------------------------------------------------------------------
Interface                   Packet-Type  rate(pps)                                
----------------------------------------------------------------------------------
100GE1/0/1                  NDMISS       550     
----------------------------------------------------------------------------------
Total: 1       

ND rate-limit for exact destination ip configuration:
----------------------------------------------------------------------------------
Packet-Type    IPv6-address                                    rate(pps)          
----------------------------------------------------------------------------------
NS             2001:DB8:1::12                                  550     
----------------------------------------------------------------------------------
Total: 1       

ND rate-limit for every destination ip configuration:
----------------------------------------------------------------------------------
Packet-Type    rate(pps)                                          
----------------------------------------------------------------------------------
RS             550     
RA             550     
NS             550     
NA             550           
----------------------------------------------------------------------------------

ND rate-limit for exact target ip configuration:
----------------------------------------------------------------------------------
Packet-Type    IPv6-address                                    rate(pps)          
----------------------------------------------------------------------------------
NS             2001:DB8:1::13                                  550     
----------------------------------------------------------------------------------
Total: 1

ND rate-limit for every target ip configuration:
----------------------------------------------------------------------------------
Packet-Type    rate(pps)                                          
----------------------------------------------------------------------------------
NS             550     
NA             550           
----------------------------------------------------------------------------------

```

**Table 1** Description of the **display ipv6 nd anti-attack rate-limit configuration** command output
| Item | Description |
| --- | --- |
| ND rate-limit for VS Global configuration | ND rate limit for virtual system global configuration. |
| ND rate-limit for LS Global configuration | ND rate limit for logical system global configuration. |
| ND rate-limit for exact source mac configuration | ND rate limit for exact source MAC configuration. |
| ND rate-limit for every source mac configuration | ND rate limit for every source MAC configuration. |
| ND rate-limit for exact source ip configuration | ND rate limit for exact source IP configuration. |
| ND rate-limit for every source ip configuration | ND rate limit for every source IP configuration. |
| ND rate-limit for interface exact source ip configuration | ND rate limit for interface exact source IP configuration. |
| ND rate-limit for interface configuration | ND rate limit for interface configuration. |
| ND rate-limit for exact destination ip configuration | ND rate limit for exact destination IP configuration. |
| ND rate-limit for exact target ip configuration | ND rate limit for exact target IP configuration. |
| ND rate-limit for every destination ip configuration | ND rate limit for every destination IP configuration. |
| ND rate-limit for every target ip configuration | ND rate limit for every target IP configuration. |
| Packet-Type | RS, RA, NS, NA, or ND Miss message. |
| MAC-address | Source MAC address of the ND packet. |
| IPv6-address | IP address of the ND packet: source address, destination address, or target address. |
| Interface | The interface that received the ND packet or the ND Miss event. |
| rate | ND anti-attack rate limit. |
| Total | Total count. |