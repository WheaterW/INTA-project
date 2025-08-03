mld snooping static-group suppress-dynamic-join
===============================================

mld snooping static-group suppress-dynamic-join

Function
--------



The **mld snooping static-group suppress-dynamic-join** command disables interfaces in a VLAN from forwarding Report and Done messages to upstream routers with static groups configured.

The command enables interfaces in a VLAN to forward Report and Done messages to upstream routers with static groups configured.



By default, interfaces in a VLAN are enabled to forward Report and Done messages to upstream routers with static groups configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping static-group suppress-dynamic-join**

**undo mld snooping static-group suppress-dynamic-join**


Parameters
----------

None

Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If an upstream Layer 3 multicast device is a non-Huawei device and static groups are configured on the device, the device does not allow dynamic group join or leave. In this scenario, run the mld snooping static-group suppress-dynamic-join command on the Layer 2 device to disable interfaces in a VLAN from forwarding Report and Done messages to the upstream router.


Example
-------

# Disable interfaces in VLAN 10 from forwarding Report and Done messages to router interfaces with static groups configured.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping enable
[*HUAWEI] vlan 10
[*HUAWEI-vlan10] mld snooping static-group suppress-dynamic-join

```