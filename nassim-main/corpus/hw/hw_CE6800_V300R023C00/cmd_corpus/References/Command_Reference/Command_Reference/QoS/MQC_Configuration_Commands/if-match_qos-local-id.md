if-match qos-local-id
=====================

if-match qos-local-id

Function
--------



The **if-match qos-local-id** command configures a matching rule based on the local ID in a traffic classifier.

The **undo if-match qos-local-id** command deletes a matching rule based on the local ID in a traffic classifier.



By default, no matching rule based on the local ID is configured in a traffic classifier.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**if-match qos-local-id** *qos-local-id*

**undo if-match qos-local-id** [ *qos-local-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *qos-local-id* | Indicates the local identifier value. | The value is an integer ranging from 1 to 255. |



Views
-----

Traffic classifier view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



You can run the **remark qos-local-id** command to configure the action of re-marking priorities of packets into the same QoS local ID in a traffic policy. Then, you can configure a traffic classifier that defines if-match qos-local-id in another traffic policy. This conserves ACL resources.



**Precautions**



If you run the **if-match qos-local-id** command in the same traffic classifier view multiple times, only the latest configuration takes effect.




Example
-------

# Configure a matching rule based on the local ID of 1 in the traffic classifier class1.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier class1
[*HUAWEI-classifier-class1] if-match qos-local-id 1

```