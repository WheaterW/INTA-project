Understanding IPv6 PIM-SM in the ASM Model
==========================================

PIM-SM can implement P2MP on-demand data transmission on large-scale networks with sparsely distributed multicast data receivers.

PIM-SM assumes that no host wants to receive multicast data. Therefore, it sets up an MDT only if hosts request multicast data, and then sends the data to the hosts along the MDT.

#### Related Concepts

[Figure 1](#EN-US_CONCEPT_0000001538765142__fig_dc_vrp_multicast_feature_300110) shows the typical networking of IPv6 PIM-SM.

**Figure 1** IPv6 PIM-SM networking  
![](figure/en-us_image_0000001589190373.png)

In [Figure 1](#EN-US_CONCEPT_0000001538765142__fig_dc_vrp_multicast_feature_300110), PIM-SM involves the following basic concepts:

* IPv6 PIM-SM domain: A network consisting of IPv6 PIM devices is called an IPv6 PIM network. You can set BSR boundaries on interfaces of multicast devices to limit the transmission of BSR messages and divide an IPv6 network into multiple IPv6 PIM-SM domains. This isolates multicast services and facilitates network management.
* DR: There are two types of DRs on an IPv6 PIM network:
  + Multicast source DR: an IPv6 PIM device directly connected to a multicast source and responsible for sending Register messages to an RP on an IPv6 PIM-SM network.
  + Receiver DR: an IPv6 PIM device directly connected to multicast group members (usually receiver hosts) and responsible for forwarding multicast data to the multicast group members.
* RP: An RP is the forwarding core on an IPv6 PIM-SM network, used to process join requests from the receiver DR and registration requests from the multicast source DR. An RP constructs an RPT with itself as the root and creates (S, G) entries to transmit multicast data to multicast group members. Devices on the network must know the RP address. [Table 1](#EN-US_CONCEPT_0000001538765142__tab_007247_01) describes the types of RPs.
  
  **Table 1** RP classification
  | RP Type | Implementation | Usage Scenario | Precaution |
  | --- | --- | --- | --- |
  | Static RP | You can manually configure the same address as a static RP address on all PIM devices on the network. All PIM devices on the network use this address as the RP address. | Static RPs are recommended on small- and medium-sized networks because such networks are stable and have low requirements on network devices. If only one multicast source exists on the network, setting the device directly connected to the multicast source as a static RP is recommended. In this case, the RP is also the source DR, which eliminates the need for the source DR to register with the RP. | To use a static RP, ensure that all devices, including the RP, have the same RP information and the same range of IPv6 multicast groups that the RP serves. |
  | Dynamic RP | A dynamic RP is elected among the PIM devices that are configured as candidate-RPs (C-RPs) in the same IPv6 PIM domain. Specifically, the BSR sends Bootstrap messages to collect all C-RP information as an RP-Set, and advertises the RP-Set information to all PIM devices in the domain. Then, all the PIM devices use the same RP-Set information and follow the same rules to elect an RP. If the elected RP fails, the other C-RPs compete again for a new RP. | Dynamic RPs can be used on large-scale networks to ensure high reliability and easy maintenance. + If multiple multicast sources exist on the network and are densely distributed, configuring core devices close to the multicast sources as C-RPs is recommended. + If multiple users are densely distributed on the network, configuring core devices close to the users as C-RPs is recommended. | If dynamic RP election is used, a BSR is required. Through the BSR, the devices on the multicast network can dynamically learn the mapping between the multicast group and the RP. |
* **BSR**: A BSR on a PIM-SM network collects RP information, summarizes that information into an RP-Set (group-RP mapping database), and advertises the RP-Set in the entire PIM-SM network. A network can have only one BSR but can have multiple candidate-BSRs (C-BSRs). If the BSR fails, a new BSR is elected from the C-BSRs.
* **RPT**: An RPT is an MDT, with an RP as the root and multicast group members as leaves.
* **SPT**: An SPT is an MDT, with the multicast source as the root and multicast group members as leaves.

#### Implementation

The multicast data forwarding process in an IPv6 PIM-SM domain is as follows:

1. [Neighbor Discovery](#EN-US_CONCEPT_0000001538765142__section_dc_vrp_multicast_feature_300104): Each PIM device in an IPv6 PIM-SM domain periodically sends [Hello messages](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300502) to all other PIM devices to discover IPv6 PIM neighbors and maintain IPv6 PIM neighbor relationships. By default, a PIM device accepts other PIM control messages or multicast packets received from a neighbor, regardless of whether the PIM device has received [Hello messages](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300502) from the neighbor. However, if the neighbor check function is configured on a PIM device, the PIM device accepts other PIM control messages or multicast packets received from a neighbor only after the PIM device receives Hello messages from the neighbor.
2. [DR Election](#EN-US_CONCEPT_0000001538765142__section_dc_vrp_multicast_feature_300105): PIM devices exchange [Hello messages](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300502) to elect DRs (a receiver DR and a multicast source DR) on a shared network segment. The receiver DR is the only multicast data forwarder on the shared network segment, and the multicast source DR is responsible for forwarding multicast data received from the multicast source to the RP.
3. [RP Discovery](#EN-US_CONCEPT_0000001538765142__section_dc_vrp_multicast_feature_300106): An RP is the core device in a PIM-SM domain. An RP, either dynamic or static, forwards multicast data over the entire network.
4. [RPT Setup](#EN-US_CONCEPT_0000001538765142__section_dc_vrp_multicast_feature_300107): PIM-SM assumes that no hosts need to receive multicast data, and multicast data is transmitted only to the hosts that require the data. The core task of implementing multicast forwarding is to set up and maintain an RPT, along which the RP forwards multicast data to receivers.
5. [Switchover to an SPT](#EN-US_CONCEPT_0000001538765142__section_dc_vrp_multicast_feature_300108): In a PIM-SM domain, a multicast group uniquely corresponds to an RP and an RPT. The RP is like a transfer station, through which all multicast data is forwarded. However, the path along which the RP forwards multicast data may not be the shortest path from the multicast source to receivers. In addition, the load of the RP increases with the multicast traffic volume. If the multicast data forwarding rate exceeds a configured threshold, the multicast data is switched to an SPT, which is the optimal path from the multicast source to receivers, reducing the burden on the RP.

If a network problem occurs, the Assert mechanism or a DR switchover delay can be used to guarantee that multicast data is transmitted properly.

* [Assert](#EN-US_CONCEPT_0000001538765142__section_dc_vrp_multicast_feature_300109): If multiple PIM devices exist on a network segment, the same multicast packets may be sent to the network segment repeatedly. The Assert mechanism resolves this issue by selecting only one multicast data forwarder on a network segment.
* [DR Switchover Delay](#EN-US_CONCEPT_0000001538765142__section_dc_vrp_multicast_feature_300110): When an interface changes from a DR to a non-DR, the PIM device immediately stops using this interface to forward data. If the new DR has not received multicast data, multicast data traffic is temporarily interrupted. If a DR switchover delay is configured, the interface continues forwarding multicast data until the delay expires, which prevents multicast data traffic from being interrupted.

The implementation process is described in detail as follows:


#### Neighbor Discovery

Each PIM-enabled interface on a PIM device sends [Hello messages](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300502). A multicast packet that carries a [Hello message](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300502) has the following characteristics:

* The destination address is FF02::d, indicating that this packet is destined for all PIM devices on the same network segment as the interface that sent this packet.
* The source address is an interface IP address.
* The TTL value is 1, indicating that the packet is sent only to neighbor interfaces.

[Hello messages](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300502) are used to discover neighbors, negotiate protocol parameters, and maintain neighbor relationships.

**Discovering PIM neighbors**

All PIM devices on the same network segment must receive multicast packets with the destination address FF02::d. Directly connected multicast devices can then learn neighbor information from received [Hello messages](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300502).

**Negotiating protocol parameters**

[Hello messages](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300502) carry multiple protocol parameters, which are negotiated between neighbors and are described as follows:

* DR\_Priority: priority used by each device interface to participate in DR election. The higher the priority value, the higher the probability that the interface is elected as the DR.
* Holdtime: timeout period during which a neighbor remains in the reachable state.
* LAN\_Delay: delay for transmitting a [Prune message](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300505) on the shared network segment.
* Override-Interval: interval carried in a [Hello message](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300502) for overriding a Prune action.

**Maintaining neighbor relationships**

PIM devices periodically exchange [Hello messages](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300502). If a PIM device does not receive a new [Hello message](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300502) from its PIM neighbor within the holdtime, the device considers the neighbor unreachable and deletes it from the neighbor list.

Changes of PIM neighbors will lead to multicast topology changes on the network. If an upstream or a downstream neighbor along an MDT becomes unreachable, multicast routes re-converge, and the MDT is updated.


#### DR Election

A multicast source or group members may be connected to multiple PIM devices on the same network segment, as shown in [Figure 2](#EN-US_CONCEPT_0000001538765142__fig_dc_vrp_multicast_feature_300106). The PIM devices exchange [Hello messages](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300502) to set up PIM neighbor relationships. Each of the [Hello messages](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300502) carries the DR priority and the address of the interface connected to this network segment. Each device compares the local information with the information carried in received Hello messages to elect a DR. This process is called DR election, which adheres to the following rules:

* The device whose interface has the highest DR priority on the network segment wins.
* If the candidates have the same DR priority or some devices on the network segment do not support encapsulating DR priorities in [Hello messages](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300502), the candidate with the highest IP address wins.

**Figure 2** DR election  
![](figure/en-us_image_0000001589365329.png)

#### RP Discovery

An RP is the forwarding core on a PIM-SM network. RPs are classified as static RPs or dynamic RPs.

* Static RP: A static RP is specified by running a command to configure the same RP address on all devices on the network, with no RP election involved.
* Dynamic RP: A dynamic RP is elected from a set of PIM devices.

On the network shown in [Figure 3](#EN-US_CONCEPT_0000001538765142__fig_dc_vrp_multicast_feature_300103), dynamic RP election is used. In this case, C-BSRs must be configured, and the C-BSRs compete for the BSR.

**Figure 3** Dynamic RP election  
![](figure/en-us_image_0000001538765246.png)

The dynamic RP election rules are as follows:

1. Initially, each C-BSR considers itself a BSR and advertises a [Bootstrap message](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300506) to its neighbors. The [Bootstrap message](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300506) carries the address and priority of the C-BSR. Each device compares the C-BSR information contained in all received [Bootstrap messages](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300506) and its information to determine the BSR. All the devices follow the same election rules. Therefore, they will elect the same BSR and know the BSR's address. The election rules are as follows:
   
   1. The candidate with the highest priority (largest priority value) is elected.
   2. If the candidates have the same priority, the one with the highest IP address is elected.
2. The C-RPs send [Advertisement messages](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300510) to the BSR. Each of the message carries the address of the C-RP that sent it, the range of multicast groups that the C-RP serves, and the priority of the C-RP.
3. The BSR collects the received information as an RP-Set, encapsulates the RP-Set information in a [Bootstrap message](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300506), and advertises the Bootstrap message to all PIM-SM devices.
4. Based on the RP-Set information, each device performs calculation and comparison using the same rules to elect an RP from multiple C-RPs. The rules are as follows:
   1. The C-RP with the longest mask length of the served group address range matching the specific multicast group wins.
   2. If the corresponding group addresses that all C-RPs serve have the same mask length, the C-RP with the highest priority (lowest priority value) wins.
   3. In the case of the same priority, hash functions are executed. The candidate with the greatest result value wins.
   4. If all the preceding factors are the same, the C-RP with the highest address wins.
5. Because all devices use the same RP-Set and the same election rules, they obtain the same mapping between the multicast group and the RP. The devices save the mapping between the multicast group and the RP to guide subsequent multicast operations.

If a device needs to interwork with an auto-RP-capable device, auto-RP listening can be enabled. After auto-RP listening is enabled, the device can receive auto-RP announcement and discovery messages, parse the messages to obtain source addresses, and perform RPF checks based on the source addresses.

* If an RPF check fails, the device discards the auto-RP message.
* If an RPF check succeeds, the device forwards the auto-RP message to its PIM neighbors. The auto-RP message carries the multicast group address range served by the RP to guide subsequent multicast operations.

#### RPT Setup

The process of setting up an RPT is the process of establishing a multicast data forwarding path. [Figure 4](#EN-US_CONCEPT_0000001538765142__fig_dc_vrp_multicast_feature_300101) shows the networking.

**Figure 4** RPT setup  
![](figure/en-us_image_0000001589190389.png)

RPT setup and data forwarding are described as follows:

* After receiving the first multicast packet of the multicast group G from a multicast source, the multicast source DR encapsulates the multicast packet in a [Register message](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300503) and unicasts the message to the RP. The RP creates an (S, G) entry to register the multicast source information.
* When a receiver joins the multicast group G through IGMP, the receiver DR sends a [Join message](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300505) to the RP. An (\*, G) entry is then created on each hop along the path to the RP, and an RPT is created.
* When a receiver joins a multicast group and a multicast source sends a multicast packet for the group, the multicast packet is encapsulated in a [Register message](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300503) and unicast to the RP. The RP then forwards the multicast data along the RPT to the receiver.

The RPT helps implement on-demand multicast data forwarding, which reduces bandwidth consumption.


#### Switchover to an SPT

On a PIM-SM network, a multicast group corresponds to only one RP, and only one RPT is set up for this group. Before the switchover to an SPT is performed, all multicast packets of a multicast group must be encapsulated in [Register messages](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300503) and then sent to the RP. After receiving the messages, the RP de-encapsulates them and forwards the multicast packets along the RPT.

Since the RP transfers all of the multicast packets forwarded along the RPT, it may be overloaded when multicast traffic is heavy. To solve this problem, PIM-SM allows the RP or receiver DR to trigger a switchover to an SPT. On the network shown in [Figure 5](#EN-US_CONCEPT_0000001538765142__fig_dc_vrp_multicast_feature_300102), an SPT is set up from the multicast source to the receiver, and multicast data can be transmitted along the SPT.

**Figure 5** Switchover to an SPT triggered by the receiver DR  
![](figure/en-us_image_0000001589285113.png)

The modes for a switchover to an SPT are described as follows:

* Switchover to an SPT triggered by the RP: After receiving a [Register message](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300503) from the source DR, the RP decapsulates the message and forwards the multicast data in the message along the RPT to receivers. In addition, the RP sends SPT [Join messages](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300505) to the source DR to set up an SPT from the RP to the source. After the SPT is set up and the RP receives the first multicast data packet along the SPT, the RP stops processing [Register messages](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300503), preventing frequent encapsulation and decapsulation on the source DR and RP. Multicast data is sent from the device directly connected to the multicast source to the RP along the SPT, and then forwarded to receivers along the RPT.
* The process of a switchover to an SPT triggered by the receiver DR is described in detail as follows:
  1. On the network shown in [Figure 5](#EN-US_CONCEPT_0000001538765142__fig_dc_vrp_multicast_feature_300102), multicast data is forwarded along the RPT, which is a part of the following path: multicast source DR (DeviceA) -> RP (DeviceB) -> receiver DR (DeviceD) -> Receiver.
  2. The receiver DR periodically checks the forwarding rate of multicast packets corresponding to an (S, G) entry. If the receiver DR finds that the forwarding rate is greater than the configured threshold, it triggers a switchover to the SPT.
  3. The receiver DR sends (S, G) [Join messages](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300505) to the multicast source DR. After receiving multicast data along the SPT, the receiver DR discards the multicast data received along the RPT and sends a [Prune message](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300505) to the RP to instruct it to delete the receiver from the RPT. At this point, the switchover from the RPT to the SPT is completed.
  4. Multicast data is forwarded along the SPT, which is a part of the following path: multicast source DR (DeviceA) -> receiver DR (DeviceD) -> Receiver.

After the SPT is set up from the source to multicast group members, subsequent multicast packets may bypass the RP. As the RPT may not be the shortest path, a switchover to the SPT reduces the delay in transmitting multicast data on the network.

If one multicast source sends packets to multiple multicast groups simultaneously and a policy is specified for the switchover to the SPT for a specified group range:

* Before a switchover to the SPT is performed, these packets reach the receiver DR along the RPT.
* After a switchover to the SPT is performed, only the packets sent to the multicast groups within the range specified in the policy for the switchover are forwarded along the SPT, whereas the packets sent to other multicast groups are still forwarded along the RPT.

![](public_sys-resources/note_3.0-en-us.png) 

When the receiver DR triggers a switchover to an SPT, it sends a Prune message containing information about multicast sources to be pruned to the RP. The RP then prunes these multicast sources. If the number of packed multicast sources to be pruned exceeds the maximum number of multicast sources that can be packed in a single Join/Prune message (calculated based on the MTU of the interface), only some multicast sources are packed and sent to the RP for pruning. Traffic of the multicast sources that are not packed for prune is still forwarded to the receiver DR through the RP and is discarded after the RPF check.



#### Assert

Either of the following conditions indicates that another multicast forwarder exists on the network segment:

* A multicast packet fails the RPF check.
* The interface that receives a multicast packet is a downstream interface corresponding to the (S, G) entry on the local device.

In this case, the device performs the Assert mechanism.

The device sends an [Assert message](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300507) through the downstream interface. The downstream interface also receives an [Assert message](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300507) from a different multicast forwarder on the network segment. In the packet in which an [Assert message](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300507) is encapsulated, the destination address is FF02::d, the source address is the downstream interface's address, and the TTL value is 1. The [Assert message](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300507) carries the route cost from the PIM device to the multicast source or RP, the priority of the used unicast routing protocol, and the address of the multicast group (G).

The device compares its information with that contained in the received message for Assert election. The rules are as follows:

1. The device with the highest unicast routing priority wins.
2. If devices have the same unicast routing priority, the one with the smallest route cost to the multicast source wins.
3. If all the preceding conditions are the same, the device with the highest downstream interface IP address wins.

The device performs the following operations based on the Assert election result:

* If the device wins the election, its downstream interface remains in the forwarding state and is responsible for forwarding multicast packets corresponding to the (S, G) entry on the network segment. This downstream interface is called an Assert winner.
* If the device fails in the election, its downstream interface is prohibited from forwarding multicast packets and is deleted from the downstream interface list of the (S, G) entry. This downstream interface is called an Assert loser.

After Assert election is complete, only one upstream device has a downstream interface that serves the network segment, and the downstream interface transmits only one copy of each multicast packet. The Assert winner then periodically sends [Assert messages](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300507) to maintain its status as the Assert winner. If the Assert loser does not receive any [Assert message](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300507) from the Assert winner within the timer maintained by the Assert loser, the loser restores the forwarding status of its downstream interface.


#### DR Switchover Delay

If an existing DR fails, PIM neighbor relationships time out, triggering the election of a new DR. By default, when an interface changes from a DR to a non-DR, the device immediately stops using this interface to forward data. If the new DR has not received multicast data, multicast data traffic is temporarily interrupted.

If a PIM-SM interface with a PIM DR switchover delay configured changes from a DR to a non-DR upon reception of [Hello messages](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300502) from a new neighbor, the interface retains some DR functions and continues forwarding multicast packets until the delay times out. If the device in the DR switchover delay state receives data from a new DR, it immediately stops forwarding packets, which prevents duplicate data flows. When a new IGMP Report message is received on the shared network segment, the new DR (instead of the original DR in the DR switchover delay state) sends a PIM [Join message](vrp_ipv6pim_cfg_0005.html#EN-US_CONCEPT_0000001589284989__section_dc_vrp_multicast_feature_300505) upstream. If the new DR receives multicast data from the original DR before the DR switchover delay expires, an Assert election is triggered.