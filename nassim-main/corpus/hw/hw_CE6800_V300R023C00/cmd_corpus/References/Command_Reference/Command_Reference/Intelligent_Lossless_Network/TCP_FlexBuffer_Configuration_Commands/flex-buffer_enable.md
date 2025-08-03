flex-buffer enable
==================

flex-buffer enable

Function
--------



The **flex-buffer enable** command enables TCP FlexBuffer.

The **undo flex-buffer enable** command disables TCP FlexBuffer.



By default, TCP FlexBuffer is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**flex-buffer enable**

**undo flex-buffer enable**


Parameters
----------

None

Views
-----

mice-elephant-flow view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A data center network is dominated by delay-sensitive mice flows, with many typical services made up of mice flows only. Differentiated flow scheduling can prevent mice flows from being hindered by elephant flows. However, it is largely ineffective when only mice flows exist, and also fails to address the packet loss problem caused by burst traffic and incast traffic.The most effective solution to this packet loss problem is to increase the queue buffer to absorb traffic. TCP FlexBuffer can dynamically adjust the buffer for mice- and elephant-flow queues to improve performance.

**Precautions**

* When TCP FlexBuffer is enabled, differentiated flow scheduling can be enabled for only one queue.
* If TCP FlexBuffer is enabled on the device, a queue cannot have both the WRED drop profile bound and differentiated flow scheduling enabled. If a queue has both the WRED drop profile bound and differentiated flow scheduling enabled, TCP FlexBuffer cannot be enabled.
* TCP FlexBuffer takes effect only for interface queues enabled with differentiated flow scheduling.

For the CE6866, CE6866K, CE6860-SAN, CE6860-HAM, CE8851-32CQ8DQ-P, CE8851K, CE8850-SAN, and CE8850-HAM:

* If TCP FlexBuffer is enabled on the device, a queue cannot have both static ECN and differentiated flow scheduling enabled. If a queue has both static ECN and differentiated flow scheduling enabled, TCP FlexBuffer cannot be enabled.
* Global ECN and TCP FlexBuffer cannot be both enabled. That is, the **qos ecn enable** and **flex-buffer enable** commands are mutually exclusive.
* TCP FlexBuffer occupies four WRED drop profiles. After TCP FlexBuffer is enabled, the number of WRED drop profiles that can be configured on the device decreases by four.

For the CE6820H, CE6820S, CE6820H-K, CE6863H, CE6863H-K, CE6881H, and CE6881H-K:

* TCP FlexBuffer occupies nine WRED drop profiles. After TCP FlexBuffer is enabled, the number of WRED drop profiles that can be configured on the device decreases by nine.
* TCP FlexBuffer takes effect only when the dynamic threshold of the queue-level service buffer for the elephant-flow queue is set to 9 using the qos buffer queue queue-index shared-threshold dynamic dynamic-value command.

For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-T, and CE6863E-48S8CQ:

* If TCP FlexBuffer is enabled on the device, a queue cannot have both static ECN and differentiated flow scheduling enabled. If a queue has both static ECN and differentiated flow scheduling enabled, TCP FlexBuffer cannot be enabled.
* Global ECN and TCP FlexBuffer cannot be both enabled. That is, the **qos ecn enable** and **flex-buffer enable** commands are mutually exclusive.


Example
-------

# Enable TCP FlexBuffer.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] mice-elephant-flow
[*HUAWEI-ai-service-mice-elephant-flow] flex-buffer enable

```