display arp interface
=====================

display arp interface

Function
--------



The **display arp interface** command displays the ARP entries of a specified interface.




Format
------

**display arp interface** { *interface-name* | *interface-type* *interface-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Displays ARP entries learned by a specified interface. | - |
| **interface** *interface-name* | Displays ARP entries learned by a specified interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To check entries of all interface boards, run the display arp all command.To check ARP entries learned by an interface or locate ARP faults on an interface, run the display arp interface command. The specified interface can be a Layer 3 interface or a Layer 2 interface added to a VLAN.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display ARP entries learned by an interface named vbdif 100.
```
<HUAWEI> display arp interface vbdif 100
ARP timeout:1200s
ARP Entry Types: D - Dynamic, S - Static, I - Interface, O - OpenFlow, RD - Redirect
EXP: Expire-time  src: source ip   dst: destination ip

IP ADDRESS      MAC ADDRESS    EXP(M) TYPE/VLAN/CEVLAN INTERFACE
------------------------------------------------------------------------------
10.1.1.1        00e0-fc8b-5902        I                Vbdif100        
10.1.1.2        00e0-fc01-0001        S                VNI10(src:1.1.1.1 dst:2.2.2.2)  
1.1.1.5         00e0-fc01-0005        S/10/100         100GE1/0/2.1       
------------------------------------------------------------------------------
Total:3         Dynamic:0       Static:2    Interface:1    OpenFlow:0
Redirect:0

```

# Display ARP entries learned by the interface.
```
<HUAWEI> display arp interface 100ge1/0/1
ARP timeout:1200s
ARP Entry Types: D - Dynamic, S - Static, I - Interface, O - OpenFlow, RD - Redirect
EXP: Expire-time VLAN:VLAN or Bridge Domain

IP ADDRESS      MAC ADDRESS     EXP(M)    TYPE/VLAN   INTERFACE   VPN-INSTANCE
------------------------------------------------------------------------------
10.1.1.11       00e0-fc01-0001            I           100GE1/0/1  
10.1.1.1        00e0-fcd2-3802    20      D/10        100GE1/0/1  
------------------------------------------------------------------------------
Total:2         Dynamic:1       Static:0    Interface:1    OpenFlow:0
Redirect:0

```

**Table 1** Description of the **display arp interface** command output
| Item | Description |
| --- | --- |
| ARP timeout | Effective aging time of ARP entries on an interface, in seconds. |
| ARP Entry Types | ARP entry type:   * D: Dynamic, indicating a dynamic ARP entry obtained using ARP messages. * S: Static, indicating an ARP entry statically configured. * I: Interface, indicating an ARP entry of an interface. * O: OpenFlow, indicating an ARP entry delivered from the controller to a forwarder. * RD: Redirect, indicating a redirected ARP entry. |
| IP ADDRESS | IP address in an ARP entry. |
| MAC ADDRESS | MAC address in the ARP entry. When an IP packet triggers an ARP Miss message, the device generates a MAC address with the Incomplete flag based on the ARP Miss message. |
| INTERFACE | Type and number of an interface that has learned ARP entries.   * VNI: indicates the network-side identifier. * src: indicates the source IP address. * dst: indicates the destination IP address. |
| VPN-INSTANCE | Name of the VPN instance to which the ARP entry belongs. |
| Redirect | Number of redirected ARP entries. |
| EXP(M) | Remaining aging time of an ARP entry, in minutes. |
| TYPE/VLAN/CEVLAN | Entry type and inner and outer VLAN IDs of the entry. The entry types are as follows:   * I: interface, indicating an ARP entry of an interface. * D: dynamic, indicating dynamic entries obtained using ARP packets. * S: static, indicating the static entry obtained through static configuration. * O: OpenFlow, indicating an ARP entry delivered by the controller to a forwarder. * RD: redirect, indicating the redirected ARP entry. |
| Interface | Number of ARP entries for the interface. |
| TYPE/VLAN | ARP entry type and ID of the VLAN to which the ARP entry belongs. The entry types are as follows:   * I: interface, indicating an ARP entry of an interface. * D: dynamic, indicating dynamic entries obtained using ARP packets. * S: static, indicating the static entry obtained through static configuration. * O: OpenFlow, indicating an ARP entry delivered by the controller to a forwarder. * RD: redirect, indicating the redirected ARP entry. |
| Total | Total number of ARP entries. |
| Dynamic | Number of dynamic ARP entries. |
| Static | Number of static ARP entries. |
| OpenFlow | Number of ARP entries delivered by the controller to the forwarder. |
| VNI | VNI ID. |
| src | VXLAN source IP address. |
| dst | VXLAN remote IP address. |