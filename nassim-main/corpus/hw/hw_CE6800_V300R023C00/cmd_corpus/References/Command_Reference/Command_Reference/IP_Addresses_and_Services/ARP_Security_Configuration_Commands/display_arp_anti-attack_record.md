display arp anti-attack record
==============================

display arp anti-attack record

Function
--------



The **display arp anti-attack record** command displays information about discarded Address Resolution Protocol (ARP) packets whose rate exceeds the limit.

The **display arp miss anti-attack record** command displays information about discarded Address Resolution Protocol (ARP) Miss messages whose rate exceeds the limit.




Format
------

**display arp anti-attack record**

**display arp miss anti-attack record**


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



After ARP packet rate limit is configured, the device counts the number of received ARP packets. If the number of ARP packets received in a specified period exceeds the upper limit, the device discards the excess ARP packets. To facilitate fault location, the device records information about discarded ARP packets whose rate exceeds the limit. To check information about discarded ARP packets whose rate exceeds the limit, run the display arp anti-attack record command.After ARP Miss message rate limit is configured, the device counts the number of received ARP Miss messages. If the number of ARP Miss messages received in a specified period exceeds the upper limit, the device discards the excess ARP Miss messages. To facilitate fault location, the device records information about discarded ARP Miss messages whose rate exceeds the limit. To check information about discarded ARP Miss messages whose rate exceeds the limit, run the display arp miss anti-attack record command.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about discarded ARP packets whose rate exceeds the limit.
```
<HUAWEI> display arp anti-attack record
Source IP       Destination IP  Interface   Attack Time
--------------------------------------------------------------------------------
10.1.115.234    10.1.1.1        10GE1/0/1    09-10 15:53:34      
10.1.115.234    10.1.1.1        10GE1/0/1    09-10 15:53:34      
10.1.115.236    10.1.1.1        10GE1/0/1    09-10 15:53:34      
10.1.115.237    10.1.1.1        10GE1/0/1    09-10 15:53:34      
10.1.115.238    10.1.1.1        10GE1/0/1    09-10 15:53:34      
10.1.115.239    10.1.1.1        10GE1/0/1    09-10 15:53:34      
--------------------------------------------------------------------------------
There are 6 records in ARP table

```

# Display information about discarded ARP Miss messages whose rate exceeds the limit.
```
<HUAWEI> display arp miss anti-attack record
Source IP       Destination IP  Interface   Attack Time    
--------------------------------------------------------------------------------
10.1.1.2        10.1.2.247      10GE1/0/1    09-10 16:06:04      
10.1.1.2        10.1.2.248      10GE1/0/1    09-10 16:06:04      
10.1.1.2        10.1.2.249      10GE1/0/1    09-10 16:06:04      
10.1.1.2        10.1.2.250      10GE1/0/1    09-10 16:06:04      
10.1.1.2        10.1.2.251      10GE1/0/1    09-10 16:06:04      
10.1.1.2        10.1.2.252      10GE1/0/1    09-10 16:06:04      
--------------------------------------------------------------------------------
There are 6 records in ARP-miss table

```

**Table 1** Description of the **display arp anti-attack record** command output
| Item | Description |
| --- | --- |
| Source IP | Source IP address in discarded ARP Miss messages or ARP packets. |
| Destination IP | Destination IP address in discarded ARP Miss messages or ARP packets. |
| Interface | Interface information carried in discarded ARP Miss messages or ARP packets. |
| Attack Time | Attack time of ARP Miss messages or ARP packets.  The attack time of ARP Miss messages or ARP packets refers to the time at which the ARP Miss messages or ARP packets rate reaches the limit. |