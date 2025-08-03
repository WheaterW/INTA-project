display multicast ipv6 fib
==========================

display multicast ipv6 fib

Function
--------



The **display multicast ipv6 fib** command displays information about the IPv6 multicast forwarding table.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display multicast ipv6 fib** [ [ **vpn-instance** *vpn-instance-name* ] [ **group** *group-address-v6* | **source** *source-address-v6* | **incoming-interface** { *interface-type* *src-interface-name* | **register** } ] \* | **all-vpn-instance** ] [ **slot** *slot-id* [ **cpu** *cpu-id* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance to be queried. | The value is a string of 1 to 31 case-sensitive characters. It cannot be \_public\_. If spaces are used, the string must be enclosed in double quotation marks (" "). |
| **group** *group-address-v6* | Displays forwarding information corresponding to the specified multicast group address. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **source** *source-address-v6* | Displays forwarding information corresponding to the specified multicast source address. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **incoming-interface** *interface-type* | Specifies the interface type. | The value is a string of 1 to 47 case-sensitive characters. It cannot contain spaces. |
| **incoming-interface** *src-interface-name* | Specifies the interface name. | The value is a string of 1 to 47 case-sensitive characters. It cannot contain spaces. |
| **register** | Indicates the register interface of PIM-SM. | - |
| **all-vpn-instance** | Specifies all VPN instances. | - |
| **slot** *slot-id* | Displays entry information of a specified slot ID. | The value is a string of 1 to 23 case-sensitive characters, spaces not supported. |
| **cpu** *cpu-id* | Displays entry information about a specified CPU. | The value is an integer ranging from 0 to 4294967295. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

This command displays information about the Layer 3 multicast forwarding table.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the IPv6 multicast forwarding table.
```
<HUAWEI> display multicast ipv6 fib incoming-interface 100GE 1/0/1
IPv6 Multicast Forwarding Table of VPN-Instance: public net
Total 1 entry, 1 matched
1.(FC00:1::3, FF1E::1)
     Index   : 1
     Timeout : 00:03:30
     Incoming interface : 100GE1/0/1
     Outgoing interfaces: 1
       1: 100GE1/0/2
     Matched packets :1768 packets(183872 bytes)
     Wrong interface :0 packets     
     Forwarded       :1768 packets(183872 bytes)

```

**Table 1** Description of the **display multicast ipv6 fib** command output
| Item | Description |
| --- | --- |
| IPv6 Multicast Forwarding Table of VPN-Instance | VPN instance of the multicast forwarding table. |
| Total 1 entry, 1 matched | Total number of forwarding entries and number of matching forwarding entries. |
| 1 | ID of the (S, G) entry. |
| Index | It uniquely identifies the multicast forwarding entry in the MFIB table and is used to rapidly search the multicast forwarding table. |
| Timeout | Remaining time of the (S, G) entry. |
| Incoming interface | Inbound interface of the (S, G) entry. |
| Outgoing interfaces | Numbers of each outbound interface. |
| 1: 100GE1/0/2 | Name and number of the outbound interface. |
| Matched packets | Volume of the multicast traffic forwarded through this outbound interface, in bytes. |
| Wrong interface | Number of packets with incorrect inbound interface. |
| Forwarded | Volume of forwarded multicast traffic, in bytes. |
| (FC00:1::3, FF1E::1) | (S, G) entry in the multicast routing table. |