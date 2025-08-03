display dns statistics
======================

display dns statistics

Function
--------



The **display dns statistics** command displays statistics about DNS packets.




Format
------

**display dns statistics**


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

**Usage Scenario**



You can use this command to check statistics about DNS packets, including IPv4 and IPv6 DNS packets.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about DNS packets.
```
<HUAWEI> display dns statistics
                                                                     
SumFromDNSv4Client           : 0                                                
SumToDNSv4Client             : 0                                                
SumFromDNSv4Server           : 0                                                
SumToDNSv4Server             : 0                                                
                                                                                
SumFromDNSv6Client           : 0                                                                                                    
SumToDNSv6Client             : 0                                                                                                    
SumFromDNSv6Server           : 0                                                                                                    
SumToDNSv6Server             : 0

RetryFromClient              : 0                                                
NotQueryFromClient           : 0                                                
ParseFailFromClient          : 0                                                
TooLongFromClient            : 0                                                
LocalQueryFromClient         : 0                                                
NotStandardQueryFromClient   : 0        
FwdTableFullFromClient       : 0                                        
                                                                                
NotRespFromServer            : 0                                                
NoAnswerFromServer           : 0                                                
ParseFailFromServer          : 0                                                
TooLongFromServer            : 0                                                
ErrorRespFromServer          : 0                                                
NotStandardQueryFromServer   : 0

```

**Table 1** Description of the **display dns statistics** command output
| Item | Description |
| --- | --- |
| SumFromDNSv4Client | Total number of packets sent from IPv4 DNS clients. |
| SumToDNSv4Client | Total number of packets sent to IPv4 DNS clients. |
| SumFromDNSv4Server | Total number of packets sent from IPv4 DNS servers. |
| SumToDNSv4Server | Total number of packets sent to IPv4 DNS servers. |
| SumFromDNSv6Client | Total number of packets sent from IPv6 DNS clients. |
| SumToDNSv6Client | Total number of packets sent to IPv6 DNS clients. |
| SumFromDNSv6Server | Total number of packets sent from IPv6 DNS servers. |
| SumToDNSv6Server | Total number of packets sent to IPv6 DNS servers. |
| RetryFromClient | Number of packets retransmitted from clients. |
| NotQueryFromClient | Number of non-query packets sent from clients. |
| ParseFailFromClient | Number of packets that failed to be parsed and are sent from clients. |
| TooLongFromClient | Number of packets longer than 512 bytes sent from clients. |
| LocalQueryFromClient | Number of query packets of which the source address is a local address and sent from clients. |
| NotStandardQueryFromClient | Number of nonstandard query packets sent from clients. |
| FwdTableFullFromClient | Number of query packets from the client dropped because the forwarding table exceeds the specifications. |
| NotRespFromServer | Number of non-response packets sent from servers. |
| NoAnswerFromServer | Number of response packets of which the ANCOUNT field is 0 and sent from servers. |
| ParseFailFromServer | Number of packets that failed to be parsed and are sent from servers. |
| TooLongFromServer | Number of packets longer than 512 bytes sent from servers. |
| ErrorRespFromServer | Number of error response packets sent from servers. |
| NotStandardQueryFromServer | Number of nonstandard query packets sent from servers. |