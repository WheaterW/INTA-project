policy vpn-target (BGP-EVPN address family view)
================================================

policy vpn-target (BGP-EVPN address family view)

Function
--------



The **policy vpn-target** command configures a device to implement VPN target-based filtering for received routes.

The **undo policy vpn-target** command cancels VPN target-based filtering.



By default, VPN target-based filtering is enabled for VPN routes.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**policy vpn-target**

**undo policy vpn-target**


Parameters
----------

None

Views
-----

BGP-EVPN address family view,bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the **undo policy vpn-target** command is run on a device, the device does not compare the export RT of a VPN route with the import RT of the local VPN instance. In the inter-AS VPN Option B scenario, if the **undo policy vpn-target** command is not run, ensure that a VPN instance is created on the RR and the import RT of the local VPN instance matches the export RT of received VPN routes; otherwise, received VPN routes may be discarded.

**Configuration Impact**

After the policy vpn-target command is run on a device, the device accepts a VPN route if one export RT attribute contained in the VPN route matches the import IT of the local VPN instance, and then adds the VPN route to the VPN routing tables of the VPN instances of which the import RT matches the export RT of the VPN route.

**Precautions**



The following commands need to be run in EVPN L3VPN scenarios:VPN instance view: vxlan vni




Example
-------

# Configure a device to implement VPN target-based filtering for received EVPN routes.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.9 as-number 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer 10.1.1.9 enable
[*HUAWEI-bgp-af-evpn] policy vpn-target

```