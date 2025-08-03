display multicast ipv6 routing-table (All views)
================================================

display multicast ipv6 routing-table (All views)

Function
--------



The **display multicast ipv6 routing-table** command displays the IPv6 multicast routing table.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display multicast ipv6 routing-table** [ *groupAddr* [ **mask** *group-mask-length* ] | *srcAddr* [ **mask** *source-mask-length* ] | **incoming-interface** { { *iif-port-type* *iif-port-num* | *iif-port-name* } | **register** } | **outgoing-interface** { **include** | **exclude** | **match** } { { *oif-port-type* *oif-port-num* | *oif-port-name* } | **register** | **none** } ] \* [ **outgoing-interface-number** [ *oif-number* ] ]

**display multicast ipv6** { **vpn-instance** *vpn-instance-name* | **all-instance** } **routing-table** [ *groupAddr* [ **mask** *group-mask-length* ] | *srcAddr* [ **mask** *source-mask-length* ] | **incoming-interface** { { *iif-port-type* *iif-port-num* | *iif-port-name* } | **register** } | **outgoing-interface** { **include** | **exclude** | **match** } { { *oif-port-type* *oif-port-num* | *oif-port-name* } | **register** | **none** } ] \* [ **outgoing-interface-number** [ *oif-number* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *groupAddr* | Indicates the address of the multicast group. | The value ranges from 224.0.0.0 to 239.255.255.255, in dotted decimal notation. |
| **mask** | Specifies the mask length. | - |
| *group-mask-length* | Specifies the mask length of an IPv6 multicast group address. | The value is an integer that ranges from 8 to 128. |
| *srcAddr* | Specifies the IPv6 address of a multicast source. | The value is a string case-sensitive characters, spaces not supported. |
| *source-mask-length* | Specifies the mask length of a multicast source address. | The value is an integer that ranges from 0 to 128. |
| **incoming-interface** | Indicates the incoming interface of a multicast forwarding entry. | - |
| *iif-port-type* | Specifies the type of an inbound interface. | - |
| *iif-port-num* | Specifies the number of an inbound interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| *iif-port-name* | Specifies the name of an inbound interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **register** | Indicates the register interface of IPv6 PIM-SM. | - |
| **outgoing-interface** | Indicates the outbound interface of a multicast forwarding entry. | - |
| **include** | Displays the (S, G) entries whose downstream interface list contains specified outbound interfaces. | - |
| **exclude** | Displays the (S, G) entries whose downstream interface list does not contain specified outbound interfaces. | - |
| **match** | Displays (S, G) entries whose the downstream interface list contains only one interface that is the same as a specified outbound interface. | If no interface is specified, the (S, G) entry with the null downstream interface list is displayed. |
| *oif-port-type* | Specifies the type of an outbound interface. | - |
| *oif-port-num* | Specifies the number of an outbound interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| *oif-port-name* | Specifies the name of an outbound interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **none** | Displays the routing entry without a downstream interface. | - |
| **outgoing-interface-number** | Displays the number of the outbound interfaces of multicast routing entries. | - |
| *oif-number* | Displays the number of the outbound interfaces of multicast routing entries. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all-instance** | Specifies all VPN instance. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When the **display multicast ipv6 routing-table** command is used, the following situations occur:

* If srcAddr is specified, information about the IPv6 multicast routing table to which a specified multicast source corresponds is displayed.
* If source-mask-length is specified, information about the IPv6 multicast routing table to which a multicast source within a specified address range corresponds is displayed.
* If groupAddr is specified, information about the IPv6 multicast routing table to which a specified multicast group corresponds is displayed.
* If group-mask-length is specified, information about the IPv6 multicast routing table to which a multicast group within a specified address range corresponds is displayed.
* If outgoing-interface-number is specified, the number of the outbound interfaces of multicast routing entries is displayed.
* If oif-number is specified, information about the multicast groups corresponding to the number of outbound interfaces is displayed.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the number of outbound interfaces in the IPv6 multicast routing table.
```
<HUAWEI> display multicast ipv6 routing-table outgoing-interface-number
Multicast routing table of VPN-Instance: public net
 Total 1 (*, G) entry; 0 (S, G) entry

 00001 . (*, FF5E::6)
       Uptime: 02:41:19
       Upstream Interface: 100GE1/0/1
       List of 2 downstream interfaces

```

# Display the routing entries in the IPv6 multicast routing table.
```
<HUAWEI> display multicast ipv6 routing-table
Multicast routing table of VPN Instance: public net
 Total 1 (*, G) entry; 0 (S, G) entry

 00001 : (*, FF5E::6)
       Uptime: 01:01:01
       Upstream Interface: 100GE1/0/3
       List of 2 downstream interfaces
           1: 100GE1/0/1
           2: 100GE1/0/2

```

# Display information about IPv6 multicast routing entries in which the outbound interface is a BAS interface.
```
<HUAWEI> display multicast ipv6 routing-table
Multicast routing table of VPN-Instance: public net
 Total 1 entry

 00001. (2001:db8:1::2, FF18::1)
       Uptime: 01:00:39
       Upstream Interface: 100GE1/0/2
       List of 1 downstream interface
           1: 100GE1/0/1(bas)

```

# Display routing entries in the IPv6 BIDIR-PIM routing table of the public network instance.
```
<HUAWEI> display multicast ipv6 routing-table
Multicast routing table of VPN-Instance: public net
 Total 1 (*, G) entry; 0 (S, G) entry

 00001. (*, FF5E::6)
       Uptime: 01:01:01
       Upstream Interface: --
       List of 2 downstream interfaces
           1: Vlanif200
           2: LoopBack0

```

**Table 1** Description of the **display multicast ipv6 routing-table (All views)** command output
| Item | Description |
| --- | --- |
| Multicast routing table of VPN-Instance | Indicates the VPN instance to which the multicast routing information corresponds. |
| Multicast routing table of VPN Instance | Indicates the VPN instance to which the multicast routing information corresponds. |
| Total 1 entry | Indicates the number of eligible routing entries. |
| (\*, FF5E::6) | Indicates the (S, G) entry in the IPv6 multicast routing table. |
| 00001 | Indicates the sequence number of the (S, G) entry. |
| Upstream Interface | Upstream interface in an IPv6 BIDIR-PIM (S, G) entry. In IPv6 BIDIR-PIM, this field displays only --, indicating that no upstream interface information is displayed. |
| List of 1 downstream interface | Indicates the downstream interface list. |
| Uptime | Indicates the period during which the (S, G) entry exists. |