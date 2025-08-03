Understanding Association Between BFD Session Status and Interface Status
=========================================================================

Understanding Association Between BFD Session Status and Interface Status

#### Related Concepts

BFD for process interface status (PIS) is a simple mechanism, in which the status of a BFD session is associated with the status of an interface. This improves the sensitivity of interfaces in detecting link faults and minimizes the impact of faults on indirect links.

BFD for PIS allows BFD to immediately send a message reporting a BFD down event to the associated interface upon detecting a link fault. The interface then enters the BFD Down state, which is equivalent to the down state of a link protocol. In this state, the interface can process only BFD packets, enabling it to quickly detect link faults. Each BFD session that needs to be associated with an interface is configured as a multicast BFD session to enable BFD packet forwarding to be independent from the IP attributes on the interface.

In [Figure 1](#EN-US_CONCEPT_0000001176741809__fig1149154118296), a BFD session that uses the default multicast address as the peer address and is bound to interface 1 is set up on DeviceA and DeviceB to monitor the link between them. After BFD for PIS is configured and BFD detects a link fault, BFD immediately sends a message reporting a BFD down event to the associated interface. The interface then enters the BFD Down state.

**Figure 1** Network diagram of BFD for PIS  
![](figure/en-us_image_0000001130622390.png)

#### Application Scenarios

On the network shown in [Figure 2](#EN-US_CONCEPT_0000001176741809__fig74979313249), a BFD session is established on DeviceA and DeviceB, which are directly connected at the network layer but are segmented physically by transmission devices. If the link fails, it takes the devices a long time to detect the fault and age the direct route. As a result, the network interruption lasts for a long time.

**Figure 2** Network diagram of the link with transmission devices between two ends  
![](figure/en-us_image_0000001130622388.png)

To speed up route convergence, associate the BFD status with the interface status so that a change in the BFD session will trigger the protocol status change on the interface. When BFD detects a fault, it enters the Down state, and then the bound interface also enters the BFD Down state. The association between the BFD status and the interface status applies only to single-hop BFD sessions with a multicast IP address configured as the peer address.