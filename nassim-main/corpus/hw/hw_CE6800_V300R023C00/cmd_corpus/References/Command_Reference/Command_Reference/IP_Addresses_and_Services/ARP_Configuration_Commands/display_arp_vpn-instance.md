display arp vpn-instance
========================

display arp vpn-instance

Function
--------



The **display arp vpn-instance** command displays the ARP entries of a VPN instance.




Format
------

**display arp vpn-instance** *vpn-instance-name* [ **dynamic** | **static** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **dynamic** | Displays dynamic ARP entries. | - |
| **static** | Displays static ARP entries. | - |
| **vpn-instance** *vpn-instance-name* | Displays the ARP entries of a VPN instance. | The value is a string of 1 to 31. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To check ARP entries or locate ARP faults of a specified VPN instance, run the display arp vpn-instance command.



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


# Display all ARP entries of the VPN instance name r1.
```
<HUAWEI> display arp vpn-instance r1
ARP Entry Types: D - Dynamic, S - Static, I - Interface, O - OpenFlow, RD - Redirect
EXP: Expire-time VLAN:VLAN or Bridge Domain

IP ADDRESS      MAC ADDRESS     EXP(M)    TYPE/VLAN   INTERFACE   VPN-INSTANCE
------------------------------------------------------------------------------
10.1.1.11       00e0-fc01-0001            I           100GE1/0/1   r1
10.1.1.1        00e0-fcd2-3802    20      D/10        100GE1/0/1   r1
------------------------------------------------------------------------------
Total:2         Dynamic:1       Static:0    Interface:1    OpenFlow:0
Redirect:0

```

**Table 1** Description of the **display arp vpn-instance** command output
| Item | Description |
| --- | --- |
| IP ADDRESS | IP address in an ARP entry. |
| MAC ADDRESS | MAC address in the ARP entry. When an IP packet triggers an ARP Miss message, the device generates a MAC address with the Incomplete flag based on the ARP Miss message. |
| INTERFACE | Type and number of an interface that has learned ARP entries. |
| VPN-INSTANCE | VPN instance name of an ARP entry. |
| ARP Entry Types | ARP entry type:   * I: Interface, indicating an ARP entry of an interface. * D: Dynamic, indicating a dynamic ARP entry obtained using ARP messages. * S: Static, indicating an ARP entry statically configured. * O: OpenFlow, indicating an ARP entry delivered from the controller to a forwarder.RD: Redirect, indicating a redirected ARP entry. * RD: Redirect, indicating a redirected ARP entry. |
| Interface | Number of ARP entries for the local interface in the ARP table. |
| EXP(M) | Remaining lifetime of an ARP entry, in minutes. |
| TYPE/VLAN | Type and VLAN ID of an ARP entry. The ARP entry can be:   * I: Interface, indicating an ARP entry of an interface. * D: Dynamic, indicating a dynamic ARP entry obtained using ARP messages. * S: Static, indicating an ARP entry statically configured. * O: OpenFlow, indicating an ARP entry delivered from the controller to a forwarder. * RD: Redirect, indicating a redirected ARP entry. |
| Redirect | Number of redirected ARP entries. |
| Total | Number of ARP entries in the ARP table. |
| Dynamic | Number of dynamic ARP entries in the ARP table. |
| Static | Number of static ARP entries in the ARP table. |
| OpenFlow | Number of ARP entries delivered from the controller to a forwarder. |