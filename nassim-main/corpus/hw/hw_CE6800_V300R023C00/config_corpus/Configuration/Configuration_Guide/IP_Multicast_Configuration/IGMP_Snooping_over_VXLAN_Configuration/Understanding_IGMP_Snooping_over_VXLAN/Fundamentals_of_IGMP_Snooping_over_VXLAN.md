Fundamentals of IGMP Snooping over VXLAN
========================================

On a VXLAN network, a VXLAN tunnel endpoint (VTEP) broadcasts received multicast traffic to user hosts in a BD by default. This not only increases the traffic load of the data network, but also causes many user hosts that have not ordered the corresponding programs to receive unnecessary multicast traffic, wasting bandwidth. To solve these problems, you can deploy IGMP snooping over VXLAN â a Layer 2 multicast feature â on the VXLAN network to implement on-demand multicast traffic forwarding.

Currently, IGMP snooping over VXLAN applies only to IPv4 underlay networks. This section describes only the fundamentals of IGMP snooping over VXLAN. For more information about IGMP snooping, see [IGMP Snooping Configuration](vrp/vrp_l2mc_cfg_0001.html).

#### Networking Description

On the IGMP snooping over VXLAN configured with ingress replication and unicast tunnels shown in [Figure 1](#EN-US_CONCEPT_0000001192881643__fig_dc_vrp_feature_l2mc_100101), the multicast source is connected to a leaf node, and multicast receivers are connected to other leaf nodes. VTEPs are configured on the leaf nodes that need to establish VXLAN tunnels. A VXLAN tunnel is established between VTEP1 and VTEP2, and another one is established between VTEP1 and VTEP3. HostA and HostB order a program, whereas HostC and HostD do not. IGMP snooping over VXLAN can be used to implement accurate multicast traffic forwarding in a BD, ensuring on-demand multicast data replication on VXLAN tunnels and user-side interfaces. Compared with the broadcast mode, this function effectively conserves VXLAN network bandwidth.

**Figure 1** Network diagram of IGMP snooping over VXLAN  
![](figure/en-us_image_0000001148381730.png)

#### Implementation

IGMP snooping over VXLAN is implemented as follows:

* Layer 2 multicast forwarding entries need to be created on the control plane. Each Layer 2 multicast forwarding entry consists of the BD name, multicast group address, router port, and dynamic multicast group member port.
  
  1. Leaf1, Leaf2, and Leaf3 are each configured with a Layer 2 BD. Multicast data is forwarded between the leaf nodes and the multicast source or receivers through Layer 2 sub-interfaces within each BD.
  2. IGMP snooping is configured in the BD of each leaf node. The leaf nodes listen to IGMP messages to create Layer 2 multicast forwarding entries, based on which the leaf nodes forward multicast data on demand at the data link layer.
  3. The querier function or IGMP snooping proxy is enabled in the BD on Leaf1. As such, Leaf1 functions as the querier and sends an IGMP Query message to Leaf2 and Leaf3.
  4. After receiving the IGMP Query message over the VXLAN tunnels, Leaf2 and Leaf3 forward the message to the hosts in the corresponding BDs and set their VXLAN tunnel interfaces (pseudo-interfaces) as router ports.
  5. After receiving the IGMP Query message, each user host that has ordered the program responds with an IGMP Report message. In this example, only HostA and HostB connected to Leaf2 respond with an IGMP Report message.
  6. After Leaf2 receives the IGMP Report messages, it parses them to obtain the address of the multicast group that the hosts want to join. It then sets the inbound interfaces of the messages as dynamic multicast group member ports (outbound interfaces used to forward multicast data) and sends the IGMP Report messages to Leaf1.
  7. After Leaf1 receives the IGMP Report messages through the VXLAN tunnel, it parses them to obtain the address of the multicast group that the hosts want to join. It then sets the VXLAN tunnel interface as a dynamic multicast group member port.
* On the forwarding plane, when multicast traffic passes through Leaf1 and Leaf2, they forward multicast data based on Layer 2 multicast forwarding entries. After multicast traffic enters a VXLAN tunnel, the encapsulated data is forwarded in ingress replication mode on the underlay network.