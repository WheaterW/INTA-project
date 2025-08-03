local mac-only-route no-generate
================================

local mac-only-route no-generate

Function
--------



The **local mac-only-route no-generate** command disables the device from generating EVPN MAC routes when both MAC address entries and ARP/ND entries contain local MAC addresses.

The **undo local mac-only-route no-generate** command restores the default configuration.



By default, EVPN MAC routes are generated when both MAC address entries and ARP/ND entries contain local MAC addresses.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**local mac-only-route no-generate**

**undo local mac-only-route no-generate**


Parameters
----------

None

Views
-----

EVPN instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If a MAC address entry and an ARP/ND entry on the local gateway both contain the local MAC address in EVPN scenarios, the gateway generates both an EVPN MAC/IP route and an EVPN MAC route by default. To optimize memory utilization, perform this step so that the gateway generates only a MAC/IP route. To ensure normal Layer 2 traffic forwarding, also run the **mac-ip route generate-mac** command on the peer gateway to enable the function to generate MAC address entries based on MAC/IP routes.


Example
-------

# Disable the device from generating EVPN MAC routes when both MAC address entries and ARP/ND entries contain local MAC addresses.
```
<HUAWEI> system-view
Enter system view, return user view with return command.
[~HUAWEI] bridge-domain 100
[*HUAWEI-bd100] vxlan vni 100
[*HUAWEI-bd100] evpn
[*HUAWEI-bd100-evpn] local mac-only-route no-generate

```