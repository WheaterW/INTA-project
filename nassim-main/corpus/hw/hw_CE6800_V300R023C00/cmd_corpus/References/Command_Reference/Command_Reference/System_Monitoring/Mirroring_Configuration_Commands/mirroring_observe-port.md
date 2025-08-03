mirroring observe-port
======================

mirroring observe-port

Function
--------



The **mirroring observe-port** command mirrors the traffic matching certain rules to an observing port or an observing port group.

The **undo mirroring** command disables traffic mirroring that mirrors the traffic matching certain rules to an observing port or an observing port group.



By default, traffic mirroring that mirrors the traffic matching certain rules to an observing port or an observing port group is disabled.


Format
------

**mirroring observe-port** *observe-port-index*

**mirroring observe-port group** *group-id*

**undo mirroring** [ **observe-port** *observe-port-index* ]

**undo mirroring observe-port group** *group-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *observe-port-index* | Specifies the index of an observing port. | The value is an integer that ranges from 1 to 8. |
| **group** *group-id* | Specifies the ID of the observing port group. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 128.  For the CE6885-LL (low latency mode):The value is an integer that ranges from 1 to 8. |



Views
-----

Traffic behavior view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



You can run the **mirroring observe-port** command to mirror the traffic matching certain rules to an observing port. You can also run the **mirroring observe-port group** command to mirror the traffic to an observing port group so that the packets are copied to all the member ports of the observing port group.



**Prerequisites**



An observing port has been configured using the **observe-port** command or an observing port group has been configured using the **observe-port group** command.



**Precautions**



An ACL rule defining **logging** (used to log the matching packets) cannot be used together with the mirroring action in the same traffic policy.




Example
-------

# Mirror the traffic matching certain rules to observing port 1.
```
<HUAWEI> system-view
[~HUAWEI] observe-port 1 interface 100GE 1/0/1
[*HUAWEI] traffic behavior tb1
[*HUAWEI-behavior-tb1] mirroring observe-port 1

```