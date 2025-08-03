queue shaping
=============

queue shaping

Function
--------



The **queue shaping** command enables traffic shaping for an interface queue and sets shaping parameters.

The **undo queue shaping** command disables traffic shaping for an interface queue.



By default, traffic shaping is disabled for an interface queue.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**queue** { *start-queue-index* [ **to** *end-queue-index* ] } &<1-8> **shaping** **cir** *cir-value* { **kbps** | **mbps** | **gbps** } **pir** *pir-value* { **kbps** | **mbps** | **gbps** } [ **cbs** *cbs-value* { **kbytes** | **mbytes** } **pbs** *pbs-value* { **kbytes** | **mbytes** } ]

**undo queue** { *start-queue-index* [ **to** *end-queue-index* ] } &<1-8> **shaping** [ **cir** *cir-value* { **kbps** | **mbps** | **gbps** } **pir** *pir-value* { **kbps** | **mbps** | **gbps** } [ **cbs** *cbs-value* { **kbytes** | **mbytes** } **pbs** *pbs-value* { **kbytes** | **mbytes** } ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *start-queue-index* | Specify queue-start value. | The value is an integer that ranges from 0 to 7 . |
| **to** *end-queue-index* | Specify queue-end value.  end-queue-index must be larger than or equal to start-queue-index. start-queue-index and end-queue-index determine a range of queues. If end-queue-index is not specified, a scheduling mode is configured for the queue specified by start-queue-index. | The value is an integer that ranges from 0 to 7 . |
| **cir** *cir-value* | Specifies the CIR for a priority group. | The value is an integer that ranges from 1 Mbit/s to 400 Gbit/s. |
| **kbps** | Specifies the rate unit as kbit/s. | - |
| **mbps** | Specifies the rate unit as mbit/s. | - |
| **gbps** | Specifies the rate unit as gbit/s. | - |
| **pir** *pir-value* | Specifies the PIR for a priority group. | The value is an integer that ranges from 1 Mbit/s to 400 Gbit/s. |
| **cbs** *cbs-value* | Specifies the CBS, which is the committed volume of burst traffic that can pass through an interface.  If this parameter is not specified, the CBS is 125 times the CIR. If the CBS exceeds the maximum value, the maximum value takes effect. | The value is an integer that ranges from 1 kilobyte to 512 megabytes. The default unit is kilobyte. |
| **kbytes** | Specifies that the CBS is expressed in kilobytes. | - |
| **mbytes** | Specifies that the CBS is expressed in megabytes. | - |
| **pbs** *pbs-value* | Specifies the PBS, which is the maximum volume of burst traffic that can pass through an interface.  If this parameter is not specified, the PBS is 125 times the PIR. If the PBS exceeds the maximum value, the maximum value takes effect. | The value is an integer that ranges from 1 kilobyte to 512 megabytes. The default unit is kilobyte. |



Views
-----

ETS view of the DCB


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

ETS supports two-level traffic shaping: traffic shaping based on priority groups and queues. ETS provides fine-grained QoS services.You can run the **queue shaping** command to configure traffic shaping for priority queues in a priority group. The **priority-group shaping** command configures traffic shaping for priority groups.


Example
-------

# Set the CIR to 1 mbit/s, PIR to 2 mbit/s, CBS to 12 kbytes, and PBS to 24 kbytes for queues 5, 6, and 7.
```
<HUAWEI> system-view
[~HUAWEI] dcb ets-profile myets
[*HUAWEI-ets-myets] queue 5 to 7 shaping cir 1 mbps pir 2 mbps cbs 12 kbytes pbs 24 kbytes

```