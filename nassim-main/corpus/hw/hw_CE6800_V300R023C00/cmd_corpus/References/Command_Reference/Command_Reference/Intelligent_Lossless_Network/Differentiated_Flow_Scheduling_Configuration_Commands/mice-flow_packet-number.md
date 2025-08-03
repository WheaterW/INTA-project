mice-flow packet-number
=======================

mice-flow packet-number

Function
--------



The **mice-flow packet-number** command configures the first N (specified by number) packets in a flow to be identified as a mice flow.

The **undo mice-flow packet-number** command restores the default configuration.



By default, the number of packets in a mice flow is set to 128 in differentiated flow scheduling.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mice-flow packet-number** *number*

**undo mice-flow packet-number** [ *number* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *number* | Number of packets in a mice flow. The first N (specified by number) packets in a flow are identified as a mice flow. | For the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer that ranges from 2 to 1024. The default value is 128.  For the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM:The value is an integer that ranges from 1 to 1024. The default value is 128. |



Views
-----

mice-elephant-flow view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to set the number of packets in a mice flow. On a device enabled with differentiated flow scheduling, the first N (specified by number) packets in a flow are identified as a mice flow and are preferentially scheduled.

**Precautions**

When the number of packets in a mice flow is configured during traffic transmission, packets may be out of order. You are advised to stop traffic transmission before the configuration.


Example
-------

# Set the number of packets in a mice flow to 100.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[~HUAWEI-ai-service] mice-elephant-flow
[~HUAWEI-ai-service-mice-elephant-flow] mice-flow packet-number 100

```