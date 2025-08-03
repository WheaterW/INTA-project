Understanding OSPF Neighbor Relationship Flapping Suppression
=============================================================

Understanding OSPF Neighbor Relationship Flapping Suppression

#### Context

If an interface carrying OSPF services frequently alternates between up and down, OSPF neighbor relationship flapping will occur on the interface. In this case, OSPF quickly sends Hello packets to re-establish neighbor relationships, synchronizes LSDBs, and triggers route calculation. As a result, a large number of packets are exchanged, compromising the stability of existing neighbor relationships, OSPF services, and other OSPF-dependent services (such as BGP). OSPF neighbor relationship flapping suppression can be used to address this issue. If OSPF neighbor relationships flap frequently, this function delays the re-establishment of the relationships or prevents service traffic from passing through flapping links.


#### Related Concepts

flapping-event: reported when the final status of a neighbor relationship on an interface changes from Full to a non-Full state. The flapping-event triggers flapping detection.

flapping-count: number of times flapping has occurred.

detecting-interval: detection interval. The interval is used to determine whether to trigger a valid flapping\_event.

threshold: flapping suppression threshold. When the flapping\_count reaches or exceeds the threshold, flapping suppression takes effect.

resume-interval: interval for exiting OSPF neighbor relationship flapping suppression. If the interval between two successive valid flapping\_events is longer than the resume-interval, the flapping\_count is reset.


#### Fundamentals

**Flapping detection**

When configured with OSPF neighbor relationship flapping suppression, an OSPF interface starts a flapping counter. If the interval between two successive neighbor relationship states (changing from Full to a non-Full state) is shorter than the **detecting-interval**, a valid flapping\_event is recorded, and the flapping\_count is incremented by 1. When the flapping\_count reaches or exceeds the **threshold**, flapping suppression takes effect. If the interval between two successive neighbor relationship states (changing from Full to a non-Full state) is longer than the **resume-interval**, the flapping\_count is reset.

The **detecting-interval**, **threshold**, and **resume-interval** parameters are configurable.

![](../public_sys-resources/note_3.0-en-us.png) 

The value of **resume-interval** must be greater than that of **detecting-interval**.

**Flapping suppression**

OSPF neighbor relationship flapping suppression operates in two modes:

* Hold-down mode: If flooding and topology changes frequently occur during the establishment of neighbor relationships, re-establishment of these relationships is disabled during Hold-down suppression. This minimizes LSDB synchronization attempts and packet exchanges.
* Hold-max-cost mode: If the traffic forwarding path changes frequently, interfaces use 65535 (maximum value) as the cost of the flapping link during Hold-max-cost suppression. This prevents traffic from passing through the flapping link.

If both modes are enabled, flapping suppression initially works in Hold-down mode (until its duration expires) and then in Hold-max-cost mode.

By default, the Hold-max-cost mode is enabled for OSPF. The mode and suppression duration can be changed manually.

If an attack causes frequent neighbor relationship flapping, Hold-down mode can minimize the impact of the attack.

![](../public_sys-resources/note_3.0-en-us.png) 

When an interface enters the flapping suppression state, all neighbor relationships on the interface enter the state accordingly.

**Exiting flapping suppression**

Interfaces exit flapping suppression in the following scenarios:

* The suppression timer expires.
* The corresponding OSPF process is reset.
* An OSPF neighbor relationship is reset.
* A user forcibly exits flapping suppression.

#### Typical Scenarios

**Basic scenario**

