Overview of MAC Flapping-based Loop Detection
=============================================

This section describes the MAC flapping-based loop detection application on a virtual private LAN service (VPLS) network in terms of background, introduction, and basic concepts.

#### Background

Generally, redundant links are used on an Ethernet network
to provide link backup and enhance network reliability. Redundant
links, however, may produce loops and cause broadcast storms and MAC
address entry flapping. As a result, the communication quality deteriorates,
and communication services may even be interrupted. To eliminate loops
on the network, the spanning tree protocols or Layer 2 loop detection
technology was introduced. If you want to apply a spanning tree protocol,
the protocol must be supported and you need to configure it on each
user network device. If you want to apply the Layer 2 loop detection
technology, user network devices must allow Layer 2 loop detection
packets to pass. Therefore, the spanning tree protocols or the Layer
2 loop detection technology cannot be used to eliminate loops on user
networks with unknown connections or user networks that do not support
the spanning tree protocols or Layer 2 loop detection technology.

MAC flapping-based loop detection is introduced to address
this problem. It does not require protocol packet negotiation between
devices. A device independently checks whether a loop occurs on the
network based on MAC address entry flapping.


#### Introduction

Devices can block redundant links based on the frequency of MAC address entry flapping to eliminate loops on the network.

On the virtual private LAN service (VPLS) network shown
in [Figure 1](feature_0003992559.html#EN-US_CONCEPT_0172352701__fig_dc_vrp_mflp_feature_000801), pseudo wires
(PWs) are established over Multiprotocol Label Switching (MPLS) tunnels
between virtual private network (VPN) sites to transparently transmit
Layer 2 packets. When forwarding packets, the provider edges (PEs)
learn the source MAC addresses of the packets, create MAC address
entries, and establish mapping between the MAC addresses and AC interfaces
and mapping between the MAC addresses and PWs.

**Figure 1** VPLS network with MAC flapping-based loop detection enabled
  
![](images/fig_feature_image_0003993364.png)  


On the network shown in [Figure 1](feature_0003992559.html#EN-US_CONCEPT_0172352701__fig_dc_vrp_mflp_feature_000801), CE2 and CE3 are connected
to PE1 to provide redundant links. This deployment may generate loops
because the connections on the user network of CE2 and CE3 are unknown.
Specifically, if CE2 and CE3 are connected, PE1 interfaces connected
to CE2 and CE3 may receive user packets with the same source MAC address,
causing MAC address entry flapping or even damaging MAC address entries.
In this situation, you can deploy MAC flapping-based loop detection
on PE1 and configure a blocking policy for AC interfaces to prevent
such loops. The blocking policy can be either of the following:

* Blocking interfaces based on their blocking priorities: If a device
  detects a loop, it blocks the interface with a lower blocking priority.
* Blocking interfaces based on their trusted or untrusted states:
  If a device detects a loop, it blocks the untrusted interface.

MAC flapping-based loop detection can also detect PW-side
loops. The principles of blocking PWs are similar to those of blocking
AC interfaces.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

After MAC flapping-based loop detection
is configured on a device and the device receives packets with fake
source MAC addresses from attackers, the device may mistakenly conclude
that a loop has occurred and block an interface based on the configured
blocking policy. Therefore, key user traffic may be blocked. It is
recommended that you disable MAC flapping-based loop detection on
properly running devices. If you have to use MAC flapping-based loop
detection to detect whether links operate properly during site deployment,
be sure to disable this function after this stage.



#### Basic Concepts

The basic concepts for MAC flapping-based loop detection are as follows:

* **Detection cycle**
  
  If a device detects a specified number of MAC address entry flaps within a detection cycle, the device concludes that a loop has occurred. The detection cycle is configurable.
* **Temporary blocking**
  
  If a device concludes that a loop has occurred, it blocks an interface or PW for a specified period of time.
* **Permanent blocking**
  
  After an interface or a PW is blocked and then unblocked, if the total number of times that loops occur exceeds the configured allowed maximum number, the interface or PW is permanently blocked.
  
  An interface or PW that is permanently blocked can be unblocked only manually.
* **Blocking policy**
  
  MAC flapping-based loop detection has the following blocking policies:
  + Blocking interfaces based on their blocking priorities
    
    The blocking priority of an interface can be configured. When detecting a loop, a device blocks the interface with a lower blocking priority.
  + Blocking interfaces based on their trusted or untrusted states (accurate blocking)
    
    If a dynamic MAC address entry remains the same in the MAC address table within a specified period and is not deleted, the outbound interface in the MAC address entry is trusted. When detecting a loop, a device blocks an interface that is not trusted.
* **Accurate blocking**
  
  After MAC flapping-based loop detection is deployed on a device and the device detects a loop, the device blocks an AC interface with a lower blocking priority by default. However, MAC address entries of interfaces without loops may change due to the impact from a remote loop, and traffic over the interfaces with lower blocking priorities is interrupted. To address this problem, deploy accurate blocking of MAC flapping-based loop detection. Accurate blocking determines trusted and untrusted interfaces by analyzing the frequency of MAC address entry flapping. When a MAC address entry changes repeatedly, accurate blocking can accurately locate and block the interface with a loop, which is an untrusted interface.
  
  For PWs, accurate blocking in the MAC flapping-based loop detection function records trusted PWs. When the MAC address table corresponding to a PW flaps, this function can quickly locate the point where a loop occurs and block the PW.