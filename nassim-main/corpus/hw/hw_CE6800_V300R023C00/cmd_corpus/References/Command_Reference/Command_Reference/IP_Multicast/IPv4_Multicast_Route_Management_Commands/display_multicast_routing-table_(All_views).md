display multicast routing-table (All views)
===========================================

display multicast routing-table (All views)

Function
--------



The **display multicast routing-table** command displays information about multicast routing tables.




Format
------

**display multicast routing-table** { *groupAddr* [ **mask** { *group-mask-length* | *group-mask-addr* } ] | *srcAddr* [ **mask** { *source-mask-length* | *source-mask-addr* } ] | **incoming-interface** { { *iif-port-type* *iif-port-num* | *iif-port-name* } | **register** } | **backup-incoming-interface** { *biif-port-type* *biif-port-num* | *biif-port-name* } | **outgoing-interface** { **include** | **exclude** | **match** } { { *oif-port-type* *oif-port-num* | *oif-port-name* } | **register** | **none** } } \* [ **outgoing-interface-number** [ *oif-number* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *groupAddr* | Displays information about a multicast routing table that contains a specified multicast group address. | The address is in dotted decimal notation. The value ranges from 224.0.1.0 to 239.255.255.255. |
| **mask** | Displays information about a multicast routing table that contains a specified multicast group or source address mask. | - |
| *group-mask-length* | Displays information about a multicast routing table in which the multicast group address mask has the specified length. | The value is a decimal integer ranging from 4 to 32. |
| *group-mask-addr* | Displays information about a multicast routing table that contains a specified multicast group address mask. | The address mask is in dotted decimal notation. |
| *srcAddr* | Displays information about a multicast routing table that contains a specified multicast source address. | The address is in dotted decimal notation. |
| *source-mask-length* | Displays information about a multicast routing table that contains the mask length of a specified source address. | The value is a decimal integer that ranges from 0 to 32. |
| *source-mask-addr* | Displays information about a multicast routing table that contains a specified source mask. | The address mask is in dotted decimal notation. |
| **incoming-interface** | Displays information about a multicast routing table that contains a specified inbound interface. | - |
| *iif-port-type* | Specifies the type of an inbound interface. | - |
| *iif-port-num* | Specifies the number of an inbound interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| *iif-port-name* | Specifies the name of an inbound interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **register** | Displays information about a multicast routing table that contains a specified PIM-SM register interface. | - |
| **backup-incoming-interface** | Specifies a backup inbound interface. | - |
| *biif-port-type* | Indicates the type of the backup inbound interface. | - |
| *biif-port-num* | Specifies the number of the backup inbound interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| *biif-port-name* | Specifies the name of the backup inbound interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| **outgoing-interface** | Displays information about a multicast routing table that contains a specified outbound interface. | - |
| **include** | Displays the (S, G) entries whose downstream interface list contains specified downstream interfaces. | - |
| **exclude** | Displays the (S, G) entries whose downstream interface list does not contain specified downstream interfaces. | - |
| **match** | Displays (S, G) entries whose the downstream interface list contains only one interface that is the same as a specified downstream interface. | - |
| *oif-port-type* | Specifies the type of an outbound interface. | - |
| *oif-port-num* | Specifies the number of an outbound interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| *oif-port-name* | Specifies the name of an outbound interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **none** | Displays information about a multicast routing table that contains a null outbound interface list. | - |
| **outgoing-interface-number** | Displays information about a multicast routing table that contains a specified number of outbound interfaces. | - |
| *oif-number* | Specifies the number of outbound interfaces. | The value is an integer that ranges from 0 to 2048. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display multicast all-instance routing-table** command is used to display the information of a multicast routing table.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display routing entries in the multicast routing table of the public network instance.
```
<HUAWEI> display multicast routing-table
Multicast routing table of VPN Instance: public net
Total 0 (*, G) entry; 1 (S, G) entries
 00001: (192.168.0.2, 227.0.0.1)
       Uptime: 00:00:28
       Upstream Interface: 100GE1/0/1
       List of 2 downstream interfaces
           1:  100GE1/0/2
           2:  100GE1/0/3

```

**Table 1** Description of the **display multicast routing-table (All views)** command output
| Item | Description |
| --- | --- |
| Multicast routing table of VPN Instance | VPN instance to which the multicast routing information corresponds. |
| Total 0 (\*, G) entry; 1 (S, G) entries | Number of eligible routing entries. |
| (192.168.0.2, 227.0.0.1) | (S, G) entry in the multicast routing table. |
| Upstream Interface | Upstream interface of the (S, G) entry. |
| List of 2 downstream interfaces | Downstream interface list. |
| 00001 | Sequence number of the (S, G) entry. |
| Uptime | Indicates the period during which the (S, G) entry exists. |