igmp snooping send-router-alert disable
=======================================

igmp snooping send-router-alert disable

Function
--------



The **igmp snooping send-router-alert disable** command configures a device to send IGMP messages that do not contain the Router-Alert option in the IP header to a VLAN or VSI.

The **undo igmp snooping send-router-alert disable** command configures a device to send IGMP messages that contain the Router-Alert option in the IP header to a VLAN or VSI.



By default, a device sends IGMP messages that contain the Router-Alert option in the IP header to a VLAN.


Format
------

**igmp snooping send-router-alert disable**

**undo igmp snooping send-router-alert disable**


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

Router-Alert is a mechanism used to identify protocol packets. Packets carrying Router-Alert options are delivered to the routing protocol layer for processing.By default, devices do not check whether packets carry Router-Alert options for the sake of compatibility, and send all IGMP messages to the upper layer for processing. To improve device performance, reduce costs, and ensure protocol security, configure devices to send packets without Router-Alert options.

**Precautions**

The igmp snooping send-router-alert command fails to be run in the VLAN view in any of the following situations:

* A Dot1q termination sub-interface has been added to the VLAN.

Example
-------

# Configure a device to send IGMP messages that do not contain the Router-Alert option in the IP header to VLAN 2.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] vlan 2
[*HUAWEI-vlan2] igmp snooping send-router-alert disable

```