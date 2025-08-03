display arp (All views)
=======================

display arp (All views)

Function
--------



The **display arp** command displays the Address Resolution Protocol (ARP) entries.




Format
------

**display arp** [ **network** *ip-address* [ *ip-mask* | *mask-length* ] ] [ **dynamic** | **static** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **network** *ip-address* | Displays ARP entries based on the network ID expressed in dotted decimal notation. | The value is in dotted decimal notation. |
| *ip-mask* | Displays ARP entries based on the subnet mask of a specified network ID. The format of the subnet mask is X.X.X.X. | The value is in dotted decimal notation. |
| *mask-length* | Displays ARP entries based on the subnet mask length of a specified network ID. | The value ranges from 1 to 32 |
| **dynamic** | Displays dynamic ARP entries. | - |
| **static** | Displays static ARP entries. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To check ARP entries or locate ARP faults on an interface board, run the display arp slot command.



**Precautions**

This command displays dynamic entries of the following types:

* Interface entry generated after an IP address is configured for an interface. The entry identifier is I.
* Dynamic ARP entry learned using ARP packets. The entry identifier is D.
* Redirected ARP entry. The entry identifier is RD.
* ARP entry delivered by the controller to the forwarder. The entry identifier is O.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display ARP entries.
```
<HUAWEI> display arp
ARP Entry Types: D - Dynamic, S - Static, I - Interface, O - OpenFlow, RD - Redirect
EXP: Expire-time VLAN: VLAN or Bridge Domain

IP ADDRESS      MAC ADDRESS    EXP(M) TYPE/VLAN       INTERFACE        VPN-INSTANCE
----------------------------------------------------------------------------------------
192.168.1.12    00e0-fc41-0202            I           100GE1/0/1       r2
192.168.1.1     00e0-fc41-0200  17        D           100GE1/0/1       r2
192.168.1.11    00e0-fc41-0201            I           100GE1/0/1       r1
192.168.1.1     00e0-fc41-0200  17        D           100GE1/0/1       r1
----------------------------------------------------------------------------------------
Total:4         Dynamic:2       Static:0    Interface:2    OpenFlow:0
Redirect:0

```

**Table 1** Description of the **display arp (All views)** command output
| Item | Description |
| --- | --- |
| IP ADDRESS | IP address in an ARP entry. |
| MAC ADDRESS | MAC address in the ARP entry. When an IP packet triggers an ARP Miss message, the device generates a MAC address with the Incomplete flag based on the ARP Miss message. |
| INTERFACE | Type and number of the interface that has learned ARP entries. |
| VPN-INSTANCE | VPN instance name of an ARP entry. |
| Redirect | Number of redirected ARP entries. |
| EXP(M) | Remaining lifetime of an ARP entry, in minutes. |
| TYPE/VLAN | Type and VLAN ID of an ARP entry. The ARP entry type can be:   * I: Interface, indicating an interface's ARP entry. * D: Dynamic, indicating dynamic entries obtained using ARP messages. * S: Static, indicating static ARP entries configured. * O: OpenFlow, indicating an ARP entry delivered from the controller to a forwarder. * RD: Redirect, indicating a redirected ARP entry. |
| Interface | Number of ARP entries for the local interface in the ARP table. |
| Total | Number of ARP entries in the ARP table. |
| Dynamic | Number of dynamic ARP entries in the ARP table. |
| Static | Number of static ARP entries in the ARP table. |
| OpenFlow | Number of ARP entries delivered from the controller to a forwarder. |