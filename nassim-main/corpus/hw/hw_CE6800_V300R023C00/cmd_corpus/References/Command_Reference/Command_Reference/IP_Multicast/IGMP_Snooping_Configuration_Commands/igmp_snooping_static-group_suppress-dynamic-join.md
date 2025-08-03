igmp snooping static-group suppress-dynamic-join
================================================

igmp snooping static-group suppress-dynamic-join

Function
--------



The **igmp snooping static-group suppress-dynamic-join** command disables a Layer 2 device from sending Report and Leave messages received from a VLAN to the upstream device with static groups configured.

The **undo igmp snooping static-group suppress-dynamic-join** command cancels the configuration.



By default, a Layer 2 device sends Report and Leave messages received from a VLAN to the upstream device with static groups configured.


Format
------

**igmp snooping static-group suppress-dynamic-join**

**undo igmp snooping static-group suppress-dynamic-join**


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

**Usage Scenario**

If the upstream Layer 3 multicast device is a non-Huawei device and static multicast groups have been configured on interfaces of the Layer 3 device, users cannot dynamically join or leave multicast groups. To prevent this problem, disable the from sending Report and Leave messages to the Layer 3 multicast device.

**Prerequisites**

IGMP snooping has been configured globally and in a VLAN.


Example
-------

# Disable the device from sending the Report and Leave messages received in a VLAN to the upstream router with static groups configured.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] vlan 10
[*HUAWEI-vlan10] igmp snooping enable
[*HUAWEI-vlan10] igmp snooping static-group suppress-dynamic-join

```