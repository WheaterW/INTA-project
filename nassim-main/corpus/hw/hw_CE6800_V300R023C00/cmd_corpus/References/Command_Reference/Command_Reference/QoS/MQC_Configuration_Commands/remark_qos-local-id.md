remark qos-local-id
===================

remark qos-local-id

Function
--------



The **remark qos-local-id** command configures an action of re-marking the local ID in a traffic behavior.

The **undo remark qos-local-id** command deletes the configuration.



By default, an action of re-marking the local ID is not configured in a traffic behavior.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**remark qos-local-id** *qos-local-id* [ **inbound-match** ]

**undo remark qos-local-id** [ *qos-local-id* ] [ **inbound-match** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *qos-local-id* | Specifies the value of a local ID. | The value is an integer ranging from 1 to 255. |
| **inbound-match** | Specifies the matching phase as uplink. | - |



Views
-----

Traffic behavior view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can configure the action of re-marking priorities of packets into the same QoS local ID in a traffic policy, and then configure a traffic classifier that defines if-match qos-local-id in another traffic policy to match packets. This conserves ACL resources.

* When the inbound-match parameter is not specified:On the inbound interface of packets, apply a traffic policy containing a traffic behavior that defines remark qos-local-id to change the QoS local ID of packets to be matched. On the outbound interface of packets, apply a traffic policy containing a traffic behavior that defines if-match qos-local-id so that the device provides QoS services for to-be-matched packets based on the re-marked QoS local ID.
* When the inbound-match parameter is specified:On the inbound interface of packets, apply a traffic policy containing a traffic behavior that defines remark qos-local-id inbound-match to change the QoS local ID of packets to be matched. Then apply another traffic policy containing a traffic classifier that defines if-match qos-local-id so that the device provides QoS services for to-be-matched packets based on the re-marked QoS local ID.

**Follow-up Procedure**

Run the **traffic policy** command to create a traffic policy and run the **classifier behavior** command in the traffic policy view to bind the traffic classifier to the traffic behavior containing local ID re-marking.

**Precautions**

* If you run the **remark qos-local-id** command in the same traffic behavior view multiple times, only the latest configuration takes effect.
* Traffic policies which define this traffic behavior can only be applied in the inbound direction.

Example
-------

# Re-mark the local ID of packets with 1 in the traffic behavior b1.
```
<HUAWEI> system-view
[~HUAWEI] traffic behavior b1
[*HUAWEI-behavior-b1] remark qos-local-id 1

```