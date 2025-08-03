assign queue(mice-elephant-flow view)
=====================================

assign queue(mice-elephant-flow view)

Function
--------



The **assign queue** command specifies a queue for which differentiated flow scheduling is enabled.

The **undo assign queue** command disables differentiated flow scheduling in a specified queue.



By default, differentiated flow scheduling is not enabled in any queue.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

For CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K:

**assign queue** { *start-queue-index* [ **to** *end-queue-index* ] } &<1-6>

**undo assign queue** { *start-queue-index* [ **to** *end-queue-index* ] } &<1-6>

For CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ:

**assign queue** { *start-queue-index* [ **to** *end-queue-index* ] } &<1-2>

**undo assign queue** { *start-queue-index* [ **to** *end-queue-index* ] } &<1-2>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *start-queue-index* | Specifies the start queue index. | For the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 0 to 7.  For the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM:The value is an integer ranging from 0 to 5. |
| **to** | Two queue indexes connected by "to" indicate all queues between the two queues. | - |
| *end-queue-index* | Specifies the end queue index.  The value of end-queue-index must be greater than or equal to the value of start-queue-index. start-queue-index and end-queue-index together specify a queue range. If end-queue-index is not specified, the queue is specified only by start-queue-index. | For the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 0 to 7.  For the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM:The value is an integer ranging from 0 to 5. |



Views
-----

mice-elephant-flow view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to specify the queues for which differentiated flow scheduling is enabled.

**Precautions**

If PFC is enabled for a queue, differentiated flow scheduling cannot be configured for the queue.For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-T, and CE6863E-48S8CQ:Differentiated flow scheduling cannot be enabled for more than two queues.


Example
-------

# Enable differentiated flow scheduling in queue 3.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[~HUAWEI-ai-service] mice-elephant-flow
[~HUAWEI-ai-service-mice-elephant-flow] assign queue 3

```