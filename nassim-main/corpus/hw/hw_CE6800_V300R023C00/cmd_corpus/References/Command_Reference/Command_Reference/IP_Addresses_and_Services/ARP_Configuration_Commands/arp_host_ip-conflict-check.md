arp host ip-conflict-check
==========================

arp host ip-conflict-check

Function
--------



The **arp host ip-conflict-check** command configures a detection option for host IP address conflicts.

The **undo arp host ip-conflict-check** command cancels the configured detection option.



By default, host IP address conflicts are detected within a period of 180 seconds and and threshold for host IP address conflicts as five times.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**arp host ip-conflict-check period** *period-value* **retry-times** *retry-times-value*

**undo arp host ip-conflict-check period** *period-value* **retry-times** *retry-times-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **retry-times** *retry-times-value* | Specifies a threshold for host IP address conflicts. | The value is an integer ranging from 1 to 1000. |
| **period** *period-value* | Specifies the period for host IP address conflict detection. | The value is an integer ranging from 2 to 36000, in seconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To configure host IP address conflict check options, run the **arp host ip-conflict-check** command. The system counts the number of IP address conflicts in ARP entries learned between the local and remote ends or between different local interfaces. If the number of IP address conflicts is greater than or equal to the configured threshold for IP address conflicts within a specified period, the system reports a host IP address conflict alarm.If no IP address conflict occurs on the host that reports a host IP address conflict alarm for 10 consecutive minutes, the alarm is cleared.


Example
-------

# Configure the period for detecting host IP address conflicts as 200 seconds and configure the threshold for host IP address conflicts as 50.
```
<HUAWEI> system-view
[~HUAWEI] arp host ip-conflict-check period 200 retry-times 50

```