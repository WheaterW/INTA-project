igmp snooping router-aging-time
===============================

igmp snooping router-aging-time

Function
--------



The **igmp snooping router-aging-time** command sets the aging time for a dynamic router port. The port updates the remaining time to the configured value if the remaining time of the aging timer is shorter than the value, no matter the port receives PIM Hello messages or IGMP Query messages.

The **undo igmp snooping router-aging-time** command restores the default configuration.



By default, the aging time of a dynamic router port is 180s or equals the holdtime value contained in a Protocol Independent Multicast (PIM) Hello packet.


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

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Network congestion may delay the transmission of a Query message from an IGMP Querier to a device. If a router port does not receive any IGMP Query message with source IP addresses other than 0.0.0.0 or PIM Hello packet within the aging time, it becomes a non-router port. If a dynamic router port ages before the Query message reaches a device, the device no longer sends Report or Leave messages upstream from this interface. This may lead to interruption of multicast data transmission. Therefore, if a network is instable, a larger aging time value is recommended for a dynamic router port. The device resets the aging time of a dynamic router port when the port receives an IGMP Query or PIM Hello message.

**Configuration Impact**

The aging time of the router port is set to the value configured using the igmp-snooping router-aging-time command, if the current remaining aging time of the router port is smaller than the configured value.

**Precautions**

The igmp snooping router-aging-time command fails to be run in the VLAN view in any of the following situations:

* A Dot1q termination sub-interface has been added to the VLAN.

Example
-------

# Set the aging time of router ports in VLAN 2 to 500 seconds.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] vlan 2
[*HUAWEI-vlan2] igmp snooping router-aging-time 500

```