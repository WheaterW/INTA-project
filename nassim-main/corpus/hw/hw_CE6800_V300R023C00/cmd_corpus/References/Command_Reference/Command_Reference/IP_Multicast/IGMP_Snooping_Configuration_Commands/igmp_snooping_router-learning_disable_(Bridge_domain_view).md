igmp snooping router-learning disable (Bridge domain view)
==========================================================

igmp snooping router-learning disable (Bridge domain view)

Function
--------



The **igmp snooping router-learning disable** command disables dynamic router port learning.

The **undo igmp snooping router-learning disable** command enables dynamic router port learning.



By default, dynamic router port learning is enabled on a device.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**igmp snooping router-learning disable**

**undo igmp snooping router-learning disable**


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

On a device enabled with IGMP snooping, the interfaces that receive any IGMP general query messages with the source IP addresses other than 0.0.0.0 or Protocol Independent Multicast (PIM) Hello packets are considered as dynamic router ports. The device records all router ports in a list. In this manner, multicast data forwarding to hosts is uncontrollable. To control the multicast data available to users, you can disable dynamic router port learning in a VLAN.

**Prerequisites**

IGMP snooping has been enabled both globally and in a BD.

**Configuration Impact**

After dynamic router port learning is disabled, no interface will listen to IGMP Query messages, and static router ports must be configured.


Example
-------

# Enable dynamic router port learning in BD 10.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] bridge-domain 10
[*HUAWEI-bd10] igmp snooping enable
[*HUAWEI-bd10] undo igmp snooping router-learning disable

```