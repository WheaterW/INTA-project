mld snooping proxy router-protocol-pass
=======================================

mld snooping proxy router-protocol-pass

Function
--------



The **mld snooping proxy router-protocol-pass** command configures an MLD snooping proxy-enabled device to transparently transmit MLD Report messages.

The **undo mld snooping proxy router-protocol-pass** command restores the default configuration.



By default, an MLD snooping proxy-enabled device does not transparently transmit MLD Report messages, Done, Group-Specific Query, and Group-and-Source-Specific Query messages.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping proxy router-protocol-pass**

**undo mld snooping proxy router-protocol-pass**


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

If MLD snooping proxy is enabled on a Layer 2 device and its upstream device, the devices will learn the same multicast forwarding entries and constantly exchange MLD Query and Report messages, causing multicast entries not to age. Such multicast protocol and data message forwarding is meaninglessly. To address this issue, run the mld snooping proxy router-protocol-pass command to enable the Layer 2 device to transparently transmit MLD Report messages from a router interface to other router interfaces.Running the mld snooping proxy router-protocol-pass command is recommended on a network where an MLD snooping proxy-enabled device is dual-homed to upstream devices.


Example
-------

# Configure router interfaces in VLAN 10 to transparently transmit MLD Report messages.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping enable
[*HUAWEI] vlan 10
[*HUAWEI-vlan10] mld snooping proxy router-protocol-pass

```