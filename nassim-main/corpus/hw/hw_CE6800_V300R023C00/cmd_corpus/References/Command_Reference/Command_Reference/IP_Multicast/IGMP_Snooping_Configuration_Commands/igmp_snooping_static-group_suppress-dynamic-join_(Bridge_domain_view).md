igmp snooping static-group suppress-dynamic-join (Bridge domain view)
=====================================================================

igmp snooping static-group suppress-dynamic-join (Bridge domain view)

Function
--------



The **igmp snooping static-group suppress-dynamic-join** command disables a Layer 2 device from sending Report and Leave messages received from a BD to the upstream device with static groups configured.

The **undo igmp snooping static-group suppress-dynamic-join** command cancels the configuration.



By default, a Layer 2 device sends Report and Leave messages received from a BD to the upstream device with static groups configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**igmp snooping static-group suppress-dynamic-join**

**undo igmp snooping static-group suppress-dynamic-join**


Parameters
----------

None

Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the upstream Layer 3 multicast device is a non-Huawei device and static multicast groups have been configured on interfaces of the Layer 3 device, users cannot dynamically join or leave multicast groups. To prevent this problem, disable the from sending Report and Leave messages to the Layer 3 multicast device.

**Prerequisites**

IGMP snooping has been configured globally and in a BD.


Example
-------

# Disable a device from sending Report and Leave messages received in a BD to the upstream router with static groups configured.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] bridge-domain 10
[*HUAWEI-bd10] igmp snooping enable
[*HUAWEI-bd10] igmp snooping static-group suppress-dynamic-join

```