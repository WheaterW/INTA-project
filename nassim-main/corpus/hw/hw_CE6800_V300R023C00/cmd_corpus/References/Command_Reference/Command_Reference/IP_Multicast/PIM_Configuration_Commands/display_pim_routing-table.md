display pim routing-table
=========================

display pim routing-table

Function
--------



The **display pim routing-table** command displays PIM routing entries in the PIM routing table.




Format
------

**display pim** { **vpn-instance** *vpn-instance-name* | **all-instance** } **routing-table** { *groupAddr* [ **mask** { *group-mask-length* | *group-mask-addr* } ] | *srcAddr* [ **mask** { *source-mask-length* | *source-mask-addr* } ] | **incoming-interface** { { *iif-port-type* *iif-port-num* | *iif-port-name* } | **register** } | **outgoing-interface** { **include** | **exclude** | **match** } { { *oif-port-type* *oif-port-num* | *oif-port-name* } | **register** | **none** } | **mode** { **ssm** | **sm** } | **flags** { **2msdp** | **act** | **del** | **exprune** | **ext** | **loc** | **msdp** | **niif** | **nonbr** | **none** | **rpt** | **sg\_rcvr** | **sgjoin** | **spt** | **swt** | **upchg** | **wc** | **excl** | **frrchg** | **pd** | **bs** } | **fsm** | **backup-incoming-interface** { *biif-port-type* *biif-port-num* | *biif-port-name* } } \* [ **outgoing-interface-number** [ *oif-number* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Displays information about unicast routes in a specified VPN instance.  vpn-instance-name specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name "\_public\_" cannot be used. The string can contain spaces if it is enclosed with double quotation marks ("). |
| **all-instance** | Indicates all VPN instances. | - |
| *groupAddr* | Specifies the address of a multicast group. This parameter is used to specify a multicast group and display the information about the routing table corresponding to the multicast group. | The value ranges from 224.0.0.0 to 239.255.255.255, in dotted decimal notation. |
| **mask** | Displays PIM routing entries of a specified multicast group or source address mask. | - |
| *group-mask-length* | Specifies the mask length of a multicast group. | The value is an integer that ranges from 4 to 32. |
| *group-mask-addr* | Indicates the mask of a multicast group. | The value is in dotted decimal notation. |
| *srcAddr* | Specifies a multicast source address. This parameter is used to specify a multicast source and display information about the routing table corresponding to the multicast source. | The value is in dotted decimal notation. |
| *source-mask-length* | Specifies the mask length of a multicast source. | The value is an integer that ranges from 0 to 32. |
| *source-mask-addr* | Specifies the mask of the multicast source address. | The value is in dotted decimal notation. |
| **incoming-interface** | Displays the routing entry with a specified inbound interface. | - |
| *iif-port-type* *iif-port-num* | Indicates the inbound interface. | - |
| *iif-port-name* | - | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| **register** | Displays PIM routing entries of register interfaces. | - |
| **outgoing-interface** | Displays PIM routing entries with a specified outbound interface. | - |
| **include** | Displays PIM routing entries of a specified interface in the outbound interface list. | - |
| **exclude** | Displays PIM routing entries that do not contain a specified interface in the outbound interface list. | - |
| **match** | Displays PIM routing entries of a specified interface in the outbound interface list. | - |
| *oif-port-type* *oif-port-num* | Specifies the outbound interface. | - |
| *oif-port-name* | - | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| **none** | Displays PIM routing entries with an empty outbound interface list. | - |
| **none** | Indicates the PIM routing entry with no specified flag. | - |
| **mode** | Displays PIM routing entries of a specified PIM running mode. | The value can be dm, sm or ssm, which indicates DM, SM and source-specific multicast (SSM) entries, respectively. |
| **ssm** | Indicates routing information of the PIM SSM protocol. | - |
| **sm** | Indicates PIM-SM routing information. | - |
| **flags** | Displays PIM routing entries that contain a specified flag.  flag-value specifies the type flag of entries. | flag-value: type of a routing entry. The value is -2msdp  * ac * del * exprune * ext * loc * msdp * niif * nonbr * none * rpt * sg\_rcvr * sgjoin * spt * swt * upchg * wc * excl * extranet * 2bgp * bgpvxlan * pd * bs |
| **2msdp** | Notifies the MSDP that the next SA message contains routing entries. | - |
| **act** | Indicates the multicast routing entry with received data. | - |
| **del** | Indicates the multicast routing entries to be deleted. | - |
| **exprune** | Indicates the routes with the ex-pruned flag. | - |
| **ext** | Indicates the routing entry that contains outbound interfaces contributed by multiple protocol components. | - |
| **loc** | Indicates the multicast routing entry on the directly connected network. | - |
| **msdp** | Indicates the routing entries learned from MSDP SA messages. | - |
| **niif** | Routing entry whose inbound interface is not determined. | - |
| **nonbr** | Indicates the neighbor mapping failure flag. | - |
| **rpt** | Indicates the information about routes on the shared tree. | - |
| **sg\_rcvr** | Indicates the routes learned from (s, g) Aux Join messages. | - |
| **sgjoin** | Indicates the routes learned from (s, g) Include Join messages. | - |
| **spt** | Routing information on the shortest path tree. | - |
| **swt** | Indicates the routing entry that has been switched to the shortest path tree. | - |
| **upchg** | Indicates the routing entry with the upstream changed. | - |
| **wc** | Indicates the routing entry with the wc flag. | - |
| **excl** | Indicates the routing entry whose downstream is in the exclude state. | - |
| **frrchg** | Indicates the route change flag, indicating that the current entry is using the backup upstream interface to forward data and is waiting for data from the primary upstream interface. | - |
| **pd** | This flag is displayed when there is a Join-Prune queue with delayed pruning. | - |
| **bs** | This flag is displayed when forwarding entries on the backup inbound interface of PIM FRR are suppressed. | - |
| **fsm** | Indicates the detailed information about the finite state machine of the protocol. | - |
| **backup-incoming-interface** | Displays routing entries with the backup inbound interface being the specified interface. | - |
| *biif-port-type* | Specifies the type of a backup interface. | - |
| *biif-port-num* | Specifies the number of a backup interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| *biif-port-name* | Specifies the name of a backup interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| **outgoing-interface-number** | Specifies the number of outbound interfaces. | - |
| *oif-number* | Indicates the number of outbound interfaces. | The value is an integer ranging from 0 to 2048. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

The **display pim routing-table** command displays contents in a PIM routing table, including information about multicast source and group addresses, RPs, inbound interfaces, and outbound interface lists in (S, G) and (\*, G) entries.

**Precautions**

If neither vpn-instance nor all-instance is specified, the command displays PIM routing entries of the public network instance.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display contents in the PIM-SM multicast routing.
```
<HUAWEI> display pim all-instance routing-table mode sm
VPN-Instance: public net
 Total 0 (*, G) entry; 1 (S, G) entry

 (192.168.0.2, 227.0.0.1)
     RP: 2.2.2.2
     Protocol: pim-sm, Flag: SPT LOC ACT
     UpTime: 02:54:43
     Upstream interface: 100GE1/0/1, Refresh time: 02:54:43
         Upstream neighbor: NULL
         RPF prime neighbor: NULL
     Downstream interface(s) information:
     Total number of downstreams: 1
         1: 100GE1/0/2
             Protocol: pim-sm, UpTime: 02:54:43, Expires: 00:02:47

```

**Table 1** Description of the **display pim routing-table** command output
| Item | Description |
| --- | --- |
| Total 0 (\*, G) entry; 1 (S, G) entry | Total number of (S, G) entries and (\*, G) entries in the PIM routing table. |
| Total number of downstreams | Total number of downstream interfaces. |
| Upstream neighbor | Upstream neighbor of the (S, G) entry or (\*, G) entry. |
| Upstream interface | Inbound interface of the (S, G) entry or (\*, G) entry. |
| Refresh time | Time when the upstream interface is refreshed. |
| RPF prime neighbor | RPF neighbor of the (S, G) entry or (\*, G) entry.   * For an (\*, G) entry, when the local device is an RP, the RPF neighbor is NULL. * For an (S, G) entry, when the local device is directly connected to the multicast source, the RPF neighbor is NULL. |
| Downstream interface(s) information | Information about the downstream interface, including:   * Total number of downstream interfaces. * Name of a downstream interface. * Type of the PIM protocol configured on the downstream interface. * Existing time and timeout period of the downstream interface. |
| VPN-Instance | VPN instance to which PIM routing information belongs. |
| RP | RP address. |
| Protocol | PIM protocol type: PIM-DM, PIM-SM, or PIM-SSM. |
| UpTime | UpTime under (S, G) or (\*, G) indicates the lifetime of the entry. UpTime in the interface list indicates the lifetime of the entry on the corresponding interface. |
| Expires | Timeout interval. |