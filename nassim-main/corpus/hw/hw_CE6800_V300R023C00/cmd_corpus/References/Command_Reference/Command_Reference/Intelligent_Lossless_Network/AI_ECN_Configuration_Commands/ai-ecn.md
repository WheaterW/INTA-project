ai-ecn
======

ai-ecn

Function
--------



The **ai-ecn** command displays the AI ECN view.

The **undo ai-ecn** command deletes all configurations in the AI ECN view and disables AI ECN.



By default, the AI ECN is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ai-ecn**

**undo ai-ecn**


Parameters
----------

None

Views
-----

AI Service view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run the ai-ecn command to enter the AI ECN view and configure the AI ECN threshold function for lossless queues. After this function is enabled, the ECN threshold of lossless queues can be intelligently adjusted through the intelligent algorithm.


Example
-------

# Enter the AI ECN view.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] ai-ecn
[*HUAWEI-ai-service-ai-ecn]

```