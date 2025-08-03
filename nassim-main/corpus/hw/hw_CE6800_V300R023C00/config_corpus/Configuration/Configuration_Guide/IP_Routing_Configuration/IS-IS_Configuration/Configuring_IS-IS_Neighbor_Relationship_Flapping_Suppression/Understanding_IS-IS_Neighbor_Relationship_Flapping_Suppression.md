Understanding IS-IS Neighbor Relationship Flapping Suppression
==============================================================

IS-IS neighbor relationship flapping suppression works by delaying IS-IS neighbor relationship reestablishment or setting the link cost to the maximum value (16777214 for the cost style wide and 63 for the cost style narrow).

#### Context

If an IS-IS interface alternates between up and down, IS-IS neighbor relationship flapping occurs on the interface. During the flapping, IS-IS frequently sends IIHs to reestablish the neighbor relationship, synchronizes LSDBs, and recalculates routes. In this process, a large number of packets are exchanged, impacting neighbor relationship stability, IS-IS services, and IS-IS-dependent services. IS-IS neighbor relationship flapping suppression can address this problem by either delaying IS-IS neighbor relationship reestablishment, or setting the link cost to the maximum value to prevent service traffic from passing through flapping links.


#### Related Concepts

Flapping\_event: reported when the state of a neighbor relationship on an interface last changes from Up to Initial or Down. The flapping\_event triggers flapping detection. Flapping\_count: number of times flapping has occurred.

Detecting-interval: interval at which flapping is detected. It is used to determine whether a valid flapping\_event should be triggered.

Threshold: flapping suppression threshold. When the flapping\_count reaches or exceeds the threshold, flapping suppression starts.

Resume-interval: interval used to determine whether flapping suppression exits. If the interval between two valid flapping\_events is greater than or equal to the resume-interval, flapping suppression exits.


#### Fundamentals of IS-IS Neighbor Relationship Flapping Suppression

**Flapping detection**

IS-IS interfaces start a flapping counter. If the interval between two consecutive flapping\_events is shorter than the detecting-interval, a valid flapping\_event is recorded, and the flapping\_count increases by 1. When the flapping\_count reaches or exceeds the threshold, the system determines that flapping occurs, implements flapping suppression, and sets the flapping\_count to 0. If the interval between two valid flapping\_events is greater than or equal to the resume-interval before the flapping\_count reaches the threshold again, the system sets the flapping\_count to 0. Interfaces start the suppression timer when the state of a neighbor relationship last changes to Init or Down. The detecting-interval, threshold, and resume-interval are configurable.

**Flapping suppression**

Flapping suppression works in either Hold-down or Hold-max-cost mode.

* Hold-down mode: If frequent flooding and network topology changes occur during neighbor relationship establishment, interfaces prevent neighbor relationship reestablishment during Hold-down suppression to minimize LSDB synchronization attempts and packet exchanges.
* Hold-max-cost mode: If the traffic forwarding path frequently changes, interfaces use the maximum cost of the flapping link during the suppression period to prevent traffic from passing through the flapping link.

If both modes are enabled, flapping suppression first works in Hold-down mode and then in Hold-max-cost mode.

The default mode is Hold-max-cost mode. The mode and suppression period can be changed manually.

![](public_sys-resources/note_3.0-en-us.png) 

When an interface enters the flapping suppression state, all neighbor relationships on the interface enter the state accordingly.

**Exiting flapping suppression**

Interfaces exit flapping suppression in the following scenarios:

* The suppression timer expires.
* The corresponding IS-IS process is reset.
* A command is run to exit flapping suppression.
* Three IIHs in which the padding TLV carries a sub-TLV with the value being 251 are sent consecutively to instruct a neighbor to forcibly exit flapping suppression.

#### Typical Scenarios

**Basic scenario**

