Overview of TCP FlexBuffer
==========================

Overview of TCP FlexBuffer

#### Definition

TCP FlexBuffer is a technology that dynamically adjusts the buffer allocation for mice- and elephant-flow queues.


#### Purpose

A data center network is dominated by delay-sensitive mice flows, with many typical services made up of mice flows only. Differentiated flow scheduling can prevent mice flows from being hindered by elephant flows. However, it is largely ineffective when only mice flows exist, and also fails to address the packet loss problem caused by burst traffic and incast traffic. The most effective solution to this packet loss problem is to increase the queue buffer to absorb traffic. To this end, TCP FlexBuffer is introduced to dynamically adjust the buffer sizes of mice- and elephant-flow queues while differentiated flow scheduling ensures the preferential forwarding of mice flows. In this way, the low delay and high throughput of mice- and elephant-flow queues can be ensured.