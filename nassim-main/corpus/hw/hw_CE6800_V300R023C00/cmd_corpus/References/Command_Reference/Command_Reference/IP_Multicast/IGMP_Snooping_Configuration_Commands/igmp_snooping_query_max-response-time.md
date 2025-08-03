igmp snooping query max-response-time
=====================================

igmp snooping query max-response-time

Function
--------



The **igmp snooping query max-response-time** command sets the maximum time for a downstream host to respond to a querier.

The **undo igmp snooping query max-response-time** command restores the default setting.



By default, the maximum time for a downstream host to respond to a querier is 10s.


Format
------

**igmp snooping query max-response-time** *QueryRspIntValue*

**undo igmp snooping query max-response-time**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *QueryRspIntValue* | Specifies the maximum time for a downstream host to respond to a querier. | The value ranges from 1 to 127 in the VSI view and 1 to 25 in other views, in seconds. |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The igmp snooping max-response-time command has the following functions:

* Sets the maximum response time to control the deadline for hosts to send IGMP Report messages. If the querier function is enabled, set a short maximum response time to enable hosts to rapidly respond to IGMP Query messages, and set a long maximum response time to prevent traffic congestion caused by too many Report or Leave messages sent by hosts on a network. Check that the interval at which IGMP general query messages are sent is greater than the maximum response time for a downstream host to respond to the querier. Otherwise, multicast group members may be deleted mistakenly.
* Changes the aging time of member ports. After receiving a Report message from a downstream device, a device sets the aging time of the corresponding member port based on the following formula: Aging time of a member port = Number of times group-specific query messages are sent x Interval at which general query messages are sent + Maximum time for a downstream host to respond to a querier. The default aging time is 130s. The maximum time for a downstream host to respond to a querier is set using the igmp snooping query max-response-time command. The number of times group-specific group query messages are sent is set using the **igmp snooping robust-count** command. The interval at which general query messages are sent is set using the **igmp snooping query-interval** command.

**Prerequisites**

IGMP snooping has been configured using the **igmp snooping enable** command.

**Configuration Impact**

If the igmp snooping query max-response-time command is run in the same view several times, the latest configuration overrides the previous one.

**Precautions**

When this command is used to set the aging time of member ports, the settings of parameters in this command must be consistent on a Layer 2 device and its upstream Layer 3 device; otherwise, multicast data transmission between Layer 2 and Layer 3 networks will be interrupted.The maximum time for a downstream host to respond to a querier fails to be set in a VLAN in the following situation:

* A dot1q termination sub-interface has been added to the VLAN.

Example
-------

# Set the maximum time for a downstream host to respond to a querier to 20s in VLAN 10.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] vlan 10
[*HUAWEI-vlan10] igmp snooping query max-response-time 20

```