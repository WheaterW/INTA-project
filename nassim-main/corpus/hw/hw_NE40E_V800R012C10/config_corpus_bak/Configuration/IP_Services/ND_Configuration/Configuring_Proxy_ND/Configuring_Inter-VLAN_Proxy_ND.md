Configuring Inter-VLAN Proxy ND
===============================

Inter-VLAN proxy ND can be deployed if hosts that are on the same network segment and physical network but belong to different VLANs need to communicate with each other at Layer 3.

#### Context

If hosts are on the same network segment and physical network but belong to different VLANs, inter-VLAN proxy ND must be enabled on the associated VLAN interfaces to enable Layer 3 interworking between the hosts.

In a VLAN aggregation scenario shown in [Figure 1](#EN-US_TASK_0161511717__en-us_concept_0161511699_fig_dc_vrp_nd_feature_002903), HostA and HostB are on the same network segment, but HostA belongs to sub-VLAN 2 and HostB belongs to sub-VLAN 3. HostA and HostB cannot implement Layer 2 interworking.**Figure 1** Typical networking of inter-VLAN proxy ND in a VLAN aggregation scenario  
![](images/fig_dc_vrp_nd_feature_003708.png)  

To address this problem, enable inter-VLAN proxy ND on Device's interface 1.

On the L2VPN+L3VPN IP RAN shown in [Figure 2](#EN-US_TASK_0161511717__en-us_concept_0161511699_fig_dc_vrp_nd_feature_002906), the CSGs are connected to the ASG through L2VE sub-interfaces, and the ASG terminates L2VPN packets and is connected to the BGP/MPLS IPv6 VPN through an L3VE sub-interface. eNodeB1 and eNodeB2 belong to VLAN 2 and VLAN 3, respectively. As such, users on the same network segment on the eNodeBs cannot directly communicate with each other at Layer 2.**Figure 2** Typical networking of inter-VLAN proxy ND in an L2VPN+L3VPN IP RAN  
![](images/fig_dc_vrp_nd_feature_003715.png)

To address this problem, enable inter-VLAN proxy ND on the L3VE sub-interfaces of the ASG.

1. CSG1 sends an NS packet to request for the MAC address of CSG2.
2. Upon receipt of the NS packet, the ASG finds that the destination IPv6 address in the packet is not its own IPv6 address and therefore determines that the NS packet does not request for its MAC address. The ASG then checks whether ND entries destined for CSG2 exist.
   * If such ND entries exist and the VLAN information in the ND entries is inconsistent with the VLAN information configured on the interface receiving the NS packet, the ASG determines whether inter-VLAN proxy ND is enabled on the L3VE sub-interface.
     + If inter-VLAN proxy ND is enabled, the ASG sends the MAC address of the L3VE sub-interface to CSG1.
       
       Upon receipt of the NA packet, CSG1 considers that this packet is sent by CSG2. CSG1 learns the MAC address of the ASG's L3VE sub-interface in the NA packet and sends data packets to CSG2 using this MAC address.
     + If inter-VLAN proxy ND is not enabled, the NS packet is discarded.
   * If such ND entries do not exist, the NS packet sent by CSG1 is discarded and CSG2 checks whether inter-VLAN proxy ND is enabled on the associated L3VE sub-interface.
     + If inter-VLAN proxy ND is enabled, the NS packet is forwarded in VLAN 3 as a multicast packet and the destination IPv6 address of the NS packet is CSG2's IPv6 address. The corresponding ND entries are generated after the NA packet sent by CSG2 is received.
     + If inter-VLAN proxy ND is not enabled, no action is required.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is enabled on the interface.
4. Run [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address*/*prefix-length* } [ **tag** *tag-value* ]
   
   
   
   A global unicast address is configured for the interface.
5. Run [**ipv6 nd proxy inter-access-vlan enable**](cmdqueryname=ipv6+nd+proxy+inter-access-vlan+enable)
   
   
   
   Inter-VLAN proxy ND is enabled.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.