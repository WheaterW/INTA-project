peer advertise route-reoriginated (BGP-EVPN address family view) (group)
========================================================================

peer advertise route-reoriginated (BGP-EVPN address family view) (group)

Function
--------



The **peer advertise route-reoriginated** command configures a device to send the routes that are regenerated in the EVPN or VPNv4/v6 address family to a BGP EVPN peer group.

The **undo peer advertise route-reoriginated** command restores the default configuration.



By default, a device does not send the routes that are regenerated in the EVPN or VPNv4/v6 address family to a BGP EVPN peer group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerGroupName* **advertise** **route-reoriginated** **evpn** { **mac-ip** | **mac** }

**peer** *peerGroupName* **advertise** **route-reoriginated** **evpn** **ip**

**peer** *peerGroupName* **advertise** **route-reoriginated** **evpn** { **mac-ipv6** | **ipv6** }

**undo peer** *peerGroupName* **advertise** **route-reoriginated** **evpn** { **mac-ip** | **mac** }

**undo peer** *peerGroupName* **advertise** **route-reoriginated** **evpn** **ip**

**undo peer** *peerGroupName* **advertise** **route-reoriginated** **evpn** { **mac-ipv6** | **ipv6** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerGroupName* | Specifies the name of a BGP EVPN peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **evpn** | Re-encapsulates received EVPN routes. | - |
| **mac-ip** | Re-encapsulates the IRB or ARP routes in received EVPN routes. | - |
| **mac** | Re-encapsulates MAC routes in received EVPN routes. | - |
| **ip** | Re-encapsulates received prefix routes. | - |
| **mac-ipv6** | Re-encapsulates the IRBv6 or ND routes in received EVPN routes. | - |
| **ipv6** | Re-encapsulates received IPv6 prefix routes. | - |



Views
-----

BGP-EVPN address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

DCI is an umbrella term covering multiple DC interconnection solutions. In the DCI solution, a DCI-PE re-encapsulates received EVPN or VPNv4/v6 routes and then sends these routes to its peers.

* After a DCI-PE receives EVPN routes with the VXLAN encapsulation attribute from a DC, the DCI-PE re-originates these EVPN routes and advertises them with the MPLS encapsulation attribute to its BGP EVPN peers on the DCI backbone network.
* After a DCI-PE receives EVPN, VPNv4, or VPNv6 routes with the MPLS encapsulation attribute from BGP EVPN, VPNv4, or VPNv6 peers on the DCI backbone network, the DCI-PE re-originates these routes and advertises them with the VXLAN encapsulation attribute to the DC side.

**Prerequisites**

Route information exchange has been enabled between the local device and a specified peer group using the **peer enable** command.


Example
-------

# Configure a DCI-PE to advertise reoriginated prefix routes to a BGP EVPN peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 1.1.1.1 as-number 100
[*HUAWEI-bgp] group gp1
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer gp1 enable
[*HUAWEI-bgp-af-evpn] peer 1.1.1.1 group gp1
[*HUAWEI-bgp-af-evpn] peer gp1 advertise route-reoriginated evpn mac-ip

```