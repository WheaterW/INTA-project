display multicast ip fib
========================

display multicast ip fib

Function
--------



The **display multicast ip fib** command displays information about the multicast forwarding table.




Format
------

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**display multicast ip fib** [ [ **vpn-instance** *vpn-instance-name* ] [ **group** *group-address* | **source** *source-address* | **incoming-interface** { *interface-type* *interface-name* | **register** } ] \* | **all-vpn-instance** ] [ **slot** *slot-id* [ **cpu** *cpu-id* ] ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display multicast ip fib** [ [ **vpn-instance** *vpn-instance-name* ] [ **group** *group-address* | **source** *source-address* | **incoming-interface** { *interface-type* *interface-name* | **register** } | **backup-incoming-interface** *interface-type* *interface-name* | **receive-incoming-interface** *interface-type* *interface-name* ] \* | **all-vpn-instance** ] [ **slot** *slot-id* [ **cpu** *cpu-id* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **group** *group-address* | Displays information about the forwarding table of the multicast group with the specified address. The value ranges from 224.0.0.0 to 239.255.255.255, in dotted decimal notation. | The value is in dotted decimal notation. The value ranges from 224.0.0.0 to 239.255.255.255. |
| **source** *source-address* | Specifies the address of a multicast source. After this parameter is specified, the forwarding table of the multicast source is displayed. The value ranges from 0.0.0.0 to 223.255.255.255, in dotted decimal notation. | The value ranges from 0.0.0.0 to 223.255.255.255, in dotted decimal notation. |
| **incoming-interface** | Indicates the inbound interface of multicast forwarding entries. | - |
| **incoming-interface** *interface-type* | Specifies the type of an interface. | The value is a string of 1 to 47 case-sensitive characters. It cannot contain spaces. |
| **incoming-interface** *interface-name* | Indicates the interface name. | The value is a string of 1 to 47 case-sensitive characters. It cannot contain spaces. |
| **register** | Indicates the register interface of PIM-SM. | - |
| **all-vpn-instance** | Specifies all VPN instances. | - |
| **slot** *slot-id* | Displays entry information of a specified slot ID. | The value is a string of 1 to 23 case-sensitive characters, spaces not supported. |
| **cpu** *cpu-id* | Displays entry information about a specified CPU. | The value is an integer ranging from 0 to 4294967295. |
| **backup-incoming-interface** | Indicates the backup inbound interface of multicast forwarding entries.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **backup-incoming-interface** *interface-type* | Indicates the type of the backup inbound interface.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a string of 1 to 47 case-sensitive characters. It cannot contain spaces. |
| **backup-incoming-interface** *interface-name* | Specifies the name of the backup inbound interface.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a string of 1 to 47 case-sensitive characters. It cannot contain spaces. |
| **receive-incoming-interface** | Indicates the inbound interface for selective receiving of multicast forwarding entries.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **receive-incoming-interface** *interface-type* | Indicates the type of the inbound interface for selective receiving.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a string of 1 to 47 case-sensitive characters. It cannot contain spaces. |
| **receive-incoming-interface** *interface-name* | Specifies the name of the inbound interface for selective receiving.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a string of 1 to 47 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check information about the Layer 3 multicast forwarding table, run this command.Currently, only information about public network instances is displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the multicast forwarding table.
```
<HUAWEI> display multicast ip fib incoming-interface 100GE 1/0/1
Multicast Forwarding Table of VPN-Instance: public net
Total 1 entry, 1 matched
1.(10.10.10.2, 225.0.0.1)
     Index   : 1
     Timeout : 00:03:30
     Incoming interface : 100GE1/0/1
     Outgoing interfaces: 1
       1: 100GE1/0/2
     Matched packets :1768 packets(183872 bytes)
     Wrong interface :0 packets
     Forwarded       :1768 packets(183872 bytes)

```

# Display information about the multicast forwarding table in MoFRR scenarios.
```
<HUAWEI> display multicast ip fib source 100.0.1.2 group  229.0.0.1
Multicast Forwarding Table of VPN-Instance: public net
Total 1 entry, 1 matched
1.(100.0.1.2, 229.0.0.1)
    Index   : 521
    Timeout : 16:41:49
    Incoming interface : 100GE1/0/3.1
    Backup incoming interface : 100GE1/0/2.1
    Receive incoming interface : 100GE1/0/2.1
    Outgoing interface : 1
        1: 100GE1/0/1
    Matched packets : 1342090223 packets(175518226992 bytes)
    Wrong interface  : 0 packets(0 bytes)
    Forwarded       : 1342090223 packets(175518226992 bytes)

```

# Display information about the multicast forwarding table when forwarding resources are insufficient in MoFRR scenarios.
```
<HUAWEI> display multicast ip fib source 100.0.1.2 group  229.0.0.1
Multicast Forwarding Table of VPN-Instance: public net
Total 1 entry, 1 matched
1.(100.0.1.2, 229.0.0.1)
    Index   : 521
    Timeout : 16:41:49
    Incoming interface : 100GE1/0/3.1
    Backup incoming interface : 100GE1/0/2.1
    Receive incoming interface : 100GE1/0/2.1
    (Frr forward resource lacked)
    Outgoing interface : 1
        1: 100GE1/0/1
    Matched packets : 1342090223 packets(175518226992 bytes)
    Wrong interface  : 0 packets(0 bytes)
    Forwarded       : 1342090223 packets(175518226992 bytes)

```

**Table 1** Description of the **display multicast ip fib** command output
| Item | Description |
| --- | --- |
| Multicast Forwarding Table of VPN-Instance | VPN instance to which the multicast forwarding table belongs. |
| Total 1 entry, 1 matched | Total number of forwarding entries and number of eligible forwarding entries. |
| 1 | Sequence number of the (S, G) entry. |
| Index | Unique ID of a multicast forwarding entry in the multicast forwarding table, which is used to quickly retrieve the entry. |
| Timeout | Remaining time of the (S, G) entry. |
| Incoming interface | Inbound interface of the (S, G) entry. |
| Outgoing interfaces | Numbers of each outbound interface. |
| 1: 100GE1/0/2 | Name and number of the outbound interface. |
| Matched packets | Volume of the multicast traffic forwarded through this outbound interface, in bytes. |
| Wrong interface | Number of packets with incorrect inbound interface. |
| Forwarded | Volume of forwarded multicast traffic, in bytes. |
| Backup incoming interface | Backup inbound interface of (S, G) entries. |
| Receive incoming interface | Inbound interface for selective receiving of (S, G) entries. |
| (10.10.10.2, 225.0.0.1) | (S, G) entry in the multicast routing table. |