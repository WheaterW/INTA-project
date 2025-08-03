igmp snooping query max-response-time (Bridge domain view)
==========================================================

igmp snooping query max-response-time (Bridge domain view)

Function
--------



The **igmp snooping query max-response-time** command sets the maximum time for a downstream host to respond to a querier.

The **undo igmp snooping query max-response-time** command restores the default setting.



By default, the maximum time for a downstream host to respond to a querier is 10s.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**igmp snooping query max-response-time** *QueryRspIntValue*

**undo igmp snooping query max-response-time**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *QueryRspIntValue* | Specifies the maximum time for a downstream host to respond to a querier. | The value ranges from 1 to 25, in seconds. |



Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The igmp-snooping max-response-time command has the following functions:

* Sets the maximum response time to control the deadline for hosts to send IGMP Report messages. If the querier function is enabled, set a short maximum response time to enable hosts to rapidly respond to IGMP Query messages, and set a long maximum response time to prevent traffic congestion caused by too many Report or Leave messages sent by hosts on a network. Check that the interval at which IGMP general query messages are sent is greater than the maximum response time for a downstream host to respond to the querier; otherwise, multicast group members may be deleted mistakenly.
* Changes the aging time of member ports. After receiving a Report message from a downstream device, a device sets the aging time of the corresponding member port based on the following formula: Aging time of a member port = Number of times group-specific query messages are sent x Interval at which general query messages are sent + Maximum time for a downstream host to respond to a querier. The default aging time is 130s. The maximum time for a downstream host to respond to a querier is set using the igmp snooping query max-response-time command. The number of times group-specific group query messages are sent is set using the igmp-snooping robust-count**igmp snooping robust-count** command. The interval at which general query messages are sent is set using the **igmp snooping query-interval** command.

**Prerequisites**

IGMP snooping has been configured using the **igmp snooping enable** command.

**Configuration Impact**

If the igmp snooping query max-response-time command is run in the same view several times, the latest configuration overrides the previous one.

**Precautions**

The aging time configured on a Layer 2 device must be the same as that on its upstream Layer 3 device. Otherwise, multicast data transmission between Layer 2 and Layer 3 networks will be affected.


Example
-------

# Set the maximum time for a downstream host to respond to a querier to 20s in BD 10.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] bridge-domain 10
[*HUAWEI-bd10] igmp snooping query max-response-time 20

```