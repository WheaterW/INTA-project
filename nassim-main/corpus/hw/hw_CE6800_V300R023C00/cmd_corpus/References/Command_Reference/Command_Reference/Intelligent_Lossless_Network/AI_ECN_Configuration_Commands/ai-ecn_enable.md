ai-ecn enable
=============

ai-ecn enable

Function
--------



The **ai-ecn enable** command enables the AI ECN threshold function for lossless queues.

The **undo ai-ecn enable** command disables the AI ECN threshold function for lossless queues.



By default, the AI ECN threshold function is disabled for lossless queues.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ai-ecn enable**

**undo ai-ecn enable**


Parameters
----------

None

Views
-----

AI ECN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the ai-ecn enable command to enable the AI ECN threshold function for lossless queues. After this function is enabled, the device collects traffic characteristics on the live network and sends them to the AI service component. The AI service component intelligently sets the optimal ECN threshold for lossless queues based on the preloaded traffic model file to ensure low latency and high throughput of lossless queues. In this way, the optimal lossless service performance can be achieved in different traffic scenarios.

**Precautions**

* The AI ECN threshold function identifies lossless queues based on the PFC priority enabled on an interface. This function is not affected after you run the **dcb pfc global disable** command in the system view to disable PFC.
* If the static ECN or WRED function has been enabled for a lossless queue on a PFC-enabled interface, the AI ECN function cannot be enabled for the queue. Similarly, if the AI ECN function has been enabled for a lossless queue, the static ECN or WRED function cannot be enabled for the queue.

Example
-------

# Enable the AI ECN threshold function for lossless queues.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] ai-ecn
[*HUAWEI-ai-service-ai-ecn] ai-ecn enable

```