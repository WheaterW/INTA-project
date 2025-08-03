display arp ip-conflict track
=============================

display arp ip-conflict track

Function
--------



The **display arp ip-conflict track** command displays IP address conflict information.




Format
------

**display arp ip-conflict track** [ **ip** *ip-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip** *ip-address* | Displays conflict information of a specified IP address. | The value is in dotted decimal notation. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



If IP address conflicts exist on a network, device routes will frequently flap, greatly affecting user services.To faster locate the conflicting IP address and better manage devices' IP addresses, run the display arp ip-conflict track command to check IP address conflict information, including the conflicting IP address, MAC address corresponding to the IP address, number of IP address conflicts, date and time when an IP address conflict occurred, and number of times that the conflicting IP address is suppressed.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display IP address conflict information.
```
<HUAWEI> display arp ip-conflict track
Conflict type       : Remote IP Confilct       
    IP address          : 3.3.3.3
    System time         : 04-13 08:44:11-08:00
    Conflict count      : 1                        
    Suppress count      : 0
    Old interface       : Ge1/0/1                 
    Receive interface   : Ge1/0/1
    Old VLAN/CEVLAN     : 0/0                      
    Receive VLAN/CEVLAN : 0/0
    Old MAC             : xxxx-xxxx-xxxx           
    Receive MAC         : xxxx-xxxx-xxxx
    Receive Head DMAC   : xxxx-xxxx-xxxx
    Receive Head SMAC   : xxxx-xxxx-xxxx

    Conflict type       : Local IP Confilct       
    Local IP address    : 4.3.3.3
    System time         : 04-13 08:44:11-08:00
    Conflict count      : 1                        
    Suppress count      : 0
    Local interface     : Ge1/0/2                 
    Receive interface   : Ge1/0/2
    Receive VLAN/CEVLAN : 0/0           
    Receive MAC         : xxxx-xxxx-xxxx
    Receive Head DMAC   : xxxx-xxxx-xxxx
    Receive Head SMAC   : xxxx-xxxx-xxxx

    Conflict type       : Local-ce IP Confilct       
    IP address          : 5.3.3.3
    System time         : 04-13 08:44:11-08:00
    Conflict count      : 1                        
    Suppress count      : 0
    Local interface     : Ge1/0/3                 
    Receive interface   : Ge1/0/3                      
    Receive VLAN/CEVLAN : 0/0
    Local MAC           : xxxx-xxxx-xxxx           
    Receive MAC         : xxxx-xxxx-xxxx  
    Receive Head DMAC   : xxxx-xxxx-xxxx
    Receive Head SMAC   : xxxx-xxxx-xxxx

```

**Table 1** Description of the **display arp ip-conflict track** command output
| Item | Description |
| --- | --- |
| Conflict type | Conflict type:   * Local IP conflict: The IP address of the local device conflicts with that of another device. * Remote IP conflict: The local device functions as an access device and detects an IP address conflict between connected devices or users. * Local-ce IP conflict: In heterogeneous interworking scenarios, a PE detects that the IP or MAC address of the connected CE is different from that configured using the local-ce ip or local-ce mac command on the PE. |
| Conflict count | Number of IP address conflicts.  If the ARP entry corresponding to the IP address is aged or deleted, this field is cleared. |
| IP address | Conflicting IP address.  When the conflict type is Local-ce IP conflict, this field indicates the IP address of the CE device when the conflict occurs. |
| System time | System time when an IP address conflict occurred. |
| Suppress count | Number of times that IP address conflicts are suppressed.  If the ARP entry corresponding to the IP address is aged or deleted, this field is cleared. |
| Old interface | Interface recorded in the ARP entry corresponding to the IP address before the conflict.  If the conflict type is Local IP conflict or Local-ce IP conflict, this field is displayed as Local interface, indicating the interface where the conflicting IP address resides. |
| Old VLAN/CEVLAN | VLAN and CE VLAN recorded in the ARP entry corresponding to the IP address before the conflict.  Old MAC is displayed only when Conflict type is Remote IP conflict. |
| Old MAC | MAC address recorded in the ARP entry corresponding to the IP address before the conflict.  Old MAC is displayed only when Conflict type is Remote IP conflict. |
| Receive interface | Interface that receives an ARP packet when a conflict occurs. |
| Receive VLAN/CEVLAN | VLAN and CE VLAN that receive ARP packets during a conflict. |
| Receive MAC | Source MAC address in the ARP packet received during a conflict. |
| Receive Head DMAC | Destination MAC address in the Ethernet header in the received ARP packet when an IP address conflict occurs. |
| Receive Head SMAC | Source MAC address in the Ethernet header in the received ARP packet when an IP address conflict occurs. |
| Local interface | Interface where the conflicting IP address resides.  When the conflict type is Remote IP conflict, this field is displayed as Old interface, indicating the interface that learns the ARP entry corresponding to the IP address before the conflict. |
| Local MAC | Value of local-ce mac configured on the interface. If local-ce mac is not configured, the value of this field is displayed as 0000-0000-0000.  Old MAC is displayed only when Conflict type is Local-ce IP conflict. |
| Local IP address | Conflicting IP address. |