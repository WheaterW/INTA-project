display arp vlan
================

display arp vlan

Function
--------



The **display arp vlan** command displays ARP entries learned by a specified VLAN.




Format
------

**display arp vlan** *vlan-id* **interface** { *interface-name* | *interface-type* *interface-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id* | Specifies a VLAN ID. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **interface** *interface-name* | Specifies the name of an interface. | - |
| **interface** *interface-type* *interface-number* | Specifies the type and number of an interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check ARP entries or locate ARP faults in a specified VLAN, run the display arp vlan command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display ARP entries on the member interface of VLAN 1.
```
<HUAWEI> display arp vlan 1 interface 100ge 1/0/1
ARP Entry Types: D - Dynamic, S - Static, I - Interface, O - OpenFlow, RD - Redirect
EXP: Expire-time VLAN:VLAN or Bridge Domain

IP ADDRESS      MAC ADDRESS     EXP(M)    TYPE/VLAN   INTERFACE   VPN-INSTANCE
------------------------------------------------------------------------------
10.1.1.1        00e0-fcd2-3802    20      D/10        100GE1/0/1  
------------------------------------------------------------------------------
Total:1         Dynamic:1       Static:0    Interface:0    OpenFlow:0
Redirect:0

```

**Table 1** Description of the **display arp vlan** command output
| Item | Description |
| --- | --- |
| ARP Entry Types | ARP entry type:   * I: Interface, indicating an interface's ARP entry. * D: Dynamic, indicating dynamic entries obtained using ARP messages. * S: Static, indicating static ARP entries configured. * O: OpenFlow, indicating an ARP entry delivered from the controller to a forwarder. * RD: Redirect, indicating a redirected ARP entry. |
| Redirect | Number of redirected ARP entries. |
| IP ADDRESS | IP address in an ARP entry. |
| MAC ADDRESS | MAC address in the ARP entry. When an IP packet triggers an ARP Miss message, the device generates a MAC address with the Incomplete flag based on the ARP Miss message. |
| EXP(M) | Remaining lifetime of an ARP entry, in minutes. |
| TYPE/VLAN | Type and VLAN ID of an ARP entry. The ARP entry can be:   * I: Interface, indicating an ARP entry of an interface. * D: Dynamic, indicating a dynamic ARP entry obtained using ARP messages. * S: Static, indicating an ARP entry statically configured. * O: OpenFlow, indicating an ARP entry delivered from the controller to a forwarder. * RD: Redirect, indicating a redirected ARP entry. |
| INTERFACE | Type and number of an interface that has learned ARP entries. |
| VPN-INSTANCE | VPN instance name of an ARP entry. |
| Interface | Number of ARP entries for the local interface in the ARP table. |
| Total | Number of ARP entries in the ARP table. |
| Dynamic | Number of dynamic ARP entries in the ARP table. |
| Static | Number of static ARP entries in the ARP table. |
| OpenFlow | Number of ARP entries delivered from the controller to a forwarder. |