display multicast vpn-instance routing-table
============================================

display multicast vpn-instance routing-table

Function
--------



The **display multicast vpn-instance routing-table** command displays information about multicast routing tables.




Format
------

**display multicast** { **vpn-instance** *vpn-instance-name* | **all-instance** } **routing-table** [ *group-address* [ **mask** { *group-mask-length* | *group-mask-addr* } ] | *source-address* [ **mask** { *source-mask-length* | *source-mask-addr* } ] | **incoming-interface** { { *iif-port-type* *iif-port-num* | *iif-port-name* } | **register** } | **backup-incoming-interface** { *biif-port-type* *biif-port-num* | *biif-port-name* } | **outgoing-interface** { **include** | **exclude** | **match** } { { *oif-port-type* *oif-port-num* | *oif-port-name* } | **register** | **none** } ] \* [ **outgoing-interface-number** [ *number* ] ]

**display multicast routing-table outgoing-interface-number** [ *number* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-address* | Displays information about a multicast routing table that contains a specified multicast group address. | The address is in dotted decimal notation. The value ranges from 224.0.1.0 to 239.255.255.255. |
| **mask** | Displays information about a multicast routing table that contains a specified multicast group or source address mask. | - |
| *group-mask-length* | Displays information about a multicast routing table in which the multicast group address mask has the specified length. | The value is a decimal integer ranging from 4 to 32. |
| *group-mask-addr* | Displays information about a multicast routing table that contains a specified multicast group address mask. | The address mask is in dotted decimal notation. |
| *source-address* | Displays information about a multicast routing table that contains a specified multicast source address. | The address is in dotted decimal notation. |
| *source-mask-length* | Displays information about a multicast routing table that contains the mask length of a specified source address. | The value is a decimal integer that ranges from 0 to 32. |
| *source-mask-addr* | Displays information about a multicast routing table that contains a specified source mask. | The address mask is in dotted decimal notation. |
| **incoming-interface** | Displays information about a multicast routing table that contains a specified inbound interface. | - |
| *iif-port-type* | Specifies the type of an inbound interface. | - |
| *iif-port-num* | Specifies the number of an inbound interface. | - |
| *iif-port-name* | Specifies the name of an inbound interface. | - |
| **register** | Displays information about a multicast routing table that contains a specified PIM-SM register interface. | - |
| **backup-incoming-interface** | Specifies the backup inbound interface. | - |
| *biif-port-type* | Indicates the type of the backup inbound interface. | - |
| *biif-port-num* | Specifies the number of the backup inbound interface. | - |
| *biif-port-name* | Specifies the name of the backup inbound interface. | - |
| **outgoing-interface** | Displays information about a multicast routing table that contains a specified outbound interface. | - |
| **include** | Displays the (S, G) entries whose downstream interface list contains specified downstream interfaces. | - |
| **exclude** | Displays the (S, G) entries whose downstream interface list does not contain specified downstream interfaces. | - |
| **match** | Displays (S, G) entries whose the downstream interface list contains only one interface that is the same as a specified downstream interface. | - |
| *oif-port-type* | Specifies the type of an outbound interface. | - |
| *oif-port-num* | Specifies the number of an outbound interface. | - |
| *oif-port-name* | Specifies the name of an outbound interface. | - |
| **none** | Displays information about a multicast routing table that contains a null outbound interface list. | - |
| **vpn-instance** *vpn-instance-name* | Displays information about the multicast routing table in a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **outgoing-interface-number** | Displays information about a multicast routing table that contains a specified number of outbound interfaces. | - |
| *number* | Specifies the number of outbound interfaces. | The value is an integer that ranges from 0 to 2048. |
| **all-instance** | Displays information about multicast routing tables in all instances. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

The **display multicast vpn-instance routing-table** command is used to display the information of a multicast routing table.

**Precautions**

When the **display multicast routing-table** command is used, the following situations occur:

* If vpn-instance or all-instance is not specified, information about the multicast routing table of the public network instance is displayed.
* If group-address is specified, information about the multicast routing table to which a specified multicast group corresponds is displayed.
* If group-address mask is specified, information about the multicast routing table to which a multicast group address within a specified address range corresponds is displayed.
* If source-address is specified, information about the multicast routing table to which a specified multicast source address corresponds is displayed.
* If source-address mask is specified, information about the multicast routing table to which a multicast source address within a specified address range corresponds is displayed.
* If outgoing-interface-number is specified, the number of downstream interfaces of multicast routing entries is displayed.
* If number is specified, information about the multicast groups corresponding to the number of downstream interfaces is displayed.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the multicast routing table of the VPN instance VPNA on the sender PE after an NG MVPN is configured.
```
<HUAWEI> display multicast vpn-instance VPNA routing-table
Multicast routing table of VPN-Instance: VPNA
 Total 0 (*, G) entry; 1 (S, G) entry

 00001: (10.0.5.101, 225.1.0.0)
       Uptime: 01:44:00
       Upstream Interface: 100GE1/0/1
       List of 1 downstream interface
           1: pseudo

```

# Display the multicast routing table of the VPN instance VPNA on the receiver PE after an NG MVPN is configured.
```
<HUAWEI> display multicast vpn-instance VPNA routing-table
Multicast routing table of VPN-Instance: VPNA
 Total 1 entry
 00001. (1.1.1.1, 224.1.1.1)
       Uptime: 00:12:21
       Upstream Interface: pseudo
       List of 1 downstream interface
           1: Vlanif10

```

**Table 1** Description of the **display multicast vpn-instance routing-table** command output
| Item | Description |
| --- | --- |
| Multicast routing table of VPN-Instance | VPN instance to which the multicast routing information corresponds. |
| Total 1 entry | Number of eligible routing entries. |
| Upstream Interface | Upstream interface of the (S, G) entry or MVPN extranet entry. |
| List of 1 downstream interface | Downstream interface list. |
| (10.0.5.101, 225.1.0.0) | (S, G) entry in the multicast routing table. |
| 00001 | Sequence number of the (S, G) entry. |
| Uptime | Indicates the period during which the (S, G) entry exists. |