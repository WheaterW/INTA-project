peer split-group (BGP-EVPN address family view)
===============================================

peer split-group (BGP-EVPN address family view)

Function
--------



The **peer split-group** command configures a split horizon group (SHG) to which BGP EVPN peers belong.

The **undo peer split-group** command restores the default configuration.



By default, no SHG is configured for BGP EVPN peers.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv4-address* **split-group** *split-group-name*

**undo peer** *ipv4-address* **split-group** *split-group-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a BGP EVPN peer. | The value is in dotted decimal notation. |
| **split-group** *split-group-name* | Specifies the name of the SHG to which BGP EVPN peers belong. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

BGP-EVPN address family view,bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In a scenario where segment VXLAN is used to implement Layer 2 interworking between DCs, a VXLAN tunnel is established in BGP EVPN mode between the DCs. To prevent forwarding BUM traffic from causing loops, run the peer split-group command on the transit leaf nodes (edge devices interconnecting the DCs) to configure an SHG to which the BGP EVPN peers (transit leaf nodes) belong. After the configuration is complete, devices within a DC belong to the default SHG, and transit leaf nodes between DCs belong to the specified SHG. In this manner, when a transit leaf node receives BUM traffic, it does not forward traffic to a device belonging to the same SHG, therefore preventing loops.

**Prerequisites**

BGP EVPN peers have been enabled to exchange route information using the **peer enable** command.


Example
-------

# Configure an SHG to which the BGP EVPN peers belong.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.9 as-number 200
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer 10.1.1.9 enable
[*HUAWEI-bgp-af-evpn] peer 10.1.1.9 split-group aa

```