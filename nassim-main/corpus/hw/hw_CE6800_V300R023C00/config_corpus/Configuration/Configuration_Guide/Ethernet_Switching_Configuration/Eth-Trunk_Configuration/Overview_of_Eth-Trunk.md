Overview of Eth-Trunk
=====================

![](public_sys-resources/note_3.0-en-us.png) 

Related services cannot be configured on Layer 3 Eth-Trunk interfaces of the CE6885-LL (low latency mode).


#### Definition

Eth-Trunk, also called Ethernet link aggregation, bundles multiple physical links into a logical link to increase link bandwidth. The bundled links back each other up, increasing reliability.


#### Purpose

As networks grow in scale, users require Ethernet backbone networks to provide higher bandwidth and reliability. In the past, the usual way to increase the bandwidth was to use higher-speed boards or larger-capacity devices, which is costly and inflexible.

Using Eth-Trunk, bandwidth is increased by bundling a group of physical interfaces into a single logical interface, without having to upgrade hardware. Eth-Trunk also greatly improves link reliability by providing the link backup mechanism.

Eth-Trunk has the following advantages:

* Increased bandwidth
  
  The maximum bandwidth of the link aggregation group (LAG) interface is the sum of the bandwidth of its member interfaces.
* Higher reliability
  
  When an active link fails, traffic on this active link is switched to another functional active link, improving link reliability.
* Load balancing
  
  In a LAG, traffic is load balanced among all functional active links.