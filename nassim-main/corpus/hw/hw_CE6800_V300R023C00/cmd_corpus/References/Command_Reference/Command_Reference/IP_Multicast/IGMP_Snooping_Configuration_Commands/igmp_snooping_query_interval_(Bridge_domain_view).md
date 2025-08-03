igmp snooping query interval (Bridge domain view)
=================================================

igmp snooping query interval (Bridge domain view)

Function
--------



The **igmp snooping query interval** command sets the interval at which a querier sends general query messages.

The **undo igmp snooping query interval** command restores the default setting.



By default, a querier sends general query messages at an interval of 60s.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



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

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The igmp snooping query interval command has the following functions:

* Sets the interval at which a querier sends general query messages. If the querier function is enabled, the igmp snooping query interval command can be used to set the interval at which a querier sends general query messages. This enables a device to periodically send general query messages in order to maintain group memberships. The shorter the interval is, the more frequently general query messages are sent and the more bandwidth and device resources are consumed. Ensure that the interval at which IGMP general query messages are sent is greater than the maximum response time of IGMP general query messages. Otherwise, multicast group members may be deleted mistakenly.
* Changes the aging time of member ports. After receiving a Report message from a downstream device, a device sets the aging time of the corresponding member port based on the following formula: Aging time of a member port = Number of times group-specific query messages are sent x Interval at which general query messages are sent + Maximum time for a downstream host to respond to a querier. The default aging time is 130 seconds. The interval at which IGMP general query messages are sent in the formula is set using the igmp snooping query interval command. The number of times group-specific group query messages are sent is set using the **igmp snooping robust-count** command. The maximum time for a downstream host to respond to a querier is set using the **igmp snooping query max-response-time** command.

**Prerequisites**

IGMP snooping has been configured using the **igmp snooping enable** command.

**Configuration Impact**

If the igmp snooping query interval command is run in the same view several times, the latest configuration overrides the previous one.The default query-interval value in this command is 60 seconds, which is different than the default value 125 seconds defined by the relevant standard. A Huawei querier and a non-Huawei querier must send IGMP general query messages at the same interval.

**Precautions**

The aging time configured on a Layer 2 device must be the same as that on its upstream Layer 3 device. Otherwise, multicast data transmission between Layer 2 and Layer 3 networks will be affected.


Example
-------

# Set the interval at which a querier sends general query messages to 100s in VSI vsi1.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] bridge-domain 10
[*HUAWEI-bd10] igmp snooping query interval 100

```