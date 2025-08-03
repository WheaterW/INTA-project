policy vpn-target (BGP-MVPN address family view)
================================================

policy vpn-target (BGP-MVPN address family view)

Function
--------



The **policy vpn-target** command configures a device to implement VPN target-based filtering for received routes.

The **undo policy vpn-target** command cancels VPN target-based filtering.



By default, BGP MVPN target-based filtering is enabled for VPN routes.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**policy vpn-target**

**undo policy vpn-target**


Parameters
----------

None

Views
-----

BGP-MVPN address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, a device compares whether the export RT of a VPN route matches the import RT of a local VPN instance. A VPN instance must exist on the device.

* Generally, VPN instances have been configured on PEs and do not need to be reconfigured.
* In an inter-AS VPN Option B scenario, no VPN instance is configured on the RR. Therefore, a VPN instance must be configured on the RR. In addition, the import RT of the VPN instance must match the export RT of the received VPN route; otherwise, the VPN route may be discarded because there is no matched import RT.

After the **undo policy vpn-target** command is run, the device does not compare whether the export RT of a VPN route matches the import RT of the local VPN instance.

**Configuration Impact**

After the policy vpn-target command is run on a device, the device accepts a VPN route if one export RT attribute contained in the VPN route matches the import RT of the local VPN instance, and then adds the VPN route to the VPN routing tables of the VPN instances of which the import RT matches the export RT of the VPN route.

**Precautions**

Running the **undo policy vpn-target** command cancels VPN target-based filtering for VPN routes, which may cause the device to accept a large number of routes. Therefore, exercise caution when running this command.


Example
-------

# Configure a device to implement VPN target-based filtering for received MVPN routes.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family mvpn
[*HUAWEI-bgp-af-mvpn] policy vpn-target

```