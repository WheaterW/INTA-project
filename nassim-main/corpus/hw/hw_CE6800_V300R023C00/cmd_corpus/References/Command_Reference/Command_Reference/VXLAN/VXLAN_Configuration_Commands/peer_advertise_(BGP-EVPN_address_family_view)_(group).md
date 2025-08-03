peer advertise (BGP-EVPN address family view) (group)
=====================================================

peer advertise (BGP-EVPN address family view) (group)

Function
--------



The **peer advertise** command enables a device to advertise ND, IRBv6, ARP or IRB routes to a BGP EVPN peer.

The **undo peer advertise** command restores the default configuration.



By default, a device does not advertise ND, IRBv6, ARP or IRB routes to a BGP EVPN peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *group-name* **advertise** { **irb** | **arp** }

**peer** *group-name* **advertise** { **irbv6** | **nd** }

**undo peer** *group-name* **advertise** { **irb** | **arp** }

**undo peer** *group-name* **advertise** { **irbv6** | **nd** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP EVPN peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **irb** | Configures a device to advertise IRB routes to its BGP EVPN peers. | - |
| **arp** | Configures a device to advertise ARP routes to its BGP EVPN peers. | - |
| **irbv6** | Configures a device to advertise IRBv6 routes to its BGP EVPN peers. | - |
| **nd** | Configures a device to advertise ND routes to its BGP EVPN peers. | - |



Views
-----

BGP-EVPN address family view,bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To allow a device to advertise ARP or IRB routes to its BGP EVPN peers, run the **peer advertise** command. This command allows VTEPs to establish VXLAN tunnels and implements ARP broadcast suppression on networks. If you specify irb, VTEPs can also transmit host routes.If you specify nd or irbv6, the local device can advertise ND or IRBv6 routes to a BGP EVPN peer. After receiving the routes, the BGP EVPN peer generates a proxy table locally. After the BGP EVPN peer receives NS packets, it searches the local proxy table. If an entry is hit, the VXLAN gateway directly performs proxy ND or multicast-to-unicast processing.

**Precautions**

You cannot specify both arp and irb in the same BGP-EVPN address family view.You cannot specify both nd and irbv6 in the same BGP-EVPN address family view.


Example
-------

# Configure a device to advertise ARP routes to its BGP EVPN peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.10.1.1 as-number 100
[*HUAWEI-bgp] group gp1
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer gp1 enable
[*HUAWEI-bgp-af-evpn] peer 10.10.1.1 group gp1
[*HUAWEI-bgp-af-evpn] peer gp1 advertise arp

```