mice-elephant-flow enable
=========================

mice-elephant-flow enable

Function
--------



The **mice-elephant-flow enable** command enables differentiated flow scheduling on an interface.

The **undo mice-elephant-flow enable** command disables differentiated flow scheduling on an interface.



By default, differentiated flow scheduling is disabled on an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mice-elephant-flow enable**

**undo mice-elephant-flow enable**


Parameters
----------

None

Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to enable differentiated flow scheduling based on interfaces. For traffic passing through an interface where this function is enabled, the device differentiates elephant and mice flows in queues and preferentially schedules packets in mice flows. In this way, the latency of mice flows is not affected by elephant flows.

**Precautions**

For the CE6866, CE6866K, CE6860-SAN, CE6860-HAM, CE8851-32CQ8DQ-P, CE8851K, CE8850-SAN, and CE8850-HAM:

* Differentiated flow scheduling and ETS are mutually exclusive on an interface.
* Differentiated flow scheduling can be configured only when queue 6 or queue 7 uses PQ scheduling.
* If PFC is enabled for a queue, differentiated flow scheduling cannot be configured for the queue.
* On an interface, PFC for priority queue 1 is mutually exclusive with differentiated flow scheduling for any queue.
* In a priority queue of an interface, differentiated flow scheduling is mutually exclusive with antilocking PFC.
* On an interface, antilocking PFC for priority queue 1 is mutually exclusive with differentiated flow scheduling for any queue.

For the CE6820H, CE6820S, CE6820H-K, CE6863H, CE6863H-K, CE6881H, and CE6881H-K:

* Differentiated flow scheduling can be enabled on an interface only when the mice-flow queue specified by the assign queue adjust command and the queues with a higher priority than the mice-flow queue all use PQ scheduling. You can run the **display mice-elephant-flow configuration** command to view information about the interfaces and queues for which differentiated flow scheduling is enabled.
* If the flex-buffer enable and assign queue adjust commands have been run, differentiated flow scheduling can be enabled on an interface only when the dynamic threshold of the queue-level service buffer for elephant-flow queues on the interface is set to 9 using the qos buffer queue queue-index shared-threshold dynamic dynamic-value command. You can run the **display mice-elephant-flow configuration** command to view information about the interfaces and queues for which differentiated flow scheduling is enabled.
* If the flex-buffer enable and assign queue adjust commands have been run, and the dynamic threshold of the queue-level service buffer for elephant-flow queues on an interface has been set to 9, you can change this dynamic threshold only after differentiated flow scheduling is disabled using the **undo mice-elephant-flow enable** command.
* If the flex-buffer enable and assign queue adjust commands have been run, differentiated flow scheduling can be enabled on an interface only when no WRED drop profile is configured for elephant-flow queues on the interface.

For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-T, and CE6863E-48S8CQ:

* Differentiated flow scheduling and ETS are mutually exclusive on an interface.


Example
-------

# Enable differentiated flow scheduling on an interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] mice-elephant-flow enable

```