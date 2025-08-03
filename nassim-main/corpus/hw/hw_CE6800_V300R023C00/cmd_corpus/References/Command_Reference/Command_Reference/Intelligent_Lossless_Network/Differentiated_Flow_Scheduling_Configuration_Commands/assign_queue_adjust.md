assign queue adjust
===================

assign queue adjust

Function
--------



The **assign queue adjust** command specifies an elephant-flow queue for which differentiated flow scheduling is to be enabled and adjusts mice flows in the elephant-flow queue to the mice-flow queue.

The **undo assign queue** command disables the functions of specifying an elephant-flow queue for which differentiated flow scheduling is to be enabled and adjusting mice flows in the elephant-flow queue to the mice-flow queue.



By default, no queue is specified for which differentiated flow scheduling is to be enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**assign queue** { *start-queue-index* [ **to** *end-queue-index* ] } &<1-7> **adjust** **mice-flow** **to** **queue** *queue-id*

**undo assign queue** { *start-queue-index* [ **to** *end-queue-index* ] } &<1-7>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *start-queue-index* | Specifies the start queue ID of elephant-flow queues. | The value is an integer that ranges from 0 to 6. |
| **to** *end-queue-index* | Specifies the end queue ID of elephant-flow queues.  The value of end-queue-index must be greater than or equal to that of start-queue-index. start-queue-index and end-queue-index determine the range of elephant-flow queues. Elephant-flow queues include all queues from start-queue-index to end-queue-index.  If to end-queue-index is not specified, the elephant-flow queue is the one specified by start-queue-index. | The value is an integer that ranges from 0 to 6. |
| **mice-flow** | Moves mice flows from the elephant-flow queue to the mice-flow queue. | - |
| **queue** | Specifies a mice-flow queue. | - |
| *queue-id* | Specifies a mice-flow queue.  Mice flows in an elephant-flow queue are moved to a mice-flow queue. queue-id must be greater than end-queue-index. | The value is an integer ranging from 1 to 7. |



Views
-----

mice-elephant-flow view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to specify the queue for which differentiated flow scheduling is to be enabled on the device and adjust mice flows in the elephant-flow queue to the mice-flow queue.

**Precautions**

* Only one mice-flow queue can be configured, and multiple elephant-flow queues can be configured.
* If the new mice-flow queue is different from the existing mice-flow queue, delete the original mice-flow queue configuration. For example, if you run the command to specify elephant-flow queues a and b and mice-flow queue c, and then run the command to specify elephant-flow queues d and e and mice-flow queue f, you need to delete the original configuration of elephant-flow queues a and b and mice-flow queue c.
* If the mice-flow queue is not changed, the elephant-flow queue configuration is accumulated. For example, if elephant-flow queues a and b and mice-flow queue c are configured first, and then elephant-flow queues d and e and mice-flow queue c are configured, elephant-flow queues are queues a, b, d, and e.
* On an interface enabled with differentiated flow scheduling, PQ scheduling must be configured for the mice-flow queue and queues with higher priorities than the mice-flow queue. Otherwise, the assign queue adjust command cannot be configured globally.
* If TCP FlexBuffer has been enabled globally and when you run the assign queue adjust command globally, the dynamic threshold of the queue-level service buffer space for elephant-flow queues configured on the interface where differentiated flow scheduling is enabled must be set to 9 using the qos buffer queue queue-index shared-threshold dynamic dynamic-value command.
* If TCP FlexBuffer has been enabled globally and when you run the assign queue adjust command globally, ensure that no WRED profile is bound to elephant-flow queues on the interface where differentiated flow scheduling is enabled.
* Queues 6 and 7 are typically used for high-priority protocols or other services. Therefore, exercise caution when using queues 6 and 7.

Example
-------

# Enable differentiated flow scheduling in queue 3 and adjust mice flows in elephant-flow queue 3 to mice-flow queue 4.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[~HUAWEI-ai-service] mice-elephant-flow
[~HUAWEI-ai-service-mice-elephant-flow] assign queue 3 adjust mice-flow to queue 4

```