qos traffic-policy only-one-effective
=====================================

qos traffic-policy only-one-effective

Function
--------



The **qos traffic-policy only-one-effective** command enables the mode in which two MQC-based traffic policies do not take effect at the same time.

The **undo qos traffic-policy only-one-effective** command disables the mode in which two MQC-based traffic policies do not take effect at the same time.



By default, the qos traffic-policy only-one-effective mode is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**qos traffic-policy only-one-effective**

**undo qos traffic-policy only-one-effective**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After this command is configured, two traffic policies (two traffic policies configured in the same direction in the same view) in the system cannot take effect at the same time. After a packet matches the first traffic policy, the system does not search for the second traffic policy.


Example
-------

# Enable the qos traffic-policy only-one-effective mode.
```
<HUAWEI> system-view
[~HUAWEI] qos traffic-policy only-one-effective

```