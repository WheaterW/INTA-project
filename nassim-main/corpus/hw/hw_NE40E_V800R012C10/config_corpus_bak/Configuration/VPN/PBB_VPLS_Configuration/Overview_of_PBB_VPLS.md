Overview of PBB VPLS
====================

Overview_of_PBB_VPLS

#### Definition

Provider backbone bridge (PBB), a technique defined in IEEE 802.1ah, precedes customer MAC (C-MAC) addresses with backbone MAC (B-MAC) addresses in user packets to completely separate the user network from the carrier network. Unlike traditional Ethernet local area networks (LANs), a PBB network uses both public and user MAC addresses. This implementation ensures network stability and reduces the number of MAC entries required on public network devices. In addition, the VLAN tag field defined in IEEE 802.1Q has only 12 bits and can identify only a maximum of 4K VLANs, which cannot meet the user requirements for sufficient tunnels. PBB, which uses instance-virtual service instances (I-VSIs) identified by 24-bit IDs, allows you to establish sufficient tunnels to transmit traffic over an Ethernet transport network.

Virtual private LAN service (VPLS) is an L2VPN technology implemented based on Multiprotocol Label Switching (MPLS) and Ethernet technologies.

PBB VPLS uses MAC-in-MAC instead of QinQ to transmit packets over a VPLS network, reducing the number of MAC entries that PEs must learn.


#### Purpose

Carriers generally use hierarchical virtual private LAN service (HVPLS) to carry metropolitan area network (MAN) services. As shown in [Figure 1](#EN-US_CONCEPT_0172370761__en-us_concept_0172356678_fig_dc_vrp_pbb-vpls_feature_000201), by dividing the VPLS network into multiple layers, HVPLS decreases the number of required pseudo wires (PWs), reduces signaling exchange and packet replication frequency, and solves the expansibility problem confronted by full-mesh VPLS networks. HVPLS enables VPLS networks to be applied on a large scale. On the HVPLS network shown in [Figure 1](#EN-US_CONCEPT_0172370761__en-us_concept_0172356678_fig_dc_vrp_pbb-vpls_feature_000201), user-end provider edges (UPEs) only need to learn the MAC addresses of local and remote users; superstratum provider edges (SPEs) serving as service aggregation points, however, must learn the MAC addresses of all public network devices (UPEs) and customer devices (CEs) on the metro Ethernet. As the metro Ethernet expands in scale, SPEs have to learn increasingly more MAC addresses. Expanding the capacities of MAC address tables on SPEs then becomes a challenging task.

**Figure 1** Typical HVPLS networking  
![](images/fig_feature_image_0018383525.png)  

To address the problem faced by HVPLS networks, PBB VPLS is introduced. PBB VPLS combines PBB with HVPLS by preceding C-SMAC addresses with B-MAC addresses. This approach allows SPEs to learn only the B-MAC addresses of public network devices (UPEs) rather than the C-MAC addresses of all customer devices (CEs) on the Metro Ethernet. By relieving the MAC address learning pressure on SPEs, PBB VPLS improves network scalability.


#### Benefits

Compared to HVPLS, PBB VPLS offers the following benefits:

* Flexible network expansion and reduced network costs
  
  On the HVPLS network shown in [Figure 2](#EN-US_CONCEPT_0172370761__en-us_concept_0172356678_fig_dc_vrp_pbb-vpls_feature_000202), SPEs need to learn the MAC addresses of all users. Therefore, when expanding the HVPLS network by connecting more UPEs to SPEs, you need to check whether the MAC address learning capabilities of SPEs meet requirements. If their MAC address learning capabilities do not meet requirements, you also need to add SPEs.
  
  **Figure 2** Comparison of MAC address learning pressure faced by SPEs on HVPLS and PBB VPLS networks  
  ![](images/fig_feature_image_0018383528.png)
  
  PBB VPLS enables SPEs to learn only the MAC addresses of UPEs, significantly alleviating the MAC address learning pressure of SPEs. This means that as a PBB VPLS network is expanded by adding more UPEs, the MAC address learning pressure on SPEs does not need to be considered, lowering carriers' investments on SPEs. Moreover, this approach enhances the user access capabilities of UPEs, thereby lowering carriers' investments on these devices.
* Improved network security
  
  After a user packet arrives at the public network, B-MAC addresses are inserted before the C-MAC addresses in the packet. This implementation masks detailed packet information and separates the user network from the carrier network, improving network security.
* Reduced maintenance costs
  
  On the HVPLS network shown in [Figure 3](#EN-US_CONCEPT_0172370761__en-us_concept_0172356678_fig_dc_vrp_pbb-vpls_feature_000203), the SPE has to establish a PW for each pair of UPEs that need to communicate, incurring high maintenance costs.
  
  **Figure 3** Comparison of PW quantities required by HVPLS and PBB HVPLS networks  
  ![](images/fig_feature_image_0018383535.png)
  
  On a PBB VPLS network, packets sent by different UPEs can share the same PW. This significantly reduces the number of PWs needed on UPEs and SPEs. Only a few configurations are required for capacity expansion, lowering maintenance costs.