display pim ipv6 routing-table
==============================

display pim ipv6 routing-table

Function
--------



The **display pim ipv6 routing-table** command displays information about an IPv6 PIM routing table.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display pim ipv6 routing-table** [ *groupAddr* [ **mask** *group-mask-length* ] | *srcAddr* [ **mask** *source-mask-length* ] | **incoming-interface** { { *iif-port-type* *iif-port-num* | *iif-port-name* } | **register** } | **outgoing-interface** { **include** | **exclude** | **match** } { { *oif-port-type* *oif-port-num* | *oif-port-name* } | **register** | **none** } | **mode** { **ssm** | **sm** } | **flags** { **act** | **del** | **exprune** | **ext** | **loc** | **niif** | **nonbr** | **none** | **rpt** | **sg\_rcvr** | **sgjoin** | **spt** | **swt** | **upchg** | **wc** | **excl** } | **fsm** ] \* [ **outgoing-interface-number** [ *oif-number* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *groupAddr* | Specifies the IPv6 address of a multicast group. | The address is in the format of X:X:X:X:X:X:X:X. |
| **mask** *group-mask-length* | Specifies the mask length of a multicast group. | The value is an integer.The mask length of the address of a multicast group ranges from 8 to 128. |
| **mask** *source-mask-length* | Specifies the mask length of a multicast source. | The value is an integer. The mask length of the address of a multicast source ranges from 0 to 128. |
| *srcAddr* | Specifies the IPv6 address of a multicast source. | The address is in the format of X:X:X:X:X:X:X:X. |
| **incoming-interface** *iif-port-type* *iif-port-num* | Displays the PIM routing entries with specified upstream interfaces. | - |
| *iif-port-name* | Displays the PIM routing entries with specified upstream interfaces. | - |
| **register** | Displays information about a register interface. | - |
| **outgoing-interface** *oif-port-type* *oif-port-num* | Displays the PIM routing entries with specified downstream interfaces. | - |
| **include** | Displays the (S, G) routing entries with a specified downstream interface included. | If this keyword is set, the type and number of an interface must be specified. |
| **exclude** | Displays the (S, G) routing entries with a specified downstream interface excluded. | If this keyword is set, the type and number of an interface must be specified. |
| **match** | Displays the (S, G) routing entries with the downstream interfaces being a specified interface. | If the type and number of the interface is not specified, the (S, G) routing entries with no downstream interfaces are displayed. |
| *oif-port-name* | Displays the PIM routing entries with specified downstream interfaces. | - |
| **none** | Displays the PIM routing entries with no downstream interfaces. | - |
| **mode** | Indicates an IPv6 PIM mode. | - |
| **ssm** | Displays Protocol Independent Multicast-Source-Specific Multicast (PIM-SSM) routing entries. | - |
| **sm** | Displays Protocol Independent Multicast-Sparse Mode (PIM-SM) routing entries. | - |
| **flags** | Indicates the type of a routing entry. | The type flag of entries can be the following values:   * act * del * exprune * ext * loc * niif * nonbr * none * rpt * sg\_rcvr * sgjoin * spt * swt * upchg * wc * excl |
| **fsm** | Indicates the details of FSM states. | - |
| **outgoing-interface-number** *oif-number* | Displays the IPv6 PIM routing entries with a specified number of downstream interfaces. | - |



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


# Display information about an IPv6 PIM routing table.
```
<HUAWEI> display pim ipv6 routing-table
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

# Display the IPv6 PIM routing entries with a specified number of downstream interfaces.
```
<HUAWEI> display pim ipv6 routing-table outgoing-interface-number
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

**Table 1** Description of the **display pim ipv6 routing-table** command output
| Item | Description |
| --- | --- |
| Total 1 (\*, G) entry; 1 (S, G) entry | Total number of (S, G) entries and (\*, G) entries in the PIM routing table. |
| Total number of downstreams | Total number of downstream interfaces. |
| (\*, FFE3::1) | (\*, G) entry in the PIM routing table. |
| Upstream interface | Inbound interface of an (S, G) entry or (\*, G) entry. |
| Upstream neighbor | Upstream neighbor of the (S, G) entry or (\*, G) entry. |
| Refresh time | Time when the upstream interface was refreshed. |
| RPF prime neighbor | RPF neighbor of the (S, G) entry or (\*, G) entry:   * For an (\*, G) entry, when the local router is an RP, the RPF neighbor is Nullz. * For an (S, G) entry, when the local router is directly connected to the multicast source, the RPF neighbor is Null. |
| Downstream interface(s) information | Information about downstream interfaces, including:   * Total number of downstream interfaces. * Downstream interface name. * Type of the PIM protocol configured on the downstream interface. * Existing time and timeout period of the downstream interface. |
| VPN-Instance | VPN instance to which PIM routing information belongs. |
| Protocol | PIM protocol type, which can be PIM-SM or PIM-SSM. |
| Flag | Flag of a PIM (S, G) entry or (\*, G) entry. |
| UpTime | UpTime under (S, G) or (\*, G) indicates the lifetime of the entry. UpTime in the interface list indicates the lifetime of the entry on the corresponding interface. |
| Expires | Timeout interval. |
| RP | RP address. |