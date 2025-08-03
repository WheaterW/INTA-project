igmp snooping query interval
============================

igmp snooping query interval

Function
--------



The **igmp snooping query interval** command sets the interval at which a querier sends general query messages.

The **undo igmp snooping query interval** command restores the default setting.



By default, a querier sends general query messages at an interval of 60s.


Format
------

**igmp snooping query interval** *QueryIntervalValue*

**undo igmp snooping query interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *QueryIntervalValue* | Specifies the interval at which a querier sends general query messages. | The value ranges from 1 to 65535, in seconds. |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The igmp snooping query interval command has the following functions:

* Sets the interval at which a querier sends general query messages. If the querier function is enabled, the igmp snooping query interval command can be used to set the interval at which a querier sends general query messages. This enables a device to periodically send general query messages in order to maintain group memberships. The shorter the interval is, the more frequently general query messages are sent and the more bandwidth and device resources are consumed. Ensure that the interval at which IGMP general query messages are sent is greater than the maximum response time of IGMP general query messages; otherwise, multicast group members may be deleted mistakenly.
* Changes the aging time of member ports. After receiving a Report message from a downstream device, a device sets the aging time of the corresponding member port based on the following formula: Aging time of a member port = Number of times group-specific query messages are sent x Interval at which general query messages are sent + Maximum time for a downstream host to respond to a querier. The default aging time is 130 seconds. The interval at which IGMP general query messages are sent in the formula is set using the igmp snooping query interval command. The number of times group-specific group query messages are sent is set using the **igmp snooping robust-count** command. The maximum time for a downstream host to respond to a querier is set using the **igmp snooping query max-response-time** command.

**Prerequisites**

IGMP snooping has been configured using the **igmp snooping enable** command.

**Configuration Impact**

If the igmp snooping query interval command is run in the same view several times, the latest configuration overrides the previous one.The default query-interval value in this command is 60 seconds, which is different than the default value 125 seconds defined by the relevant standard. A Huawei querier and a non-Huawei querier must send IGMP general query messages at the same interval.

**Precautions**

When the igmp snooping query interval command is used to set the aging time of member ports, the settings of parameters in this command must be consistent on a Layer 2 device and its upstream Layer 3 device. Otherwise, multicast data transmission between Layer 2 and Layer 3 networks will be interrupted.The interval at which a querier sends general query messages in a VLAN fails to be set in any of the following situations:

* A Dot1q termination sub-interface has been added to the VLAN.

Example
-------

# Set the interval at which a querier sends general query messages to 100s in VLAN 2.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] vlan 2
[*HUAWEI-vlan2] igmp snooping query interval 100

```