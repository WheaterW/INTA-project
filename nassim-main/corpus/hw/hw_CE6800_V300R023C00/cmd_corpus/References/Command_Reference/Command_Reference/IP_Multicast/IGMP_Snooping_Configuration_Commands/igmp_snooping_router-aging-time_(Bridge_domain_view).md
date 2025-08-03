igmp snooping router-aging-time (Bridge domain view)
====================================================

igmp snooping router-aging-time (Bridge domain view)

Function
--------



The **igmp snooping router-aging-time** command sets the aging time for a dynamic router port.

The **undo igmp snooping router-aging-time** command restores the default configuration.



By default, the aging time of a dynamic router port is 180s or equals the holdtime value contained in a Protocol Independent Multicast (PIM) Hello packet.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**igmp snooping router-aging-time** *routerAgingTimeValue*

**undo igmp snooping router-aging-time**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *routerAgingTimeValue* | Specifies the aging time of a dynamic router port. | The value ranges from 1 to 1000, expressed in seconds. |



Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Network congestion may delay the transmission of a Query message from an IGMP Querier to a device. If a router port does not receive any IGMP Query message with source IP addresses other than 0.0.0.0 or PIM Hello packet within the aging time, it becomes a non-router port. If a dynamic router port ages before the Query message reaches a device, the device no longer sends Report or Leave messages upstream from this interface. This may lead to interruption of multicast data transmission. Therefore, if a network is instable, a larger aging time value is recommended for a dynamic router port. The device resets the aging time of a dynamic router port when the port receives an IGMP Query or PIM Hello message.

**Configuration Impact**

The aging time of the router port is set to the value configured using the igmp snooping router-aging-time command, if the current remaining aging time of the router port is smaller than the configured value.


Example
-------

# Set the aging time of router ports in BD 10 to 500 seconds.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] bridge-domain 10
[*HUAWEI-bd10] igmp snooping router-aging-time 500

```