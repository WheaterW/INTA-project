igmp snooping require-router-alert (Bridge domain view)
=======================================================

igmp snooping require-router-alert (Bridge domain view)

Function
--------



The **igmp snooping require-router-alert** command configures a device to accept IGMP messages that contain the Router-Alert option in the IP header from a BD.

The **undo igmp snooping require-router-alert** command restores the default setting.



By default, the IGMP messages accepted by a device from a BD do not need to carry the Router Alert option.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**igmp snooping require-router-alert**

**undo igmp snooping require-router-alert**


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

Router-Alert is a mechanism used to identify protocol packets. Packets carrying Router-Alert options are delivered to the routing protocol layer for processing.By default, devices do not check whether packets carry Router-Alert options for the sake of compatibility, and send all IGMP messages to the upper layer for processing. To improve device performance, reduce costs, and ensure protocol security, the igmp snooping require-router-alert command can be used to configure a device to discard IGMP messages that do not carry the Router-Alert option. After receiving IGMP messages, this device will check whether these messages carry the Router-Alert option. If the messages do not carry the Router-Alert option, this device will discard them.


Example
-------

# Configure a device in BD10 to accept only IGMP messages that carry the Router-Alert option in the IP header.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] bridge-domain 10
[*HUAWEI-bd10] igmp snooping enable
[*HUAWEI-bd10] igmp snooping require-router-alert

```