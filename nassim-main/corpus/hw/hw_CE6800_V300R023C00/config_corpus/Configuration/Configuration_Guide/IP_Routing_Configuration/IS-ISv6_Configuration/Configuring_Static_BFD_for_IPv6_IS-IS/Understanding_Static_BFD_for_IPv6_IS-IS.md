Understanding Static BFD for IPv6 IS-IS
=======================================

IS-IS detects neighbor state changes through IIH exchanges. By default, if no response is received to three consecutive IIHs within a specified period (30 seconds by default), a neighbor is considered down. For networks that require fast convergence and zero packet loss, IS-IS cannot meet link fault detection requirements. To address this problem, you can configure static BFD for IS-IS.

#### Fundamentals of Static BFD for IS-IS

In static BFD, BFD session parameters (including local and remote discriminators) are manually configured, and the requests for establishing BFD sessions are manually delivered.

Static BFD is easy to control and flexible to deploy. To conserve memory resources and ensure the reliability of key links, you can deploy static BFD to monitor these links. Static BFD helps detect link faults rapidly to achieve fast route convergence.

However, the establishment and deletion of static BFD sessions require manual intervention, meaning that these processes are inflexible and error-prone. For example, if an incorrect local or remote discriminator is configured, the BFD session cannot work.

To implement static BFD for IS-IS, a static BFD session is established based on the IPv6 address of an IS-IS neighbor interface, and static BFD is enabled on the IS-IS interface. When static BFD detects a fault, it immediately notifies IS-IS of the fault. IS-IS then deletes corresponding neighbor relationships, which triggers topology calculation and LSP update, thereby implementing fast network convergence.

In [Figure 1](#EN-US_CONCEPT_0000001176742071__en-us_concept_0275864017_fig_dc_feature_isis_001501), basic IS-IS functions are enabled on each routing device, and static BFD for IS-IS is configured on DeviceA and DeviceB.

**Figure 1** Network diagram of static BFD for IPv6 IS-IS  
![](figure/en-us_image_0000001229122465.png)

When the primary link fails, static BFD rapidly detects the fault and notifies IS-IS of the fault. IS-IS then deletes the neighbor relationship between DeviceA and DeviceB, recalculates routes, and switches traffic to the backup link.

![](public_sys-resources/note_3.0-en-us.png) 

BFD uses local and remote discriminators to distinguish multiple BFD sessions between two ends.

BFD does not replace the Hello mechanism of IS-IS. Instead, it works with IS-IS to rapidly detect faults.



#### Establishment and Deletion of a Static BFD for IS-IS Session

**Prerequisites for BFD session establishment**

* Basic IS-IS functions have been configured on each device, and IS-IS has been enabled on each involved interface.
* BFD has been configured globally on each device.
* Static BFD has been enabled on IS-IS interfaces, and the neighbor relationship has gone up (a DIS has been elected on a broadcast network).

**Process of establishing a BFD session**

* On a P2P network, when the prerequisites for BFD session establishment are met, IS-IS instructs the BFD module to establish a BFD session and trigger BFD parameter negotiation between neighbors.
* On a broadcast network, when the prerequisites for BFD session establishment are met and a DIS is elected, IS-IS instructs BFD to establish a BFD session and trigger BFD parameter negotiation between the DIS and other devices. No BFD sessions are established between non-DISs.

On broadcast networks, all devices (including non-DIS devices) of the same level residing on the same network segment establish neighbor relationships with each other. However, no static BFD for IS-IS sessions are established between non-DISs. Conversely, on P2P networks, static BFD for IS-IS sessions are established between neighbors.

On a network where a Level-1-2 neighbor relationship is established between the devices at two ends of a link, IS-IS establishes a Level-1 BFD session and a Level-2 BFD session if the network is a broadcast network, and establishes only one BFD session if the network is a P2P network.

**Process of deleting a BFD session**

* On a P2P network, when an IS-IS neighbor relationship is not up, the corresponding BFD session is deleted.
* On a broadcast network, when an IS-IS neighbor relationship is not up or a new DIS is elected, the corresponding BFD session is deleted.

![](public_sys-resources/note_3.0-en-us.png) 

BFD detects faults only on one-hop links between IS-IS neighbors. This is because IS-IS establishes only one-hop neighbor relationships.

**Response to the down event of a BFD session**

When BFD detects a link failure, it generates a down event and informs IS-IS of the failure. IS-IS then suppresses the involved neighbor relationship and recalculates routes, ensuring fast network convergence.