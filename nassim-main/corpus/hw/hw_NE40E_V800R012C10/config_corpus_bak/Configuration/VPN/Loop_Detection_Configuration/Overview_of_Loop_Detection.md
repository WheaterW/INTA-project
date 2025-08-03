Overview of Loop Detection
==========================

Overview_of_Loop_Detection

#### Definition

Loop detection can detect and eliminate loops, preventing broadcast storms.


#### Purpose

Generally, redundant links are used on an Ethernet switching network to provide link backup for higher network reliability. The use of redundant links, however, may cause loops on the switching network, leading to broadcast storms and unstable MAC address entries. As a result, the communication quality deteriorates, and communication services may even be interrupted. To prevent loops on a switching network, the IEEE introduced the Spanning Tree Protocol (STP).

L2VPN technologies, including VPLS and VLL, enable geographically isolated sites to communicate over an MPLS network as if they used the same LAN or private line. As Layer 2 Ethernet technologies, VPLS and VLL encounter the following problems in application:

* If a customer network uses multiple private lines, loops may accidentally occur due to reasons such as incorrect network configurations, resulting in broadcast storms.
* If a customer network traverses a third-party network, loops may accidentally occur due to reasons such as incorrect third-party network configurations, resulting in broadcast storms.

However, because STP also needs to be deployed on CEs and relies on customer networks to some extent, varying and complex customer networks will pose great network maintenance difficulties to carriers if they use STP to prevent L2VPN loops.

This is where loop detection comes in.


#### Benefits

Loop detection offers the following benefits to carriers:

* Reduced device burdens: loop detection effectively prevents broadcast storms, reducing device burdens.
* Flexible and controllable deployment: loop detection only needs to be deployed on PEs and is totally independent of the CE network.