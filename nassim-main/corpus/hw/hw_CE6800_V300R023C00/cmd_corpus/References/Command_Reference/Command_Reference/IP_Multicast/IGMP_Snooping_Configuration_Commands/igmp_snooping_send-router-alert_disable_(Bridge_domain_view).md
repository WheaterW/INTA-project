igmp snooping send-router-alert disable (Bridge domain view)
============================================================

igmp snooping send-router-alert disable (Bridge domain view)

Function
--------



The **igmp snooping send-router-alert disable** command configures a device to send IGMP messages that do not contain the Router Alert option in the IP header to a bridge domain.

The **undo igmp snooping send-router-alert disable** command configures a device to send IGMP messages that contain the Router Alert option in the IP header to a bridge domain.



By default, a device sends IGMP messages that contain the Router-Alert option in the IP header to a BD.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**igmp snooping send-router-alert disable**

**undo igmp snooping send-router-alert disable**


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

Router-Alert is a mechanism used to identify protocol packets. Packets carrying Router-Alert options are delivered to the routing protocol layer for processing.By default, devices do not check whether packets carry Router-Alert options for the sake of compatibility, and send all IGMP messages to the upper layer for processing. To improve device performance, reduce costs, and ensure protocol security, configure devices to send packets without Router-Alert options.


Example
-------

# Configure a device to send IGMP messages that do not contain the Router-Alert option in the IP header to BD 10.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] igmp snooping send-router-alert disable

```