mice-elephant-flow
==================

mice-elephant-flow

Function
--------



The **mice-elephant-flow** command displays the mice-elephant-flow view.

The **undo mice-elephant-flow** command deletes and exits the mice-elephant-flow view.



By default, the mice-elephant-flow view is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mice-elephant-flow**

**undo mice-elephant-flow**


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

**Usage Scenario**

You can run this command to enter the mice-elephant-flow view or delete the mice-elephant-flow view. In the mice-elephant-flow view, you can configure differentiated flow scheduling. The device differentiates elephant and mice flows in queues and preferentially schedules packets in mice flows so that the latency of mice flows is not affected by elephant flows.

**Precautions**

For the CE6820H, CE6820S, CE6820H-K, CE6863H, CE6863H-K, CE6881H, and CE6881H-K:

* You can run the **mice-elephant-flow** command to enter the mice-elephant-flow view only after you run the **system resource balance** command to set the resource mode to balance and restart the device to make the configuration take effect. If another mode is configured, the mice-elephant-flow view cannot be displayed even if the configured mode does not take effect.
* If the system resource mode has been set to balance and differentiated flow scheduling has been configured, you need to delete the differentiated flow scheduling configuration in the AI service view before changing the system resource mode. (You can run the **ai-service** command to enter the AI service view, and then run the **undo mice-elephant-flow** command to delete the mice-elephant-flow view.)


Example
-------

# Enter the mice-elephant-flow view.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] mice-elephant-flow
[*HUAWEI-ai-service-mice-elephant-flow]

```