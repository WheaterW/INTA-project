Configuring an L2VPN Service on a QinQ Stacking Sub-interface
=============================================================

To enable a physical interface to provide multiple users with access to an L2VPN, configure a QinQ stacking sub-interface and bind it to a VSI or L2VC.

#### Usage Scenario

In early stages, QinQ was primarily deployed on CEs on Layer 2 networks. VLAN tags are added to packets using VLAN stacking and services are forwarded on Layer 2 networks based on the outer VLAN tags. QinQ stacking sub-interfaces are configured on PEs to identify user VLANs and add outer VLAN tags to Layer 2 frames.

This implementation, however, faces a problem that one physical interface cannot provide L2VPN access to multiple users. To address this problem, you can configure a QinQ stacking sub-interface and bind it to a VSI or L2VC to provide L2VPN access to multiple users.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

QinQ stacking sub-interfaces cannot forward packets at Layer 2 and must be deployed with the L2VPN.

* VPWS
  
  VPWS is a point-to-point virtual leased line technology and supports almost all link layer protocols. VPWS simulates the traditional leased line services on IP networks and provides asymmetric and low-cost digital data network (DDN) services. For users on both ends of the leased line, VPWS is similar to the traditional leased line services.
* VPLS
  
  VPLS makes a multipoint-to-multipoint VPN networking possible. With VPLS, the carrier can transmit Ethernet-based multipoint-to-multipoint services for users over an MPLS backbone network.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

When receiving a Layer 2 multicast packet from the network side, a QinQ stacking sub-interface connected to a VPLS network removes the outer tag, adds the learned inner and outer tags to the packet, and then forwards the packet to a downstream device.

#### Pre-configuration Tasks

Before you configure the QinQ stacking sub-interface provide L2VPN access, plan user VLANs properly so that packets received by QinQ stacking sub-interfaces carry one VLAN tag.



[Configuring a QinQ Stacking Sub-interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_qinq_cfg_0018.html)

This section describes how to configure a QinQ stacking sub-interface on a provider edge (PE) to provide Layer 2 virtual private network (L2VPN) access so that the inner virtual local area network (VLAN) tags of user packets are transparently transmitted over an ISP network.

[(Optional) Configuring a PW-tag Action](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_qinq_cfg_0057b.html)

This section describes how to configure a PW-tag action so that a PE changes the P-Tag of packets to be forwarded over a PW in tagged mode to ensure normal communication with non-Huawei devices on an L2VPN network.

[Configuring an L2VPN Service](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_qinq_cfg_0019.html)

Layer 2 virtual private network (L2VPN) services include virtual private wire service (VPWS) and virtual private LAN service (VPLS). After you configure QinQ stacking sub-interfaces, bind these sub-interfaces to a virtual switching instance (VSI) or VPWS instance to provide L2VPN access for users.

[Verifying the L2VPN Service Configuration on the QinQ Stacking Sub-interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_qinq_cfg_0020.html)

After you configure an L2VPN service on a QinQ stacking sub-interface, verify the configuration