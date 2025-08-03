igmp snooping router-learning disable
=====================================

igmp snooping router-learning disable

Function
--------



The **igmp snooping router-learning disable** command disables dynamic router port learning.

The **undo igmp snooping router-learning disable** command enables dynamic router port learning.



By default, dynamic router port learning is enabled on a device.


Format
------

**igmp snooping router-learning disable**

**undo igmp snooping router-learning disable**


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

On a device enabled with IGMP snooping, the interfaces receive any IGMP general query messages with the source IP addresses other than 0.0.0.0 or Protocol Independent Multicast (PIM) Hello packets are considered as dynamic router ports. The device records all router ports in a router port list. Receiving multicast data through router ports causes multicast data available to users to be uncontrollable. To control the multicast data available to users, you can disable dynamic router port learning.

**Prerequisites**

IGMP snooping has been enabled both globally and in a VLAN.

**Configuration Impact**

After dynamic router port learning is disabled, no interface will listen to IGMP Query messages, and static router ports must be configured.

**Precautions**

The igmp snooping router-learning command fails to be run in a VLAN in either of the following situations:A Dot1q termination sub-interface has been added to the VLAN.


Example
-------

# Enable dynamic router port learning in VLAN 10.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] vlan 10
[*HUAWEI-vlan10] igmp snooping enable
[*HUAWEI-vlan10] undo igmp snooping router-learning disable

```