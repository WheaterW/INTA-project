Overview of Smart Link
======================

Overview of Smart Link

#### Definition

Smart Link, also called backup link, is often used in dual-uplink networking for reliable and effective backup as well as fast switchover.


#### Purpose

If a downstream device is single-homed to an upstream device, services will be interrupted when a single point of failure occurs on the uplink. Conversely, if a downstream device is dual-homed to two upstream devices, the impact on services due to a single point of failure is reduced.

**Figure 1** Smart Link  
![](figure/en-us_image_0000001176743183.png)

On the network shown in [Figure 1](#EN-US_CONCEPT_0000001176743175__fig10647257125310), DeviceA is dual-homed to DeviceB and DeviceC. DeviceA has two links to DeviceD: DeviceA -> DeviceB -> DeviceD and DeviceA -> DeviceC -> DeviceD. This would usually cause a loop and a subsequent network storm. However, if you configure a Smart Link group on DeviceA, the two links can work in active/standby mode. In normal cases, the link where interface1 resides is the primary link, and the link where interface2 resides is the secondary link. If the link where interface1 resides fails, Smart Link automatically switches data traffic to the link where interface2 resides to ensure service continuity.

Smart Link delivers the following benefits to dual-homing networks:

* Prevents loops in dual-uplink networking.
* Is easy to configure and use compared with other active/standby backup technologies.
* Switches between primary and secondary links within milliseconds and ensures that data is forwarded normally to the greatest extent.