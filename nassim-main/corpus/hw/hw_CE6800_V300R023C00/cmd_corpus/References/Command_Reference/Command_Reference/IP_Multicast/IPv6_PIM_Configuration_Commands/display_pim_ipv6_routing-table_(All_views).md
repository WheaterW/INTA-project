display pim ipv6 routing-table (All views)
==========================================

display pim ipv6 routing-table (All views)

Function
--------



The **display pim ipv6 routing-table** command displays information about an IPv6 PIM routing table.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display pim ipv6** { **vpn-instance** *vpn-instance-name* | **all-instance** } **routing-table** [ *groupAddr* [ **mask** *group-mask-length* ] | *srcAddr* [ **mask** *source-mask-length* ] | **incoming-interface** { { *iif-port-type* *iif-port-num* | *iif-port-name* } | **register** } | **outgoing-interface** { **include** | **exclude** | **match** } { { *oif-port-type* *oif-port-num* | *oif-port-name* } | **register** | **none** } | **mode** { **ssm** | **sm** } | **flags** { **act** | **del** | **exprune** | **ext** | **loc** | **niif** | **nonbr** | **none** | **rpt** | **sg\_rcvr** | **sgjoin** | **spt** | **swt** | **upchg** | **wc** | **excl** } | **fsm** ] \* [ **outgoing-interface-number** [ *oif-number* ] ]

