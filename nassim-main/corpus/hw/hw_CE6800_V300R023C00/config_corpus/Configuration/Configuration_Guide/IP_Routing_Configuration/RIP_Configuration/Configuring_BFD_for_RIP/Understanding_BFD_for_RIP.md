Understanding BFD for RIP
=========================

Understanding BFD for RIP

#### Context

On a RIP network, RIP devices monitor neighbor status by exchanging Update messages. If a link fault occurs on the network, it takes a long time for RIP to detect the fault. For high-speed services, a large number of packets may be lost during this period, causing loss to users. As such, it is recommended to speed up fault detection and route convergence to improve network reliability.

You can configure Bidirectional Forwarding Detection (BFD) for RIP on a routing device to enable BFD to detect a fault (if any) within milliseconds and notify the RIP module of the fault accordingly. Then, the routing device will delete the route that passes through the faulty link and switch traffic to the backup link to speed up RIP convergence.

[Table 1](#EN-US_CONCEPT_0000001176742607__en-us_concept_0190705515_tab_dc_vrp_rip_feature_002012) lists the link fault detection mechanisms and convergence speeds before and after BFD for RIP is configured.

**Table 1** Differences before and after BFD for RIP is configured
| BFD for RIP | Link Fault Detection Mechanism | Convergence Speed |
| --- | --- | --- |
| Not configured | The RIP age timer expires. | Within seconds |
| Configured | A BFD session goes down to indicate that the neighbor is down. | Within milliseconds |



#### Related Concepts

The BFD mechanism bidirectionally detects the connectivity of a data protocol on the same path between routing devices. It rapidly detects a fault (if any) and notifies the protocol module of the fault, which speeds up route convergence and minimizes traffic loss caused by network topology changes.

BFD is classified into either static BFD or dynamic BFD.

* Static BFD
  
  BFD session parameters, including local and remote discriminators, are manually configured through commands.
  
  Static BFD applies to networks with only a few links that require high reliability.
* Dynamic BFD
  
  BFD session setup is dynamically triggered by routing protocols. The local discriminator is dynamically allocated, and the remote discriminator is obtained from BFD packets sent by the peer.
  
  After a new RIP neighbor relationship is established, RIP notifies BFD of the neighbor relationship and detection parameters (including destination and source addresses), and then BFD sets up a session based on these parameters. When a fault occurs on the link, the routing protocol associated with BFD can quickly detect the BFD session down event, and traffic is immediately switched to the backup link to minimize data loss.
  
  Dynamic BFD applies to networks with network-wide high reliability requirements.


#### Implementation

[Figure 1](#EN-US_CONCEPT_0000001176742607__en-us_concept_0190705515_fig_dc_vrp_rip_feature_002001) shows how BFD is implemented on a RIP network.

* Implementation of dynamic BFD for RIP:
  
  1. RIP neighbor relationships are established among DeviceA, DeviceB, and DeviceC, and between DeviceB and DeviceD.
  2. BFD for RIP is enabled on DeviceA and DeviceB.
  3. Based on route calculation, the next hop of the route originating from DeviceA to DeviceD is DeviceB.
  4. If the link between DeviceA and DeviceB fails, BFD will rapidly detect the fault and report it to DeviceA. DeviceA then deletes the route with DeviceB as its next hop from its routing table.
  5. DeviceA recalculates routes and selects the following path: DeviceC -> DeviceB -> DeviceD.
  6. After the link between DeviceA and DeviceB recovers, a new BFD session is established between them. DeviceA can then receive routing information from DeviceB and reselect an optimal link to forward packets.
* Implementation of static BFD for RIP:
  
  1. RIP neighbor relationships are established among DeviceA, DeviceB, and DeviceC, and between DeviceB and DeviceD.
  2. Static BFD is configured on the interfaces that connect DeviceA and DeviceB.
  3. If the link between DeviceA and DeviceB fails, BFD will rapidly detect the fault and report it to DeviceA. DeviceA then deletes the route with DeviceB as its next hop from its routing table.
  4. After the link between DeviceA and DeviceB recovers, a new BFD session is established between them. DeviceA can then receive routing information from DeviceB and reselect an optimal link to forward packets.

**Figure 1** Network diagram of BFD for RIP  
![](figure/en-us_image_0000001176742637.png)

#### Application Scenarios

BFD for RIP is applicable to networks with high reliability requirements.


#### Benefits

BFD for RIP improves network reliability and enables devices to rapidly detect link faults, speeding up route convergence on RIP networks.