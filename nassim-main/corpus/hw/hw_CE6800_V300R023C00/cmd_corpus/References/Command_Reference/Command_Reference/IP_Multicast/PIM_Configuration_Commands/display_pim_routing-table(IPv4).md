display pim routing-table(IPv4)
===============================

display pim routing-table(IPv4)

Function
--------



The **display pim routing-table** command displays PIM routing entries in the PIM routing table.




Format
------

**display pim routing-table brief** [ *groupAddr* [ **mask** { *group-mask-length* | *group-mask-addr* } ] | *srcAddr* [ **mask** { *source-mask-length* | *source-mask-addr* } ] | **incoming-interface** { { *iif-port-type* *iif-port-num* | *iif-port-name* } | **register** } ] \*

**display pim** { **vpn-instance** *vpn-instance-name* | **all-instance** } **routing-table** **brief** [ *groupAddr* [ **mask** { *group-mask-length* | *group-mask-addr* } ] | *srcAddr* [ **mask** { *source-mask-length* | *source-mask-addr* } ] | **incoming-interface** { { *iif-port-type* *iif-port-num* | *iif-port-name* } | **register** } ] \*

**display pim routing-table outgoing-interface-number** [ *oif-number* ]

**display pim routing-table** [ *groupAddr* [ **mask** { *group-mask-length* | *group-mask-addr* } ] ] **rpf-interface** { *iif-port-type* *iif-port-num* | *iif-port-name* } [ **outgoing-interface** { **include** | **exclude** | **match** } { { *oif-port-type* *oif-port-num* | *oif-port-name* } | **none** } | **flags** { **wc** | **act** | **niif** } | **fsm** ] \* [ **outgoing-interface-number** [ *oif-number* ] ]

**display pim** { **vpn-instance** *vpn-instance-name* | **all-instance** } **routing-table**

