Understanding Dynamic BFD for IS-IS
===================================

IS-IS detects neighbor state changes through IIH exchanges. By default, if no response is received to three consecutive IIHs within a specified period (30 seconds by default), a neighbor is considered down. For networks that require fast convergence and zero packet loss, IS-IS cannot meet link fault detection requirements. To address this problem, you can configure dynamic BFD for IS-IS.

#### Fundamentals of Dynamic BFD for IS-IS

In dynamic BFD for IS-IS, BFD sessions are dynamically established by IS-IS rather than being manually configured. Dynamic BFD notifies IS-IS if it detects a fault, and IS-IS then immediately sets the involved neighbor to down, updates LSPs, and performs PRC. This process ensures fast IS-IS route convergence.

Dynamic BFD for IS-IS is more flexible than static BFD for IS-IS, is easy to configure, and can be used in scenarios where BFD needs to be configured on the entire network. Dynamic BFD for IS-IS sessions are dynamically established by IS-IS, preventing manual misconfigurations.

In [Figure 1](#EN-US_CONCEPT_0000001176743791__fig_dc_feature_isis_001501), basic IS-IS functions are enabled on each routing device, and dynamic BFD for IS-IS is configured on DeviceA and DeviceB.

**Figure 1** Network diagram of dynamic BFD for IS-IS  
![](figure/en-us_image_0000001130624374.png)

When the primary link fails, dynamic BFD rapidly detects the fault and notifies IS-IS of the fault. IS-IS then deletes the neighbor relationship between DeviceA and DeviceB, recalculates routes, and switches traffic to the backup link.

![](public_sys-resources/note_3.0-en-us.png) 

BFD uses local and remote discriminators to distinguish multiple BFD sessions between two ends.

BFD does not replace the Hello mechanism of IS-IS. Instead, it works with IS-IS to rapidly detect faults.



#### Establishment and Deletion of a Dynamic BFD for IS-IS Session

**Prerequisites for BFD session establishment**

* Basic IS-IS functions have been configured on each device, and IS-IS has been enabled on each involved interface.
* BFD has been configured globally on each device.
* BFD has been enabled on IS-IS interfaces or for an IS-IS process, and the neighbor has gone up (a DIS has been elected on a broadcast network).

**Process of establishing a BFD session**

* On a P2P network, when the prerequisites for BFD session establishment are met, IS-IS instructs the BFD module to establish a BFD session and trigger BFD parameter negotiation between neighbors.
* On a broadcast network, when the prerequisites for BFD session establishment are met and a DIS is elected, IS-IS instructs BFD to establish a BFD session and trigger BFD parameter negotiation between the DIS and other devices. No BFD sessions are established between non-DISs.

On broadcast networks, all devices (including non-DIS devices) of the same level residing on the same network segment establish neighbor relationships with each other. However, no dynamic BFD for IS-IS sessions are established between non-DISs. Conversely, on P2P networks, static BFD for IS-IS sessions are established between neighbors.

On a network where a Level-1-2 neighbor relationship is established between the devices at two ends of a link, IS-IS establishes a Level-1 BFD session and a Level-2 BFD session if the network is a broadcast network, and establishes only one BFD session if the network is a P2P network.

**Process of deleting a BFD session**

* On a P2P network, when an IS-IS neighbor relationship is not up, the corresponding BFD session is deleted.
* On a broadcast network, when an IS-IS neighbor relationship is not up or a new DIS is elected, the corresponding BFD session is deleted.

If the configurations of dynamic BFD sessions are deleted or dynamic BFD for IS-IS is disabled from an interface, all BFD sessions corresponding to the neighbor relationships that are up on the interface are deleted. Furthermore, if the interface is a DIS and the DIS is up, all BFD sessions corresponding to the neighbor relationships on the interface are deleted.

If BFD is disabled from an IS-IS process, BFD sessions are deleted from the process.

![](public_sys-resources/note_3.0-en-us.png) 

BFD detects faults only on one-hop links between IS-IS neighbors. This is because IS-IS establishes only one-hop neighbor relationships.

After dynamic BFD is globally disabled in an IS-IS process, the BFD sessions on all the interfaces in this IS-IS process are deleted.

**Response to the down event of a BFD session**

When BFD detects a link failure, it generates a down event and informs IS-IS of the failure. IS-IS then suppresses the involved neighbor relationship and recalculates routes, ensuring fast network convergence.