As shown in [Figure 1](#EN-US_CONCEPT_0000001130783218__ospf_suppress_flapping_0001), traffic is forwarded along the path DeviceA -> DeviceB -> DeviceC -> DeviceE when the links are working properly. If the link between DeviceB and DeviceC fails, the forwarding path switches to DeviceA -> DeviceB -> DeviceD -> DeviceE. If the neighbor relationship between DeviceB and DeviceC frequently flaps at the early stage of the path switchover, the DeviceA -> DeviceE traffic will alternate between the primary and backup paths frequently, causing traffic loss and affecting network stability. If neighbor relationship flapping is severe, flapping suppression takes effect.

* If flapping suppression works in Hold-down mode, the neighbor relationship between DeviceB and DeviceC is not re-established during the suppression period, in which traffic is forwarded along the path DeviceA -> DeviceB -> DeviceD -> DeviceE.
* If flapping suppression works in Hold-max-cost mode, 65535 is used as the cost of the link between DeviceB and DeviceC during the suppression period, and traffic is forwarded along the path DeviceA -> DeviceB -> DeviceD -> DeviceE.

**Figure 1** Flapping suppression in a basic scenario  
![](figure/en-us_image_0000001176663047.png)

**Single forwarding path scenario**

When only one forwarding path exists on the network, disconnecting the neighbor relationship between any two devices on the path will interrupt traffic. As shown in [Figure 2](#EN-US_CONCEPT_0000001130783218__ospf_suppress_flapping_0002), traffic is forwarded through the DeviceA -> DeviceB -> DeviceC -> DeviceE path. If the neighbor relationship between DeviceB and DeviceC flaps and the flapping meets suppression conditions, flapping suppression takes effect. However, if the neighbor relationship between DeviceB and DeviceC is not re-established, the whole network will be divided. Therefore, Hold-max-cost mode (rather than Hold-down mode) is recommended. If flapping suppression works in Hold-max-cost mode, 65535 is used as the cost of the link between DeviceB and DeviceC during the suppression period. After the network becomes stable and the suppression timer expires, flapping suppression exits automatically, and services recover immediately.

![](../public_sys-resources/note_3.0-en-us.png) 

By default, the Hold-max-cost mode is enabled for OSPF.


**Figure 2** Flapping suppression in a single forwarding path scenario  
![](figure/en-us_image_0000001130623504.png)

**Broadcast scenario**

As shown in [Figure 3](#EN-US_CONCEPT_0000001130783218__ospf_suppress_flapping_0003), four devices are connected to the same broadcast network and establish neighbor relationships of the broadcast network type. If DeviceC flaps due to a link failure, and DeviceA and DeviceB were deployed at different time points (DeviceA was deployed earlier for example) or the flapping suppression parameters on DeviceA and DeviceB are different, DeviceA first detects the flapping and suppresses DeviceC, and therefore the Hello packets sent by DeviceA do not carry DeviceC's router ID. However, DeviceB has not detected any flapping and still considers DeviceC a valid node. As a result, the DR candidates identified by DeviceA are DeviceB and DeviceD, whereas the DR candidates identified by DeviceB are DeviceA, DeviceC, and DeviceD. This may lead to route calculation errors due to different DR election results. To prevent this problem in scenarios where an interface has multiple neighbors, such as on a broadcast, P2MP, or NBMA network, all neighbors on the interface need to be suppressed if one or more of the interface's neighbor relationships are in Exstart or Down state. Specifically, if DeviceC flaps, DeviceA, DeviceB, and DeviceD on the broadcast network are all suppressed. After the network becomes stable and the suppression timer expires, flapping suppression exits automatically, and DeviceA, DeviceB, and DeviceD are restored to normal status.

**Figure 3** Flapping suppression on a broadcast network  
![](figure/en-us_image_0000001130623498.png)

**Multi-area scenario**

As shown in [Figure 4](#EN-US_CONCEPT_0000001130783218__ospf_suppress_flapping_0004), DeviceA, DeviceB, DeviceC, DeviceE, and DeviceF are connected in area 1, and DeviceB, DeviceD, and DeviceE are connected in area 0 (backbone area). Traffic from DeviceA to DeviceF is preferentially forwarded along an intra-area route, and the forwarding path is DeviceA -> DeviceB -> DeviceC -> DeviceE -> DeviceF. If the neighbor relationship between DeviceB and DeviceC flaps and the flapping meets suppression conditions, flapping suppression takes effect and defaults to the Hold-max-cost mode. However, the forwarding path remains unchanged (DeviceA -> DeviceB -> DeviceC -> DeviceE -> DeviceF) after the neighbor flapping occurs because intra-area routes take precedence over inter-area routes during route selection regardless of costs according to OSPF route selection rules. The Hold-max-cost mode cannot suppress traffic path switching in this case. To prevent traffic loss in multi-area scenarios, configure the Hold-down mode to prevent the neighbor relationship between DeviceB and DeviceC from being re-established during the suppression period. During this period, traffic is forwarded along the path DeviceA -> DeviceB -> DeviceD -> DeviceE -> DeviceF.

![](../public_sys-resources/note_3.0-en-us.png) 

By default, the Hold-max-cost mode is enabled for OSPF. You can change the mode to Hold-down using a command.


**Figure 4** Flapping suppression in a multi-area scenario  
![](figure/en-us_image_0000001176663045.png)