**display pim routing-table** { *groupAddr* [ **mask** { *group-mask-length* | *group-mask-addr* } ] | *srcAddr* [ **mask** { *source-mask-length* | *source-mask-addr* } ] | **incoming-interface** { { *iif-port-type* *iif-port-num* | *iif-port-name* } | **register** } | **outgoing-interface** { **include** | **exclude** | **match** } { { *oif-port-type* *oif-port-num* | *oif-port-name* } | **register** | **none** } | **mode** { **dm** | **ssm** | **sm** } | **flags** { **2msdp** | **act** | **del** | **exprune** | **ext** | **loc** | **msdp** | **niif** | **nonbr** | **none** | **rpt** | **sg\_rcvr** | **sgjoin** | **spt** | **swt** | **upchg** | **wc** | **excl** | **frrchg** | **pd** | **bs** } | **fsm** | **backup-incoming-interface** { *biif-port-type* *biif-port-num* | *biif-port-name* } } \* [ **outgoing-interface-number** [ *oif-number* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *groupAddr* | Displays PIM routing entries that contain a specified group address. | The value ranges from 224.0.0.0 to 239.255.255.255, in dotted decimal notation. |
| **mask** | Displays PIM routing entries that contain a specified source or group address mask. | - |
| *group-mask-length* | Displays PIM routing entries that contain a specified group address mask length.  group-mask-length specifies the length of a group address mask. | The value is an integer that ranges from 4 to 32. |
| *group-mask-addr* | Displays PIM routing entries that contain a specified group address mask. | The value is in dotted decimal notation. |
| *srcAddr* | Displays PIM routing entries that contain a specified source address. | The value is in dotted decimal notation. |
| *source-mask-length* | Displays PIM routing entries that contain a specified source address mask length. | The value is an integer ranging from 0 to 32. |
| *source-mask-addr* | Displays PIM routing entries that contain a specified source address mask. | The value is in dotted decimal notation. |
| **incoming-interface** | Displays PIM routing entries of a specified inbound interface. | - |
| *iif-port-type* | Specifies the type of an inbound interface. | - |
| *iif-port-num* | Specifies the number of an inbound interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| *iif-port-name* | Specifies the name of an inbound interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **register** | Displays PIM routing entries of register interfaces. | - |
| **brief** | Summary information. | - |
| **vpn-instance** *vpn-instance-name* | Displays PIM routing entries of a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all-instance** | Displays PIM routing entries of all instances. | - |
| **outgoing-interface-number** *oif-number* | Specify the number of interfaces. | - |
| **outgoing-interface** | Displays PIM routing entries of outbound interfaces. | - |
| **include** | Displays PIM routing information of interfaces that are included in the outbound interface list. | - |
| **exclude** | Displays PIM routing entries of interfaces that are excluded from the outbound interface list. | - |
| **match** | Displays PIM routing entries of a specified interface in the outbound interface list. | - |
| *oif-port-type* | Specifies the outbound interface type. | - |
| *oif-port-num* | Specifies the outbound interface number. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| *oif-port-name* | Specifies the outbound interfacename. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **none** | Indicates that the downstream interface list does not have any routing entry.  Displays PIM routing entries of an outbound interface list that does not contain any interfaces. | - |
| **mode** | Displays PIM routing entries of a specified PIM mode. | - |
| **ssm** | Source specific multicast routes. | - |
| **sm** | Sparse mode routes. | - |
| **flags** | Routes matching these flags. | - |
| **2msdp** | Indicates that the RP receives a Register message recently and learns the (S, G) entry. The RP prepares to inform Multicast Source Discovery Protocol (MSDP) of the source active (SA) message that contains the (S, G) entry. | - |
| **act** | Indicates that the multicast routing entry at which actual data arrives exists. | - |
| **del** | Indicates the multicast routing entry to be deleted. | - |
| **exprune** | Indicates that the entry on the rendezvous point tree (RPT) is pruned and no receiver on the RPT requests the information sent by the source. | - |
| **ext** | Indicates routing entries that contain outgoing interfaces provided by other multicast routing protocols. | - |
| **loc** | Indicates routing entries on the router directly connected to the network segment where the multicast source resides. | - |
| **msdp** | Indicates the routing entries learned from recently received MSDP SA messages. | - |
| **niif** | Indicates routing entries with unknown incoming interfaces. | - |
| **nonbr** | Indicates that the routing entry of the upstream neighbor address (link-local address) towards the RP or the source is not found. | - |
| **rpt** | Indicates the routing entries that are on the RPT but do not use the RPT data. | - |
| **sg\_rcvr** | Indicates that the source S has local (S, G) receivers and PIM is the owner of the downstream interface. | - |
| **sgjoin** | Indicates that the source S has local (S, G) receivers but PIM is not the owner of the downstream interface. | - |
| **spt** | Indicates routing entries on the shortest path tree (SPT). | - |
| **swt** | Indicates routing entries during the SPT switchover. | - |
| **upchg** | Identifies the route change. It indicates that the current entry uses the original upstream interface to forward data and waits for data received from a new interface. | - |
| **wc** | Indicates a (\*, G) entry. | - |
| **excl** | Indicates an (S, G) entry created after an IGMPv3 message in exclude mode is received. | - |
| **fsm** | Detailed information of FSM states. | - |
| **rpf-interface** | Displays PIM routing entries of reverse path forwarding (RPF) interfaces. | - |
| **dm** | Dense mode routes. | - |
| **pd** | Indicates Join-Prune queue in pruning delay mode exists. | - |
| **bs** | Indicates backup inbound interface forwarding entry is suppressed in PIM FRR. | - |
| **frrchg** | Specifies the type of a frrchg routing entry. | - |
| **backup-incoming-interface** | Displays routing entries with the backup inbound interface being the specified interface. | - |
| *biif-port-type* | Specifies the type of a backup interface. | - |
| *biif-port-num* | Specifies the number of a backup interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| *biif-port-name* | Specifies the name of a backup interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |



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

* If vpn-instance or all-instance is specified, no VPN instance can be specified for an outbound interface. That is, neither vpn-instance nor all-instance can be specified after outgoing-interface is specified.
* If neither vpn-instance nor all-instance is specified, the command displays PIM routing entries of the public network instance.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the PIM-SM multicast routing table of the public network instance.
```
<HUAWEI> display pim routing-table
VPN-Instance: public net
 Total 0 (*, G) entry; 1 (S, G) entry
 (192.168.0.2, 239.0.0.1)
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

# Display information about the PIM routes of the public network instance in PIM-DM mode.
```
<HUAWEI> display pim routing-table
 VPN-Instance: public net
 Total 0 (*, G) entry; 1 (S, G) entry
 (10.1.4.100, 239.1.1.1)
     Protocol: pim-dm, Flag: LOC ACT 
     UpTime: 00:08:18     
     Upstream interface: 100GE1/0/1, Refresh time: 00:08:18
         Upstream neighbor: NULL
         RPF prime neighbor: NULL
     Downstream interface(s) information:
     Total number of downstreams: 1
        1: 100GE1/0/2
             Protocol: pim-dm, UpTime: 00:08:18, Expires: never

```

# Display the PIM multicast routing table of the public network instance after multicast replication is configured on a VXLAN network.
```
<HUAWEI> display pim routing-table
 VPN-Instance: public net
 Total 1 (*, G) entry; 2 (S, G) entries
 (*, 239.0.0.1)
     RP: NULL
     Protocol: pim-sm, Flag: WC NIIF 
     UpTime: 00:29:50     
     Upstream interface: NULL, Refresh time: 00:29:50
         Upstream neighbor: NULL
         RPF prime neighbor: NULL
     Downstream interface(s) information:
     Total number of downstreams: 1
        1: Nve
             Protocol: vxlan, UpTime: 00:29:50, Expires: -
 (4.4.4.4, 239.0.0.1)
     RP: NULL
     Protocol: pim-sm, Flag: SPT LOC VXLAN 
     UpTime: 00:12:05     
     Upstream interface: LoopBack0, Refresh time: 00:12:05
         Upstream neighbor: NULL
         RPF prime neighbor: NULL
     Downstream interface(s) information:
     Total number of downstreams: 1
        1: 100GE1/0/1
             Protocol: pim-sm, UpTime: 00:12:05, Expires: 00:03:25
 (5.5.5.5, 239.0.0.1)
     RP: NULL
     Protocol: pim-sm, Flag: SPT SG_RCVR 
     UpTime: 00:11:39     
     Upstream interface: 100GE1/0/1, Refresh time: 00:11:39
         Upstream neighbor: 1.1.1.2
         RPF prime neighbor: 1.1.1.2
     Downstream interface(s) information:
     Total number of downstreams: 1
        1: Nve
             Protocol: vxlan, UpTime: 00:11:39, Expires: -

```

**Table 1** Description of the **display pim routing-table(IPv4)** command output
| Item | Description |
| --- | --- |
| Total 0 (\*, G) entry; 1 (S, G) entry | Total number of (S, G) and (\*, G) entries in the PIM routing table. |
| Total number of downstreams | Number of downstream interfaces. |
| (192.168.0.2, 239.0.0.1) | (S, G) entry in the PIM routing table. |
| Upstream neighbor | Upstream neighbor of the (S, G) or (\*, G) entry. |
| Upstream interface | Inbound interface of the (S, G) or (\*, G) entry. |
| Refresh time | Refresh time of upstream interface. |
| RPF prime neighbor | RPF neighbor of the (S, G) or (\*, G) entry.   * For the (\*, G) entry, when the local device is an RP, the RPF neighbor in the (\*, G) entry is NULL. * For the (S, G) entry, when the local device is directly connected to a source, the RPF neighbor in the (S, G) entry is NULL. |
| Downstream interface(s) information | Information about downstream interfaces, including:   * Total number of downstream interfaces. * Name of a downstream interface. * PIM protocol type configured for a downstream interface. * Keepalive period and timeout period of a downstream interface. |
| VPN-Instance | Instance in which PIM routing entries are displayed. |
| RP | RP address. |
| Flag | Flag of a PIM (S, G) or (\*, G) entry. For details.  Run the display pim routing-table command on the MSDP peer nearest to the source to view routing information. If an (S, G) entry does not have a 2MSDP flag, the MSDP peer is not an RP. Change the configurations of the RP or MSDP peer on the PIM-SM network to ensure that the MSDP peer is an RP. |
| UpTime | UpTime in (S, G) or (\*, G) indicates the lifetime of the entry. UpTime in the interface list indicates the lifetime of the entry on the corresponding interface. |
| Expires | Timeout period of the (S, G) or (\*, G) entry. |
| vxlan | Indicates routing entries learned from the VXLAN network after multicast replication is enabled on the VXLAN network. |
| Protocol | PIM protocol type, which can be PIM-DM, PIM-SM or PIM-SSM. |
| Backup designated router | Backup designated router. |