In [Figure 1](#EN-US_CONCEPT_0000001130624308__isis_suppress_flapping_0001), the traffic forwarding path is DeviceA -> DeviceB -> DeviceC -> DeviceE -> DeviceF. After the link between DeviceB and DeviceC fails, the forwarding path switches to DeviceA -> DeviceB -> DeviceD -> DeviceE -> DeviceF. If the neighbor relationship between DeviceB and DeviceC frequently flaps when the path switchover commences, the forwarding path will also experience frequent switching, causing traffic loss and affecting network stability. If the neighbor relationship flapping meets suppression conditions, flapping suppression takes effect.

* If flapping suppression works in Hold-down mode, the neighbor relationship between DeviceB and DeviceC is prevented from being reestablished during the suppression period, in which traffic is forwarded along the path DeviceA -> DeviceB -> DeviceD -> DeviceE -> DeviceF.
* If flapping suppression works in Hold-max-cost mode, the maximum cost is used as the cost of the link between DeviceB and DeviceC during the suppression period, and traffic is forwarded along the path DeviceA -> DeviceB -> DeviceD -> DeviceE -> DeviceF.

**Figure 1** Flapping suppression in a basic scenario  
![](figure/en-us_image_0000001130784158.png)

**Broadcast scenario**

In [Figure 2](#EN-US_CONCEPT_0000001130624308__isis_suppress_flapping_0003), four devices are neighbors on the same broadcast network. If DeviceC flaps due to a link failure, and DeviceA and DeviceB were deployed at different times (for example, DeviceA was deployed earlier) or their flapping suppression parameters are different, DeviceA first detects the flapping and suppresses the neighbor relationship with DeviceC. Consequently, the IIHs sent by DeviceA do not carry DeviceC's router ID. However, DeviceB has not yet detected the flapping and still considers DeviceC valid. As a result, the DIS candidates identified by Device A are Device B and Device D, whereas the DIS candidates identified by Device B are Device A, Device C, and Device D. Different candidates result in different election results, which may lead to route calculation errors. To prevent this problem in scenarios where a broadcast interface has multiple neighbors, all the neighbor relationships on the interface are suppressed when the state of a neighbor relationship last changes to Initial or Down. Specifically, if DeviceC flaps, neighbor relationships with DeviceA, DeviceB, and DeviceD are all suppressed. After the network stabilizes and the suppression timer expires, DeviceA, DeviceB, and DeviceD are restored to normal status.

**Figure 2** Flapping suppression on a broadcast network  
![](figure/en-us_image_0000001176663907.png)

**Scenario of multi-level networking**

In [Figure 3](#EN-US_CONCEPT_0000001130624308__isis_suppress_flapping_0004), DeviceA, DeviceB, DeviceC, DeviceE, and DeviceF are Level-1 neighbors in area 1. DeviceB, DeviceD, and DeviceE are Level-2 neighbors in area 0. Traffic from DeviceA to DeviceF is preferentially forwarded along an intra-area route, and the forwarding path is DeviceA -> DeviceB -> DeviceC -> DeviceE -> DeviceF. When the neighbor relationship between DeviceB and DeviceC flaps and the flapping meets suppression conditions, flapping suppression takes effect in the default mode (Hold-max-cost mode). Consequently, the maximum cost is used as the cost of the link between DeviceB and DeviceC. However, the forwarding path remains unchanged because intra-area routes take precedence over inter-area routes during route selection according to IS-IS route selection rules. To prevent traffic loss in multi-area scenarios, configure the Hold-down mode to prevent the neighbor relationship between DeviceB and DeviceC from being reestablished during the suppression period. During this period, traffic is forwarded along the path DeviceA -> DeviceB -> DeviceD -> DeviceE -> DeviceF.

![](public_sys-resources/note_3.0-en-us.png) 

By default, the Hold-max-cost mode takes effect. The mode can be changed to Hold-down manually.


**Figure 3** Flapping suppression in a multi-level scenario  
![](figure/en-us_image_0000001130784156.png)

**Scenario with both link-bundle and IS-IS neighbor relationship flapping suppression configured**

When the traffic rate is too high for one link to tolerate, multiple links must be used. In such cases, if one link fails, traffic is switched to another link and excess traffic is discarded due to the new link's limited forwarding capacity. If the number of faulty links reaches the upper threshold, the maximum cost is used as the cost of all links in the link bundle to switch all service traffic to the backup nodes. If both link-bundle and neighbor relationship flapping suppression are configured and the number of flapping links reaches the upper threshold, the maximum cost must be configured as the cost of all other links in the link bundle to prevent service loss caused by user traffic congestion. In [Figure 4](#EN-US_CONCEPT_0000001130624308__isis_suppress_flapping_0006), two parallel links exist between DeviceA and DeviceC. If link 1 is faulty and link 2 is incapable of bearing all service traffic, traffic loss occurs. If both link-bundle and neighbor relationship flapping suppression are configured and link 1 flaps, the maximum cost must also be configured for link 2 to avoid service traffic congestion. Only the Hold-max-cost mode therefore can be configured for neighbor relationship flapping suppression to switch the traffic forwarding path to DeviceA -> DeviceB -> DeviceC.

**Figure 4** Scenario with both link-bundle and IS-IS neighbor relationship flapping suppression configured  
![](figure/en-us_image_0000001176663905.png)