**display pim ipv6** { **vpn-instance** *vpn-instance-name* | **all-instance** } **routing-table** [ *groupAddr* [ **mask** *group-mask-length* ] ] { **rpf-interface** { *iif-port-type* *iif-port-num* | *iif-port-name* } } \* [ **outgoing-interface** { **include** | **exclude** | **match** } { { *oif-port-type* *oif-port-num* | *oif-port-name* } | **none** } | **flags** { **wc** | **act** | **niif** } | **fsm** ] \* [ **outgoing-interface-number** [ *oif-number* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **all-instance** | Indicates all VPN instances. | - |
| *groupAddr* | Specifies the IPv6 address of a multicast group. | The format is X:X:X:X:X:X:X:X. |
| **mask** *group-mask-length* | Specifies the mask length of a multicast group. | The value is an integer that ranges from 0 to 128. |
| **mask** *source-mask-length* | Specifies the mask length for a multicast source address. | The value is an integer. The mask length of the multicast source ranges from 0 to 128. |
| *srcAddr* | Specifies the IPv6 address of a multicast source. | The format is X:X:X:X:X:X:X:X. |
| **incoming-interface** *iif-port-type* *iif-port-num* | Displays the routing entry with a specified inbound interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| *iif-port-name* | Displays the routing entry with a specified inbound interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **register** | Register interface. | - |
| **outgoing-interface** *oif-port-type* *oif-port-num* | Displays the PIM routing entries with specified downstream interfaces. | The values of outgoing-interface are as follows:   * include * exclude * match |
| **include** | Indicates all PIM routing entries that contain the specified outbound interface. | - |
| **exclude** | Indicates all PIM routing entries that do not contain the specified outbound interface. | - |
| **match** | Indicates the PIM routing entries that contain only the specified outbound interface. | - |
| *oif-port-name* | Displays the PIM routing entries with specified downstream interfaces. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **none** | Indicates the PIM routing entry without the specified flag. | - |
| **mode** | Indicates an IPv6 PIM mode. | - |
| **ssm** | Displays routing entries of a specified source mode. | - |
| **sm** | Displays routing entries in sparse mode. | - |
| **flags** | Indicates the type of a routing entry. | Type of a routing entry:   * act: indicates that the multicast routing entry has received actual data. * del: Multicast routing entries are to be deleted. * exprune: indicates that the entry on the rendezvous point tree (RPT) is pruned and no receiver on the RPT is interested in the source. * ext: indicates that a multicast routing entry contains the outbound interfaces contributed by other multicast routing protocols. * loc: indicates the routing entry directly connected to the network segment of the multicast source. * niif: indicates that the inbound interface of the multicast routing entry is not determined. * nonbr: indicates that the upstream neighbor address (link-local address) towards the RP or source cannot be found. * none: The outbound interface list is empty. * rpt: indicates the routing entry on the RPT. * sg\_rcvr: indicates the local (S, G) receiver of S, and PIM is the owner of the downstream interface. * sgjoin: The device is the local (S, G) receiver of S, but PIM is not the owner of the downstream interface. * spt: indicates the routing entry on the SPT. * swt: indicates the routing entry during the switchover to the SPT. * upchg: indicates that the current entry is using the original upstream interface to forward data and is waiting for data to arrive from a new interface. * wc: (\*, G) entry; * excl: indicates the (S, G) entry created when the device receives an IGMPv3 message in exclude mode. * bgp: routing entries learned from Source Active A-D routes received by BGP; * 2bgp: BGP is ready to advertise Source Active A-D routes. * frrchg: indicates that the current entry uses the backup upstream interface to forward data and is waiting for data from the master upstream interface. |
| **act** | Indicates the multicast routing entry that has actual data. | - |
| **del** | Indicates the multicast routes to be deleted. | - |
| **exprune** | Routes which are ex-pruned. | - |
| **ext** | Indicates the routing entry with one or more interfaces owned by other components. | - |
| **loc** | Indicates the multicast routing entry on the directly connected network. | - |
| **niif** | Indicates the routing entry without the inbound interface. | - |
| **nonbr** | Indicates the neighbor mapping failure flag. | - |
| **rpt** | Displays related routing information on the shared tree. | - |
| **sg\_rcvr** | Indicates the routes learned from (s, g) Aux Join messages. | - |
| **sgjoin** | Routes with active (S, G) joins. | - |
| **spt** | Displays routing information on the shortest path tree. | - |
| **swt** | Indicates the routing entry that has been switched to the shortest path tree. | - |
| **upchg** | Indicates the routing entry whose upstream interface is changed. | - |
| **wc** | Indicates the routing entry with the wc flag. | - |
| **excl** | Indicates the routing entry whose downstream interface is in the exclude state. | - |
| **fsm** | Displays detailed information about the finite state machine (FSM). | - |
| **outgoing-interface-number** *oif-number* | Displays the number of the outbound interfaces of IPv6 PIM routing entries. | - |
| **rpf-interface** | Indicates the RPF interface of a PIM route. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display pim ipv6 routing-table** command is used to display the contents of an IPv6 PIM routing table, including the source addresses and group addresses, Rendezvous Points (RPs), and upstream interface and downstream interface lists of the (S, G) and (\*, G) entries.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the IPv6 PIM routing entries with a specified number of downstream interfaces.
```
<HUAWEI> display pim ipv6 all-instance routing-table mode sm outgoing-interface-number
 VPN-Instance: public net
 Total 2 (*, G) entries; 0 (S, G) entry

 (*, FF25::1)
     RP: 2001:DB8:1::1 (local)
     Protocol: pim-sm, Flag: WC
     UpTime: 00:00:04
     Upstream interface: Register, Refresh time: 00:00:04
         Upstream neighbor: NULL
         RPF prime neighbor: NULL
     Downstream interface(s) information:
     Total number of downstreams: 2048

 (*, FF25::2)
     RP: 2001:DB8:1::1 (local)
     Protocol: pim-sm, Flag: WC
     UpTime: 00:00:05
     Upstream interface: Register, Refresh time: 00:00:05
         Upstream neighbor: NULL
         RPF prime neighbor: NULL
     Downstream interface(s) information:
     Total number of downstreams: 2048

```

# Display the IPv6 PIM routing table of the backup upstream interface that is through-BGP.
```
<HUAWEI> display pim ipv6 all-instance routing-table backup-incoming-interface through-bgp
 VPN-Instance: ng_bier
 Total 2 (*, G) entries; 2 (S, G) entries 
 
 Total matched 0 (*, G) entry; 1 (S, G) entry
 
 (2001:DB8:1::6, FF1E::4)
     RP: 2001:DB8:1::2 
     Protocol: pim-sm, Flag: SPT ACT BGP 
     UpTime: 19:12:08
     Upstream interface: through-BGP, Refresh time: 19:12:08     
         Upstream neighbor: ::FFFF:1.1.1.2
         RPF prime neighbor: ::FFFF:1.1.1.2
     Backup upstream interface: through-BGP
         Backup upstream neighbor: ::FFFF:1.1.1.3
         Backup RPF prime neighbor: ::FFFF:1.1.1.3
     Downstream interface(s) information:
     Total number of downstreams: 1
        1: 100GE1/0/1.1
             Protocol: pim-sm, UpTime: 19:12:08, Expires: -

```

# Display information about an IPv6 PIM routing table.
```
<HUAWEI> display pim ipv6 all-instance routing-table mode sm
VPN-Instance: public net
Total 1 (*, G) entry; 1 (S, G) entry

(*, FFE3::1)
  Protocol: pim-sm, Flag: WC
  UpTime: 00:57:31
  Upstream interface: NULL, Refresh time: 00:57:31
     Upstream neighbor: NULL
     RPF prime neighbor: NULL
  Downstream interface(s) information:
  Total number of downstreams: 1
     1: 100GE1/0/1
         Protocol: static, UpTime: 00:57:31, Expires: never

(2001:DB8:1::1, FFE3::1)
  Protocol: pim-sm, Flag:
  UpTime: 00:04:24
  Upstream interface: 100GE1/0/2, Refresh time: 00:04:24
    Upstream neighbor: FE80::A01:100:1
    RPF prime neighbor: FE80::A01:100:1
 Downstream interface(s) information:
 Total number of downstreams: 1
    1: 100GE1/0/1
        Protocol: pim-sm, UpTime: 00:04:24, Expires:  -

```

**Table 1** Description of the **display pim ipv6 routing-table (All views)** command output
| Item | Description |
| --- | --- |
| Total 1 (\*, G) entry; 1 (S, G) entry | Total number of (S, G) entries and (\*, G) entries in the PIM routing table. |
| Total number of downstreams | Total number of downstream interfaces. |
| (\*, FFE3::1) | (\*, G) entry in the PIM routing table. |
| Upstream interface | Upstream interface of an (S, G) entry or (\*, G) entry. |
| Upstream neighbor | Upstream neighbor of an (S, G) entry or (\*, G) entry. |
| Refresh time | Refresh time of upstream interface. |
| RPF prime neighbor | RPF neighbor of an (S, G) entry or (\*, G) entry.   * For an (\*, G) entry, when the local router is an RP, the RPF neighbor is Null. * For an (S, G) entry, when the local router is directly connected to the multicast source, the RPF neighbor is Null. |
| Downstream interface(s) information | Information about downstream interfaces, including:   * Total number of downstream interfaces. * Downstream interface name. * Type of the PIM protocol configured on the downstream interface. * Existing period and timeout period of the downstream interface. |
| Backup upstream interface | Backup upstream interface of an (S, G) entry. |
| Backup upstream neighbor | Backup upstream neighbor of an (S, G) entry. |
| Backup RPF prime neighbor | Backup RPF neighbor of an (S, G) entry. |
| VPN-Instance | VPN instance to which PIM route information belongs. |
| Protocol | PIM protocol type, which can be PIM-SM or PIM-SSM. |
| Flag | Flag of a PIM (S, G) entry or (\*, G) entry. |
| UpTime | UpTime under (S, G) or (\*, G) indicates the lifetime of the entry. UpTime under the interface list indicates the lifetime of the entry on the corresponding interface. |
| Expires | Timeout interval. |
| RP | RP information. |