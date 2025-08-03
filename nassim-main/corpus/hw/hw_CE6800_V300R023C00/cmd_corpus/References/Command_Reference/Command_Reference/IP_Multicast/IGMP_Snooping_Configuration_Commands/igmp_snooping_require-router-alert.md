igmp snooping require-router-alert
==================================

igmp snooping require-router-alert

Function
--------



The **igmp snooping require-router-alert** command configures a device to accept IGMP messages that contain the Router-Alert option in the IP header from a VLAN.

The **undo igmp snooping require-router-alert** command restores the default setting.



y default, the IGMP messages accepted by a device from a VLAN do not need to carry the Router Alert option.


Format
------

**igmp snooping require-router-alert**

**undo igmp snooping require-router-alert**


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

Router-Alert is a mechanism used to identify protocol packets. Packets carrying Router-Alert options are delivered to the routing protocol layer for processing.By default, devices do not check whether packets carry Router-Alert options for the sake of compatibility, and send all IGMP messages to the upper layer for processing. To improve device performance, reduce costs, and ensure protocol security, the igmp-snooping require-router-alert command can be used to configure a device to discard IGMP messages that do not carry the Router-Alert option. After receiving IGMP messages, this device will check whether these messages carry the Router-Alert option. If the messages do not carry the Router-Alert option, this device will discard them.

**Precautions**

The igmp-snooping require-router-alert command fails to be run in the VLAN view in any of the following situations:

* A Dot1q termination sub-interface has been added to the VLAN.

Example
-------

# Configure a device in VLAN 2 to accept only IGMP messages that carry the Router-Alert option in the IP header.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] vlan 2
[*HUAWEI-vlan2] igmp snooping enable
[*HUAWEI-vlan2] igmp snooping require-router-alert

```