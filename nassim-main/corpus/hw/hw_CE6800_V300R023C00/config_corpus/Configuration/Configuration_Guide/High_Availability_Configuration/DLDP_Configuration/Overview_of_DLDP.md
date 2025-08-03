Overview of DLDP
================

Overview of DLDP

#### Definition

The Device Link Detection Protocol (DLDP) monitors the link status of optical fibers or copper twisted pairs such as super category 5 twisted pairs. Upon detecting a unidirectional link on an interface, DLDP automatically shuts down or prompts the user to manually shut down the interface to prevent network faults.


#### Purpose

Sometimes unidirectional links occur on networks. On a unidirectional link, the local device can receive packets from the remote device at the link layer, but the remote device cannot receive packets from the local device. On the network shown in [Figure 1](#EN-US_CONCEPT_0000001464856137__fig7417125513482) and [Figure 2](#EN-US_CONCEPT_0000001464856137__fig16506825185214), a unidirectional link fault may be caused by intersected fibers or disconnection of an optical fiber.

**Figure 1** Cross-disconnected optical fibers  
![](figure/en-us_image_0000001415619122.png)
**Figure 2** Disconnected or broken optical fibers.  
![](figure/en-us_image_0000001415015970.png)

Unidirectional links may result in problems such as loops on a spanning tree protocol (STP) topology. As a link layer protocol, DLDP works with physical layer protocols to monitor the link status on a device. The auto-negotiation mechanism at the physical layer detects physical signals and faults, and DLDP identifies the remote device, detects unidirectional links, shuts down unreachable interfaces, and more. The auto-negotiation mechanism and DLDP work together to detect and disable physical and logical unidirectional links. When both ends of a link are working properly at the physical layer, DLDP detects whether the link is properly connected at the link layer and whether the two ends can exchange packets. This detection capability goes beyond that of the auto-negotiation mechanism at the physical layer.