peer advertise route-reoriginated evpn (bgp-muli-instance-af-evpn view) (group)
===============================================================================

peer advertise route-reoriginated evpn (bgp-muli-instance-af-evpn view) (group)

Function
--------



The **peer advertise route-reoriginated evpn** command enables a device to re-encapsulate EVPN routes and then advertise them to BGP EVPN peers.

The **undo peer advertise route-reoriginated evpn** command restores the default configuration.



By default, a device does not re-encapsulate EVPN routes or advertise regenerated EVPN routes to BGP EVPN peers.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerGroupName* **advertise** **route-reoriginated** **evpn** { **mac-ip** | **mac** | **ip** | **mac-ipv6** | **ipv6** }

**undo peer** *peerGroupName* **advertise** **route-reoriginated** **evpn** { **mac-ip** | **mac** | **ip** | **mac-ipv6** | **ipv6** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerGroupName* | Specifies the name of a BGP EVPN peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **mac-ip** | Re-encapsulates the IRB or ARP routes in the received EVPN routes. | - |
| **mac** | Re-encapsulates the MAC routes in the received EVPN routes. | - |
| **ip** | Re-encapsulates the IP prefix routes in the received EVPN routes. | - |
| **mac-ipv6** | Re-encapsulates the IRBv6 or ND routes in received EVPN routes. | - |
| **ipv6** | Re-encapsulates received IPv6 prefix routes. | - |



Views
-----

bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In a segment VXLAN scenario for DCI, to allow VMs in different DCs to communicate with each other, run the **peer advertise route-reoriginated** command on a DC edge device connecting to a carrier backbone network. The edge device then re-encapsulates the EVPN routes received from one DC and sends them to BGP EVPN peers in another DC.After receiving an EVPN route from a DC, an edge leaf node re-encapsulates the EVPN route as follows: Modifies the next hop address of the EVPN route as its own VTEP address, replaces the source MAC address (functioning as the gateway MAC address) of the host route contained in the EVPN route with its own MAC address, and replaces the L3VNI in the EVPN route with the L3VNI in the edge leaf's L3VPN instance.

**Prerequisites**

The device has been enabled to add a regeneration flag to the routes received from BGP EVPN peers using the **peer group-name import reoriginate** command.


Example
-------

# Enable a device to advertise regenerated IRB or ARP routes to a BGP EVPN peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instance evrf
[*HUAWEI-bgp-instance-evrf] group gp1
[*HUAWEI-bgp-instance-evrf] peer 1.1.1.1 group gp1
[*HUAWEI-bgp-instance-evrf] peer 2.2.2.2 group gp1
[*HUAWEI-bgp-instance-evrf] l2vpn-family evpn
[*HUAWEI-bgp-instance-evrf-af-evpn] peer gp1 enable
[*HUAWEI-bgp-instance-evrf-af-evpn] peer gp1 import reoriginate
[*HUAWEI-bgp-instance-evrf-af-evpn] peer gp1 advertise route-reoriginated evpn mac-ip

```